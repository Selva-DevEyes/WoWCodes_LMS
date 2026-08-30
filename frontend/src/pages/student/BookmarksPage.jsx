import { useState, useEffect } from 'react'
import { FiBookmark, FiTrash2 } from 'react-icons/fi'
import { Link } from 'react-router-dom'
import { apiClient } from '../../api/apiClient'
import { ENDPOINTS } from '../../api/endpoints'

const BookmarksPage = () => {
  const [bookmarks, setBookmarks] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    apiClient.get(ENDPOINTS.bookmarks)
      .then((res) => {
        setBookmarks(res.data)
        setLoading(false)
      })
      .catch(() => setLoading(false))
  }, [])

  const deleteBookmark = async (id) => {
    await apiClient.delete(ENDPOINTS.bookmark(id))
    setBookmarks(bookmarks.filter((b) => b.id !== id))
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>
    )
  }

  return (
    <div>
      <div className="flex items-center gap-3 mb-8">
        <FiBookmark className="text-3xl text-primary-600" />
        <div>
          <h1 className="text-2xl font-bold">Bookmarks</h1>
          <p className="text-gray-500 text-sm">Your saved topics and lessons</p>
        </div>
      </div>

      {bookmarks.length === 0 ? (
        <div className="card text-center py-16">
          <FiBookmark className="text-6xl text-gray-300 mx-auto mb-4" />
          <p className="text-gray-500">No bookmarks yet. Save topics to access them quickly!</p>
        </div>
      ) : (
        <div className="space-y-3">
          {bookmarks.map((bookmark) => (
            <div key={bookmark.id} className="card flex items-center gap-4 group">
              <div className="flex-1">
                <h3 className="font-semibold">{bookmark.title}</h3>
                {bookmark.url && (
                  <Link to={bookmark.url} className="text-sm text-primary-600 hover:underline">
                    View content
                  </Link>
                )}
              </div>
              <button
                onClick={() => deleteBookmark(bookmark.id)}
                className="p-2 text-gray-400 hover:text-red-600 opacity-0 group-hover:opacity-100 transition-opacity"
              >
                <FiTrash2 />
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default BookmarksPage
