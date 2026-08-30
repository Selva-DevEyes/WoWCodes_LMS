import { useState, useEffect } from 'react'
import { FiPlus, FiTrash2, FiEdit2, FiFileText } from 'react-icons/fi'
import { apiClient } from '../../api/apiClient'
import { ENDPOINTS } from '../../api/endpoints'

const NotesPage = () => {
  const [notes, setNotes] = useState([])
  const [loading, setLoading] = useState(true)
  const [showForm, setShowForm] = useState(false)
  const [form, setForm] = useState({ topic_id: 1, title: '', content: '' })

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
    const { data } = await apiClient.post(ENDPOINTS.notes, form)
    setNotes([data, ...notes])
    setShowForm(false)
    setForm({ topic_id: 1, title: '', content: '' })
  }

  const deleteNote = async (id) => {
    await apiClient.delete(ENDPOINTS.note(id))
    setNotes(notes.filter((n) => n.id !== id))
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
      <div className="flex items-center justify-between mb-8">
        <div className="flex items-center gap-3">
          <FiFileText className="text-3xl text-primary-600" />
          <div>
            <h1 className="text-2xl font-bold">My Notes</h1>
            <p className="text-gray-500 text-sm">Capture and organize your learning notes</p>
          </div>
        </div>
        <button onClick={() => setShowForm(!showForm)} className="btn-primary">
          <FiPlus className="mr-2" /> New Note
        </button>
      </div>

      {showForm && (
        <form onSubmit={createNote} className="card mb-6 space-y-4">
          <input
            type="text"
            placeholder="Note title"
            value={form.title}
            onChange={(e) => setForm({ ...form, title: e.target.value })}
            className="input"
            required
          />
          <textarea
            placeholder="Write your note..."
            value={form.content}
            onChange={(e) => setForm({ ...form, content: e.target.value })}
            className="input min-h-[120px]"
            required
          />
          <button type="submit" className="btn-primary">Save Note</button>
        </form>
      )}

      {notes.length === 0 ? (
        <div className="card text-center py-16">
          <FiFileText className="text-6xl text-gray-300 mx-auto mb-4" />
          <p className="text-gray-500">No notes yet. Create your first note!</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {notes.map((note) => (
            <div key={note.id} className="card group relative">
              <button
                onClick={() => deleteNote(note.id)}
                className="absolute top-4 right-4 p-2 text-gray-400 hover:text-red-600 opacity-0 group-hover:opacity-100 transition-opacity"
              >
                <FiTrash2 />
              </button>
              <h3 className="font-semibold mb-2 pr-8">{note.title}</h3>
              <p className="text-sm text-gray-600 dark:text-gray-400 line-clamp-5 whitespace-pre-wrap">
                {note.content}
              </p>
              <p className="text-xs text-gray-400 mt-4">
                {new Date(note.updated_at).toLocaleDateString()}
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default NotesPage
