import { useSelector, useDispatch } from 'react-redux'
import { FiMoon, FiSun, FiSettings, FiBell } from 'react-icons/fi'
import { toggleTheme } from '../../redux/slices/themeSlice'

const SettingsPage = () => {
  const theme = useSelector((state) => state.theme.mode)
  const dispatch = useDispatch()

  return (
    <div className="max-w-3xl mx-auto space-y-6 font-sans pb-16">
      {/* Header */}
      <div className="flex items-center gap-3">
        <div className="w-12 h-12 rounded-2xl bg-indigo-500/10 border border-indigo-500/20 text-indigo-500 flex items-center justify-center text-2xl shrink-0">
          <FiSettings />
        </div>
        <div>
          <h1 className="text-2xl sm:text-3xl font-bold tracking-tight text-slate-900 dark:text-white">
            Platform Settings
          </h1>
          <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400 font-normal mt-1">
            Customize visual theme preferences and notification options
          </p>
        </div>
      </div>

      <div className="card p-6 space-y-6">
        {/* Dark Mode */}
        <div className="flex items-center justify-between pb-6 border-b border-slate-100 dark:border-slate-800">
          <div>
            <h2 className="text-base sm:text-lg font-semibold text-slate-900 dark:text-white">
              Visual Appearance
            </h2>
            <p className="text-xs text-slate-500 mt-0.5">
              Toggle between high-contrast light and corporate dark themes
            </p>
          </div>
          <button
            onClick={() => dispatch(toggleTheme())}
            aria-label="Toggle theme"
            className="p-3 rounded-2xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-amber-400 hover:scale-105 transition"
          >
            {theme === 'light' ? <FiMoon className="text-xl" /> : <FiSun className="text-xl" />}
          </button>
        </div>

        {/* Notifications */}
        <div className="space-y-4">
          <div>
            <h2 className="text-base sm:text-lg font-semibold text-slate-900 dark:text-white flex items-center gap-2">
              <FiBell className="text-indigo-500" /> Notifications & Alerts
            </h2>
            <p className="text-xs text-slate-500 mt-0.5">
              Receive updates when quizzes are evaluated, scores are ranked, or certificates are issued
            </p>
          </div>

          <div className="space-y-3 pt-2">
            <label className="flex items-center gap-3 text-sm font-semibold text-slate-700 dark:text-slate-300 cursor-pointer select-none">
              <input type="checkbox" defaultChecked className="w-4 h-4 rounded text-indigo-600 focus:ring-indigo-500" />
              <span>Email study reminders & weekly streak summaries</span>
            </label>
            <label className="flex items-center gap-3 text-sm font-semibold text-slate-700 dark:text-slate-300 cursor-pointer select-none">
              <input type="checkbox" defaultChecked className="w-4 h-4 rounded text-indigo-600 focus:ring-indigo-500" />
              <span>In-app evaluation feedback & badge awards</span>
            </label>
          </div>
        </div>
      </div>
    </div>
  )
}

export default SettingsPage
