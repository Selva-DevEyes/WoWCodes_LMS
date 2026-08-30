import { FiSun, FiMoon } from 'react-icons/fi'
import { useDispatch, useSelector } from 'react-redux'
import { toggleTheme } from '../../redux/slices/themeSlice'

const ThemeToggle = () => {
  const dispatch = useDispatch()
  const theme = useSelector((state) => state.theme.mode)

  return (
    <button
      onClick={() => dispatch(toggleTheme())}
      className="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
      aria-label="Toggle theme"
    >
      {theme === 'light' ? <FiMoon className="text-lg" /> : <FiSun className="text-lg" />}
    </button>
  )
}

export default ThemeToggle
