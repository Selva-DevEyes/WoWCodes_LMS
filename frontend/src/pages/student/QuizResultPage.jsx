import { useState, useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'
import {
  FiCheckCircle,
  FiXCircle,
  FiHome,
  FiAward,
  FiRotateCcw,
  FiArrowRight,
  FiBookOpen,
} from 'react-icons/fi'
import { apiClient } from '../../api/apiClient'

const QuizResultPage = () => {
  const { resultId } = useParams()
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    apiClient
      .get(`/quiz/result/${resultId}`)
      .then((res) => {
        setResult(res.data)
        setLoading(false)
      })
      .catch(() => {
        apiClient
          .get('/quiz/results/mine')
          .then((res) => {
            const found = res.data.find((r) => r.id === parseInt(resultId))
            if (found) {
              setResult(found)
            }
            setLoading(false)
          })
          .catch(() => setLoading(false))
      })
  }, [resultId])

  if (loading) {
    return (
      <div className="flex flex-col items-center justify-center h-64 space-y-3">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600" />
        <p className="text-sm text-slate-400">Loading Evaluation Results...</p>
      </div>
    )
  }

  if (!result) {
    return (
      <div className="text-center py-20 bg-slate-900 border border-slate-800 rounded-3xl p-8 max-w-lg mx-auto">
        <h2 className="text-lg font-bold text-white">Result Not Found</h2>
        <Link to="/dashboard" className="mt-4 inline-block px-4 py-2 bg-indigo-600 text-white rounded-xl text-xs font-semibold">
          Return to Dashboard
        </Link>
      </div>
    )
  }

  const passed = result.passed === 1

  return (
    <div className="max-w-3xl mx-auto space-y-6 font-sans pb-3 sm:pb-8 text-left">
      {/* Result Hero Card */}
      <div
        className={`relative overflow-hidden border rounded-3xl p-6 sm:p-10 shadow-2xl text-center flex flex-col items-center justify-center ${
          passed
            ? 'bg-gradient-to-b from-slate-900 via-emerald-950/40 to-slate-900 border-emerald-500/40 text-emerald-100'
            : 'bg-gradient-to-b from-slate-900 via-rose-950/40 to-slate-900 border-rose-500/40 text-rose-100'
        }`}
      >
        <div className="mb-4">
          {passed ? (
            <div className="p-4 bg-emerald-500/20 text-emerald-400 rounded-full border border-emerald-500/30 inline-block animate-bounce duration-1000">
              <FiCheckCircle className="w-16 h-16" />
            </div>
          ) : (
            <div className="p-4 bg-rose-500/20 text-rose-400 rounded-full border border-rose-500/30 inline-block">
              <FiXCircle className="w-16 h-16" />
            </div>
          )}
        </div>

        <span className="text-xs font-mono font-bold uppercase tracking-widest px-3 py-1 rounded-full bg-slate-950 border border-slate-800 text-slate-300 mb-2">
          {passed ? 'Evaluation Passed' : 'Evaluation Needs Improvement'}
        </span>

        <h1 className="text-2xl sm:text-3xl font-black tracking-tight text-white mb-2">
          {passed ? 'Congratulations! Excellent Performance! 🎉' : 'Keep Practicing & Re-try! 💪'}
        </h1>

        <p className="text-sm text-slate-300 max-w-md mx-auto mb-6">
          {passed
            ? 'You have successfully passed this topic technical assessment and earned score mastery points!'
            : 'Review the answer explanation notes below and attempt the quiz again to achieve passing score threshold.'}
        </p>

        {/* Big Score Percentage Display */}
        <div className="bg-slate-950/80 border border-slate-800 px-8 py-4 rounded-2xl mb-8 shadow-inner">
          <p className="text-xs text-slate-400 uppercase font-mono tracking-wider">Final Accuracy Score</p>
          <p className="text-4xl sm:text-5xl font-black font-mono text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 via-purple-300 to-emerald-400 mt-1">
            {result.percentage}%
          </p>
        </div>

        {/* 3 Metric Stat Blocks */}
        <div className="grid grid-cols-3 gap-4 w-full max-w-md mb-8">
          <div className="bg-slate-950 p-4 rounded-2xl border border-slate-800 text-center">
            <p className="text-xl sm:text-2xl font-extrabold text-emerald-400 font-mono">{result.score}</p>
            <p className="text-xs text-slate-400 mt-0.5">Points Earned</p>
          </div>
          <div className="bg-slate-950 p-4 rounded-2xl border border-slate-800 text-center">
            <p className="text-xl sm:text-2xl font-extrabold text-indigo-400 font-mono">{result.total_points}</p>
            <p className="text-xs text-slate-400 mt-0.5">Total Points</p>
          </div>
          <div className="bg-slate-950 p-4 rounded-2xl border border-slate-800 text-center">
            <p className="text-xl sm:text-2xl font-extrabold text-amber-400 font-mono capitalize">{result.rank || 'Bronze'}</p>
            <p className="text-xs text-slate-400 mt-0.5">Badge Rank</p>
          </div>
        </div>

        {/* Action Triggers */}
        <div className="flex flex-wrap items-center justify-center gap-3 w-full">
          <Link
            to="/dashboard"
            className="px-6 py-3.5 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold rounded-2xl transition border border-slate-700 flex items-center gap-2"
          >
            <FiHome className="w-4 h-4" /> Back to Dashboard
          </Link>
          <Link
            to="/learn"
            className="px-6 py-3.5 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold rounded-2xl transition shadow-lg shadow-indigo-600/30 flex items-center gap-2"
          >
            <FiBookOpen className="w-4 h-4" /> Continue Learning Path <FiArrowRight className="w-4 h-4" />
          </Link>
        </div>
      </div>
    </div>
  )
}

export default QuizResultPage
