import { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'
import {
  FiArrowLeft,
  FiClock,
  FiChevronRight,
  FiBookOpen,
  FiClipboard,
  FiLayers,
  FiAward,
  FiCheckCircle,
  FiZap,
  FiCpu,
  FiGlobe,
  FiDatabase,
  FiShield,
  FiStar,
} from 'react-icons/fi'
import { apiClient } from '../../api/apiClient'
import { ENDPOINTS } from '../../api/endpoints'

const CourseDetail = () => {
  const { courseId } = useParams()
  const [course, setCourse] = useState(null)
  const [topics, setTopics] = useState([])
  const [loading, setLoading] = useState(true)
  const [activeModuleTab, setActiveModuleTab] = useState(0)

  useEffect(() => {
    const load = async () => {
      try {
        let courseData = null
        let targetCourseId = courseId

        try {
          const courseRes = await apiClient.get(ENDPOINTS.course(courseId))
          courseData = courseRes.data
        } catch {
          const { data: courses } = await apiClient.get(ENDPOINTS.courses)
          courseData =
            courses.find((c) => c.slug === 'final-evaluation-sde' || c.slug === 'WoWCodes') ||
            courses[0]
          targetCourseId = courseData?.id
        }

        if (courseData) {
          setCourse(courseData)
          const topicsRes = await apiClient.get(ENDPOINTS.topicsByCourse(targetCourseId || courseData.id))
          setTopics(topicsRes.data)
        }
      } catch (err) {
        console.error('Failed to load course details:', err)
      } finally {
        setLoading(false)
      }
    }
    load()
  }, [courseId])

  if (loading) {
    return (
      <div className="flex flex-col items-center justify-center h-64 space-y-3">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600"></div>
        <p className="text-sm text-slate-400">Loading Program Modules...</p>
      </div>
    )
  }

  if (!course) {
    return (
      <div className="text-center py-12 bg-slate-900 border border-slate-800 rounded-3xl p-8 max-w-md mx-auto">
        <h2 className="text-xl font-semibold text-white">Program Not Found</h2>
        <Link to="/learn" className="px-4 py-2 bg-indigo-600 text-white rounded-xl text-xs font-bold mt-4 inline-block">
          Back to Program Overview
        </Link>
      </div>
    )
  }

  // 6 Structured Modules + 1 Capstone Definition
  const moduleTabs = [
    {
      num: 'MODULE 01',
      name: 'Front-End Web Development',
      desc: 'HTML5, CSS3, JavaScript, React 19, Redux Toolkit, Node.js & Express.js',
      matchKeywords: ['html', 'css', 'javascript', 'react', 'redux', 'fe-js', 'nodejs', 'express']
    },
    {
      num: 'MODULE 02',
      name: 'Python & Data Structures',
      desc: 'Python programming core, memory reference model, and algorithmic problem solving',
      matchKeywords: ['python', 'python-core', 'dsa']
    },
    {
      num: 'MODULE 03',
      name: 'FastAPI Backend & REST APIs',
      desc: 'High-performance asynchronous backend services, Pydantic v2, and HTTP specs',
      matchKeywords: ['fastapi', 'sql', 'fastapi-arch', 'apis']
    },
    {
      num: 'MODULE 04',
      name: 'Version Control & DevOps',
      desc: 'Distributed version control, GitHub enterprise workflows, and rebase strategies',
      matchKeywords: ['git', 'vcs']
    },
    {
      num: 'MODULE 05',
      name: 'Databases & ORM Integration',
      desc: 'Relational vs NoSQL architecture, SQL execution optimization, and SQLAlchemy ORM',
      matchKeywords: ['db-sql', 'nosql', 'orm']
    },
    {
      num: 'MODULE 06',
      name: 'LLM Engineering & Applied AI',
      desc: 'Transformer pipeline, self-attention, RAG architecture, vector embeddings, and AI observability',
      matchKeywords: ['llms', 'rag', 'ai-dev']
    },
    {
      num: 'MODULE 07',
      name: 'Final 100-Mark Capstone Exam',
      desc: '50 High-Stakes Employer Questions (100 Marks) + Practical Capstone Project Submission',
      matchKeywords: ['certification-exam']
    }
  ]

  // Filter topics for active module tab
  const currentTab = moduleTabs[activeModuleTab]
  const activeTopics = topics.filter((t) => {
    if (currentTab.num === 'MODULE 07') {
      return t.slug.includes('certification-exam')
    }
    return currentTab.matchKeywords.some((kw) => t.slug.toLowerCase().includes(kw))
  })

  return (
    <div className="space-y-6 max-w-7xl mx-auto font-sans pb-16 px-2 sm:px-4">
      <Link to="/learn" className="inline-flex items-center gap-2 text-slate-400 hover:text-indigo-400 transition font-bold text-xs sm:text-sm">
        <FiArrowLeft /> Back to Program Overview
      </Link>

      {/* Course Header Banner */}
      <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 sm:p-8 shadow-xl text-white">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div className="space-y-2">
            <span className="text-xs px-2.5 py-0.5 rounded-full bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 uppercase font-semibold font-mono">
              Certificate Program
            </span>
            <h1 className="text-2xl sm:text-3xl font-black text-white">Certificate of Software Development Engineering Program</h1>
            <p className="text-slate-300 text-xs sm:text-sm max-w-3xl leading-relaxed">{course.description}</p>
          </div>
          <div className="bg-slate-950 p-4 rounded-2xl border border-slate-800 text-center shrink-0 font-mono self-start sm:self-auto w-full sm:w-auto">
            <p className="text-xs text-slate-400">Total Program Topics</p>
            <p className="text-2xl font-black text-indigo-400">{topics.length} Topics</p>
          </div>
        </div>
      </div>

      {/* 3 Tabs Per Row Grid */}
      <div className="space-y-3">
        <h2 className="text-base font-black text-slate-900 dark:text-white flex items-center gap-2">
          <FiLayers className="text-indigo-500" /> Select Module Learning Path
        </h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {moduleTabs.map((tab, idx) => {
            const isActive = activeModuleTab === idx
            return (
              <button
                key={idx}
                onClick={() => setActiveModuleTab(idx)}
                className={`p-5 rounded-2xl text-left transition-all border flex flex-col justify-between space-y-3 relative overflow-hidden group ${
                  isActive
                    ? 'bg-slate-900 border-indigo-500 text-white ring-2 ring-indigo-500/40 shadow-lg shadow-indigo-500/20'
                    : 'bg-slate-900/80 hover:bg-slate-900 border-slate-800 text-slate-200 hover:border-slate-700'
                }`}
              >
                {isActive && (
                  <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-indigo-500 via-purple-500 to-emerald-400" />
                )}
                <div className="flex items-center justify-between">
                  <span className={`text-[11px] font-mono font-black px-2 py-0.5 rounded border ${
                    isActive ? 'bg-indigo-500/20 text-indigo-300 border-indigo-500/30' : 'bg-slate-950 text-slate-400 border-slate-800'
                  }`}>
                    {tab.num}
                  </span>
                </div>
                <div>
                  <h3 className={`text-base sm:text-lg font-semibold leading-snug tracking-normal ${isActive ? 'text-white' : 'text-slate-100 group-hover:text-indigo-300'}`}>
                    {tab.name}
                  </h3>
                  <p className="text-xs text-slate-400 mt-1 line-clamp-2 leading-relaxed font-normal">{tab.desc}</p>
                </div>
              </button>
            )
          })}
        </div>
      </div>

      {/* Module Topics Display */}
      <div className="bg-slate-900 border border-slate-800 rounded-3xl p-5 sm:p-8 shadow-xl space-y-4">
        <div className="pb-3 border-b border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <h3 className="text-lg font-black text-white">{currentTab.name} Topics</h3>
          <span className="text-xs px-3 py-1 rounded-full bg-slate-800 text-slate-200 font-mono font-bold self-start sm:self-auto">
            {activeTopics.length} Topics
          </span>
        </div>

        <div className="space-y-3">
          {activeTopics.map((topic, index) => (
            <Link
              key={topic.id}
              to={`/learn/topic/${topic.id}`}
              className="p-4 sm:p-5 rounded-2xl bg-slate-950 border border-slate-800 hover:border-indigo-500/60 transition flex flex-col sm:flex-row sm:items-center justify-between gap-4 group"
            >
              <div className="flex items-center gap-4">
                <div className="w-9 h-9 rounded-xl bg-indigo-600/20 text-indigo-400 border border-indigo-500/30 flex items-center justify-center font-bold text-xs font-mono shrink-0">
                  {index + 1}
                </div>
                <div>
                  <h4 className="font-bold text-slate-100 group-hover:text-indigo-300 transition text-sm">
                    {topic.title}
                  </h4>
                  <p className="text-xs text-slate-400 line-clamp-1 mt-0.5">{topic.description}</p>
                </div>
              </div>

              <div className="flex items-center justify-between sm:justify-end gap-3 w-full sm:w-auto pt-2 sm:pt-0 border-t sm:border-t-0 border-slate-800/60">
                <span className="text-[11px] text-slate-300 font-mono bg-slate-900 px-3 py-1 rounded-full border border-slate-800 flex items-center gap-1 font-semibold">
                  <FiStar className="text-amber-400 w-3 h-3" /> 10-Q Employer Quiz
                </span>
                <FiChevronRight className="text-slate-500 group-hover:text-indigo-400 group-hover:translate-x-1 transition" />
              </div>
            </Link>
          ))}

          {activeTopics.length === 0 && (
            <p className="text-slate-400 text-center py-8 text-xs font-mono">
              All topics in this module are active under the primary curriculum.
            </p>
          )}
        </div>
      </div>
    </div>
  )
}

export default CourseDetail
