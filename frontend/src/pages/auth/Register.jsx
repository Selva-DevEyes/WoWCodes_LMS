import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { FiUser, FiMail, FiLock, FiLoader, FiArrowRight } from 'react-icons/fi'
import { apiClient } from '../../api/apiClient'
import { ENDPOINTS } from '../../api/endpoints'

const Register = () => {
  const navigate = useNavigate()
  const [form, setForm] = useState({
    email: '',
    username: '',
    full_name: '',
    password: '',
    confirmPassword: '',
  })
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (form.password !== form.confirmPassword) {
      setError('Passwords do not match. Please verify your password.')
      return
    }
    setLoading(true)
    setError('')
    try {
      // 1. Create the new user account in the database
      await apiClient.post(ENDPOINTS.register, {
        email: form.email,
        username: form.username,
        full_name: form.full_name,
        password: form.password,
      })

      // 2. Redirect to Login page with prefilled email and success confirmation
      navigate('/login', {
        state: {
          registeredEmail: form.email,
          successMessage: 'Account created successfully! Please enter your password to sign in.',
        },
      })
    } catch (err) {
      const errorMsg = err.response?.data?.detail || 'Registration failed. Please check your credentials.'
      setError(typeof errorMsg === 'string' ? errorMsg : JSON.stringify(errorMsg))
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="card p-6 sm:p-8 space-y-6 border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-2xl">
      <div className="text-center space-y-1">
        <h1 className="text-xl sm:text-2xl font-bold tracking-tight text-slate-900 dark:text-white">
          Create Student Account
        </h1>
        <p className="text-xs text-slate-500 dark:text-slate-400">
          Join WoWCodes to access all 14 courses, code sandboxes, and certifications
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
            Full Name
          </label>
          <input
            type="text"
            required
            value={form.full_name}
            onChange={(e) => setForm({ ...form, full_name: e.target.value })}
            className="input text-xs sm:text-sm font-medium"
            placeholder="e.g. Alex Chen"
          />
        </div>

        <div>
          <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider mb-1.5">
            Username
          </label>
          <div className="relative">
            <FiUser className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" />
            <input
              type="text"
              required
              value={form.username}
              onChange={(e) => setForm({ ...form, username: e.target.value })}
              className="input pl-10 text-xs sm:text-sm font-medium"
              placeholder="alexchen_dev"
            />
          </div>
        </div>

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
              onChange={(e) => setForm({ ...form, email: e.target.value })}
              className="input pl-10 text-xs sm:text-sm font-medium"
              placeholder="alex@example.com"
            />
          </div>
        </div>

        <div>
          <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider mb-1.5">
            Password (Min 8 Characters)
          </label>
          <div className="relative">
            <FiLock className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" />
            <input
              type="password"
              required
              minLength={8}
              value={form.password}
              onChange={(e) => setForm({ ...form, password: e.target.value })}
              className="input pl-10 text-xs sm:text-sm font-medium"
              placeholder="••••••••"
            />
          </div>
        </div>

        <div>
          <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider mb-1.5">
            Confirm Password
          </label>
          <div className="relative">
            <FiLock className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" />
            <input
              type="password"
              required
              value={form.confirmPassword}
              onChange={(e) => setForm({ ...form, confirmPassword: e.target.value })}
              className="input pl-10 text-xs sm:text-sm font-medium"
              placeholder="••••••••"
            />
          </div>
        </div>

        <button type="submit" disabled={loading} className="btn-primary w-full py-3">
          {loading ? (
            <span className="inline-flex items-center gap-2">
              <FiLoader className="animate-spin" /> Creating Account...
            </span>
          ) : (
            <span className="inline-flex items-center gap-2">
              Register & Proceed to Login <FiArrowRight />
            </span>
          )}
        </button>
      </form>

      <div className="pt-4 border-t border-slate-100 dark:border-slate-800 text-center">
        <p className="text-xs text-slate-600 dark:text-slate-400">
          Already registered?{' '}
          <Link to="/login" className="text-indigo-600 dark:text-indigo-400 font-bold hover:underline">
            Log In Here
          </Link>
        </p>
      </div>
    </div>
  )
}

export default Register
