import { useSelector, useDispatch } from 'react-redux'
import { FiMoon, FiSun } from 'react-icons/fi'
import { toggleTheme } from '../../redux/slices/themeSlice'

const SettingsPage = () => {
  const theme = useSelector((state) => state.theme.mode)
  const dispatch = useDispatch()

  return (
    <div className="max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold mb-8">Settings</h1>

      <div className="card space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="font-semibold">Dark Mode</h2>
            <p className="text-sm text-gray-500">Toggle between light and dark theme</p>
          </div>
          <button
            onClick={() => dispatch(toggleTheme())}
            className="p-3 rounded-lg bg-gray-100 dark:bg-gray-700 text-2xl"
          >
            {theme === 'light' ? <FiMoon /> : <FiSun />}
          </button>
        </div>

        <div className="border-t border-gray-200 dark:border-gray-600 pt-6">
          <h2 className="font-semibold mb-2">Notifications</h2>
          <p className="text-sm text-gray-500 mb-4">
            Get notified when quizzes are graded and certificates are issued.
          </p>
          <div className="flex items-center gap-3">
            <input type="checkbox" defaultChecked className="w-4 h-4 text-primary-600" />
            <span className="text-sm">Email notifications</span>
          </div>
          <div className="flex items-center gap-3 mt-2">
            <input type="checkbox" defaultChecked className="w-4 h-4 text-primary-600" />
            <span className="text-sm">In-app notifications</span>
          </div>
        </div>
      </div>
    </div>
  )
}

export default SettingsPage
