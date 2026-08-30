import { useState, useEffect } from 'react'
import { FiBookmark, FiTrash2, FiArrowRight } from 'react-icons/fi'
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
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600"></div>
      </div>
    )
  }

  return (
    <div className="space-y-6 max-w-7xl mx-auto font-sans pb-16">
      {/* Header */}
      <div className="flex items-center gap-3">
        <div className="w-12 h-12 rounded-2xl bg-indigo-500/10 border border-indigo-500/20 text-indigo-500 flex items-center justify-center text-2xl shrink-0">
          <FiBookmark />
        </div>
        <div>
          <h1 className="text-2xl sm:text-3xl font-bold tracking-tight text-slate-900 dark:text-white">
            Saved Bookmarks
          </h1>
          <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400 font-normal mt-1">
            Fast access to your bookmarked topics, algorithms, and modules
          </p>
        </div>
      </div>

      {bookmarks.length === 0 ? (
        <div className="card text-center py-16 space-y-3">
          <div className="w-16 h-16 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-400 mx-auto flex items-center justify-center text-3xl">
            <FiBookmark />
          </div>
          <h2 className="text-lg sm:text-xl font-bold tracking-tight text-slate-800 dark:text-slate-200">
            No Bookmarks Saved Yet
          </h2>
          <p className="text-xs sm:text-sm text-slate-500 max-w-md mx-auto">
            Bookmark tricky interview topics or system design guides while studying to review them anytime here.
          </p>
        </div>
      ) : (
        <div className="space-y-3">
          {bookmarks.map((bookmark) => (
            <div key={bookmark.id} className="card p-4 sm:p-5 flex items-center justify-between gap-4 group hover:border-slate-300 dark:hover:border-slate-700 transition">
              <div className="flex items-center gap-3 min-w-0">
                <div className="w-9 h-9 rounded-xl bg-indigo-50 dark:bg-indigo-950/60 text-indigo-600 dark:text-indigo-400 flex items-center justify-center shrink-0">
                  <FiBookmark />
                </div>
                <div className="min-w-0">
                  <h3 className="text-base sm:text-lg font-semibold text-slate-900 dark:text-white tracking-normal truncate">
                    {bookmark.title}
                  </h3>
                  {bookmark.url && (
                    <Link to={bookmark.url} className="text-xs font-semibold text-indigo-600 dark:text-indigo-400 hover:underline flex items-center gap-1 mt-0.5">
                      Navigate to study content <FiArrowRight />
                    </Link>
                  )}
                </div>
              </div>

              <button
                onClick={() => deleteBookmark(bookmark.id)}
                className="text-slate-400 hover:text-rose-500 p-2 rounded-xl hover:bg-rose-50 dark:hover:bg-rose-950/50 transition shrink-0"
                aria-label="Delete bookmark"
              >
                <FiTrash2 className="w-4 h-4" />
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default BookmarksPage
