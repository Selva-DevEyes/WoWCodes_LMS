import { useEffect, useState } from 'react'
import { useParams, Link, useNavigate } from 'react-router-dom'
import {
  FiArrowLeft,
  FiCheckCircle,
  FiClipboard,
  FiFileText,
  FiCode,
  FiGithub,
  FiGlobe,
  FiAward,
  FiCheck,
  FiLayers,
  FiUpload,
} from 'react-icons/fi'
import { apiClient } from '../../api/apiClient'
import { ENDPOINTS } from '../../api/endpoints'
import QuizCard from '../../components/quiz/QuizCard'
import CodePlayground from '../../components/CodePlayground'

const TopicDetail = () => {
  const { topicId } = useParams()
  const navigate = useNavigate()
  const [topic, setTopic] = useState(null)
  const [quizzes, setQuizzes] = useState([])
  const [lessons, setLessons] = useState([])
  const [loading, setLoading] = useState(true)
  const [completed, setCompleted] = useState(false)

  // Project Submission Form State
  const [projectTitle, setProjectTitle] = useState('')
  const [githubUrl, setGithubUrl] = useState('')
  const [liveUrl, setLiveUrl] = useState('')
  const [notes, setNotes] = useState('')
  const [submittingProject, setSubmittingProject] = useState(false)
  const [submissionResult, setSubmissionResult] = useState(null)

  useEffect(() => {
    const load = async () => {
      try {
        const [topicRes, quizRes, lessonRes] = await Promise.all([
          apiClient.get(ENDPOINTS.topic(topicId)),
          apiClient.get(ENDPOINTS.quizzesByTopic(topicId)),
          apiClient.get(ENDPOINTS.lessonsByTopic(topicId)),
        ])
        setTopic(topicRes.data)
        setQuizzes(quizRes.data)
        setLessons(lessonRes.data)
      } catch (err) {
        console.error('Failed to fetch topic details:', err)
      } finally {
        setLoading(false)
      }
    }
    load()
  }, [topicId])

  const markComplete = async () => {
    try {
      await apiClient.post(ENDPOINTS.topicProgress(topicId), { is_completed: true })
      setCompleted(true)
    } catch (err) {
      console.error('Failed to update progress:', err)
    }
  }

  const handleProjectSubmit = async (e) => {
    e.preventDefault()
    if (!projectTitle || !githubUrl) return
    setSubmittingProject(true)
    try {
      const payload = {
        course_id: topic.course_id,
        project_title: projectTitle,
        github_url: githubUrl,
        live_demo_url: liveUrl,
        architecture_notes: notes,
      }
      const { data } = await apiClient.post('/projects/submit', payload)
      setSubmissionResult(data)
    } catch (err) {
      console.error('Failed to submit project:', err)
    } finally {
      setSubmittingProject(false)
    }
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600"></div>
      </div>
    )
  }

  if (!topic) {
    return (
      <div className="p-6 text-center">
        <p className="text-gray-500">Topic not found.</p>
        <Link to="/learn" className="text-indigo-600 font-medium mt-2 inline-block">Back to Courses</Link>
      </div>
    )
  }

  const isFinalExamTopic = topic.slug?.includes('final-sde-certification-exam')

  return (
    <div className="space-y-6 max-w-7xl mx-auto font-sans pb-16">
      <Link to="/learn" className="inline-flex items-center gap-2 text-slate-400 hover:text-indigo-400 transition font-medium text-sm">
        <FiArrowLeft /> Back to Learning Paths
      </Link>

      {/* Main Header Banner */}
      <div className="card border border-slate-200 dark:border-slate-800 bg-slate-900 text-white p-6 sm:p-8 rounded-3xl shadow-xl">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <div className="flex items-center gap-2 mb-2">
              <span className="text-xs px-2.5 py-0.5 rounded-full bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 uppercase font-semibold font-mono">
                {isFinalExamTopic ? 'Certification Capstone' : 'Topic Module'}
              </span>
            </div>
            <h1 className="text-2xl sm:text-3xl font-black text-white">{topic.title}</h1>
            <p className="text-slate-300 text-sm max-w-3xl mt-2 leading-relaxed">{topic.description}</p>
          </div>
          <button
            onClick={markComplete}
            className={`px-5 py-2.5 rounded-2xl text-xs font-bold transition flex items-center gap-2 self-start sm:self-auto ${
              completed ? 'bg-emerald-600 text-white shadow-lg shadow-emerald-600/30' : 'bg-indigo-600 hover:bg-indigo-500 text-white'
            }`}
          >
            <FiCheckCircle /> {completed ? 'Topic Completed!' : 'Mark as Complete'}
          </button>
        </div>
      </div>

      {/* Capstone Project Submission Portal for Final Evaluation Exam */}
      {isFinalExamTopic && (
        <div className="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 border border-indigo-500/30 rounded-3xl p-6 sm:p-8 shadow-2xl space-y-6 text-white">
          <div className="flex items-center gap-3 border-b border-indigo-500/20 pb-4">
            <div className="p-3 bg-indigo-600/20 text-indigo-400 rounded-2xl border border-indigo-500/30">
              <FiUpload className="w-6 h-6" />
            </div>
            <div>
              <h2 className="text-xl font-black text-white">Practical Capstone Project Submission</h2>
              <p className="text-xs text-slate-300">Submit your final Software Development Engineering capstone project to generate your Certificate.</p>
            </div>
          </div>

          {submissionResult ? (
            <div className="p-6 rounded-2xl bg-emerald-950/40 border border-emerald-500/40 text-emerald-100 text-center space-y-4">
              <FiAward className="w-16 h-16 text-emerald-400 mx-auto animate-bounce" />
              <h3 className="text-2xl font-black text-white">Capstone Evaluation Approved! 🎉</h3>
              <p className="text-sm text-slate-300 max-w-md mx-auto">
                Your practical project has been evaluated and your official certification certificate has been generated!
              </p>
              <div className="inline-block bg-slate-950 px-6 py-3 rounded-2xl border border-emerald-500/30 font-mono text-indigo-300 font-extrabold text-lg">
                Certificate ID: {submissionResult.certificate_code}
              </div>
              <div>
                <Link
                  to="/certificates"
                  className="px-6 py-3 bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs rounded-xl inline-flex items-center gap-2 transition"
                >
                  View & Download Official Certificate <FiAward />
                </Link>
              </div>
            </div>
          ) : (
            <form onSubmit={handleProjectSubmit} className="space-y-4">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label className="block text-xs font-semibold text-slate-300 mb-1">Project Title *</label>
                  <input
                    type="text"
                    required
                    placeholder="e.g. Enterprise Full-Stack E-Commerce System"
                    value={projectTitle}
                    onChange={(e) => setProjectTitle(e.target.value)}
                    className="w-full px-4 py-3 bg-slate-950 border border-slate-800 rounded-xl text-xs text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500"
                  />
                </div>
                <div>
                  <label className="block text-xs font-semibold text-slate-300 mb-1 flex items-center gap-1">
                    <FiGithub /> GitHub Repository URL *
                  </label>
                  <input
                    type="url"
                    required
                    placeholder="https://github.com/your-username/repo-name"
                    value={githubUrl}
                    onChange={(e) => setGithubUrl(e.target.value)}
                    className="w-full px-4 py-3 bg-slate-950 border border-slate-800 rounded-xl text-xs text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500"
                  />
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label className="block text-xs font-semibold text-slate-300 mb-1 flex items-center gap-1">
                    <FiGlobe /> Live Demo Application URL (Optional)
                  </label>
                  <input
                    type="url"
                    placeholder="https://my-app.vercel.app"
                    value={liveUrl}
                    onChange={(e) => setLiveUrl(e.target.value)}
                    className="w-full px-4 py-3 bg-slate-950 border border-slate-800 rounded-xl text-xs text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500"
                  />
                </div>
                <div>
                  <label className="block text-xs font-semibold text-slate-300 mb-1 flex items-center gap-1">
                    <FiLayers /> Architecture & Design Notes
                  </label>
                  <input
                    type="text"
                    placeholder="FastAPI + React 19 + PostgreSQL + RAG AI Engine"
                    value={notes}
                    onChange={(e) => setNotes(e.target.value)}
                    className="w-full px-4 py-3 bg-slate-950 border border-slate-800 rounded-xl text-xs text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500"
                  />
                </div>
              </div>

              <button
                type="submit"
                disabled={submittingProject}
                className="w-full py-3.5 bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-500 hover:to-purple-500 text-white font-extrabold text-xs rounded-xl shadow-lg shadow-indigo-600/30 transition flex items-center justify-center gap-2"
              >
                {submittingProject ? 'Evaluating Capstone Project...' : 'Submit Project & Issue Software Engineering Certificate'}
              </button>
            </form>
          )}
        </div>
      )}

      {/* Lesson Content Markdown */}
      {topic.content && (
        <div className="card border border-slate-200 dark:border-slate-800 p-6 sm:p-8 rounded-3xl">
          <h2 className="text-lg font-bold text-slate-900 dark:text-white mb-4">Engineering Study Guide Notes</h2>
          <div className="prose max-w-none dark:prose-invert text-slate-700 dark:text-slate-300 whitespace-pre-wrap leading-relaxed">
            {topic.content}
          </div>
        </div>
      )}

      {/* Embedded Live Code Playground */}
      <div className="space-y-3">
        <div className="flex items-center gap-2 text-slate-900 dark:text-white font-bold text-lg">
          <FiCode className="text-indigo-500" /> Interactive Practice Playground
        </div>
        <CodePlayground
          initialCode={`// Interactive Sandbox for: ${topic.title}\nconsole.log("Testing ${topic.title}...");\n\n// Write your algorithm or backend test code below:`}
        />
      </div>

      {lessons.length > 0 && (
        <div className="card border border-slate-200 dark:border-slate-800 p-6 rounded-3xl">
          <h2 className="text-lg font-bold text-slate-900 dark:text-white mb-4 flex items-center gap-2">
            <FiFileText /> Supplemental Masterclass Lessons
          </h2>
          <div className="space-y-3">
            {lessons.map((lesson) => (
              <div key={lesson.id} className="p-4 bg-slate-50 dark:bg-slate-800/60 rounded-2xl border border-slate-200/50 dark:border-slate-700/50">
                <h3 className="font-semibold text-slate-900 dark:text-white">{lesson.title}</h3>
                <p className="text-sm text-slate-600 dark:text-slate-300 mt-1">{lesson.content}</p>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Quizzes Section */}
      {quizzes.length > 0 && (
        <div className="space-y-4">
          <h2 className="text-lg font-bold text-slate-900 dark:text-white flex items-center gap-2">
            <FiClipboard /> Employer-Side Technical Evaluation Quizzes
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {quizzes.map((quiz) => (
              <QuizCard key={quiz.id} quiz={quiz} />
            ))}
          </div>
        </div>
      )}
    </div>
  )
}

export default TopicDetail
