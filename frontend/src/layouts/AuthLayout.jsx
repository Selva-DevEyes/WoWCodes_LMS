import { Outlet } from 'react-router-dom'
import Logo from '../components/layout/Logo'

const AuthLayout = () => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-950 p-4 font-sans relative overflow-hidden">
      {/* Background Decorative Blur Orbs */}
      <div className="absolute -top-32 -left-32 w-96 h-96 bg-indigo-500/10 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute -bottom-32 -right-32 w-96 h-96 bg-purple-500/10 rounded-full blur-3xl pointer-events-none" />

      <div className="w-full max-w-md relative z-10 space-y-6">
        <div className="flex flex-col items-center justify-center text-center space-y-2">
          <Logo size="xl" />
          <p className="text-slate-400 text-xs font-mono tracking-wide pt-1">
            Learn • Practice • Build • Crack Interviews
          </p>
        </div>

        <Outlet />

        {/* Professional Signature Footer */}
        <div className="text-center pt-2">
          <div className="inline-flex flex-wrap items-center justify-center gap-x-2.5 gap-y-1 text-[11px] text-slate-400 bg-slate-900/60 px-4 py-2 rounded-full border border-slate-800/80 backdrop-blur-sm">
            <span className="font-bold text-slate-200 tracking-tight">WOWCode</span>
            <span className="text-slate-600 select-none">•</span>
            <span className="text-slate-300 font-medium">Learn. Practice. Grow.</span>
            <span className="text-slate-600 select-none">•</span>
            <span className="text-indigo-400 font-semibold">Created by Selvam S</span>
          </div>
        </div>
      </div>
    </div>
  )
}

export default AuthLayout
