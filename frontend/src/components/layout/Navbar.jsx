import { useState, useEffect } from 'react'
import { FiSearch, FiBell, FiSun, FiMoon, FiX, FiMenu } from 'react-icons/fi'
import { useDispatch, useSelector } from 'react-redux'
import { toggleTheme } from '../../redux/slices/themeSlice'
import { apiClient } from '../../api/apiClient'
import { ENDPOINTS } from '../../api/endpoints'

const Navbar = ({ onOpenSidebar }) => {
  const dispatch = useDispatch()
  const theme = useSelector((state) => state.theme.mode)
  const user = useSelector((state) => state.auth.user)
  const [searchResults, setSearchResults] = useState([])
  const [searchQuery, setSearchQuery] = useState('')
  const [showSearch, setShowSearch] = useState(false)
  const [notifCount, setNotifCount] = useState(0)
  const [showNotifs, setShowNotifs] = useState(false)

  useEffect(() => {
    apiClient.get('/notifications/unread-count')
      .then((res) => setNotifCount(res.data.count))
      .catch(() => {})
  }, [])

  const handleSearch = async (e) => {
    const q = e.target.value
    setSearchQuery(q)
    if (q.length > 1) {
      try {
        const { data } = await apiClient.get(ENDPOINTS.search(q))
        setSearchResults(data)
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

  const clearSearch = () => {
    setSearchQuery('')
    setSearchResults([])
    setShowSearch(false)
  }

  return (
    <header className="sticky top-0 z-30 border-b border-slate-200/80 bg-white/95 shadow-sm backdrop-blur dark:border-slate-800 dark:bg-slate-900/95">
      <div className="flex items-center justify-between gap-3 px-4 py-3 lg:px-8">
        <button
          type="button"
          aria-label="Open navigation menu"
          aria-controls="mobile-sidebar"
          onClick={onOpenSidebar}
          className="shrink-0 rounded-xl p-2 text-slate-600 transition hover:bg-slate-100 hover:text-slate-900 focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-slate-300 dark:hover:bg-slate-800 lg:hidden"
        >
          <FiMenu className="text-xl" aria-hidden="true" />
        </button>

        {/* Global Search Bar */}
        <div className="relative min-w-0 flex-1 max-w-xl">
          <FiSearch className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400 text-base" />
          <input
            type="text"
            value={searchQuery}
            placeholder="Search topics, modules, coding interview challenges..."
            className="input pl-10 pr-10 bg-slate-50/70 dark:bg-slate-950/60"
            onChange={handleSearch}
            onKeyDown={(e) => e.key === 'Escape' && clearSearch()}
          />
          {searchQuery && (
            <button
              type="button"
              onClick={clearSearch}
              aria-label="Clear search"
              className="absolute right-2.5 top-1/2 -translate-y-1/2 rounded-full p-1 text-slate-400 hover:bg-slate-200 hover:text-slate-700 dark:hover:bg-slate-700"
            >
              <FiX aria-hidden="true" className="text-sm" />
            </button>
          )}
          {showSearch && searchResults.length > 0 && (
            <div className="absolute z-50 mt-2 w-full overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-2xl dark:border-slate-700 dark:bg-slate-800">
              {searchResults.map((r) => (
                <a
                  key={`${r.type}-${r.id}`}
                  href={r.url}
                  className="block px-4 py-2.5 hover:bg-slate-50 dark:hover:bg-slate-700/70 border-b border-slate-100 dark:border-slate-700/50 last:border-0"
                >
                  <span className="text-sm font-semibold text-slate-800 dark:text-slate-100">{r.title}</span>
                  <span className="text-[11px] font-mono font-bold text-indigo-600 dark:text-indigo-400 ml-2 uppercase px-2 py-0.5 rounded-full bg-indigo-50 dark:bg-indigo-950/80">{r.type}</span>
                </a>
              ))}
            </div>
          )}
        </div>

        {/* Right Actions */}
        <div className="flex shrink-0 items-center gap-2 sm:gap-3">
          <button
            onClick={() => dispatch(toggleTheme())}
            aria-label="Toggle dark mode"
            className="p-2 rounded-xl text-slate-600 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-300 dark:hover:bg-slate-800 transition"
          >
            {theme === 'light' ? <FiMoon className="text-lg" /> : <FiSun className="text-lg text-amber-400" />}
          </button>

          <div className="relative">
            <button
              onClick={() => setShowNotifs(!showNotifs)}
              aria-label="Notifications"
              className="p-2 rounded-xl text-slate-600 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-300 dark:hover:bg-slate-800 relative transition"
            >
              <FiBell className="text-lg" />
              {notifCount > 0 && (
                <span className="absolute 1.5 top-1.5 right-1.5 bg-rose-500 text-white text-[10px] font-bold rounded-full w-4 h-4 flex items-center justify-center ring-2 ring-white dark:ring-slate-900">
                  {notifCount}
                </span>
              )}
            </button>
          </div>

          <div className="flex items-center gap-2.5 pl-2 border-l border-slate-200 dark:border-slate-800">
            <img
              src={user?.avatar_url || `https://ui-avatars.com/api/?name=${user?.username || 'U'}&background=6366f1&color=fff`}
              alt="Profile"
              className="w-8 h-8 rounded-xl object-cover ring-2 ring-indigo-500/20"
            />
            <div className="hidden sm:flex flex-col text-left">
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
    </header>
  )
}

export default Navbar
