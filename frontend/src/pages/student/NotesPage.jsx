import { useState, useEffect } from 'react'
import { FiPlus, FiTrash2, FiFileText, FiBookOpen } from 'react-icons/fi'
import { apiClient } from '../../api/apiClient'
import { ENDPOINTS } from '../../api/endpoints'

const NotesPage = () => {
  const [notes, setNotes] = useState([])
  const [loading, setLoading] = useState(true)
  const [showForm, setShowForm] = useState(false)
  const [form, setForm] = useState({ topic_id: 14, title: '', content: '' })

  useEffect(() => {
    apiClient.get(ENDPOINTS.notes)
      .then((res) => {
        setNotes(res.data)
        setLoading(false)
      })
      .catch(() => setLoading(false))
  }, [])

  const createNote = async (e) => {
    e.preventDefault()
    if (!form.title) return
    const { data } = await apiClient.post(ENDPOINTS.notes, form)
    setNotes([data, ...notes])
    setShowForm(false)
    setForm({ topic_id: 14, title: '', content: '' })
  }

  const deleteNote = async (id) => {
    await apiClient.delete(ENDPOINTS.note(id))
    setNotes(notes.filter((n) => n.id !== id))
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600"></div>
      </div>
    )
  }

  return (
    <div className="space-y-6 max-w-7xl mx-auto font-sans pb-3 sm:pb-8 text-left">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 text-left">
        <div className="flex items-start gap-3 text-left">
          <div className="w-11 h-11 sm:w-12 sm:h-12 rounded-2xl bg-indigo-500/10 border border-indigo-500/20 text-indigo-500 flex items-center justify-center text-xl sm:text-2xl shrink-0 mt-0.5">
            <FiFileText />
          </div>
          <div className="text-left">
            <h1 className="text-xl sm:text-2xl lg:text-3xl font-bold tracking-tight text-slate-900 dark:text-white">
              My Engineering Study Notes
            </h1>
            <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400 font-normal mt-0.5">
              Capture code snippets, system design insights, and interview tips
            </p>
          </div>
        </div>

        <button onClick={() => setShowForm(!showForm)} className="btn-primary self-start sm:self-auto w-fit shrink-0 whitespace-nowrap">
          <FiPlus className="mr-1.5 shrink-0" /> {showForm ? 'Cancel Note' : 'Create New Note'}
        </button>
      </div>

      {showForm && (
        <form onSubmit={createNote} className="card p-6 space-y-4 border border-indigo-500/30">
          <h2 className="text-lg sm:text-xl font-bold tracking-tight text-slate-900 dark:text-white">
            Add New Study Note
          </h2>
          <input
            type="text"
            placeholder="Note title (e.g. Redux Toolkit vs Zustand Architecture)"
            value={form.title}
            onChange={(e) => setForm({ ...form, title: e.target.value })}
            className="input text-sm font-medium"
            required
          />
          <textarea
            placeholder="Write your technical study notes here..."
            value={form.content}
            onChange={(e) => setForm({ ...form, content: e.target.value })}
            className="input min-h-[120px] text-sm font-medium leading-relaxed"
          />
          <button type="submit" className="btn-primary">
            Save Note
          </button>
        </form>
      )}

      {notes.length === 0 ? (
        <div className="card text-center py-16 space-y-3">
          <div className="w-16 h-16 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-400 mx-auto flex items-center justify-center text-3xl">
            <FiFileText />
          </div>
          <h2 className="text-lg sm:text-xl font-bold tracking-tight text-slate-800 dark:text-slate-200">
            No Study Notes Created Yet
          </h2>
          <p className="text-xs sm:text-sm text-slate-500 max-w-md mx-auto">
            Click 'Create New Note' above to start organizing your key algorithmic patterns and interview tips.
          </p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          {notes.map((note) => (
            <div key={note.id} className="card p-5 space-y-3 flex flex-col justify-between hover:border-slate-300 dark:hover:border-slate-700 transition">
              <div>
                <h3 className="text-base sm:text-lg font-semibold text-slate-900 dark:text-white tracking-normal line-clamp-1">
                  {note.title}
                </h3>
                <p className="text-xs text-slate-600 dark:text-slate-300 mt-2 line-clamp-4 leading-relaxed whitespace-pre-wrap font-normal">
                  {note.content}
                </p>
              </div>

              <div className="flex items-center justify-between pt-3 border-t border-slate-100 dark:border-slate-800/80 text-xs text-slate-400">
                <span className="font-mono text-[11px]">{new Date(note.created_at).toLocaleDateString()}</span>
                <button
                  onClick={() => deleteNote(note.id)}
                  className="text-rose-500 hover:text-rose-600 p-1 rounded-lg hover:bg-rose-50 dark:hover:bg-rose-950/50 transition"
                  aria-label="Delete note"
                >
                  <FiTrash2 className="w-4 h-4" />
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default NotesPage
