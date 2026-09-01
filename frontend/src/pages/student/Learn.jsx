import { useEffect, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import {
  FiBookOpen,
  FiCheckCircle,
  FiClock,
  FiAward,
  FiChevronRight,
  FiZap,
  FiLayers,
  FiCode,
  FiCpu,
  FiGlobe,
  FiDatabase,
  FiShield,
  FiArrowRight,
  FiStar,
} from 'react-icons/fi'
import { apiClient } from '../../api/apiClient'
import { ENDPOINTS } from '../../api/endpoints'

const Learn = () => {
  const navigate = useNavigate()
  const [course, setCourse] = useState(null)
  const [topics, setTopics] = useState([])
  const [loading, setLoading] = useState(true)
  const [activeModuleTab, setActiveModuleTab] = useState(0)

  useEffect(() => {
    const loadProgram = async () => {
      try {
        const { data: courses } = await apiClient.get(ENDPOINTS.courses)
        const mainCourse =
          courses.find((c) => c.slug === 'final-evaluation-sde' || c.slug === 'WoWCodes') ||
          courses[0]

        if (mainCourse) {
          setCourse(mainCourse)
          const { data: topicList } = await apiClient.get(ENDPOINTS.topicsByCourse(mainCourse.id))
          setTopics(topicList)
        }
      } catch (err) {
        console.error('Failed to load program modules:', err)
      } finally {
        setLoading(false)
      }
    }
    loadProgram()
  }, [])

  if (loading) {
    return (
      <div className="flex flex-col items-center justify-center h-64 space-y-3">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600"></div>
        <p className="text-sm text-slate-400 font-medium">Loading Certificate Program Modules...</p>
      </div>
    )
  }

  // 6 Structured Modules + 1 Capstone Exam Definition
  const moduleTabs = [
    {
      num: 'MODULE 01',
      name: 'Front-End Web Development',
      desc: 'HTML5, CSS3, JavaScript, React 19, Redux Toolkit, Node.js & Express.js',
      keywords: ['html', 'css', 'javascript', 'react', 'redux', 'fe-js', 'nodejs', 'express']
    },
    {
      num: 'MODULE 02',
      name: 'Python & Data Structures',
      desc: 'Python programming core, memory reference model, and algorithmic problem solving',
      keywords: ['python', 'python-core', 'dsa']
    },
    {
      num: 'MODULE 03',
      name: 'FastAPI Backend & REST APIs',
      desc: 'High-performance asynchronous backend services, Pydantic v2, and HTTP specs',
      keywords: ['fastapi', 'sql', 'fastapi-arch', 'apis']
    },
    {
      num: 'MODULE 04',
      name: 'Version Control & DevOps',
      desc: 'Distributed version control, GitHub enterprise workflows, and rebase strategies',
      keywords: ['git', 'vcs']
    },
    {
      num: 'MODULE 05',
      name: 'Databases & ORM Integration',
      desc: 'Relational vs NoSQL architecture, SQL execution optimization, and SQLAlchemy ORM',
      keywords: ['db-sql', 'nosql', 'orm']
    },
    {
      num: 'MODULE 06',
      name: 'LLM Engineering & Applied AI',
      desc: 'Transformer pipeline, self-attention, RAG architecture, vector embeddings, and AI observability',
      keywords: ['llms', 'rag', 'ai-dev']
    },
    {
      num: 'MODULE 07',
      name: 'Final 100-Mark Capstone Exam',
      desc: '50 High-Stakes Employer Questions (100 Marks) + Practical Capstone Project Submission',
      keywords: ['certification-exam']
    }
  ]

  const currentTab = moduleTabs[activeModuleTab]

  // Filter topics for active module tab from real DB topic list
  const activeTopics = topics.filter((t) => {
    if (currentTab.num === 'MODULE 07') {
      return t.slug.includes('certification-exam')
    }
    return currentTab.keywords.some((kw) => t.slug.toLowerCase().includes(kw))
  })

  return (
    <div className="space-y-6 max-w-7xl mx-auto font-sans pb-3 sm:pb-8 px-2 sm:px-4 text-left">
      {/* Hero Banner Header - Fully Responsive Mobile Stack */}
      <div className="relative overflow-hidden bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 border border-indigo-500/30 rounded-3xl p-6 sm:p-10 shadow-2xl text-white">
        <div className="absolute -right-24 -top-24 w-96 h-96 bg-indigo-500/10 rounded-full blur-3xl pointer-events-none" />
        <div className="relative z-10 flex flex-col lg:flex-row lg:items-center justify-between gap-6">
          <div className="space-y-3 max-w-3xl">
            <div className="flex flex-wrap items-center gap-2">
              <span className="inline-flex items-center gap-1.5 text-xs font-bold px-3 py-1 rounded-full bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 font-mono whitespace-nowrap shrink-0">
                <FiZap className="text-yellow-400 animate-pulse shrink-0" /> Flagship Track
              </span>
              <span className="inline-flex items-center gap-1 text-xs px-2.5 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 font-semibold border border-emerald-500/30 font-mono whitespace-nowrap shrink-0">
                <FiShield className="shrink-0" /> 100 Marks Capstone
              </span>
            </div>
            <h1 className="text-2xl sm:text-3xl lg:text-4xl font-black text-white tracking-tight leading-tight">
              Certificate of Software Development Engineering Program
            </h1>
            <p className="text-slate-300 text-xs sm:text-sm leading-relaxed">
              Master Front-End Engineering, Python & DSA, FastAPI Backend, DevOps, Databases, and LLM Applied AI Integration. Select a module tab below to complete employer-perspective quizzes and unlock your final Certificate.
            </p>
          </div>

          <div className="bg-slate-950 p-5 rounded-2xl border border-slate-800 text-center flex flex-col items-center justify-center whitespace-nowrap min-w-[210px] w-full sm:w-auto shadow-inner">
            <p className="text-[11px] text-slate-400 uppercase font-mono tracking-wider font-bold">Curriculum Structure</p>
            <p className="text-3xl font-black text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-emerald-400 font-mono mt-1">
              6 Modules
            </p>
            <p className="text-xs text-slate-400 mt-1 font-mono font-medium">{topics.length} Total Program Topics</p>
          </div>
        </div>
      </div>

      {/* Select Module Learning Path Tabs (3 per row on desktop, high contrast text) */}
      <div className="space-y-4">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <h2 className="text-lg sm:text-xl font-black text-slate-900 dark:text-white flex items-center gap-2">
            <FiLayers className="text-indigo-500" /> Select Module Learning Path
          </h2>
          <span className="text-xs px-3 py-1 rounded-full bg-slate-200 dark:bg-slate-800 text-slate-800 dark:text-slate-200 font-mono font-extrabold self-start sm:self-auto">
            {moduleTabs.length} Modules Available
          </span>
        </div>

        {/* 3 Tabs Per Row Grid with Clean Icon-Free Design */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {moduleTabs.map((tab, idx) => {
            const isActive = activeModuleTab === idx
            return (
              <button
                key={idx}
                onClick={() => setActiveModuleTab(idx)}
                className={`p-5 rounded-2xl text-left transition-all duration-200 border flex flex-col justify-between space-y-3 relative overflow-hidden group ${
                  isActive
                    ? 'bg-slate-900 border-indigo-500 text-white shadow-xl shadow-indigo-500/20 ring-2 ring-indigo-500/40 scale-[1.01]'
                    : 'bg-slate-950 hover:bg-slate-900 border-slate-800 text-slate-200 hover:border-slate-700'
                }`}
              >
                {/* Active Indicator Top Highlight Bar */}
                {isActive && (
                  <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-indigo-500 via-purple-500 to-emerald-400" />
                )}

                <div className="flex items-center justify-between">
                  <span className={`text-[11px] font-mono font-black px-2.5 py-0.5 rounded-md border ${
                    isActive ? 'bg-indigo-500/20 text-indigo-300 border-indigo-500/40' : 'bg-slate-950 text-slate-400 border-slate-800'
                  }`}>
                    {tab.num}
                  </span>

                  {isActive && (
                    <span className="flex h-2.5 w-2.5 relative">
                      <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75" />
                      <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-emerald-500" />
                    </span>
                  )}
                </div>

                <div>
                  <h3 className={`text-base sm:text-lg font-semibold leading-snug tracking-normal ${isActive ? 'text-white' : 'text-slate-100 group-hover:text-indigo-300'}`}>
                    {tab.name}
                  </h3>
                  <p className="text-xs text-slate-400 mt-1 line-clamp-2 leading-relaxed font-normal">
                    {tab.desc}
                  </p>
                </div>
              </button>
            )
          })}
        </div>
      </div>

      {/* Active Module Topics Section */}
      <div className="bg-slate-900 border border-slate-800 rounded-3xl p-5 sm:p-8 shadow-xl space-y-6">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-800">
          <div>
            <div className="flex flex-wrap items-center gap-2">
              <span className="text-[11px] font-mono font-black px-2.5 py-0.5 rounded-full bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 whitespace-nowrap shrink-0">
                {currentTab.num} ACTIVE
              </span>
            </div>
            <h2 className="text-xl font-black text-white mt-1">{currentTab.name}</h2>
            <p className="text-xs text-slate-300 mt-1">{currentTab.desc}</p>
          </div>

          <span className="text-xs px-3.5 py-1.5 rounded-full bg-slate-950 text-indigo-300 border border-slate-800 font-mono font-bold self-start sm:self-auto shrink-0">
            {activeTopics.length} Topics Ready
          </span>
        </div>

        {/* Real Topic Cards */}
        <div className="space-y-3">
          {activeTopics.map((topic, tIdx) => (
            <Link
              key={topic.id}
              to={`/learn/topic/${topic.id}`}
              className="p-4 sm:p-5 rounded-2xl bg-slate-950 border border-slate-800 hover:border-indigo-500/60 transition-all duration-200 flex flex-col md:flex-row md:items-center justify-between gap-3 sm:gap-4 group hover:shadow-lg text-left"
            >
              <div className="flex items-start gap-3.5 min-w-0 text-left">
                <div className="w-10 h-10 rounded-xl bg-indigo-600/20 border border-indigo-500/30 text-indigo-400 flex items-center justify-center font-mono font-black text-xs shrink-0 mt-0.5">
                  {tIdx + 1}
                </div>
                <div className="min-w-0 text-left">
                  <h3 className="text-sm font-black text-white group-hover:text-indigo-300 transition">
                    {topic.title}
                  </h3>
                  <p className="text-xs text-slate-300 mt-0.5 line-clamp-2 leading-relaxed">{topic.description}</p>
                </div>
              </div>

              <div className="flex items-center justify-between md:justify-end gap-2.5 w-full md:w-fit shrink-0 pt-2.5 md:pt-0 border-t md:border-t-0 border-slate-800/60 self-start md:self-auto">
                <span className="text-[11px] text-slate-300 font-mono bg-slate-900 px-3 py-1 rounded-full border border-slate-800 flex items-center gap-1.5 font-semibold whitespace-nowrap shrink-0 w-fit">
                  <FiStar className="text-amber-400 w-3 h-3 shrink-0" /> 10-Q Employer Quiz
                </span>
                <div className="p-2 rounded-xl bg-indigo-600/20 text-indigo-300 group-hover:bg-indigo-600 group-hover:text-white transition shrink-0">
                  <FiChevronRight className="w-4 h-4 group-hover:translate-x-0.5 transition-transform" />
                </div>
              </div>
            </Link>
          ))}

          {activeTopics.length === 0 && (
            <div className="text-center py-12 bg-slate-950 rounded-2xl border border-slate-800 text-slate-400">
              <FiBookOpen className="w-10 h-10 text-indigo-400 mx-auto mb-2" />
              <p className="text-xs font-mono">Select a module tab above to explore topic masterclasses.</p>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

export default Learn
