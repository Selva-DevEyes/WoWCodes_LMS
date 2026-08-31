const Logo = ({ size = 'md', showSubtitle = true, className = '' }) => {
  const sizeClasses = {
    sm: 'text-lg',
    md: 'text-xl',
    lg: 'text-2xl',
    xl: 'text-3xl',
  }

  const pandaSizes = {
    sm: 'w-7 h-7',
    md: 'w-9 h-9',
    lg: 'w-11 h-11',
    xl: 'w-14 h-14',
  }

  return (
    <div className={`flex items-center gap-3 select-none ${className}`}>
      {/* Cute Coder Panda Mascot in Consistent Rainbow Gradient Badge */}
      <div className={`relative flex items-center justify-center shrink-0 rounded-2xl bg-gradient-to-tr from-rose-500 via-amber-400 via-emerald-400 via-sky-400 to-violet-600 p-[2px] shadow-sm hover:scale-105 transition-transform duration-300 ${pandaSizes[size]}`}>
        <div className="w-full h-full bg-white dark:bg-slate-950 rounded-[14px] flex items-center justify-center p-1 overflow-hidden">
          <svg viewBox="0 0 100 100" className="w-full h-full" fill="none" xmlns="http://www.w3.org/2000/svg">
            {/* Panda Ears */}
            <circle cx="24" cy="24" r="14" fill="#0f172a" />
            <circle cx="76" cy="24" r="14" fill="#0f172a" />
            {/* Inner Rainbow Ear Accents */}
            <circle cx="24" cy="24" r="7" fill="url(#rainbow-ear-left)" />
            <circle cx="76" cy="24" r="7" fill="url(#rainbow-ear-right)" />

            {/* Panda Head */}
            <circle cx="50" cy="54" r="38" fill="#ffffff" stroke="#0f172a" strokeWidth="4" />

            {/* Eye Patches */}
            <ellipse cx="33" cy="50" rx="10" ry="13" transform="rotate(-15 33 50)" fill="#0f172a" />
            <ellipse cx="67" cy="50" rx="10" ry="13" transform="rotate(15 67 50)" fill="#0f172a" />

            {/* Developer Glasses (Rainbow) */}
            <rect x="20" y="40" width="24" height="18" rx="6" fill="none" stroke="url(#rainbow-grad)" strokeWidth="4" />
            <rect x="56" y="40" width="24" height="18" rx="6" fill="none" stroke="url(#rainbow-grad)" strokeWidth="4" />
            <path d="M44 49 H56" stroke="url(#rainbow-grad)" strokeWidth="4" strokeLinecap="round" />

            {/* Sparkle Pupil Eyes */}
            <circle cx="34" cy="48" r="3.5" fill="#38bdf8" />
            <circle cx="32" cy="46" r="1.5" fill="#ffffff" />
            <circle cx="66" cy="48" r="3.5" fill="#38bdf8" />
            <circle cx="64" cy="46" r="1.5" fill="#ffffff" />

            {/* Panda Cute Nose & Mouth */}
            <ellipse cx="50" cy="65" rx="5" ry="3.5" fill="#0f172a" />
            <path d="M45 71 Q50 76 55 71" stroke="#0f172a" strokeWidth="3" strokeLinecap="round" />

            {/* Gradient Definitions */}
            <defs>
              <linearGradient id="rainbow-grad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stopColor="#f43f5e" />
                <stop offset="25%" stopColor="#fbbf24" />
                <stop offset="50%" stopColor="#10b981" />
                <stop offset="75%" stopColor="#06b6d4" />
                <stop offset="100%" stopColor="#8b5cf6" />
              </linearGradient>
              <linearGradient id="rainbow-ear-left" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stopColor="#f43f5e" />
                <stop offset="100%" stopColor="#fbbf24" />
              </linearGradient>
              <linearGradient id="rainbow-ear-right" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stopColor="#06b6d4" />
                <stop offset="100%" stopColor="#8b5cf6" />
              </linearGradient>
            </defs>
          </svg>
        </div>
      </div>

      {/* Brand Name with Consistent Rainbow Gradient Text */}
      <div className="flex flex-col">
        <span className={`font-black tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-rose-500 via-amber-500 via-emerald-500 via-sky-500 to-indigo-600 ${sizeClasses[size]}`}>
          WOWCode
        </span>
        {showSubtitle && (
          <div className="flex items-center gap-1.5 -mt-0.5">
            <span className="inline-block w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
            <span className="text-[10px] font-semibold tracking-wider uppercase text-slate-500 dark:text-slate-400 font-mono">
              Learn. Practice. Grow.
            </span>
          </div>
        )}
      </div>
    </div>
  )
}

export default Logo
