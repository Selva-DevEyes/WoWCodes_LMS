import { useState, useEffect } from 'react'
import { FiTrendingUp, FiStar } from 'react-icons/fi'
import { apiClient } from '../../api/apiClient'
import { ENDPOINTS } from '../../api/endpoints'

const medalColors = ['text-yellow-500', 'text-gray-400', 'text-amber-600']

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
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>
    )
  }

  return (
    <div className="max-w-3xl mx-auto">
      <div className="flex items-center gap-3 mb-8">
        <FiTrendingUp className="text-3xl text-yellow-500" />
        <div>
          <h1 className="text-2xl font-bold">Leaderboard</h1>
          <p className="text-gray-500 text-sm">Top performers on WoWCodes</p>
        </div>
      </div>

      <div className="space-y-3">
        {players.map((player, idx) => (
          <div
            key={player.user_id}
            className="card flex items-center gap-4 hover:shadow-lg transition-shadow"
          >
            <div className="w-10 text-center">
              {idx < 3 ? (
                <FiStar className={`text-2xl mx-auto ${medalColors[idx]}`} />
              ) : (
                <span className="text-lg font-bold text-gray-400">{player.rank}</span>
              )}
            </div>
            <img
              src={player.avatar_url || `https://ui-avatars.com/api/?name=${player.username}`}
              alt={player.username}
              className="w-12 h-12 rounded-full"
            />
            <div className="flex-1">
              <div className="font-semibold">{player.full_name || player.username}</div>
              <div className="text-sm text-gray-500">@{player.username}</div>
            </div>
            <div className="text-right">
              <div className="font-bold text-primary-600">{player.total_score} pts</div>
              <div className="text-xs text-gray-500">{player.current_streak} 🔥 streak</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

export default LeaderboardPage