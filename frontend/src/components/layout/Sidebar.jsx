import { NavLink } from 'react-router-dom'
import { FiGrid, FiBookOpen, FiCode, FiAward, FiTrendingUp, FiFileText, FiBookmark, FiUser, FiSettings, FiLogOut, FiX } from 'react-icons/fi'
import { useDispatch } from 'react-redux'
import { useNavigate } from 'react-router-dom'
import { logout } from '../../redux/slices/authSlice'
import Logo from './Logo'

const Sidebar = ({ isOpen, onClose }) => {
  const dispatch = useDispatch()
  const navigate = useNavigate()

  const links = [
    { to: '/dashboard', icon: FiGrid, label: 'Dashboard' },
    { to: '/learn', icon: FiBookOpen, label: 'Learn' },
    { to: '/playground', icon: FiCode, label: 'Code Sandbox' },
    { to: '/certificates', icon: FiAward, label: 'Certificates' },
    { to: '/leaderboard', icon: FiTrendingUp, label: 'Leaderboard' },
    { to: '/notes', icon: FiFileText, label: 'Notes' },
    { to: '/bookmarks', icon: FiBookmark, label: 'Bookmarks' },
    { to: '/profile', icon: FiUser, label: 'Profile' },
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
        className={`fixed left-0 top-0 z-50 h-full w-64 border-r border-slate-800 bg-slate-900 shadow-2xl backdrop-blur transition-transform duration-300 ease-out dark:border-slate-800 dark:bg-slate-900 lg:z-40 lg:translate-x-0 ${isOpen ? 'translate-x-0' : '-translate-x-full'}`}
      >
        <div className="p-6 pr-12 border-b border-slate-800/80">
          <Logo size="md" />
        </div>
        <button
          type="button"
          aria-label="Close navigation menu"
          onClick={onClose}
          className="absolute right-3 top-5 rounded-xl p-2 text-slate-400 hover:text-white hover:bg-slate-800 transition lg:hidden"
        >
          <FiX className="text-xl" aria-hidden="true" />
        </button>
        <nav className="space-y-1.5 px-4 pt-6">
          {links.map((link) => (
            <NavLink
              key={link.to}
              to={link.to}
              onClick={onClose}
              className={({ isActive }) =>
                `sidebar-link ${isActive ? 'sidebar-link-active' : ''}`
              }
            >
              <link.icon className="text-lg" />
              <span>{link.label}</span>
            </NavLink>
          ))}
        </nav>
        <div className="absolute bottom-0 w-full p-4 border-t border-slate-800/80 bg-slate-900">
          <button onClick={handleLogout} className="sidebar-link w-full text-rose-400 hover:text-rose-300 hover:bg-rose-500/10">
            <FiLogOut className="text-lg" />
            <span>Logout</span>
          </button>
        </div>
      </aside>
    </>
  )
}

export default Sidebar
