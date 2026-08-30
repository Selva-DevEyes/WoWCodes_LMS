import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import AppRoutes from './routes/AppRoutes'
import { setTheme } from './redux/slices/themeSlice'
import { setCredentials, setUser } from './redux/slices/authSlice'
import { apiClient } from './api/apiClient'

function App() {
  const dispatch = useDispatch()
  const theme = useSelector((state) => state.theme.mode)

  useEffect(() => {
    // Load theme from localStorage
    const saved = localStorage.getItem('theme') || 'light'
    dispatch(setTheme(saved))
    document.documentElement.classList.toggle('dark', saved === 'dark')
  }, [dispatch])

  useEffect(() => {
    document.documentElement.classList.toggle('dark', theme === 'dark')
    localStorage.setItem('theme', theme)
  }, [theme])

  useEffect(() => {
    // Restore session from localStorage
    const token = localStorage.getItem('access_token')
    const refresh = localStorage.getItem('refresh_token')
    if (token) {
      dispatch(setCredentials({ access_token: token, refresh_token: refresh }))
      apiClient.get('/users/me')
        .then((res) => dispatch(setUser(res.data)))
        .catch(() => {
          localStorage.removeItem('access_token')
        })
    }
  }, [dispatch])

  return <AppRoutes />
}

export default App
