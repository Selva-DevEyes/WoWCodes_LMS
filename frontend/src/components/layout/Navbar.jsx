import { useState, useEffect, useRef } from 'react'
import { FiSearch, FiBell, FiSun, FiMoon, FiX, FiMenu, FiArrowRight } from 'react-icons/fi'
import { useDispatch, useSelector } from 'react-redux'
import { useNavigate } from 'react-router-dom'
import { toggleTheme } from '../../redux/slices/themeSlice'
import { apiClient } from '../../api/apiClient'
import { ENDPOINTS } from '../../api/endpoints'
import Logo from './Logo'

const Navbar = ({ onOpenSidebar }) => {
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const theme = useSelector((state) => state.theme.mode)
  const user = useSelector((state) => state.auth.user)

  const [searchResults, setSearchResults] = useState([])
  const [searchQuery, setSearchQuery] = useState('')
  const [showSearch, setShowSearch] = useState(false)
  const [selectedIndex, setSelectedIndex] = useState(-1)
  const [isMobileSearchOpen, setIsMobileSearchOpen] = useState(false)
  const [notifCount, setNotifCount] = useState(0)
  const [showNotifs, setShowNotifs] = useState(false)

  const searchContainerRef = useRef(null)
  const mobileInputRef = useRef(null)
  const desktopInputRef = useRef(null)

  useEffect(() => {
    apiClient.get('/notifications/unread-count')
      .then((res) => setNotifCount(res.data.count))
      .catch(() => {})
  }, [])

  // Auto focus mobile search when opened
  useEffect(() => {
    if (isMobileSearchOpen && mobileInputRef.current) {
      mobileInputRef.current.focus()
    }
  }, [isMobileSearchOpen])

  // Close search dropdown on click outside
  useEffect(() => {
    const handleClickOutside = (e) => {
      if (searchContainerRef.current && !searchContainerRef.current.contains(e.target)) {
        setShowSearch(false)
      }
    }
    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [])

  const handleSearchChange = async (e) => {
    const q = e.target.value
    setSearchQuery(q)
    setSelectedIndex(-1)
    if (q.trim().length > 0) {
      try {
        const { data } = await apiClient.get(ENDPOINTS.search(q.trim()))
        setSearchResults(data || [])
        setShowSearch(true)
      } catch {
        setSearchResults([])
        setShowSearch(false)
      }
    } else {
      setSearchResults([])
      setShowSearch(false)
    }
  }

  const navigateToResult = (url) => {
    if (!url) return
    clearSearch()
    navigate(url)
  }

  const handleSearchSubmit = async (e) => {
    if (e) e.preventDefault()
    const trimmed = searchQuery.trim()
    if (!trimmed) return

    // 1. If an item in dropdown is actively selected via arrow keys
    if (selectedIndex >= 0 && searchResults[selectedIndex]) {
      navigateToResult(searchResults[selectedIndex].url)
      return
    }

    // 2. If search results are already displayed, pick the 1st match
    if (searchResults.length > 0) {
      navigateToResult(searchResults[0].url)
      return
    }

    // 3. Otherwise fetch immediately on Enter press
    try {
      const { data } = await apiClient.get(ENDPOINTS.search(trimmed))
      if (data && data.length > 0) {
        navigateToResult(data[0].url)
      } else {
        clearSearch()
        navigate(`/learn`)
      }
    } catch {
      clearSearch()
      navigate(`/learn`)
    }
  }

  const handleKeyDown = (e) => {
    if (e.key === 'ArrowDown') {
      e.preventDefault()
      setSelectedIndex((prev) => (prev < searchResults.length - 1 ? prev + 1 : 0))
    } else if (e.key === 'ArrowUp') {
      e.preventDefault()
      setSelectedIndex((prev) => (prev > 0 ? prev - 1 : searchResults.length - 1))
    } else if (e.key === 'Escape') {
      clearSearch()
    } else if (e.key === 'Enter') {
      e.preventDefault()
      handleSearchSubmit()
    }
  }

  const clearSearch = () => {
    setSearchQuery('')
    setSearchResults([])
    setShowSearch(false)
    setSelectedIndex(-1)
    setIsMobileSearchOpen(false)
  }

  const handleThemeToggle = (e) => {
    e.preventDefault()
    e.stopPropagation()
    dispatch(toggleTheme())
  }

  return (
    <header className="sticky top-0 z-30 border-b border-slate-200/80 bg-white/95 shadow-sm backdrop-blur dark:border-slate-800 dark:bg-slate-900/95">
      <div className="flex items-center justify-between gap-2 sm:gap-4 px-3 sm:px-6 py-2 sm:py-2.5 max-w-full">
        
        {/* Left: Mobile Menu + Brand Logo */}
        <div className="flex items-center gap-2 shrink-0">
          <button
            type="button"
            aria-label="Open navigation menu"
            aria-controls="mobile-sidebar"
            onClick={onOpenSidebar}
            className="w-9 h-9 flex items-center justify-center rounded-xl bg-slate-100/90 dark:bg-slate-800/90 text-slate-700 dark:text-slate-200 hover:bg-slate-200 dark:hover:bg-slate-700 transition focus:outline-none focus:ring-2 focus:ring-indigo-500 shadow-sm lg:hidden active:scale-95"
          >
            <FiMenu className="text-lg sm:text-xl" aria-hidden="true" />
          </button>
          <div className="lg:hidden">
            <Logo size="sm" showSubtitle={false} />
          </div>
        </div>

        {/* Center: Desktop & Tablet Integrated Search Bar */}
        <div ref={searchContainerRef} className="relative hidden sm:block flex-1 max-w-lg lg:max-w-xl mx-auto">
          <form onSubmit={handleSearchSubmit} className="relative w-full">
            <FiSearch className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400 text-base pointer-events-none" />
            <input
              ref={desktopInputRef}
              type="text"
              value={searchQuery}
              placeholder="Search topics, courses, quizzes... (Press Enter ↵)"
              className="w-full h-10 pl-10 pr-10 rounded-2xl bg-slate-100/80 dark:bg-slate-950/70 border border-slate-200 dark:border-slate-800 text-xs sm:text-sm text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition"
              onChange={handleSearchChange}
              onKeyDown={handleKeyDown}
              onFocus={() => searchQuery.trim().length > 0 && searchResults.length > 0 && setShowSearch(true)}
            />
            {searchQuery && (
              <button
                type="button"
                onClick={clearSearch}
                aria-label="Clear search"
                className="absolute right-2.5 top-1/2 -translate-y-1/2 rounded-full p-1 text-slate-400 hover:bg-slate-200 hover:text-slate-700 dark:hover:bg-slate-700 transition"
              >
                <FiX aria-hidden="true" className="text-xs" />
              </button>
            )}
          </form>

          {/* Desktop Search Results Dropdown */}
          {showSearch && searchResults.length > 0 && (
            <div className="absolute left-0 right-0 z-50 mt-2 max-h-96 overflow-y-auto rounded-2xl border border-slate-200 bg-white/95 shadow-2xl backdrop-blur-md dark:border-slate-700 dark:bg-slate-900/95">
              <div className="p-2 border-b border-slate-100 dark:border-slate-800 text-[10px] uppercase font-bold tracking-wider text-slate-400 px-3 flex justify-between">
                <span>Top Results</span>
                <span className="font-mono text-indigo-500">Press Enter ↵ to open</span>
              </div>
              {searchResults.map((r, index) => (
                <div
                  key={`${r.type}-${r.id}`}
                  onClick={() => navigateToResult(r.url)}
                  onMouseEnter={() => setSelectedIndex(index)}
                  className={`flex items-center justify-between px-4 py-3 cursor-pointer transition border-b border-slate-100 dark:border-slate-800/60 last:border-0 ${
                    selectedIndex === index
                      ? 'bg-indigo-50/80 dark:bg-indigo-950/60 text-indigo-600 dark:text-indigo-300'
                      : 'hover:bg-slate-50 dark:hover:bg-slate-800/60'
                  }`}
                >
                  <div className="min-w-0 flex-1 pr-3">
                    <p className="text-xs sm:text-sm font-semibold text-slate-800 dark:text-slate-100 truncate">
                      {r.title}
                    </p>
                    {r.description && (
                      <p className="text-[11px] text-slate-400 truncate mt-0.5">
                        {r.description}
                      </p>
                    )}
                  </div>
                  <div className="flex items-center gap-2 shrink-0">
                    <span className="text-[10px] font-mono font-bold uppercase px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 border border-slate-200 dark:border-slate-700">
                      {r.type}
                    </span>
                    <FiArrowRight className="text-xs text-slate-400" />
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Right Actions: Mobile Search Toggle + Theme Toggle + Notifications + Profile */}
        <div className="flex shrink-0 items-center gap-1.5 sm:gap-2">
          
          {/* Mobile Search Button (Visible on small screens) */}
          <button
            type="button"
            onClick={() => setIsMobileSearchOpen(!isMobileSearchOpen)}
            aria-label="Open search bar"
            className="sm:hidden w-9 h-9 flex items-center justify-center rounded-xl text-slate-600 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-300 dark:hover:bg-slate-800 transition active:scale-95"
          >
            <FiSearch className="text-lg" />
          </button>

          {/* Theme Toggle Button (Light/Dark Mode) */}
          <button
            type="button"
            onClick={handleThemeToggle}
            aria-label={theme === 'light' ? 'Switch to dark mode' : 'Switch to light mode'}
            className="w-9 h-9 sm:w-10 sm:h-10 flex items-center justify-center rounded-xl bg-slate-100/90 dark:bg-slate-800/90 text-slate-700 dark:text-amber-400 hover:bg-slate-200 dark:hover:bg-slate-700 transition cursor-pointer active:scale-95 shadow-sm"
          >
            {theme === 'light' ? (
              <FiMoon className="text-base sm:text-lg text-slate-700" />
            ) : (
              <FiSun className="text-base sm:text-lg text-amber-400 animate-spin-slow" />
            )}
          </button>

          {/* Notifications Bell */}
          <div className="relative">
            <button
              type="button"
              onClick={() => setShowNotifs(!showNotifs)}
              aria-label="Notifications"
              className="w-9 h-9 sm:w-10 sm:h-10 flex items-center justify-center rounded-xl text-slate-600 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-300 dark:hover:bg-slate-800 relative transition active:scale-95"
            >
              <FiBell className="text-base sm:text-lg" />
              {notifCount > 0 && (
                <span className="absolute top-1.5 right-1.5 bg-rose-500 text-white text-[10px] font-bold rounded-full w-4 h-4 flex items-center justify-center ring-2 ring-white dark:ring-slate-900">
                  {notifCount}
                </span>
              )}
            </button>
          </div>

          {/* User Profile Badge */}
          <div className="flex items-center gap-2 pl-1 sm:pl-2 border-l border-slate-200 dark:border-slate-800">
            <img
              src={user?.avatar_url || `https://ui-avatars.com/api/?name=${user?.username || 'U'}&background=6366f1&color=fff`}
              alt="Profile"
              className="w-8 h-8 rounded-xl object-cover ring-2 ring-indigo-500/20"
            />
            <div className="hidden md:flex flex-col text-left">
              <span className="text-xs font-bold text-slate-800 dark:text-slate-100 leading-tight">
                {user?.username || 'Student'}
              </span>
              <span className="text-[10px] text-slate-500 dark:text-slate-400 font-mono">
                {user?.role || 'Learner'}
              </span>
            </div>
          </div>
        </div>
      </div>

      {/* Full-Width Expandable Mobile Search Bar (Triggered on small screens) */}
      {isMobileSearchOpen && (
        <div className="sm:hidden px-3 py-2 bg-slate-50/95 dark:bg-slate-950/95 border-t border-slate-200 dark:border-slate-800 animate-fadeIn">
          <form onSubmit={handleSearchSubmit} className="relative w-full flex items-center gap-2">
            <div className="relative flex-1">
              <FiSearch className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 text-sm" />
              <input
                ref={mobileInputRef}
                type="text"
                value={searchQuery}
                placeholder="Search topics & quizzes... (Press Enter ↵)"
                className="w-full h-9 pl-9 pr-8 rounded-xl bg-white dark:bg-slate-900 border border-slate-300 dark:border-slate-700 text-xs text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                onChange={handleSearchChange}
                onKeyDown={handleKeyDown}
              />
              {searchQuery && (
                <button
                  type="button"
                  onClick={() => setSearchQuery('')}
                  className="absolute right-2 top-1/2 -translate-y-1/2 text-slate-400 p-1"
                >
                  <FiX className="text-xs" />
                </button>
              )}
            </div>
            <button
              type="submit"
              className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded-xl text-xs font-bold transition shadow"
            >
              Go ↵
            </button>
            <button
              type="button"
              onClick={() => setIsMobileSearchOpen(false)}
              className="p-1.5 text-slate-500 hover:text-slate-800 dark:text-slate-400 dark:hover:text-white"
            >
              <FiX className="text-base" />
            </button>
          </form>

          {/* Mobile Search Results */}
          {showSearch && searchResults.length > 0 && (
            <div className="mt-2 max-h-64 overflow-y-auto rounded-xl border border-slate-200 bg-white shadow-xl dark:border-slate-700 dark:bg-slate-900">
              {searchResults.map((r, index) => (
                <div
                  key={`mob-${r.type}-${r.id}`}
                  onClick={() => navigateToResult(r.url)}
                  className="px-3 py-2.5 border-b border-slate-100 dark:border-slate-800 last:border-0 flex items-center justify-between cursor-pointer hover:bg-slate-50 dark:hover:bg-slate-800"
                >
                  <span className="text-xs font-semibold text-slate-800 dark:text-slate-100 truncate pr-2">
                    {r.title}
                  </span>
                  <span className="text-[9px] font-mono font-bold uppercase px-1.5 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">
                    {r.type}
                  </span>
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </header>
  )
}

export default Navbar
