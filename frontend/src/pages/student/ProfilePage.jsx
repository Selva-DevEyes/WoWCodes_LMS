import { useRef, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { FiMail, FiSave, FiUpload, FiUser } from 'react-icons/fi'
import { apiClient } from '../../api/apiClient'
import { ENDPOINTS } from '../../api/endpoints'
import { setUser } from '../../redux/slices/authSlice'

const ProfilePage = () => {
  const dispatch = useDispatch()
  const user = useSelector((state) => state.auth.user)
  const [form, setForm] = useState({
    full_name: user?.full_name || '',
    bio: user?.bio || '',
    avatar_url: user?.avatar_url || '',
  })
  const [saving, setSaving] = useState(false)
  const [uploadingAvatar, setUploadingAvatar] = useState(false)
  const [message, setMessage] = useState('')
  const [isError, setIsError] = useState(false)
  const fileInputRef = useRef(null)

  const avatarSrc = form.avatar_url || `https://ui-avatars.com/api/?name=${user?.username || 'U'}&background=6366f1&color=fff`

  const handleAvatarUpload = async (event) => {
    const image = event.target.files?.[0]
    if (!image) return

    if (!['image/jpeg', 'image/png', 'image/webp'].includes(image.type)) {
      setIsError(true)
      setMessage('Choose a PNG, JPEG, or WebP image.')
      return
    }
    if (image.size > 5 * 1024 * 1024) {
      setIsError(true)
      setMessage('Image must be 5 MB or smaller.')
      return
    }

    setUploadingAvatar(true)
    setMessage('')
    setIsError(false)
    try {
      const imageData = new FormData()
      imageData.append('image', image)
      const { data } = await apiClient.post(ENDPOINTS.uploadAvatar, imageData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      })
      setForm((currentForm) => ({ ...currentForm, avatar_url: data.avatar_url || '' }))
      dispatch(setUser(data))
      setMessage('Profile image updated successfully!')
      setIsError(false)
    } catch (err) {
      setIsError(true)
      const errorDetail = err.response?.data?.detail || 'Failed to upload profile image.'
      const errorMessage = typeof errorDetail === 'string' ? errorDetail : JSON.stringify(errorDetail)
      setMessage(`Upload Error: ${errorMessage}`)
    } finally {
      setUploadingAvatar(false)
      event.target.value = ''
    }
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setSaving(true)
    setMessage('')
    setIsError(false)
    try {
      const { data } = await apiClient.patch(ENDPOINTS.updateMe, form)
      dispatch(setUser(data))
      setMessage('Profile updated successfully!')
    } catch (err) {
      setIsError(true)
      setMessage('Failed to update profile')
    } finally {
      setSaving(false)
    }
  }

  return (
    <div className="max-w-3xl mx-auto space-y-6 font-sans pb-16">
      {/* Header */}
      <div className="flex items-center gap-3">
        <div className="w-12 h-12 rounded-2xl bg-indigo-500/10 border border-indigo-500/20 text-indigo-500 flex items-center justify-center text-2xl shrink-0">
          <FiUser />
        </div>
        <div>
          <h1 className="text-2xl sm:text-3xl font-bold tracking-tight text-slate-900 dark:text-white">
            My Profile
          </h1>
          <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400 font-normal mt-1">
            Manage your personal details, public bio, and avatar
          </p>
        </div>
      </div>

      {/* User Card */}
      <div className="card flex items-center gap-6 p-6">
        <img
          src={avatarSrc}
          alt="Profile"
          className="w-20 h-20 rounded-2xl object-cover ring-2 ring-indigo-500/30 shrink-0"
        />
        <div className="min-w-0">
          <h2 className="text-lg sm:text-xl font-bold tracking-tight text-slate-900 dark:text-white">
            {user?.full_name || user?.username}
          </h2>
          <p className="text-xs font-mono text-indigo-600 dark:text-indigo-400 font-semibold mt-0.5">
            @{user?.username}
          </p>
          <p className="text-xs text-slate-500 dark:text-slate-400 flex items-center gap-1.5 mt-1.5 font-mono">
            <FiMail /> {user?.email}
          </p>
        </div>
      </div>

      {message && (
        <div className={`rounded-xl p-3.5 text-xs font-semibold ${isError ? 'bg-rose-50 text-rose-700 border border-rose-200 dark:bg-rose-950/50 dark:text-rose-300 dark:border-rose-800' : 'bg-emerald-50 text-emerald-700 border border-emerald-200 dark:bg-emerald-950/50 dark:text-emerald-300 dark:border-emerald-800'}`}>
          {message}
        </div>
      )}

      {/* Profile Form */}
      <form onSubmit={handleSubmit} className="card p-6 space-y-5">
        <div>
          <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider mb-2">
            Profile Avatar
          </label>
          <div className="flex flex-wrap items-center gap-4">
            <img src={avatarSrc} alt="Profile preview" className="h-16 w-16 rounded-2xl object-cover ring-2 ring-indigo-500/20" />
            <input
              ref={fileInputRef}
              type="file"
              accept="image/png,image/jpeg,image/webp"
              onChange={handleAvatarUpload}
              className="hidden"
            />
            <button
              type="button"
              onClick={() => fileInputRef.current?.click()}
              disabled={uploadingAvatar}
              className="btn-secondary text-xs font-semibold"
            >
              <FiUpload className="mr-1.5" /> {uploadingAvatar ? 'Uploading...' : 'Upload Image'}
            </button>
            <span className="text-[11px] text-slate-400 font-mono">PNG, JPEG, or WebP · Max 5 MB</span>
          </div>
        </div>

        <div>
          <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider mb-1.5">
            Full Name
          </label>
          <input
            type="text"
            value={form.full_name}
            onChange={(e) => setForm({ ...form, full_name: e.target.value })}
            className="input text-sm font-medium"
            placeholder="Your full name"
          />
        </div>

        <div>
          <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider mb-1.5">
            Bio
          </label>
          <textarea
            value={form.bio}
            onChange={(e) => setForm({ ...form, bio: e.target.value })}
            className="input min-h-[100px] text-sm font-medium leading-relaxed"
            placeholder="Tell us about yourself..."
          />
        </div>

        <button type="submit" disabled={saving} className="btn-primary">
          <FiSave className="mr-1.5" /> {saving ? 'Saving Changes...' : 'Save Profile Changes'}
        </button>
      </form>
    </div>
  )
}

export default ProfilePage
