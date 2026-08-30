const StatCard = ({ icon: Icon, label, value, color = 'from-indigo-500 to-indigo-600', trend = null }) => {
  return (
    <div className="card flex items-center justify-between p-4 sm:p-5 hover:border-indigo-200 dark:hover:border-indigo-900/50 transition-all duration-200 group">
      <div className="flex items-center gap-3.5 min-w-0">
        <div className={`shrink-0 w-11 h-11 rounded-xl bg-gradient-to-tr ${color} p-0.5 shadow-sm group-hover:scale-105 transition-transform duration-200 flex items-center justify-center text-white`}>
          <Icon className="text-xl" />
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
        <span className="hidden sm:inline-flex items-center px-2 py-0.5 rounded-full text-[11px] font-bold bg-emerald-50 text-emerald-600 dark:bg-emerald-950/80 dark:text-emerald-400 font-mono">
          {trend}
        </span>
      )}
    </div>
  )
}

export default StatCard
