import { useState } from 'react'
import { Link, useNavigate, useSearchParams } from 'react-router-dom'
import { FiLock, FiLoader, FiEye, FiEyeOff } from 'react-icons/fi'
import { apiClient } from '../../api/apiClient'
import { ENDPOINTS } from '../../api/endpoints'

const ResetPassword = () => {
  const [searchParams] = useSearchParams()
  const navigate = useNavigate()
  const token = searchParams.get('token') || ''
  const [form, setForm] = useState({ new_password: '', confirmPassword: '' })
  const [showPassword, setShowPassword] = useState(false)
  const [showConfirmPassword, setShowConfirmPassword] = useState(false)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (form.new_password !== form.confirmPassword) {
      setError('Passwords do not match')
      return
    }
    setLoading(true)
    setError('')
    try {
      await apiClient.post(ENDPOINTS.resetPassword, {
        token,
        new_password: form.new_password,
      })
      navigate('/login')
    } catch (err) {
      setError(err.response?.data?.detail || 'Reset failed')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="card p-6 sm:p-8 space-y-6 border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-2xl">
      <div className="text-center space-y-1">
        <h1 className="text-xl sm:text-2xl font-bold tracking-tight text-slate-900 dark:text-white">
          Reset Password
        </h1>
        <p className="text-xs text-slate-500 dark:text-slate-400">
          Enter your new password to regain access to your account
        </p>
      </div>

      {error && (
        <div className="p-3.5 bg-rose-50 border border-rose-200 text-rose-700 dark:bg-rose-950/60 dark:border-rose-900/60 dark:text-rose-300 rounded-xl text-xs font-semibold">
          {error}
        </div>
      )}

      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider mb-1.5">
            New Password (Min 8 Characters)
          </label>
          <div className="relative">
            <FiLock className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" />
            <input
              type={showPassword ? 'text' : 'password'}
              required
              minLength={8}
              value={form.new_password}
              onChange={(e) => setForm({ ...form, new_password: e.target.value })}
              className="input pl-10 pr-10 text-xs sm:text-sm font-medium"
              placeholder="••••••••"
            />
            <button
              type="button"
              onClick={() => setShowPassword(!showPassword)}
              aria-label={showPassword ? 'Hide password' : 'Show password'}
              className="absolute right-3.5 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 transition focus:outline-none cursor-pointer"
            >
              {showPassword ? <FiEyeOff className="w-4 h-4" /> : <FiEye className="w-4 h-4" />}
            </button>
          </div>
        </div>

        <div>
          <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider mb-1.5">
            Confirm Password
          </label>
          <div className="relative">
            <FiLock className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" />
            <input
              type={showConfirmPassword ? 'text' : 'password'}
              required
              minLength={8}
              value={form.confirmPassword}
              onChange={(e) => setForm({ ...form, confirmPassword: e.target.value })}
              className="input pl-10 pr-10 text-xs sm:text-sm font-medium"
              placeholder="••••••••"
            />
            <button
              type="button"
              onClick={() => setShowConfirmPassword(!showConfirmPassword)}
              aria-label={showConfirmPassword ? 'Hide password' : 'Show password'}
              className="absolute right-3.5 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 transition focus:outline-none cursor-pointer"
            >
              {showConfirmPassword ? <FiEyeOff className="w-4 h-4" /> : <FiEye className="w-4 h-4" />}
            </button>
          </div>
        </div>

        <button type="submit" disabled={loading} className="btn-primary w-full py-3">
          {loading ? <FiLoader className="animate-spin" /> : 'Set New Password & Sign In'}
        </button>
      </form>

      <p className="text-center text-xs text-slate-500">
        <Link to="/login" className="text-indigo-600 dark:text-indigo-400 font-bold hover:underline">
          Back to Login
        </Link>
      </p>
    </div>
  )
}

export default ResetPassword
