import { useRef, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { FiMail, FiSave, FiUpload } from 'react-icons/fi'
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

  const avatarSrc = form.avatar_url || `https://ui-avatars.com/api/?name=${user?.username || 'U'}`

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
      console.log('Uploading image to:', ENDPOINTS.uploadAvatar)
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
      console.error('Upload error:', {
        status: err.response?.status,
        data: err.response?.data,
        message: errorMessage,
      })
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
    <div className="max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold mb-8">My Profile</h1>

      <div className="card mb-6 flex items-center gap-6">
        <img
          src={avatarSrc}
          alt="Profile"
          className="w-20 h-20 rounded-full"
        />
        <div>
          <h2 className="text-xl font-bold">{user?.full_name || user?.username}</h2>
          <p className="text-gray-500">@{user?.username}</p>
          <p className="text-sm text-gray-400 flex items-center gap-1 mt-1">
            <FiMail /> {user?.email}
          </p>
        </div>
      </div>

      {message && (
        <div className={`mb-4 rounded-lg p-3 text-sm ${isError ? 'bg-red-100 text-red-700 dark:bg-red-950 dark:text-red-200' : 'bg-green-100 text-green-700 dark:bg-green-950 dark:text-green-200'}`}>
          {message}
        </div>
      )}

      <form onSubmit={handleSubmit} className="card space-y-4">
        <div>
          <label className="block text-sm font-medium mb-2">Profile Image</label>
          <div className="flex flex-wrap items-center gap-4">
            <img src={avatarSrc} alt="Profile preview" className="h-16 w-16 rounded-full object-cover ring-2 ring-primary-200 dark:ring-primary-700" />
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
              className="btn-secondary"
            >
              <FiUpload className="mr-2" /> {uploadingAvatar ? 'Uploading...' : 'Upload image'}
            </button>
            <span className="text-xs text-gray-500 dark:text-gray-400">PNG, JPEG, or WebP · Max 5 MB</span>
          </div>
        </div>
        <div>
          <label className="block text-sm font-medium mb-1">Full Name</label>
          <input
            type="text"
            value={form.full_name}
            onChange={(e) => setForm({ ...form, full_name: e.target.value })}
            className="input"
          />
        </div>
        <div>
          <label className="block text-sm font-medium mb-1">Bio</label>
          <textarea
            value={form.bio}
            onChange={(e) => setForm({ ...form, bio: e.target.value })}
            className="input min-h-[100px]"
            placeholder="Tell us about yourself..."
          />
        </div>
        <div>
          <label className="block text-sm font-medium mb-1">Avatar URL (optional)</label>
          <input
            type="url"
            value={form.avatar_url}
            onChange={(e) => setForm({ ...form, avatar_url: e.target.value })}
            className="input"
            placeholder="https://example.com/avatar.jpg"
          />
        </div>
        <button type="submit" disabled={saving} className="btn-primary">
          <FiSave className="mr-2" /> {saving ? 'Saving...' : 'Save Changes'}
        </button>
      </form>
    </div>
  )
}

export default ProfilePage
