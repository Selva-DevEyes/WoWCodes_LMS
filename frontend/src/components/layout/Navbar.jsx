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
    <header className="sticky top-0 z-30 border-b border-primary-100/80 bg-white/90 shadow-sm backdrop-blur dark:border-gray-700 dark:bg-gray-900/90">
      <div className="flex items-center justify-between gap-3 px-4 py-3 lg:px-8">
        <button
          type="button"
          aria-label="Open navigation menu"
          aria-controls="mobile-sidebar"
          onClick={onOpenSidebar}
          className="shrink-0 rounded-lg p-2 text-gray-600 transition hover:bg-primary-50 hover:text-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-400 dark:text-gray-300 dark:hover:bg-gray-700 lg:hidden"
        >
          <FiMenu className="text-xl" aria-hidden="true" />
        </button>
        <div className="relative min-w-0 flex-1 max-w-xl">
          <FiSearch className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
          <input
            type="text"
            value={searchQuery}
            placeholder="Search topics, quizzes, interview questions..."
            className="input pl-10 pr-10"
            onChange={handleSearch}
            onKeyDown={(e) => e.key === 'Escape' && clearSearch()}
          />
          {searchQuery && (
            <button
              type="button"
              onClick={clearSearch}
              aria-label="Clear search"
              className="absolute right-2 top-1/2 -translate-y-1/2 rounded-full p-1.5 text-gray-400 transition hover:bg-primary-100 hover:text-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-400 dark:hover:bg-gray-700 dark:hover:text-primary-300"
            >
              <FiX aria-hidden="true" className="text-base" />
            </button>
          )}
          {showSearch && searchResults.length > 0 && (
            <div className="absolute z-50 mt-2 w-full overflow-hidden rounded-xl border border-primary-100 bg-white shadow-xl dark:border-gray-700 dark:bg-gray-800">
              {searchResults.map((r) => (
                <a
                  key={`${r.type}-${r.id}`}
                  href={r.url}
                  className="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-700"
                >
                  <span className="text-sm font-medium">{r.title}</span>
                  <span className="text-xs text-gray-500 ml-2 uppercase">{r.type}</span>
                </a>
              ))}
            </div>
          )}
        </div>

        <div className="flex shrink-0 items-center gap-2 sm:gap-3">
          <button
            onClick={() => dispatch(toggleTheme())}
            className="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700"
          >
            {theme === 'light' ? <FiMoon /> : <FiSun />}
          </button>

          <div className="relative">
            <button
              onClick={() => setShowNotifs(!showNotifs)}
              className="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 relative"
            >
              <FiBell />
              {notifCount > 0 && (
                <span className="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full w-4 h-4 flex items-center justify-center">
                  {notifCount}
                </span>
              )}
            </button>
          </div>

          <div className="flex items-center gap-2">
            <img
              src={user?.avatar_url || `https://ui-avatars.com/api/?name=${user?.username || 'U'}`}
              alt="Profile"
              className="w-8 h-8 rounded-full"
            />
            <span className="text-sm font-medium hidden sm:block">
              {user?.username || 'User'}
            </span>
          </div>
        </div>
      </div>
    </header>
  )
}

export default Navbar
