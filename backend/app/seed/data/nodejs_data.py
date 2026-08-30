"""Node.js Basics course topics and quizzes seed data."""

NODEJS_TOPICS = [
    ("What Node.js is", "what-is-nodejs", "Architecture, V8 engine, and non-blocking I/O model", """# What Node.js Is

Node.js is an open-source, cross-platform JavaScript runtime environment built on Google Chrome's V8 JavaScript engine.

## Core Characteristics

- **V8 Engine**: Compiles JavaScript directly to native machine code for maximum execution speed.
- **Event-Driven & Non-Blocking**: Uses an asynchronous, non-blocking I/O model making it lightweight and efficient.
- **Single-Threaded**: Handles thousands of concurrent client connections on a single main thread using an Event Loop.

```javascript
// Example of asynchronous non-blocking file read in Node.js
const fs = require('fs');

fs.readFile('file.txt', 'utf8', (err, data) => {
  if (err) throw err;
  console.log('File contents loaded!');
});

console.log('Reading file asynchronously...');
// Output order:
// 1. Reading file asynchronously...
// 2. File contents loaded!
```

## When to Use Node.js

- Building RESTful APIs and Microservices.
- Real-time applications (Chat apps, WebSocket servers).
- Streaming applications (Video/Audio streaming).
- CLI tooling and build scripts.
"""),

    ("Installing Node.js", "installing-nodejs", "NVM setup, LTS vs Current releases, and version verification", """# Installing Node.js

Setting up Node.js correctly ensures reproducible development environments across machines.

## Using NVM (Node Version Manager)

It is strongly recommended to use `nvm` (Mac/Linux) or `nvm-windows` to manage multiple Node.js versions.

```bash
# Install specific Node LTS version
nvm install --lts

# Use the installed LTS version
nvm use --lts

# Verify installation
node -v
npm -v
```

## LTS vs Current Releases

- **LTS (Long Term Support)**: Recommended for most users and production environments. Receives active bug fixes and security updates for 30 months.
- **Current**: Latest features and experimental updates. Use for testing new language features.
"""),

    ("REPL", "repl", "Interactive REPL shell, underscore variable, and dot commands", """# Node.js REPL

REPL stands for **Read-Eval-Print Loop**. It is an interactive computer environment that takes single user inputs, evaluates them, and returns the result.

## Accessing REPL

Simply type `node` in your terminal:

```bash
$ node
Welcome to Node.js v20.x.x.
Type ".help" for more information.
> 10 + 20
30
> const name = "WoWCodes";
undefined
> name.toUpperCase()
'WOWCODES'
```

## Special Features

- **Underscore `_`**: Holds the result of the last evaluated expression.
- **Dot Commands**:
  - `.help`: List all commands.
  - `.break` / `.clear`: Exit multi-line expression.
  - `.editor`: Enter multi-line editing mode.
  - `.exit`: Exit the REPL shell.

```javascript
> Math.sqrt(16)
4
> _ * 2
8
```
"""),

    ("npm", "npm", "Package installation, global vs local, devDependencies, and npx", """# npm (Node Package Manager)

npm is the default package manager for Node.js, providing access to the world's largest software registry.

## Initializing Projects & Installing Packages

```bash
# Create package.json interactively
npm init -y

# Install production dependency
npm install express

# Install development dependency
npm install -D nodemon

# Install package globally
npm install -g pm2
```

## Running Scripts and npx

`npx` allows executing binaries from packages without permanent installation:

```bash
# Run command defined in package.json "scripts"
npm run dev

# Execute package binary directly
npx create-react-app my-app
```
"""),

    ("package.json", "package-json", "Manifest fields, SemVer rules (^ vs ~), and custom scripts", """# package.json in Node.js

`package.json` is the manifest file of your Node.js application, defining metadata, dependencies, and execution scripts.

## Structure Example

```json
{
  "name": "wowcodes-backend",
  "version": "1.0.0",
  "description": "Backend API for WoWCodes LMS",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js",
    "test": "jest"
  },
  "dependencies": {
    "express": "^4.18.2"
  },
  "devDependencies": {
    "nodemon": "^3.0.1"
  }
}
```

## Semantic Versioning (SemVer)

- `^4.18.2` (Caret): Allows minor updates & bug fixes (`4.x.x`, up to `< 5.0.0`).
- `~4.18.2` (Tilde): Allows patch bug fixes only (`4.18.x`, up to `< 4.19.0`).
- `4.18.2` (Exact): Locks to exact version specified.
"""),

    ("package-lock.json", "package-lock-json", "Deterministic builds, dependency trees, and npm ci", """# package-lock.json

`package-lock.json` is automatically generated when `npm install` modifies `node_modules` or `package.json`.

## Why package-lock.json Matters

- **Deterministic Installs**: Guarantees that every developer and deployment server gets the exact same dependency tree and nested sub-dependencies.
- **Security Auditability**: Tracks cryptographic hashes (`integrity` SHA-512) for all installed packages.

## `npm ci` vs `npm install`

- `npm install`: Updates `package-lock.json` if dependencies change.
- `npm ci` (Clean Install): Installs directly from `package-lock.json`. Fails if lockfile is out of sync. Used in CI/CD pipelines.

```bash
# Production deployment build command
npm ci
```
"""),

    ("CommonJS (require)", "commonjs", "Module exports, require resolution, and caching", """# CommonJS Modules

CommonJS is the traditional module system introduced by Node.js.

## Exporting & Importing

```javascript
// mathUtils.js
const add = (a, b) => a + b;
const subtract = (a, b) => a - b;

module.exports = {
  add,
  subtract
};
```

```javascript
// app.js
const { add, subtract } = require('./mathUtils');

console.log(add(10, 5)); // 15
```

## Module Caching

Node.js caches modules after the first time they are loaded via `require()`. Subsequent calls return the cached object.

```javascript
// Loaded once and cached in require.cache
const config = require('./config');
```
"""),

    ("ES Modules (import/export)", "es-modules", "Configuring ESM in Node, .mjs extension, and top-level await", """# ES Modules in Node.js

Node.js natively supports standard ECMAScript Modules (ESM).

## Enabling ES Modules

Add `"type": "module"` in `package.json` or use `.mjs` file extension:

```json
{
  "type": "module"
}
```

```javascript
// utils.js
export const formatCurrency = (amount) => `$${amount.toFixed(2)}`;
export default function log(msg) { console.log(msg); }

// main.js
import log, { formatCurrency } from './utils.js';

log(formatCurrency(49.99));
```

## Top-Level await

In ES modules, you can use `await` at the top level of a module without wrapping it in an `async` function:

```javascript
// db.js (ES Module)
import { connectDB } from './dbDriver.js';

await connectDB(); // Top-level await!
console.log('Database connected!');
```
"""),

    ("Global objects", "global-objects", "global, __dirname, __filename, Buffer, and timers", """# Global Objects in Node.js

Node.js provides global variables available in all modules without explicit import.

## Common Globals

- `global`: The root global namespace object (equivalent to `window` in browser).
- `__dirname`: Absolute path to directory containing the current module (CommonJS).
- `__filename`: Absolute path to the current module file (CommonJS).
- `Buffer`: Used to handle binary raw data streams.
- Timers: `setTimeout`, `setInterval`, `setImmediate`.

```javascript
console.log("Current Dir:", __dirname);
console.log("Current File:", __filename);

// Buffer for binary data
const buf = Buffer.from("Hello Node");
console.log(buf.toString("hex")); // "48656c6c6f204e6f6465"
```
"""),

    ("Process object", "process-object", "process.env, process.argv, exit codes, and process.nextTick", """# Process Object in Node.js

The `process` object is a global providing information about, and control over, the current Node.js process.

## Essential Process Properties

```javascript
// Access CLI arguments
const args = process.argv.slice(2);
console.log("CLI Arguments:", args);

// Access environment variables
const PORT = process.env.PORT || 3000;

// Current Working Directory
console.log("Working dir:", process.cwd());

// Exit process gracefully (0 = success, 1 = failure)
if (!process.env.DATABASE_URL) {
  console.error("FATAL: DATABASE_URL missing!");
  process.exit(1);
}
```
"""),

    ("Environment variables", "environment-variables", "Security, dotenv library, and process.env management", """# Environment Variables

Environment variables isolate configuration settings (API keys, ports, DB URLs) from application source code.

## Using dotenv Package

```bash
npm install dotenv
```

Create a `.env` file at project root (add to `.gitignore`!):

```env
PORT=5000
DATABASE_URL=mongodb://localhost:27017/mydb
SECRET_KEY=supersecretkey123
```

Load in your entry point file:

```javascript
require('dotenv').config();

const port = process.env.PORT || 3000;
const dbUrl = process.env.DATABASE_URL;

console.log(`Server starting on port ${port}`);
```
"""),

    ("Event Loop (high priority)", "event-loop", "Event loop phases, Microtasks vs Macrotasks, process.nextTick", """# Node.js Event Loop

The Event Loop is the mechanism that allows Node.js to perform non-blocking I/O operations despite JavaScript being single-threaded.

## Event Loop Phases

1. **Timers**: Executes callbacks scheduled by `setTimeout()` and `setInterval()`.
2. **Pending Callbacks**: Executes I/O callbacks deferred to the next loop iteration.
3. **Idle, Prepare**: Used internally by Node.
4. **Poll**: Retrieves new I/O events; executes I/O related callbacks.
5. **Check**: Executes callbacks scheduled by `setImmediate()`.
6. **Close Callbacks**: Executes close event callbacks (e.g. `socket.on('close')`).

## Microtasks vs Macrotasks

- **Microtasks**: `process.nextTick()` queue and Promise resolution callbacks. Microtasks run **immediately** after current operation finishes, BEFORE moving to next Event Loop phase.
- `process.nextTick()` executes before Promise microtasks.

```javascript
console.log('1. Start');

setTimeout(() => console.log('2. Timeout macrotask'), 0);

Promise.resolve().then(() => console.log('3. Promise microtask'));

process.nextTick(() => console.log('4. nextTick microtask'));

console.log('5. End');

// Execution Order:
// 1. Start
// 5. End
// 4. nextTick microtask
// 3. Promise microtask
// 2. Timeout macrotask
```
"""),

    ("Event Emitter", "event-emitter", "EventEmitter class, on, emit, once, and custom event architectures", """# Event Emitter in Node.js

Much of Node.js core architecture (HTTP servers, streams) is built around the `EventEmitter` class from the `events` module.

## Creating & Handling Events

```javascript
const EventEmitter = require('events');
const customEmitter = new EventEmitter();

// Register listener
customEmitter.on('userRegistered', (user) => {
  console.log(`Sending welcome email to ${user.email}`);
});

// Register one-time listener
customEmitter.once('init', () => {
  console.log('System initialized!');
});

// Emit events
customEmitter.emit('init');
customEmitter.emit('userRegistered', { id: 1, email: 'user@example.com' });
```

## Handling Errors

Always listen to the `'error'` event on EventEmitters to prevent unhandled error crashes!

```javascript
customEmitter.on('error', (err) => {
  console.error('Captured Emitter Error:', err.message);
});
```
""")
]

NODEJS_QUIZZES = {
    "nodejs-what-is-nodejs": [
        {
            "level": "easy",
            "title": "What is Node.js Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which JavaScript engine powers Node.js under the hood?",
                    "explanation": "Node.js uses Google Chrome's V8 engine to compile JavaScript to machine code.",
                    "options": [("SpiderMonkey", False), ("V8 Engine", True), ("JavaScriptCore", False), ("Chakra", False)],
                },
                {
                    "text": "What type of I/O model does Node.js utilize?",
                    "explanation": "Node.js uses an event-driven, non-blocking asynchronous I/O model.",
                    "options": [("Synchronous blocking", False), ("Non-blocking asynchronous I/O", True), ("Multi-threaded blocking", False), ("Parallel synchronous", False)],
                },
            ],
        }
    ],
    "nodejs-installing-nodejs": [
        {
            "level": "easy",
            "title": "Installing Node.js Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Why is Node.js LTS recommended for production applications?",
                    "explanation": "LTS releases guarantee long-term stability, bug fixes, and security patches for 30 months.",
                    "options": [("It has bleeding-edge experimental features", False), ("It provides long-term stability and security maintenance", True), ("It runs twice as fast", False), ("It removes npm dependency", False)],
                },
            ],
        }
    ],
    "nodejs-repl": [
        {
            "level": "easy",
            "title": "Node.js REPL Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "In the Node REPL, what does the special variable '_' store?",
                    "explanation": "The underscore variable '_' stores the evaluation result of the last executed expression.",
                    "options": [("The root directory", False), ("The result of the last evaluated expression", True), ("The last thrown error", False), ("The user input string", False)],
                },
            ],
        }
    ],
    "nodejs-npm": [
        {
            "level": "easy",
            "title": "npm Basics Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which flag is used to install a package as a development dependency?",
                    "explanation": "-D or --save-dev saves packages under devDependencies in package.json.",
                    "options": [("-g", False), ("-D or --save-dev", True), ("-p", False), ("--prod", False)],
                },
            ],
        }
    ],
    "nodejs-package-json": [
        {
            "level": "medium",
            "title": "package.json Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "In SemVer '^1.2.3', what updates are permitted by the caret (^)?",
                    "explanation": "Caret permitting minor updates and patches without breaking changes (1.x.x up to < 2.0.0).",
                    "options": [("Exact version only", False), ("Minor and patch updates without major breaks", True), ("Major breaking upgrades", False), ("Patch updates only", False)],
                },
            ],
        }
    ],
    "nodejs-package-lock-json": [
        {
            "level": "medium",
            "title": "package-lock.json Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which command installs exact dependencies locked in package-lock.json for CI pipelines?",
                    "explanation": "npm ci installs directly from package-lock.json for fast, clean, reproducible builds.",
                    "options": [("npm install", False), ("npm ci", True), ("npm build", False), ("npm update", False)],
                },
            ],
        }
    ],
    "nodejs-commonjs": [
        {
            "level": "medium",
            "title": "CommonJS Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which object in CommonJS is exported by default when a module is required?",
                    "explanation": "module.exports is the object returned when require() is called.",
                    "options": [("export default", False), ("module.exports", True), ("global.exports", False), ("this.exports", False)],
                },
            ],
        }
    ],
    "nodejs-es-modules": [
        {
            "level": "medium",
            "title": "ES Modules in Node Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "How do you enable native ES Modules in a Node project package.json?",
                    "explanation": "Adding 'type': 'module' in package.json instructs Node to treat .js files as ES Modules.",
                    "options": [("'module': true", False), ("'type': 'module'", True), ("'es6': true", False), ("'mode': 'import'", False)],
                },
            ],
        }
    ],
    "nodejs-global-objects": [
        {
            "level": "medium",
            "title": "Global Objects Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does __dirname represent in CommonJS Node modules?",
                    "explanation": "__dirname yields the absolute directory path of the current file.",
                    "options": [("The current working directory", False), ("The absolute directory path of the current module", True), ("The node binary path", False), ("The user home directory", False)],
                },
            ],
        }
    ],
    "nodejs-process-object": [
        {
            "level": "medium",
            "title": "Process Object Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Where are environment variables stored on the global process object?",
                    "explanation": "process.env contains key-value pairs of environment variables.",
                    "options": [("process.config", False), ("process.env", True), ("process.vars", False), ("process.globals", False)],
                },
            ],
        }
    ],
    "nodejs-environment-variables": [
        {
            "level": "easy",
            "title": "Environment Variables Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which standard file stores local environment variables and should NEVER be committed to Git?",
                    "explanation": ".env stores secrets locally and must be added to .gitignore.",
                    "options": [("config.json", False), (".env", True), ("package.json", False), ("env.js", False)],
                },
            ],
        }
    ],
    "nodejs-event-loop": [
        {
            "level": "hard",
            "title": "Event Loop High Priority Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "Which function schedules a microtask that runs BEFORE Promise microtasks and next Event Loop phase?",
                    "explanation": "process.nextTick() callbacks run immediately after current operation, before Promise microtasks.",
                    "options": [("setImmediate()", False), ("process.nextTick()", True), ("setTimeout()", False), ("requestAnimationFrame()", False)],
                },
                {
                    "text": "In which Event Loop phase are setImmediate() callbacks executed?",
                    "explanation": "setImmediate() callbacks run in the Check phase of the Event Loop.",
                    "options": [("Timers phase", False), ("Check phase", True), ("Poll phase", False), ("Idle phase", False)],
                },
            ],
        }
    ],
    "nodejs-event-emitter": [
        {
            "level": "medium",
            "title": "Event Emitter Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which method registers a listener that triggers at most ONCE when an event is emitted?",
                    "explanation": "emitter.once() automatically unregisters the listener after its first invocation.",
                    "options": [("emitter.on()", False), ("emitter.once()", True), ("emitter.single()", False), ("emitter.addListener()", False)],
                },
            ],
        }
    ],
}
