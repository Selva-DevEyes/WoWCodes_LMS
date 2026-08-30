import { useState } from 'react'
import { Link } from 'react-router-dom'
import { FiMail, FiLoader } from 'react-icons/fi'
import { apiClient } from '../../api/apiClient'
import { ENDPOINTS } from '../../api/endpoints'

const ForgotPassword = () => {
  const [email, setEmail] = useState('')
  const [loading, setLoading] = useState(false)
  const [message, setMessage] = useState('')
  const [error, setError] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setMessage('')
    setError('')
    try {
      await apiClient.post(ENDPOINTS.forgotPassword, { email })
      setMessage('If that email exists, a reset link has been sent.')
    } catch (err) {
      setError(err.response?.data?.detail || 'Something went wrong')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-8">
      <h2 className="text-2xl font-bold mb-6 text-center">Forgot Password</h2>
      {message && (
        <div className="mb-4 p-3 bg-green-100 text-green-700 rounded-lg text-sm">
          {message}
        </div>
      )}
      {error && (
        <div className="mb-4 p-3 bg-red-100 text-red-700 rounded-lg text-sm">
          {error}
        </div>
      )}
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-sm font-medium mb-1">Email</label>
          <div className="relative">
            <FiMail className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
            <input
              type="email"
              required
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="input pl-10"
              placeholder="you@example.com"
            />
          </div>
        </div>
        <button type="submit" disabled={loading} className="btn-primary w-full">
          {loading ? <FiLoader className="animate-spin" /> : 'Send Reset Link'}
        </button>
      </form>
      <p className="mt-6 text-center text-sm">
        <Link to="/login" className="text-primary-600 hover:underline">
          Back to Login
        </Link>
      </p>
    </div>
  )
}

export default ForgotPassword
