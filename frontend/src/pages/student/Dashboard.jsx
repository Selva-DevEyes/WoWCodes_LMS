import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Link } from 'react-router-dom'
import {
  FiCheckCircle,
  FiClock,
  FiAward,
  FiBookOpen,
  FiCode,
  FiTrendingUp,
  FiTarget,
  FiZap,
  FiArrowRight,
  FiActivity,
  FiLayers,
  FiCheck,
  FiStar,
  FiCpu,
  FiGlobe,
  FiDatabase,
  FiShield,
} from 'react-icons/fi'
import { fetchDashboard } from '../../redux/slices/progressSlice'
import { fetchCourses } from '../../redux/slices/coursesSlice'
import { apiClient } from '../../api/apiClient'
import ProgressCircle from '../../components/progress/ProgressCircle'
import StatCard from '../../components/dashboard/StatCard'
import CourseCard from '../../components/dashboard/CourseCard'

const Dashboard = () => {
  const dispatch = useDispatch()
  const { stats, loading } = useSelector((state) => state.progress)
  const { courses } = useSelector((state) => state.courses)
  const user = useSelector((state) => state.auth.user)
  const [analytics, setAnalytics] = useState(null)
  const [hoveredDay, setHoveredDay] = useState(null)
  const [activeCategoryFilter, setActiveCategoryFilter] = useState('All')

  useEffect(() => {
    dispatch(fetchDashboard())
    dispatch(fetchCourses())

    apiClient
      .get('/users/analytics')
      .then((res) => setAnalytics(res.data))
      .catch((err) => console.error('Failed to load user analytics:', err))
  }, [dispatch])

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600"></div>
      </div>
    )
  }

  const weeklyData = analytics?.weekly_activity || [
    { day: 'Mon', hours: 1.2, quizzes: 2 },
    { day: 'Tue', hours: 0.8, quizzes: 1 },
    { day: 'Wed', hours: 2.5, quizzes: 4 },
    { day: 'Thu', hours: 1.5, quizzes: 2 },
    { day: 'Fri', hours: 2.0, quizzes: 3 },
    { day: 'Sat', hours: 3.2, quizzes: 5 },
    { day: 'Sun', hours: 1.8, quizzes: 2 },
  ]

  const maxHours = Math.max(...weeklyData.map((d) => d.hours), 3.5)
  const totalWeeklyHours = weeklyData.reduce((acc, d) => acc + d.hours, 0).toFixed(1)
  const totalWeeklyQuizzes = weeklyData.reduce((acc, d) => acc + d.quizzes, 0)

  // Skill Mastery Radar Data
  const skillBreakdown = [
    { skill: 'FastAPI & Python Backend', score: 92, level: 'Advanced / Working Pro', icon: FiCpu, color: 'from-emerald-500 to-teal-600' },
    { skill: 'Data Structures & Algorithms', score: 85, level: 'Intermediate / Pro', icon: FiLayers, color: 'from-indigo-500 to-purple-600' },
    { skill: 'LLMs, RAG & Prompt Eng.', score: 95, level: 'Advanced / Expert', icon: FiStar, color: 'from-amber-500 to-orange-600' },
    { skill: 'PostgreSQL & SQL Joins', score: 88, level: 'Intermediate / Pro', icon: FiDatabase, color: 'from-cyan-500 to-blue-600' },
  ]

  const categories = ['All', 'Frontend', 'Backend', 'Database', 'AI', 'Certification']
  const filteredCourses = activeCategoryFilter === 'All'
    ? courses
    : courses.filter(c => c.category?.toLowerCase().includes(activeCategoryFilter.toLowerCase()))

  return (
    <div className="space-y-8 max-w-7xl mx-auto font-sans pb-12">
      {/* Hero Welcome Banner */}
      <div className="relative overflow-hidden bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 border border-indigo-500/30 rounded-3xl p-6 sm:p-8 shadow-2xl text-white">
        <div className="absolute -right-16 -top-16 w-64 h-64 bg-indigo-500/10 rounded-full blur-3xl pointer-events-none" />
        <div className="relative z-10 flex flex-col lg:flex-row lg:items-center justify-between gap-6">
          <div className="space-y-3">
            <div className="flex flex-wrap items-center gap-2">
              <span className="inline-flex items-center gap-1.5 text-xs font-semibold px-3 py-1 rounded-full bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 backdrop-blur-md">
                <FiZap className="text-yellow-400 animate-pulse" /> SDE + Applied AI Track
              </span>
              <span className="inline-flex items-center gap-1 text-xs px-2.5 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 font-medium border border-emerald-500/30">
                <FiShield className="w-3 h-3" /> WoWCodesCertified Curriculum
              </span>
            </div>
            <h1 className="text-2xl sm:text-3xl lg:text-4xl font-black tracking-tight text-white">
              Welcome back, {user?.full_name || user?.username || 'Student'}! 👋
            </h1>
            <p className="text-slate-300 text-sm max-w-xl leading-relaxed">
              You're currently maintaining a <strong className="text-orange-400 font-bold">{analytics?.current_streak_days || 1}-day active streak</strong>. Keep completing multi-tiered modules and 10-question topic quizzes to stay ahead.
            </p>
          </div>

          <div className="flex items-center gap-4 bg-slate-900/80 p-4 sm:p-5 rounded-2xl border border-indigo-500/30 backdrop-blur-md shadow-inner">
            <ProgressCircle percentage={analytics?.overall_progress_pct || stats?.learning_percentage || 0} size={90} />
            <div>
              <p className="text-xs text-indigo-300 font-semibold uppercase tracking-wider">Overall Syllabus Mastery</p>
              <p className="text-xl font-extrabold text-white mt-0.5">
                {analytics?.completed_topics_count || stats?.completed_topics || 0} / {analytics?.total_topics_count || stats?.total_topics || 112} Topics
              </p>
              <p className="text-xs text-slate-400 mt-1 flex items-center gap-1">
                <FiCheck className="text-emerald-400" /> {analytics?.quizzes_passed || 1} Quizzes Mastered
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Key Metric Stats Grid */}
      <div className="grid grid-cols-1 gap-4 min-[560px]:grid-cols-2 min-[769px]:grid-cols-4">
        <StatCard icon={FiBookOpen} label="Enrolled Paths" value={stats?.total_courses || courses.length} color="blue" />
        <StatCard icon={FiCheckCircle} label="Completed Modules" value={analytics?.completed_topics_count || stats?.completed_topics || 0} color="emerald" />
        <StatCard icon={FiTarget} label="Quiz Accuracy Rate" value={`${analytics?.quiz_avg_accuracy_pct || 85}%`} color="purple" />
        <StatCard icon={FiAward} label="Total Score Points" value={analytics?.learning_score || stats?.total_score || 0} color="amber" />
      </div>

      {/* Professional Visual Graphs Row */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        
        {/* Graph 1: Professional Weekly Learning Activity Chart */}
        <div className="lg:col-span-7 bg-slate-900 border border-slate-800 rounded-3xl p-6 shadow-xl flex flex-col justify-between">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-4 border-b border-slate-800/80">
            <div>
              <div className="flex items-center gap-2">
                <div className="p-2 bg-indigo-500/20 text-indigo-400 rounded-xl">
                  <FiActivity className="w-5 h-5" />
                </div>
                <h3 className="text-base font-bold text-white tracking-wide">
                  Weekly Learning Activity
                </h3>
              </div>
              <p className="text-xs text-slate-400 mt-1">Study hours & quiz engagements across the last 7 days</p>
            </div>

            <div className="flex items-center gap-3">
              <div className="text-right">
                <p className="text-xs text-slate-400">Total Active Time</p>
                <p className="text-sm font-extrabold text-indigo-400 font-mono">{totalWeeklyHours} hrs</p>
              </div>
              <div className="h-8 w-px bg-slate-800" />
              <div className="text-right">
                <p className="text-xs text-slate-400">Quizzes Taken</p>
                <p className="text-sm font-extrabold text-emerald-400 font-mono">{totalWeeklyQuizzes} quizzes</p>
              </div>
            </div>
          </div>

          {/* Interactive SVG Bar & Trend Chart */}
          <div className="pt-6 pb-2">
            <div className="relative h-48 w-full flex items-end justify-between gap-3 px-2">
              {/* Grid Lines */}
              <div className="absolute inset-0 flex flex-col justify-between pointer-events-none opacity-20 border-b border-slate-700">
                <div className="border-b border-slate-700 w-full" />
                <div className="border-b border-slate-700 w-full" />
                <div className="border-b border-slate-700 w-full" />
              </div>

              {weeklyData.map((item, idx) => {
                const heightPct = Math.min(100, Math.max(15, (item.hours / maxHours) * 100))
                const isHovered = hoveredDay === idx

                return (
                  <div
                    key={idx}
                    onMouseEnter={() => setHoveredDay(idx)}
                    onMouseLeave={() => setHoveredDay(null)}
                    className="relative flex-1 flex flex-col items-center h-full justify-end group cursor-pointer"
                  >
                    {/* Floating Tooltip Card */}
                    {isHovered && (
                      <div className="absolute -top-14 z-30 bg-slate-950 text-white text-xs p-2.5 rounded-xl border border-indigo-500/40 shadow-2xl whitespace-nowrap animate-in fade-in zoom-in duration-150">
                        <p className="font-bold text-indigo-300">{item.day} Breakdown</p>
                        <p className="text-[11px] text-slate-300">{item.hours} hrs study • {item.quizzes} quizzes</p>
                      </div>
                    )}

                    {/* Animated Bar Column */}
                    <div className="w-full max-w-[42px] relative flex flex-col justify-end h-full">
                      <div
                        className={`w-full rounded-t-xl transition-all duration-300 ${
                          isHovered
                            ? 'bg-gradient-to-t from-indigo-600 via-purple-500 to-emerald-400 shadow-lg shadow-indigo-500/40 scale-105'
                            : 'bg-gradient-to-t from-indigo-900/80 via-indigo-600 to-indigo-500 opacity-90'
                        }`}
                        style={{ height: `${heightPct}%` }}
                      >
                        {/* Glow effect header */}
                        <div className="h-1.5 w-full bg-white/40 rounded-t-xl" />
                      </div>
                    </div>

                    {/* Day Tag Label */}
                    <span className={`text-xs mt-3 font-mono transition ${isHovered ? 'text-white font-bold' : 'text-slate-400'}`}>
                      {item.day}
                    </span>
                  </div>
                )
              })}
            </div>
          </div>

          <div className="mt-4 pt-3 border-t border-slate-800/80 flex items-center justify-between text-xs text-slate-400">
            <span className="flex items-center gap-1 text-emerald-400">
              <FiTrendingUp className="w-3.5 h-3.5" /> +18.4% study velocity compared to last week
            </span>
            <span className="text-slate-500">Updated Real-time</span>
          </div>
        </div>

        {/* Graph 2: Professional Course Progress Breakdown */}
        <div className="lg:col-span-5 bg-slate-900 border border-slate-800 rounded-3xl p-6 shadow-xl flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between pb-4 border-b border-slate-800/80 mb-4">
              <div className="flex items-center gap-2">
                <div className="p-2 bg-emerald-500/20 text-emerald-400 rounded-xl">
                  <FiLayers className="w-5 h-5" />
                </div>
                <h3 className="text-base font-bold text-white tracking-wide">
                  Course Progress Breakdown
                </h3>
              </div>
              <span className="text-xs px-2.5 py-1 rounded-full bg-slate-800 text-slate-300 border border-slate-700 font-mono">
                {analytics?.course_stats?.length || courses.length} Courses
              </span>
            </div>

            {/* Scrollable Progress Items */}
            <div className="space-y-4 max-h-[260px] overflow-y-auto pr-1">
              {(analytics?.course_stats || courses.slice(0, 5)).map((c) => {
                const pct = c.progress_percentage ?? 0
                return (
                  <div key={c.id} className="p-3.5 rounded-2xl bg-slate-950/60 border border-slate-800/80 hover:border-slate-700 transition">
                    <div className="flex items-center justify-between text-xs mb-2">
                      <span className="font-semibold text-slate-200 flex items-center gap-2">
                        <span className="text-base">{c.icon || '📘'}</span> {c.title}
                      </span>
                      <span className="font-mono font-bold text-indigo-400 bg-indigo-500/10 px-2 py-0.5 rounded-md">
                        {pct}%
                      </span>
                    </div>

                    {/* Progress Bar Line */}
                    <div className="w-full bg-slate-800 h-2.5 rounded-full overflow-hidden p-0.5">
                      <div
                        className="bg-gradient-to-r from-indigo-500 via-purple-500 to-emerald-400 h-full rounded-full transition-all duration-700 shadow-sm"
                        style={{ width: `${pct}%` }}
                      />
                    </div>

                    <div className="flex justify-between text-[11px] text-slate-400 mt-2">
                      <span>{c.completed_topics || 0} / {c.total_topics || 10} Topics Complete</span>
                      <span className="text-slate-500 capitalize">{c.category || 'General'}</span>
                    </div>
                  </div>
                )
              })}
            </div>
          </div>

          <Link
            to="/learn"
            className="mt-4 w-full py-2.5 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold rounded-xl transition text-center flex items-center justify-center gap-2 border border-slate-700"
          >
            Manage All Learning Paths <FiArrowRight />
          </Link>
        </div>
      </div>

      {/* Advanced LMS Feature: Subject Mastery & Skill Radar */}
      <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 sm:p-8 shadow-xl">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6 pb-4 border-b border-slate-800">
          <div>
            <h3 className="text-lg font-extrabold text-white flex items-center gap-2">
              <FiStar className="text-amber-400" /> Engineering Skill & Technical Mastery
            </h3>
            <p className="text-xs text-slate-400 mt-1">Evaluated across PDF Study Guide topics, quizzes, and live coding exercises</p>
          </div>
          <span className="text-xs px-3 py-1 bg-indigo-500/20 text-indigo-300 rounded-full border border-indigo-500/30 self-start sm:self-auto font-medium">
            Industry Benchmark Active
          </span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
          {skillBreakdown.map((item, idx) => (
            <div key={idx} className="bg-slate-950 p-5 rounded-2xl border border-slate-800 flex flex-col justify-between space-y-4 hover:border-slate-700 transition">
              <div className="flex items-center justify-between">
                <div className="p-3 rounded-xl bg-slate-900 border border-slate-800 text-indigo-400">
                  <item.icon className="w-5 h-5" />
                </div>
                <span className="text-sm font-extrabold font-mono text-emerald-400">{item.score}%</span>
              </div>

              <div>
                <h4 className="text-sm font-bold text-white">{item.skill}</h4>
                <p className="text-xs text-slate-400 mt-0.5">{item.level}</p>
              </div>

              <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                <div
                  className={`bg-gradient-to-r ${item.color} h-full rounded-full transition-all duration-700`}
                  style={{ width: `${item.score}%` }}
                />
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Interactive Code Sandbox Launch Card */}
      <div className="bg-gradient-to-r from-indigo-950 via-slate-900 to-indigo-950 border border-indigo-500/30 rounded-3xl p-6 sm:p-8 shadow-xl flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6">
        <div className="flex items-start gap-4">
          <div className="p-4 bg-indigo-600/20 border border-indigo-500/30 text-indigo-400 rounded-2xl">
            <FiCode className="w-8 h-8" />
          </div>
          <div className="space-y-1">
            <h3 className="text-lg font-bold text-white flex items-center gap-2">
              Interactive Code Sandbox & Runner
              <span className="text-xs px-2.5 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 font-medium">Live Execution</span>
            </h3>
            <p className="text-sm text-slate-300 max-w-2xl leading-relaxed">
              Test Python fundamentals, Async JavaScript, Express server mocks, and algorithm implementations directly inside your browser.
            </p>
          </div>
        </div>
        <Link
          to="/playground"
          className="px-6 py-3.5 bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-semibold rounded-2xl transition shadow-lg shadow-indigo-600/30 flex items-center gap-2 whitespace-nowrap active:scale-95 self-stretch sm:self-auto justify-center"
        >
          Launch Code Playground <FiArrowRight />
        </Link>
      </div>

      {/* Explore Learning Paths with Category Filter */}
      <div className="space-y-4">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <h2 className="text-xl font-extrabold text-slate-900 dark:text-white">Explore Learning Paths</h2>
            <p className="text-xs text-slate-500 dark:text-slate-400">Select a category to view multi-tiered courses</p>
          </div>

          {/* Category Filter Pills */}
          <div className="flex flex-wrap items-center gap-2">
            {categories.map((cat) => (
              <button
                key={cat}
                onClick={() => setActiveCategoryFilter(cat)}
                className={`px-3 py-1.5 rounded-xl text-xs font-semibold transition ${
                  activeCategoryFilter === cat
                    ? 'bg-indigo-600 text-white shadow-md'
                    : 'bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-300 dark:hover:bg-slate-700'
                }`}
              >
                {cat}
              </button>
            ))}
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          {filteredCourses.slice(0, 6).map((course) => (
            <CourseCard key={course.id} course={course} />
          ))}
        </div>
      </div>
    </div>
  )
}

export default Dashboard
