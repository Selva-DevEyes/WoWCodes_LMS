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
  FiX
} from 'react-icons/fi'
import { useDispatch } from 'react-redux'
import { useNavigate } from 'react-router-dom'
import { logout } from '../../redux/slices/authSlice'
import Logo from './Logo'

const Sidebar = ({ isOpen, onClose }) => {
  const dispatch = useDispatch()
  const navigate = useNavigate()

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
          <div className="p-5 pr-12 border-b border-slate-100 dark:border-slate-800">
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

          <div className="px-4 py-3">
            <span className="text-[11px] font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 px-3">
              Navigation
            </span>
          </div>

          <nav className="space-y-1 px-3">
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

        {/* Sidebar Footer with Logout & Signature */}
        <div className="p-4 border-t border-slate-100 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/50 space-y-3">
          <div className="px-1 text-[11px] text-slate-400 dark:text-slate-500 leading-tight">
            <div className="text-[10px] text-slate-500 dark:text-slate-400 font-medium">Learn. Practice. Grow.</div>
            <div className="font-bold text-slate-700 dark:text-slate-300">
              WOWCode <span className="font-semibold text-indigo-600 dark:text-indigo-400 font-normal">Created by Selvam S</span>
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
