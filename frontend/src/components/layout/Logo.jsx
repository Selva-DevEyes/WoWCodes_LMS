import { FiCode, FiZap } from 'react-icons/fi'

const Logo = ({ size = 'md', showSubtitle = true, className = '' }) => {
  const sizeClasses = {
    sm: 'text-lg',
    md: 'text-2xl',
    lg: 'text-3xl',
    xl: 'text-4xl',
  }

  const iconSizes = {
    sm: 'w-6 h-6 text-xs',
    md: 'w-8 h-8 text-sm',
    lg: 'w-10 h-10 text-base',
    xl: 'w-12 h-12 text-lg',
  }

  return (
    <div className={`flex items-center gap-3 select-none ${className}`}>
      {/* Eye-Catching Multi-Color Glowing Icon Badge */}
      <div className={`relative flex items-center justify-center rounded-2xl bg-gradient-to-tr from-cyan-500 via-indigo-500 to-pink-500 p-0.5 shadow-lg shadow-indigo-500/25 ring-2 ring-indigo-500/30 ${iconSizes[size]}`}>
        <div className="w-full h-full bg-slate-950 rounded-[14px] flex items-center justify-center text-white">
          <FiCode className="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-pink-400 font-black animate-pulse" />
        </div>
      </div>

      <div className="flex flex-col">
        {/* Multi-Color Vibrant Gradient Brand Title */}
        <span className={`font-black tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-indigo-400 to-pink-500 ${sizeClasses[size]}`}>
          WoWCodes
        </span>
        {showSubtitle && (
          <span className="text-[11px] font-mono font-medium text-slate-400 flex items-center gap-1.5 -mt-1">
            <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping inline-block" />
            by <strong className="text-slate-300 font-semibold">SelvamSDE</strong>
          </span>
        )}
      </div>
    </div>
  )
}

export default Logo
