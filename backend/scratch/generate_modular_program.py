# Comprehensive script to generate all 6 modules, 10-question employer-perspective quizzes per topic, and the 50-question 100-mark final evaluation exam.

modules_definition = [
    {
        "module": "Module 1: Front-End Web Development & Server Runtime",
        "topics": [
            ("HTML", "html", "Semantic HTML5, Accessibility standards, Document structure, and Metadata", """# HTML5 Engineering & Accessibility

## Beginner: Semantic Markup & Hierarchy
Document structure begins with `<!DOCTYPE html>`. `<html>` holds `<head>` metadata and `<body>` UI elements. Use `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, and `<footer>` for strict semantic hierarchy. Rule: Exactly one `<h1>` per page.

## Intermediate: Accessibility & Form Security
- ARIA roles (`role='button'`, `aria-expanded='false'`) for assistive screen readers.
- Form inputs: Enforce `type='email'`, `required`, `pattern`, and `autocomplete` attributes.
- Use `alt` text on `<img>` for WCAG AA accessibility compliance.

## Advanced & Experienced Engineer: Performance & SEO
Optimize DOM node count. Defer script parsing via `<script defer src='app.js'></script>`. Preload critical fonts with `<link rel='preload'>` to optimize Core Web Vitals (LCP/INP)."""),

            ("CSS", "css", "CSS Box Model, Flexbox 1D, CSS Grid 2D, Positioning, Viewports, and Media Queries", """# CSS3 Architecture & Layout Systems

## Beginner: Box Model & Reset
- Box Model: Content, Padding, Border, Margin. Always set `box-sizing: border-box`.
- Selectors: Element, Class (`.btn`), ID (`#main`), Attribute (`[data-active='true']`).

## Intermediate: Positioning & Modern Layouts
- Positioning: `static`, `relative`, `absolute` (nearest non-static parent), `fixed` (viewport), `sticky`.
- Flexbox (1D): `display: flex; justify-content: space-between; align-items: center; gap: 1rem;`.
- Grid (2D): `display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));`.

## Advanced & Experienced Engineer: Custom Properties & Responsive Breakpoints
- CSS Variables: `:root { --primary-color: #6366f1; }`.
- Fluid media queries: `@media (min-width: 768px)` for mobile-first responsive design."""),

            ("JavaScript", "javascript", "V8 Engine execution, ES6+, Async/Await, Closures, DOM, and Event Loop", """# Modern JavaScript Engineering

## Beginner: Syntax & Scope
- Primitive types: `string`, `number`, `boolean`, `symbol`, `bigint`, `null`, `undefined`.
- Scoping: `let` and `const` are block-scoped; `var` is function-scoped. Use strict equality `===`.

## Intermediate: Functional Programming & Async JS
- Array methods: `.map()`, `.filter()`, `.reduce()`, `.find()`, `.some()`.
- Closures: Outer lexical environment binding surviving execution context teardown.
- Promises & Async/Await: `try { const data = await fetch(url); } catch(err) { ... }`.

## Advanced & Experienced Engineer: Event Loop Architecture
Single-threaded Call Stack -> Microtask Queue (Promises, `queueMicrotask`) -> Macrotask Queue (`setTimeout`, `setInterval`). Microtasks drain completely before Macrotasks run."""),

            ("React", "react", "React 19 Components, State Hooks, Props, Virtual DOM, and Reconciliation", """# React 19 Application Architecture

## Beginner: JSX & Component State
React builds UI using declarative components. State management with `useState()`. Props pass data downward. Return JSX wrapped in fragments `<>...</>`.

## Intermediate: Side Effects & Performance Hooks
- `useEffect(fn, deps)` handles data fetching, subscriptions, and DOM side-effects. Always clean up listeners in returned function.
- `useMemo()` caches computed values; `useCallback()` memoizes callback references.

## Advanced & Experienced Engineer: Virtual DOM & Custom Hooks
Reconciliation algorithm compares Fiber trees using key props. Extract business logic into custom hooks (`useAuth()`, `useFetch()`)."""),

            ("Redux", "redux", "Global State Management, Redux Toolkit, Slices, Selectors, and Thunks", """# Redux Toolkit State Management

## Beginner: Store & Single Source of Truth
Redux maintains global immutable state tree. Components dispatch actions to trigger pure reducers.

## Intermediate: Redux Toolkit (RTK)
Use `createSlice({ name, initialState, reducers })`. Actions auto-generated from reducer keys. Use `useSelector()` to query store state and `useDispatch()` to send actions.

## Advanced & Experienced Engineer: Async Thunks & RTK Query
`createAsyncThunk()` handles asynchronous API lifecycles (pending, fulfilled, rejected). RTK Query handles automatic caching, polling, and invalidation."""),

            ("Front-End Web Development: JavaScript", "fe-javascript", "DOM Selection, Event Delegation, XSS Prevention, and Web APIs", """# Front-End JavaScript & Web APIs

## Beginner: DOM Manipulation
Select elements via `document.querySelector()`. Modify properties using `element.textContent` (safe) or `element.classList.add()`.

## Intermediate: Event Delegation & Event Propagation
- Event Bubbling: Events travel up from target to document root.
- Delegation: Attach a single listener to a parent list/container and check `event.target`.

## Advanced & Experienced Engineer: Security & Storage
Prevent XSS by avoiding `innerHTML` with untrusted data. Use `localStorage` for client state and `sessionStorage` for tab-scoped storage."""),

            ("Node.js", "nodejs", "Asynchronous Event Loop, Non-blocking I/O, Buffer, Streams, and Native Modules", """# Node.js Server Engineering

## Beginner: Node Architecture
Node.js is an open-source, cross-platform JavaScript runtime environment built on V8. Uses non-blocking event-driven I/O.

## Intermediate: Modules & Native APIs
CommonJS (`require`/`module.exports`) vs ES Modules (`import`/`export`). Native modules: `fs` (file system), `path`, `http`, `events`.

## Advanced & Experienced Engineer: Streams & Cluster Threads
Handle large payloads using Streams (`createReadStream().pipe()`). Use Cluster module or Worker Threads for CPU-bound computations."""),

            ("Express.js", "express", "RESTful API routes, Middleware Pipeline, Error Handling, and CORS", """# Express.js Microservices

## Beginner: Routing & App Setup
Create server: `const app = express(); app.use(express.json());`. Define routes: `app.get()`, `app.post()`, `app.put()`, `app.delete()`.

## Intermediate: Middleware Pipeline
Middleware functions `(req, res, next)` execute sequentially. Handle CORS with `cors()`, parsing with `body-parser`, and authentication middleware.

## Advanced & Experienced Engineer: Centralized Error Handling
Pass errors to `next(err)`. Implement centralized error handling middleware `(err, req, res, next)` with structured JSON error responses.""")
        ]
    },
    {
        "module": "Module 2: Python & Fundamental Computer Science",
        "topics": [
            ("Python", "python", "Python environment setup, dynamic typing, syntax, functions, and collections", """# Python Language Architecture

## Beginner: Environment & Syntax
Python is dynamically typed and interpreted. Commands: `python --version`, `pip install`. Primitive types: `int`, `float`, `str`, `bool`.

## Intermediate: Collections & Comprehensions
- Lists (mutable, ordered), Dicts (hash maps, O(1) average lookup), Sets (unique elements), Tuples (immutable).
- List comprehensions: `[x**2 for x in range(10) if x % 2 == 0]`.

## Advanced & Experienced Engineer: Reference Memory Model
Variables store object references. Avoid default mutable parameters (`def fn(a=[])`). Use `def fn(a=None): if a is None: a = []`."""),

            ("Python Programming Fundamentals", "python-fundamentals", "Control flow, bitwise operators, functions, and memory optimization", """# Python Engineering Core

## Beginner: Control Flow & Operators
- Operators: Arithmetic `+ - * / // % **`, Bitwise `<< >> & | ^`.
- Logic: `if/elif/else`. Loops: `for` and `while` with `break` and `continue`.

## Intermediate: Functions & Decorators
Define with `def`. Decorators wrap functions `def my_decorator(func): ...` to intercept calls (logging, timing, auth).

## Advanced & Experienced Engineer: Memory & Generators
Generators use `yield` to stream data lazily with O(1) memory usage instead of building huge lists in RAM."""),

            ("Data Structures and Algorithms", "dsa", "Sorting algorithms, Searching techniques, Timsort, and Search Selection Framework", """# Advanced Data Structures and Algorithms

## Beginner: Linear Search & Insertion Sort
Linear search checks elements one-by-one in O(n) time. Insertion sort builds sorted sub-arrays in O(n^2) time.

## Intermediate: Binary Search & Timsort
Binary search requires sorted arrays, halving range in O(log n) time. Python uses Timsort (hybrid Insertion + Merge sort, O(n log n)).

## Advanced & Experienced Engineer: Search Selection Matrix
- Binary Search: Sorted static datasets.
- Interpolation Search: O(log log n) on uniform distributions.
- Multi-query break-even: Sorting once O(n log n) + Q binary searches beats Q linear scans when Q > log n.""")
        ]
    },
    {
        "module": "Module 3: Backend Development with FastAPI & APIs",
        "topics": [
            ("FastAPI", "fastapi", "FastAPI setup, ASGI Uvicorn, Pydantic schemas, and Open API docs", """# Production FastAPI Backends

## Beginner: Routes & Swagger UI
FastAPI is built on Starlette and Pydantic. Auto-generates OpenAPI docs at `/docs`. Runs on Uvicorn ASGI server.

## Intermediate: Pydantic Validation & Path/Query Params
Define request schemas with `BaseModel`. Path parameters `/items/{id}` identify resources; query parameters `/items?page=1` filter.

## Advanced & Experienced Engineer: Yield Dependencies & Middleware
`yield` dependencies open DB sessions before requests and guarantee cleanup (`finally: db.close()`) even on error."""),

            ("SQL", "sql", "SQL Querying, DDL/DML/DQL, Joins, Aggregation, and Execution Order", """# SQL Engineering & Query Optimization

## Beginner: SQL Sub-Languages
- DDL (`CREATE TABLE`), DML (`INSERT`, `UPDATE`, `DELETE`), DQL (`SELECT`).
- Constraints: PRIMARY KEY, FOREIGN KEY, NOT NULL, UNIQUE.

## Intermediate: Joins & WHERE Safety
- Joins: INNER, LEFT, RIGHT, FULL.
- Always include `WHERE` on `UPDATE`/`DELETE` to prevent updating all rows.

## Advanced & Experienced Engineer: Execution Order & Grouping
SQL Execution Order: 1. FROM 2. WHERE 3. GROUP BY 4. HAVING 5. SELECT 6. ORDER BY 7. LIMIT. `WHERE` filters rows before grouping; `HAVING` filters groups after."""),

            ("Backend Development with FastAPI", "backend-fastapi", "FastAPI Architecture, Pydantic v2 Validators, and Background Tasks", """# Advanced FastAPI Architecture

## Beginner: App Structure
Organize app into routers (`APIRouter`), schemas, models, and dependencies.

## Intermediate: Pydantic v2 Validators & Field Constraints
Use `Field(gt=0)` and `@field_validator` for custom attribute validation.

## Advanced & Experienced Engineer: Background Tasks & Security
Use `BackgroundTasks` to defer non-blocking jobs (emails, file processing). Enforce OAuth2 with JWT tokens."""),

            ("Client-Server Communication and APIs", "apis", "HTTP Verbs, Status Codes, Fetch API, LocalStorage vs Cookies, and Payload Serialization", """# Client-Server Architecture & REST APIs

## Beginner: HTTP Methods & Status Codes
- Methods: GET (read, idempotent), POST (create), PUT (replace), PATCH (update), DELETE (remove).
- Status codes: 200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 404 Not Found, 500 Server Error.

## Intermediate: Storage & Fetch API
- `localStorage` (persists), `sessionStorage` (tab lifetime), `Cookies` (auto-sent with requests).
- `fetch()` only rejects on genuine network failure, not on 404/500 HTTP errors. Check `if (!res.ok)`.

## Advanced & Experienced Engineer: JSON Payload Serialization
Use `JSON.stringify()` to serialize objects for HTTP transmission and `JSON.parse()` to deserialize.""")
        ]
    },
    {
        "module": "Module 4: Version Control & DevOps",
        "topics": [
            ("Git & GitHub", "git-github", "DVCS concepts, staging area, branching strategies, remotes, and PR code reviews", """# Git & GitHub Enterprise Workflow

## Beginner: Core Git Commands
Git is a Distributed VCS. Workflow: Working Directory -> Staging Area -> Local Repo -> Remote GitHub. `git init`, `git add .`, `git commit -m "msg"`.

## Intermediate: Branching & Remote Operations
`git switch -c feature` creates branches. `git fetch` downloads remote commits without merging; `git pull` fetches and merges.

## Advanced & Experienced Engineer: Rebase vs Merge Topology
`git merge` creates a merge commit. `git rebase` replays commits onto target branch for a clean linear history."""),

            ("Version Control with Git and GitHub", "vcs-git", "Branching, Conflict Resolution, Git Rebase, and Gitignore Security", """# Version Control & Release Engineering

## Beginner: Tracking & Status
Inspect repository state with `git status` and commit history with `git log --oneline`.

## Intermediate: Conflict Resolution
Resolve conflicts by editing markers (`<<<<<<< HEAD`), staging resolved files with `git add`, and completing commit.

## Advanced & Experienced Engineer: Git Security & Secret Protection
Never commit `.env` or credentials. Use `.gitignore` and tools like `trufflehog` to scan repository history.""")
        ]
    },
    {
        "module": "Module 5: Databases & ORM Integration",
        "topics": [
            ("Databases and SQL", "sql-databases", "Relational DBs, NoSQL, Column constraints, DELETE vs TRUNCATE vs DROP, and Joins", """# Database Engineering & Storage Engines

## Beginner: Database Classification
Relational DBs (PostgreSQL, SQLite) store structured tables with foreign keys. NoSQL DBs (MongoDB, Redis) store documents or key-value pairs.

## Intermediate: Table Lifecycle & Constraints
DELETE removes rows selectively; TRUNCATE clears all table rows keeping structure; DROP deletes table schema and data entirely.

## Advanced & Experienced Engineer: Indexing & Execution Plans
Create indexes (`CREATE INDEX`) on foreign keys and query columns to turn O(n) table scans into O(log n) B-Tree lookups."""),

            ("Relational, NoSQL databases, SQL basics, and ORMs", "relational-nosql", "RDBMS vs NoSQL, ACID compliance, Normalization, and ORM abstractions", """# Enterprise Data Systems & Normalization

## Beginner: ACID Properties
Atomicity, Consistency, Isolation, Durability guarantee reliable database transactions.

## Intermediate: Database Normalization
First Normal Form (1NF), 2NF, and 3NF reduce data redundancy and eliminate update anomalies.

## Advanced & Experienced Engineer: Polyglot Persistence
Combine RDBMS (PostgreSQL) for transactional business records, Redis for caching, and ElasticSearch for full-text search."""),

            ("ORM and Full-Stack Integration", "orm-integration", "SQLAlchemy ORM, Session CRUD lifecycle, and Pydantic v2 from_attributes bridge", """# SQLAlchemy ORM & Schema Integration

## Beginner: Models & Base
Define models inheriting from `declarative_base()`. Map columns with `Column(Integer, primary_key=True)`.

## Intermediate: Session CRUD Operations
`db.add(obj)`, `db.commit()`, `db.refresh(obj)` for create. `db.query(Model).filter().first()` for read.

## Advanced & Experienced Engineer: Pydantic v2 Bridge
Set `model_config = ConfigDict(from_attributes=True)` on Pydantic schemas to serialize SQLAlchemy ORM objects directly into API JSON.""")
        ]
    },
    {
        "module": "Module 6: Large Language Models & Applied AI Engineering",
        "topics": [
            ("Large Language Models and Prompt Engineering", "llms-prompts", "AI/ML/DL, Transformers, Tokenization, Self-Attention, Prompt Techniques, and Plan vs Act", """# LLM Architecture & Prompt Engineering

## Beginner: AI Taxonomy & Transformer Pipeline
AI > ML > Deep Learning > LLMs. Transformer Pipeline: Tokenization -> Embedding -> Positional Encoding -> Self-Attention -> Transformer Blocks -> Softmax next-token prediction.

## Intermediate: 5 Prompt Components & CoT
Components: 1. Task 2. Context 3. Constraints 4. Format 5. Examples. Chain-of-Thought (CoT) prompts model to show step-by-step reasoning.

## Advanced & Experienced Engineer: Context Management & Plan/Act Modes
Manage finite token context windows. Use Plan Mode to analyze specifications without modifying state, and Act Mode to execute validated code changes."""),

            ("AI API Integration", "ai-api-integration", "LLM APIs, Security, RAG Architecture, Vector Embeddings, Cosine Similarity, and Streaming", """# Production AI API & RAG Integration

## Beginner: API Security
Store API keys in `.env`, load via `python-dotenv`, and add `.env` to `.gitignore`. Never hardcode keys in client apps.

## Intermediate: RAG Architecture
RAG Flow: Document PDF -> PyPDF Text Extraction -> Chunking -> Vector Embeddings -> Vector DB Search -> Context Injection -> LLM Answer.

## Advanced & Experienced Engineer: Cosine Similarity & Streaming
Cosine similarity measures vector angle closeness: `cos(theta) = (A . B) / (||A|| ||B||)`. Use FastAPI `StreamingResponse` for token-by-token streaming UI."""),

            ("AI-Assisted Development Practices", "ai-assisted-development", "Debugging with AI, Golden Rule, Prompt Scoping, Observability, and Health Checks", """# AI-Assisted Engineering & Observability

## Beginner: Error Classification
Syntax Errors (malformed code), Runtime Errors (crashes like `ZeroDivisionError`), Logical Errors (incorrect outputs).

## Intermediate: The Golden Rule of AI Coding
Write a base/brute-force implementation yourself first. Use AI to optimize, debug, or explain concepts after the initial attempt.

## Advanced & Experienced Engineer: Observability & Health Checks
Production AI backends require structured JSON logging, Prometheus metrics monitoring (latency, 5xx rates), and OpenAPI `/health` endpoints.""")
        ]
    }
]

print("Module definition structured successfully!")
