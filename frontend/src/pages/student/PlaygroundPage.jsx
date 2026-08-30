import CodePlayground from '../../components/CodePlayground'
import { FiCode, FiZap, FiCpu } from 'react-icons/fi'

export default function PlaygroundPage() {
  return (
    <div className="max-w-7xl mx-auto space-y-6 font-sans pb-16">
      {/* Page Banner */}
      <div className="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 border border-indigo-500/30 rounded-3xl p-6 sm:p-8 shadow-xl text-white">
        <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
          <div className="space-y-2">
            <span className="inline-flex items-center gap-1.5 text-xs font-semibold px-3 py-1 rounded-full bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
              <FiZap className="text-amber-400" /> Interactive Execution Engine
            </span>
            <h1 className="text-2xl sm:text-3xl font-bold text-white tracking-tight">
              Interactive Code Sandbox
            </h1>
            <p className="text-slate-300 text-xs sm:text-sm max-w-2xl leading-relaxed">
              Write, execute, and experiment with JavaScript, Promises, API server routes, and data structure algorithms in real-time.
            </p>
          </div>

          <div className="flex items-center gap-3">
            <div className="flex items-center gap-2 text-xs font-mono text-slate-300 bg-slate-950 px-3.5 py-2 rounded-xl border border-slate-800">
              <FiCpu className="text-emerald-400" /> V8 Sandbox Environment
            </div>
          </div>
        </div>
      </div>

      {/* Main Interactive Playground */}
      <CodePlayground />

      {/* Helper Tips & Instructions */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
        <div className="card p-5 space-y-2">
          <div className="w-8 h-8 rounded-xl bg-indigo-50 dark:bg-indigo-950/60 text-indigo-600 dark:text-indigo-400 flex items-center justify-center font-bold text-xs font-mono">
            1
          </div>
          <h3 className="text-base font-semibold text-slate-900 dark:text-white">
            Pick a Pattern Preset
          </h3>
          <p className="text-slate-500 text-xs leading-relaxed">
            Select code templates for Async/Await, Algorithm Traversal, or API Route simulations from the presets.
          </p>
        </div>

        <div className="card p-5 space-y-2">
          <div className="w-8 h-8 rounded-xl bg-purple-50 dark:bg-purple-950/60 text-purple-600 dark:text-purple-400 flex items-center justify-center font-bold text-xs font-mono">
            2
          </div>
          <h3 className="text-base font-semibold text-slate-900 dark:text-white">
            Write & Test Logic
          </h3>
          <p className="text-slate-500 text-xs leading-relaxed">
            Modify code, test edge cases, and inspect return values directly using `console.log()` statements.
          </p>
        </div>

        <div className="card p-5 space-y-2">
          <div className="w-8 h-8 rounded-xl bg-emerald-50 dark:bg-emerald-950/60 text-emerald-600 dark:text-emerald-400 flex items-center justify-center font-bold text-xs font-mono">
            3
          </div>
          <h3 className="text-base font-semibold text-slate-900 dark:text-white">
            Inspect Output Logs
          </h3>
          <p className="text-slate-500 text-xs leading-relaxed">
            View captured console logs, runtime exceptions, and execution output inside the high-contrast terminal.
          </p>
        </div>
      </div>
    </div>
  )
}
