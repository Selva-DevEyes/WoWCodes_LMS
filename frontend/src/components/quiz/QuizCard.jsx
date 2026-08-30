import { Link } from 'react-router-dom'
import { FiClock, FiStar } from 'react-icons/fi'

const levelColors = {
  easy: 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-200 dark:ring-1 dark:ring-emerald-700/70',
  medium: 'bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-200 dark:ring-1 dark:ring-amber-700/70',
  // Support existing records that still use the older level name.
  moderate: 'bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-200 dark:ring-1 dark:ring-amber-700/70',
  hard: 'bg-red-100 text-red-800 dark:bg-red-950 dark:text-red-200 dark:ring-1 dark:ring-red-700/70',
}

const QuizCard = ({ quiz }) => {
  return (
    <Link to={`/quiz/${quiz.id}`} className="card hover:shadow-lg transition-shadow">
      <div className="flex items-center justify-between mb-3">
        <div className={`rounded-full px-2.5 py-1 text-xs font-semibold capitalize ${levelColors[quiz.level] || levelColors.easy}`}>
          {quiz.level} quiz
        </div>
        <FiStar className="text-accent-500" />
      </div>
      <h3 className="font-semibold mb-2">{quiz.title}</h3>
      <p className="text-sm text-gray-500 dark:text-gray-400 mb-3 line-clamp-1">
        {quiz.description}
      </p>
      <div className="flex items-center gap-4 text-sm text-gray-500">
        <span className="flex items-center gap-1">
          <FiClock /> {quiz.time_limit_minutes} min
        </span>
        <span>Pass: {quiz.passing_score}%</span>
      </div>
    </Link>
  )
}

export default QuizCard
