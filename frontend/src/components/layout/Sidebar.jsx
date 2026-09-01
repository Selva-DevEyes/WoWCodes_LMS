import { NavLink } from 'react-router-dom'
import {
  FiGrid,
  FiBookOpen,
  FiCode,
  FiAward,
  FiTrendingUp,
  FiFileText,
  FiBookmark,
  FiUser,
  FiSettings,
  FiLogOut,
  FiX,
  FiSun,
  FiMoon
} from 'react-icons/fi'
import { useDispatch, useSelector } from 'react-redux'
import { useNavigate } from 'react-router-dom'
import { logout } from '../../redux/slices/authSlice'
import { toggleTheme } from '../../redux/slices/themeSlice'
import Logo from './Logo'

const Sidebar = ({ isOpen, onClose }) => {
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const theme = useSelector((state) => state.theme.mode)

  const links = [
    { to: '/dashboard', icon: FiGrid, label: 'Dashboard' },
    { to: '/learn', icon: FiBookOpen, label: 'Curriculum' },
    { to: '/playground', icon: FiCode, label: 'Code Sandbox' },
    { to: '/certificates', icon: FiAward, label: 'Certificates' },
    { to: '/leaderboard', icon: FiTrendingUp, label: 'Leaderboard' },
    { to: '/notes', icon: FiFileText, label: 'Notes' },
    { to: '/bookmarks', icon: FiBookmark, label: 'Bookmarks' },
    { to: '/profile', icon: FiUser, label: 'My Profile' },
    { to: '/settings', icon: FiSettings, label: 'Settings' },
  ]

  const handleLogout = () => {
    onClose()
    dispatch(logout())
    navigate('/login')
  }

  const handleToggleTheme = () => {
    dispatch(toggleTheme())
  }

  return (
    <>
      {isOpen && (
        <button
          type="button"
          aria-label="Close navigation menu"
          onClick={onClose}
          className="fixed inset-0 z-40 bg-slate-950/60 backdrop-blur-sm lg:hidden"
        />
      )}
      <aside
        id="mobile-sidebar"
        className={`fixed left-0 top-0 z-50 h-full w-64 border-r border-slate-200/90 bg-white shadow-xl lg:shadow-none backdrop-blur transition-transform duration-300 ease-out dark:border-slate-800/90 dark:bg-slate-900 lg:z-40 lg:translate-x-0 flex flex-col justify-between ${isOpen ? 'translate-x-0' : '-translate-x-full'}`}
      >
        <div>
          {/* Sidebar Header Logo Column with padding-right: 2rem */}
          <div
            className="p-5 border-b border-slate-100 dark:border-slate-800"
            style={{ paddingRight: '2rem' }}
          >
            <Logo size="md" />
          </div>
          <button
            type="button"
            aria-label="Close navigation menu"
            onClick={onClose}
            className="absolute right-3 top-5 rounded-xl p-2 text-slate-500 hover:text-slate-900 hover:bg-slate-100 dark:text-slate-400 dark:hover:text-white dark:hover:bg-slate-800 transition lg:hidden"
          >
            <FiX className="text-xl" aria-hidden="true" />
          </button>

          <nav className="space-y-1 px-3 pt-3">
            {links.map((link) => (
              <NavLink
                key={link.to}
                to={link.to}
                onClick={onClose}
                className={({ isActive }) =>
                  `sidebar-link ${isActive ? 'sidebar-link-active' : ''}`
                }
              >
                <link.icon className="text-lg shrink-0" />
                <span>{link.label}</span>
              </NavLink>
            ))}
          </nav>
        </div>

        {/* Sidebar Footer with Theme Toggle, Logout & Consistent Rainbow WOWCode Signature */}
        <div className="p-4 border-t border-slate-100 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/50 space-y-2.5">
          {/* In-Drawer Theme Switch for mobile/tablet convenience */}
          <button
            type="button"
            onClick={handleToggleTheme}
            className="sidebar-link w-full text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition"
          >
            {theme === 'light' ? (
              <>
                <FiMoon className="text-lg shrink-0 text-slate-700" />
                <span>Dark Mode</span>
              </>
            ) : (
              <>
                <FiSun className="text-lg shrink-0 text-amber-400" />
                <span>Light Mode</span>
              </>
            )}
          </button>

          <div className="px-1 text-[11px] text-slate-400 dark:text-slate-500 leading-tight">
            <div className="text-[10px] text-slate-500 dark:text-slate-400 font-medium">Learn. Practice. Grow.</div>
            <div className="pt-0.5">
              <span className="font-black text-transparent bg-clip-text bg-gradient-to-r from-rose-500 via-amber-500 via-emerald-500 via-sky-500 to-indigo-600">
                WOWCode
              </span>{' '}
              <span className="font-semibold text-indigo-600 dark:text-indigo-400">
                Created by Selvam S
              </span>
            </div>
          </div>

          <button onClick={handleLogout} className="sidebar-link w-full text-rose-600 dark:text-rose-400 hover:text-rose-700 hover:bg-rose-50 dark:hover:bg-rose-500/10">
            <FiLogOut className="text-lg shrink-0" />
            <span>Logout</span>
          </button>
        </div>
      </aside>
    </>
  )
}

export default Sidebar
