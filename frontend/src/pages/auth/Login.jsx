import { useState, useEffect } from 'react'
import { Link, useNavigate, useLocation } from 'react-router-dom'
import { useDispatch } from 'react-redux'
import { FiMail, FiLock, FiLoader, FiArrowRight, FiCheckCircle } from 'react-icons/fi'
import { apiClient } from '../../api/apiClient'
import { ENDPOINTS } from '../../api/endpoints'
import { setCredentials, setUser } from '../../redux/slices/authSlice'

const Login = () => {
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const location = useLocation()

  const [form, setForm] = useState({
    email: location.state?.registeredEmail || '',
    password: '',
  })
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const [success, setSuccess] = useState(location.state?.successMessage || '')

  useEffect(() => {
    if (location.state?.registeredEmail) {
      setForm((prev) => ({ ...prev, email: location.state.registeredEmail }))
    }
    if (location.state?.successMessage) {
      setSuccess(location.state.successMessage)
    }
  }, [location.state])

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError('')
    try {
      const { data } = await apiClient.post(ENDPOINTS.login, form)
      dispatch(setCredentials(data))
      const me = await apiClient.get(ENDPOINTS.me)
      dispatch(setUser(me.data))
      navigate('/dashboard')
    } catch (err) {
      const errorMsg = err.response?.data?.detail || 'Invalid email or password. Please try again.'
      setError(typeof errorMsg === 'string' ? errorMsg : JSON.stringify(errorMsg))
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="card p-6 sm:p-8 space-y-6 border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-2xl">
      <div className="text-center space-y-1">
        <h1 className="text-xl sm:text-2xl font-bold tracking-tight text-slate-900 dark:text-white">
          Welcome Back to WoWCodes
        </h1>
        <p className="text-xs text-slate-500 dark:text-slate-400">
          Sign in to resume your learning track and daily streaks
        </p>
      </div>

      {success && (
        <div className="p-3.5 bg-emerald-50 border border-emerald-200 text-emerald-700 dark:bg-emerald-950/60 dark:border-emerald-900/60 dark:text-emerald-300 rounded-xl text-xs font-semibold flex items-center gap-2">
          <FiCheckCircle className="text-emerald-500 shrink-0 w-4 h-4" />
          <span>{success}</span>
        </div>
      )}

      {error && (
        <div className="p-3.5 bg-rose-50 border border-rose-200 text-rose-700 dark:bg-rose-950/60 dark:border-rose-900/60 dark:text-rose-300 rounded-xl text-xs font-semibold">
          {error}
        </div>
      )}

      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider mb-1.5">
            Email Address
          </label>
          <div className="relative">
            <FiMail className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" />
            <input
              type="email"
              required
              value={form.email}
              onChange={(e) => {
                setForm({ ...form, email: e.target.value })
                if (success) setSuccess('')
              }}
              className="input pl-10 text-xs sm:text-sm font-medium"
              placeholder="you@example.com"
            />
          </div>
        </div>

        <div>
          <div className="flex items-center justify-between mb-1.5">
            <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider">
              Password
            </label>
            <Link to="/forgot-password" className="text-xs text-indigo-600 dark:text-indigo-400 hover:underline font-semibold">
              Forgot password?
            </Link>
          </div>
          <div className="relative">
            <FiLock className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" />
            <input
              type="password"
              required
              value={form.password}
              onChange={(e) => {
                setForm({ ...form, password: e.target.value })
                if (success) setSuccess('')
              }}
              className="input pl-10 text-xs sm:text-sm font-medium"
              placeholder="••••••••"
            />
          </div>
        </div>

        <button type="submit" disabled={loading} className="btn-primary w-full py-3">
          {loading ? (
            <span className="inline-flex items-center gap-2">
              <FiLoader className="animate-spin" /> Signing In...
            </span>
          ) : (
            <span className="inline-flex items-center gap-2">
              Sign In to Dashboard <FiArrowRight />
            </span>
          )}
        </button>
      </form>

      <div className="pt-4 border-t border-slate-100 dark:border-slate-800 text-center">
        <p className="text-xs text-slate-600 dark:text-slate-400">
          New to WoWCodes?{' '}
          <Link to="/register" className="text-indigo-600 dark:text-indigo-400 font-bold hover:underline">
            Create an Account
          </Link>
        </p>
      </div>
    </div>
  )
}

export default Login
