import { useState, useEffect } from 'react'
import { FiTrendingUp, FiStar, FiAward, FiZap } from 'react-icons/fi'
import { apiClient } from '../../api/apiClient'
import { ENDPOINTS } from '../../api/endpoints'

const medalColors = ['text-amber-400', 'text-slate-300', 'text-amber-600']

const LeaderboardPage = () => {
  const [players, setPlayers] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    apiClient.get(ENDPOINTS.leaderboard)
      .then((res) => {
        setPlayers(res.data)
        setLoading(false)
      })
      .catch(() => setLoading(false))
  }, [])

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600"></div>
      </div>
    )
  }

  return (
    <div className="max-w-4xl mx-auto space-y-6 font-sans pb-3 sm:pb-8 text-left">
      {/* Header */}
      <div className="flex items-start gap-3 text-left">
        <div className="w-11 h-11 sm:w-12 sm:h-12 rounded-2xl bg-indigo-500/10 border border-indigo-500/20 text-indigo-500 flex items-center justify-center text-xl sm:text-2xl shrink-0 mt-0.5">
          <FiTrendingUp />
        </div>
        <div className="text-left">
          <h1 className="text-xl sm:text-2xl lg:text-3xl font-bold tracking-tight text-slate-900 dark:text-white">
            Leaderboard & Rankings
          </h1>
          <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400 font-normal mt-0.5">
            Top engineering achievers and overall curriculum points
          </p>
        </div>
      </div>

      <div className="space-y-3">
        {players.map((player, idx) => (
          <div
            key={player.user_id}
            className={`card flex items-center justify-between p-4 sm:p-5 border transition-all duration-200 ${
              idx === 0
                ? 'border-amber-400/40 bg-gradient-to-r from-amber-50/30 to-white dark:from-amber-950/20 dark:to-slate-900 shadow-sm'
                : 'border-slate-200/90 dark:border-slate-800/90'
            }`}
          >
            <div className="flex items-center gap-4 min-w-0">
              <div className="w-8 text-center shrink-0">
                {idx < 3 ? (
                  <FiStar className={`text-2xl mx-auto ${medalColors[idx]}`} />
                ) : (
                  <span className="text-sm font-bold font-mono text-slate-400">#{player.rank || idx + 1}</span>
                )}
              </div>
              <img
                src={player.avatar_url || `https://ui-avatars.com/api/?name=${player.username}&background=6366f1&color=fff`}
                alt={player.username}
                className="w-10 h-10 rounded-xl object-cover ring-2 ring-indigo-500/20 shrink-0"
              />
              <div className="min-w-0">
                <h3 className="text-base sm:text-lg font-semibold text-slate-900 dark:text-white tracking-normal truncate">
                  {player.full_name || player.username}
                </h3>
                <div className="text-xs text-slate-500 font-mono">@{player.username}</div>
              </div>
            </div>

            <div className="flex items-center gap-4 shrink-0">
              <div className="text-right">
                <div className="text-base sm:text-lg font-bold font-mono text-indigo-600 dark:text-indigo-400">
                  {player.total_score || 0} pts
                </div>
                <div className="text-[11px] text-slate-400 font-semibold flex items-center gap-1 justify-end">
                  <FiZap className="text-amber-500" /> {player.current_streak || 1}d Streak
                </div>
              </div>
            </div>
          </div>
        ))}

        {players.length === 0 && (
          <div className="card text-center py-16 text-slate-400 font-mono text-xs">
            No leaderboard ranks calculated yet. Complete topic quizzes to appear on the leaderboard!
          </div>
        )}
      </div>
    </div>
  )
}

export default LeaderboardPage