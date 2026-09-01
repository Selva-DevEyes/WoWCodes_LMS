const colorGradients = {
  blue: 'from-blue-600 to-indigo-600 shadow-blue-500/20',
  emerald: 'from-emerald-500 to-teal-600 shadow-emerald-500/20',
  purple: 'from-purple-600 to-indigo-600 shadow-purple-500/20',
  amber: 'from-amber-500 to-orange-500 shadow-amber-500/20',
  rose: 'from-rose-500 to-red-600 shadow-rose-500/20',
}

const colorTints = {
  blue: 'bg-blue-50 text-blue-600 border-blue-200/80 dark:bg-blue-950/50 dark:text-blue-400 dark:border-blue-800/50',
  emerald: 'bg-emerald-50 text-emerald-600 border-emerald-200/80 dark:bg-emerald-950/50 dark:text-emerald-400 dark:border-emerald-800/50',
  purple: 'bg-purple-50 text-purple-600 border-purple-200/80 dark:bg-purple-950/50 dark:text-purple-400 dark:border-purple-800/50',
  amber: 'bg-amber-50 text-amber-600 border-amber-200/80 dark:bg-amber-950/50 dark:text-amber-400 dark:border-amber-800/50',
  rose: 'bg-rose-50 text-rose-600 border-rose-200/80 dark:bg-rose-950/50 dark:text-rose-400 dark:border-rose-800/50',
}

const StatCard = ({ icon: Icon, label, value, color = 'blue', trend = null }) => {
  // Normalize color keys (handle "text-blue-500", "blue", "from-...")
  let key = 'blue'
  if (typeof color === 'string') {
    if (color.includes('emerald') || color.includes('green')) key = 'emerald'
    else if (color.includes('purple') || color.includes('violet')) key = 'purple'
    else if (color.includes('amber') || color.includes('orange') || color.includes('yellow')) key = 'amber'
    else if (color.includes('rose') || color.includes('red')) key = 'rose'
    else if (color.includes('blue') || color.includes('indigo') || color.includes('cyan')) key = 'blue'
  }

  const gradientClass = colorGradients[key] || colorGradients.blue
  const tintClass = colorTints[key] || colorTints.blue

  return (
    <div className="card flex items-center justify-between p-4 sm:p-5 hover:border-indigo-300 dark:hover:border-indigo-800 transition-all duration-200 group bg-white dark:bg-slate-900 border border-slate-200/90 dark:border-slate-800 shadow-sm">
      <div className="flex items-center gap-3.5 min-w-0">
        {/* Visible High-Contrast Icon Box in Light & Dark Mode */}
        <div className={`shrink-0 w-12 h-12 rounded-2xl bg-gradient-to-tr ${gradientClass} shadow-md group-hover:scale-105 transition-transform duration-200 flex items-center justify-center text-white ring-2 ring-white/20 dark:ring-slate-800`}>
          {Icon && <Icon className="text-2xl text-white drop-shadow-sm" />}
        </div>
        <div className="min-w-0">
          <div className="text-2xl font-black text-slate-900 dark:text-white tracking-tight leading-none">
            {value}
          </div>
          <div className="mt-1 text-xs font-semibold text-slate-500 dark:text-slate-400 truncate">
            {label}
          </div>
        </div>
      </div>

      {trend && (
        <span className="hidden sm:inline-flex items-center px-2 py-0.5 rounded-full text-[11px] font-bold bg-emerald-50 text-emerald-600 dark:bg-emerald-950/80 dark:text-emerald-400 font-mono border border-emerald-200/50 dark:border-emerald-800/50">
          {trend}
        </span>
      )}
    </div>
  )
}

export default StatCard
