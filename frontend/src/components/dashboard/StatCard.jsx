const StatCard = ({ icon: Icon, label, value, color = 'text-primary-600' }) => {
  return (
    <div className="card flex min-w-0 items-center gap-3 p-4">
      <div className={`shrink-0 rounded-lg bg-gray-100 p-2.5 dark:bg-gray-700 ${color}`}>
        <Icon className="text-xl" />
      </div>
      <div className="min-w-0">
        <div className="text-xl font-bold leading-tight">{value}</div>
        <div className="mt-0.5 break-normal text-xs leading-4 text-gray-500 dark:text-gray-400">{label}</div>
      </div>
    </div>
  )
}

export default StatCard
