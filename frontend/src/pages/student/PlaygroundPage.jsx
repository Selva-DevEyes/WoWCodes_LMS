import CodePlayground from '../../components/CodePlayground'
import { FiCode, FiZap, FiCpu } from 'react-icons/fi'

export default function PlaygroundPage() {
  return (
    <div className="max-w-7xl mx-auto space-y-6">
      {/* Page Banner */}
      <div className="bg-gradient-to-r from-indigo-900/40 via-purple-900/30 to-slate-900 border border-indigo-500/20 rounded-2xl p-6 sm:p-8 backdrop-blur-sm">
        <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
          <div className="space-y-2">
            <span className="inline-flex items-center gap-1.5 text-xs font-semibold px-3 py-1 rounded-full bg-indigo-500/20 text-indigo-400 border border-indigo-500/30">
              <FiZap className="text-yellow-400" /> Interactive Learning Sandbox
            </span>
            <h1 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
              Coding Playground
            </h1>
            <p className="text-slate-300 text-sm max-w-2xl">
              Write, execute, and experiment with JavaScript, Promises, Express server routes, and data structure logic in real-time.
            </p>
          </div>

          <div className="flex items-center gap-3">
            <div className="flex items-center gap-2 text-xs text-slate-300 bg-slate-800/80 px-3 py-2 rounded-xl border border-slate-700">
              <FiCpu className="text-emerald-400" /> Web & API Sandbox Active
            </div>
          </div>
        </div>
      </div>

      {/* Main Interactive Playground */}
      <CodePlayground />

      {/* Helper Tips & Instructions */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="bg-slate-900/60 border border-slate-800 rounded-xl p-5 space-y-2">
          <div className="w-9 h-9 rounded-lg bg-blue-500/10 text-blue-400 flex items-center justify-center font-bold">
            1
          </div>
          <h4 className="text-white font-medium text-sm">Pick a Preset</h4>
          <p className="text-slate-400 text-xs leading-relaxed">
            Select standard code templates for Async/Await, Array Transformations, or Express Route simulations from the top dropdown.
          </p>
        </div>

        <div className="bg-slate-900/60 border border-slate-800 rounded-xl p-5 space-y-2">
          <div className="w-9 h-9 rounded-lg bg-purple-500/10 text-purple-400 flex items-center justify-center font-bold">
            2
          </div>
          <h4 className="text-white font-medium text-sm">Write & Edit</h4>
          <p className="text-slate-400 text-xs leading-relaxed">
            Modify logic, test custom functions, and print values directly using `console.log()` statements.
          </p>
        </div>

        <div className="bg-slate-900/60 border border-slate-800 rounded-xl p-5 space-y-2">
          <div className="w-9 h-9 rounded-lg bg-emerald-500/10 text-emerald-400 flex items-center justify-center font-bold">
            3
          </div>
          <h4 className="text-white font-medium text-sm">Inspect Console</h4>
          <p className="text-slate-400 text-xs leading-relaxed">
            Click <strong>Run Code</strong> to inspect return outputs, error stack traces, and execution timings in the console panel.
          </p>
        </div>
      </div>
    </div>
  )
}
