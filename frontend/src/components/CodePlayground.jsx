import { useState } from 'react'
import { FiPlay, FiRefreshCw, FiTrash2, FiCode, FiTerminal, FiCheckCircle, FiAlertTriangle, FiZap } from 'react-icons/fi'
import { apiClient } from '../api/apiClient'

const PRESET_SNIPPETS = {
  js_async: {
    name: 'Async/Await & Promises',
    language: 'javascript',
    code: `// Interactive JavaScript Async/Await Playground
async function fetchUserData() {
  console.log("⏳ Fetching user profile...");
  
  const user = await new Promise((resolve) => {
    setTimeout(() => {
      resolve({ id: 101, name: "Selvam SDE", role: "Full Stack Developer", level: 5 });
    }, 500);
  });

  console.log("✅ User retrieved:", user.name);
  console.log("🚀 Role:", user.role, "| Level:", user.level);
  return user;
}

fetchUserData();`
  },
  js_array: {
    name: 'Array Methods & Transformations',
    language: 'javascript',
    code: `// Array Methods: map, filter, reduce
const scores = [85, 92, 78, 95, 88, 60, 100];

console.log("Original Scores:", scores);

const highPerformers = scores.filter(s => s >= 85);
console.log("High Performers (>=85):", highPerformers);

const scaledScores = scores.map(s => Math.min(100, s + 5));
console.log("Scaled (+5 pts):", scaledScores);

const averageScore = scores.reduce((sum, val) => sum + val, 0) / scores.length;
console.log("Average Score:", averageScore.toFixed(2));`
  },
  express_mock: {
    name: 'Express.js Route Simulation',
    language: 'javascript',
    code: `// Express.js Route & Middleware Simulator
function mockExpressServer() {
  const routes = [];
  const middlewares = [];

  function use(fn) { middlewares.push(fn); }
  function get(path, handler) { routes.push({ method: 'GET', path, handler }); }

  // Logger Middleware
  use((req) => console.log(\`[LOG] \${req.method} \${req.url} @ \${new Date().toLocaleTimeString()}\`));

  // GET /api/courses route
  get('/api/courses', (req, res) => {
    return { status: 200, data: ['JavaScript Async', 'Express.js', 'PostgreSQL Basics'] };
  });

  // Execute Simulation
  const req = { method: 'GET', url: '/api/courses' };
  middlewares.forEach(mw => mw(req));
  const route = routes.find(r => r.method === req.method && r.path === req.url);
  
  if (route) {
    const res = route.handler(req, {});
    console.log("Response:", JSON.stringify(res, null, 2));
  }
}

mockExpressServer();`
  },
  py_basics: {
    name: 'Python Data Structures',
    language: 'python',
    code: `# Python Basics Playground
courses = ["FastAPI", "PostgreSQL", "React 19", "Python Async"]
user_progress = {"completed": 12, "total": 15}

print("Available Courses:", courses)
pct = (user_progress["completed"] / user_progress["total"]) * 100
print(f"Overall Progress: {pct:.1f}%")

for idx, c in enumerate(courses, 1):
    print(f"  {idx}. {c}")`
  }
}

export default function CodePlayground({ initialCode, initialLanguage = 'javascript' }) {
  const [code, setCode] = useState(initialCode || PRESET_SNIPPETS.js_async.code)
  const [language, setLanguage] = useState(initialLanguage)
  const [outputLogs, setOutputLogs] = useState([])
  const [isRunning, setIsRunning] = useState(false)
  const [executionTime, setExecutionTime] = useState(null)
  const [activePreset, setActivePreset] = useState('js_async')

  const handleRunCode = async () => {
    setIsRunning(true)
    setOutputLogs([])
    setExecutionTime(null)
    const startTime = performance.now()
    const logs = []

    if (language === 'javascript') {
      try {
        const customConsole = {
          log: (...args) => {
            logs.push({ type: 'log', text: args.map(a => typeof a === 'object' ? JSON.stringify(a, null, 2) : String(a)).join(' ') })
          },
          error: (...args) => {
            logs.push({ type: 'error', text: args.map(a => typeof a === 'object' ? JSON.stringify(a, null, 2) : String(a)).join(' ') })
          },
          warn: (...args) => {
            logs.push({ type: 'warn', text: args.map(a => typeof a === 'object' ? JSON.stringify(a, null, 2) : String(a)).join(' ') })
          }
        }

        const runFn = new Function('console', `return (async () => { ${code} })()`)
        await runFn(customConsole)

        if (logs.length === 0) {
          logs.push({ type: 'info', text: '[Code executed successfully with no console output]' })
        }
      } catch (err) {
        logs.push({ type: 'error', text: `Runtime Error: ${err.message}` })
      }
      const endTime = performance.now()
      setExecutionTime((endTime - startTime).toFixed(1))
      setOutputLogs(logs)
      setIsRunning(false)
    } else {
      try {
        const res = await apiClient.post('/playground/execute', {
          language,
          code
        })
        const data = res.data
        if (data.output) {
          logs.push({ type: 'log', text: data.output })
        }
        if (data.error) {
          logs.push({ type: 'error', text: data.error })
        }
        setExecutionTime(data.execution_time_ms)
      } catch (err) {
        logs.push({ type: 'error', text: err.response?.data?.detail || 'Execution failed on server.' })
      }
      setOutputLogs(logs)
      setIsRunning(false)
    }
  }

  const handleSelectPreset = (key) => {
    setActivePreset(key)
    setCode(PRESET_SNIPPETS[key].code)
    setLanguage(PRESET_SNIPPETS[key].language)
    setOutputLogs([])
  }

  return (
    <div className="bg-slate-950 border border-slate-800 rounded-3xl shadow-2xl overflow-hidden font-sans">
      {/* Header Toolbar */}
      <div className="px-5 py-4 bg-slate-900 border-b border-slate-800 flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-indigo-600/20 text-indigo-400 rounded-xl border border-indigo-500/30">
            <FiCode className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-extrabold text-white flex items-center gap-2 text-base">
              Interactive Code Sandbox
              <span className="text-[11px] font-mono font-bold px-2.5 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                Live Execution
              </span>
            </h3>
            <p className="text-xs text-slate-400">Run code algorithms, test snippets, and inspect real-time outputs</p>
          </div>
        </div>

        {/* Preset Selector */}
        <div className="flex items-center gap-2">
          <label className="text-xs text-slate-300 font-mono font-semibold flex items-center gap-1">
            <FiZap className="text-amber-400" /> Presets:
          </label>
          <select
            value={activePreset}
            onChange={(e) => handleSelectPreset(e.target.value)}
            className="bg-slate-950 border border-slate-800 text-xs text-slate-100 font-mono rounded-xl px-3 py-2 focus:ring-2 focus:ring-indigo-500 focus:outline-none"
          >
            {Object.entries(PRESET_SNIPPETS).map(([key, val]) => (
              <option key={key} value={key}>{val.name}</option>
            ))}
          </select>
        </div>
      </div>

      {/* Main Grid: Code Editor & Console */}
      <div className="grid grid-cols-1 lg:grid-cols-12 min-h-[360px]">
        {/* Code Input Area */}
        <div className="lg:col-span-7 border-b lg:border-b-0 lg:border-r border-slate-800 p-4 sm:p-5 flex flex-col justify-between bg-slate-900/60">
          <div className="flex-1 flex flex-col">
            <div className="flex items-center justify-between text-xs text-slate-400 mb-2 font-mono">
              <span className="text-indigo-400 font-bold">main.{language === 'javascript' ? 'js' : 'py'}</span>
              <span>Language: <strong className="text-emerald-400 capitalize">{language}</strong></span>
            </div>
            <textarea
              value={code}
              onChange={(e) => setCode(e.target.value)}
              spellCheck="false"
              className="w-full flex-1 min-h-[280px] bg-slate-950 text-emerald-300 font-mono text-xs sm:text-sm p-4 rounded-2xl border border-slate-800 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500/40 focus:outline-none resize-y leading-relaxed shadow-inner selection:bg-indigo-600 selection:text-white"
              placeholder="// Write your code here..."
            />
          </div>

          {/* Action Buttons */}
          <div className="mt-4 flex flex-wrap items-center justify-between gap-3">
            <div className="flex items-center gap-2">
              <button
                onClick={handleRunCode}
                disabled={isRunning}
                className="flex items-center gap-2 px-5 py-2.5 bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-500 hover:to-purple-500 disabled:bg-slate-800 text-white text-xs font-extrabold rounded-xl transition shadow-lg shadow-indigo-600/30 active:scale-95"
              >
                <FiPlay className="w-4 h-4 fill-current" />
                {isRunning ? 'Running Code...' : 'Run Code'}
              </button>
              <button
                onClick={() => setCode('')}
                className="p-2 text-slate-400 hover:text-white hover:bg-slate-800 rounded-xl transition border border-slate-800"
                title="Clear Code"
              >
                <FiTrash2 className="w-4 h-4" />
              </button>
              <button
                onClick={() => handleSelectPreset(activePreset)}
                className="p-2 text-slate-400 hover:text-white hover:bg-slate-800 rounded-xl transition border border-slate-800"
                title="Reset to Preset"
              >
                <FiRefreshCw className="w-4 h-4" />
              </button>
            </div>

            {executionTime && (
              <span className="text-xs text-emerald-400 font-mono flex items-center gap-1 bg-emerald-500/10 px-3 py-1 rounded-full border border-emerald-500/20 font-bold">
                <FiCheckCircle className="w-3.5 h-3.5" /> {executionTime} ms
              </span>
            )}
          </div>
        </div>

        {/* Output Console Log Panel */}
        <div className="lg:col-span-5 bg-slate-950 p-4 sm:p-5 flex flex-col justify-between">
          <div className="flex items-center justify-between pb-3 border-b border-slate-800/80 mb-3">
            <div className="flex items-center gap-2 text-slate-200 font-bold text-xs font-mono">
              <FiTerminal className="w-4 h-4 text-emerald-400" />
              Console Terminal Output
            </div>
            {outputLogs.length > 0 && (
              <button
                onClick={() => setOutputLogs([])}
                className="text-[11px] text-slate-400 hover:text-slate-200 transition font-mono"
              >
                Clear Console
              </button>
            )}
          </div>

          <div className="flex-1 font-mono text-xs overflow-y-auto max-h-[320px] space-y-2 p-1">
            {outputLogs.length === 0 ? (
              <div className="h-full flex flex-col items-center justify-center text-slate-600 space-y-2 py-12">
                <FiTerminal className="w-8 h-8 opacity-40 text-slate-500" />
                <p className="text-xs font-mono text-slate-500">Click "Run Code" to inspect output logs here.</p>
              </div>
            ) : (
              outputLogs.map((log, i) => (
                <div
                  key={i}
                  className={`p-3 rounded-xl border leading-relaxed whitespace-pre-wrap font-mono text-xs ${
                    log.type === 'error'
                      ? 'bg-rose-950/50 border-rose-800/60 text-rose-300'
                      : log.type === 'warn'
                      ? 'bg-amber-950/50 border-amber-800/60 text-amber-300'
                      : log.type === 'info'
                      ? 'bg-slate-900 border-slate-800 text-slate-400 italic'
                      : 'bg-slate-900 border-slate-800 text-emerald-400 shadow-sm'
                  }`}
                >
                  {log.type === 'error' && <FiAlertTriangle className="w-3.5 h-3.5 inline mr-1.5 text-rose-400" />}
                  {log.text}
                </div>
              ))
            )}
          </div>
        </div>
      </div>
    </div>
  )
}
