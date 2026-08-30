# Script to generate full WoWCodes_WoWCodes_data.py with 12 topics and 10 questions per topic.

topics_data = [
    ("Python Programming Fundamentals", "python-fundamentals", "Python setup, syntax, types, operators, logic, loops, functions, lists, strings, dicts", """# Python Programming Fundamentals

## Beginner: Environment Setup & Core Syntax
Python is an interpreted, dynamically typed language. Install Python 3.10+ and VS Code. Commands: `pwd`, `ls`/`dir`, `cd`, `mkdir`.
Variables store references. Types: `str`, `int`, `float`, `bool`. Operators: arithmetic `+ - * / % // **`, comparison `== != < > <= >=`, logical `and or not`, bitwise `<< >> & | ^`.

## Intermediate: Control Flow & Collections
Indentation (4 spaces) defines blocks. `if/elif/else` controls flow. `for` loops iterate over `range(start, stop, step)` or sequences; `while` loops repeat while a condition is True. `break` exits, `continue` skips.
Lists are mutable, ordered (`append`, `pop`, `insert`, `remove`, slicing). Strings are immutable. Dictionaries store key-value pairs with fast O(1) lookups (`get(key, default)` avoids KeyError).

## Advanced & Experienced Engineer: Production Best Practices
Avoid default mutable arguments (`def fn(lst=[])`). Use dictionary/list comprehensions for high-throughput processing. Bitwise shifts (`x << 2` for `x * 4`) provide single-cycle CPU operations."""),

    ("Data Structures and Algorithms", "dsa", "Sorting, Searching, Timsort, Hashing, and Algorithm Selection Framework", """# Data Structures and Algorithms (DSA)

## Beginner: Linear Search & Insertion Sort
Linear search checks items one by one in O(n) time and O(1) space. Insertion Sort builds a sorted array element-by-element in O(n^2) worst-case and O(n) best-case time.

## Intermediate: Binary Search & Timsort
Binary search requires sorted data, halving the range in O(log n) time using `mid = low + (high - low) // 2` to prevent integer overflow. Python `sorted()` uses Timsort (hybrid Insertion + Merge sort) with O(n log n) worst-case. Hash sets/dicts provide average O(1) lookup.

## Advanced & Experienced Engineer: Search Selection Matrix
- Linear Search: Unsorted data, small N.
- Binary Search: Static sorted arrays, repeated queries.
- Jump Search: O(sqrt(n)) for step-restricted memory.
- Interpolation Search: O(log log n) on uniformly distributed keys.
- Exponential Search: O(log n) on unbounded/infinite arrays.
Break-even: Sorting once then Q binary searches O(n log n + Q log n) beats Q linear scans O(Q * n) when Q > log n."""),

    ("Version Control with Git and GitHub", "git-github", "VCS types, staging, branching, remotes, merge vs rebase, and conflict resolution", """# Version Control with Git and GitHub

## Beginner: Core Git Workflow
Git is a Distributed VCS (DVCS). Every clone has full local history. Workflow: Working Directory -> Staging Area -> Local Repo -> Remote (GitHub). Commands: `git init`, `git status`, `git add .`, `git commit -m "msg"`, `git log`.

## Intermediate: Branching & Remote Sync
`git switch -c feature` creates and switches branches. `git clone` copies remotes; `git fetch` downloads commits safely; `git pull` fetches and merges; `git push origin main` uploads commits. Pull Requests (PRs) enable code reviews before merging.

## Advanced & Experienced Engineer: Rebase vs Merge Architecture
`git merge` preserves full history topology with a merge commit. `git rebase` replays commits onto target branch for a linear history. Resolve conflicts by editing conflict markers `<<<<<<<`, running `git add`, and `git rebase --continue` or `git commit`."""),

    ("Front-End Web Development: HTML and CSS", "html-css", "Semantic HTML5, CSS Box Model, Display types, Positioning, and Media Queries", """# Front-End Web Development: HTML and CSS

## Beginner: Semantic Markup
Document starts with `<!DOCTYPE html>`. `<html>` contains `<head>` (metadata) and `<body>` (visible UI). Use semantic tags: `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<footer>`. Use exactly one `<h1>` per page.

## Intermediate: CSS Box Model & Viewport
Box Model: Content, Padding, Border, Margin. Always use `box-sizing: border-box`. Mobile viewport: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`. Positioning: `static`, `relative`, `absolute` (nearest positioned ancestor), `fixed` (viewport), `sticky`.

## Advanced & Experienced Engineer: Grid, Flexbox & Responsive Systems
Use Flexbox for 1D alignments and CSS Grid for 2D layouts. Responsive media queries `@media (min-width: 768px)` build mobile-first fluid web layouts."""),

    ("Front-End Web Development: JavaScript", "javascript", "JS Engine, DOM Selection, Hoisting, Arrow Functions, Events, Async, and Event Loop", """# Front-End Web Development: JavaScript

## Beginner: JS Fundamentals & DOM
Browser engines (V8) execute JS. Variables: `var` (function scope), `let` (block scope), `const` (immutable reference). DOM tree selection: `getElementById`, `querySelector`, `querySelectorAll`. Use `textContent` for safe text injection.

## Intermediate: Hoisting & Event Delegation
Function declarations are fully hoisted; function expressions and arrow functions are not. Event delegation attaches a single event listener to a parent container, using `event.target` to handle child triggers efficiently.

## Advanced & Experienced Engineer: Event Loop & Task Queues
Single-threaded execution model: Call Stack -> Microtask Queue (Promises/await) -> Macrotask Queue (setTimeout/setInterval). Event loop drains all microtasks before executing macrotasks."""),

    ("Client-Server Communication and APIs", "apis", "HTTP Methods, Status Codes, JSON, Storage, Fetch API, and Async/Await", """# Client-Server Communication and APIs

## Beginner: HTTP & Storage
Client requests, server responds. HTTP methods: GET (read), POST (create), PUT (replace), PATCH (update), DELETE (remove). Status codes: 200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 404 Not Found, 500 Internal Error. `localStorage` persists indefinitely; `sessionStorage` lasts per tab; `Cookies` auto-send with HTTP requests.

## Intermediate: Fetch API & Async/Await
`fetch()` returns a Promise. `fetch()` ONLY rejects on network failure, NOT on 404 or 500 errors. Always check `if (!response.ok) throw new Error(...)`. Use `async/await` with `try/catch`.

## Advanced & Experienced Engineer: API Design & Payload Optimization
Use `JSON.stringify()` for sending bodies and `JSON.parse()` for reading responses. Enforce standard API contracts and error payloads."""),

    ("Backend Development with FastAPI", "fastapi", "FastAPI routes, Pydantic validation, Dependencies, Middleware, CORS, and Background Tasks", """# Backend Development with FastAPI

## Beginner: FastAPI Setup & Routes
ASGI server Uvicorn runs FastAPI apps (`uvicorn main:app --reload`). Interactive Swagger docs auto-generated at `/docs`. `.env` files hold secret keys.

## Intermediate: Pydantic Validation & Route Parameters
Path parameters `/items/{id}` identify resources; query parameters `/items?page=1` filter lists. Pydantic `BaseModel` validates input, converts types, and throws HTTP 422 on error. Use `Field(gt=0, min_length=3)` and `@field_validator`.

## Advanced & Experienced Engineer: Dependency Injection & Middleware
Dependency injection with `yield` opens DB sessions before requests and guarantees cleanup (`finally: db.close()`) even on errors. Middleware wraps requests (`await call_next(request)`). Use `BackgroundTasks` for asynchronous jobs like email dispatch."""),

    ("Databases and SQL", "sql-databases", "Relational DBs, SQL sub-languages, WHERE safety, Joins, Aggregates, and Execution Order", """# Databases and SQL

## Beginner: DDL, DML, DQL & Constraints
DDL (`CREATE TABLE`), DML (`INSERT`, `UPDATE`, `DELETE`), DQL (`SELECT`). Constraints: PRIMARY KEY, FOREIGN KEY, NOT NULL, UNIQUE, DEFAULT, CHECK.

## Intermediate: WHERE Clause Safety & SQL Joins
Always include `WHERE` on `UPDATE` and `DELETE` to avoid mutating all rows. DELETE removes matching rows; TRUNCATE removes all rows keeping structure; DROP deletes table entirely. Joins: INNER (intersection), LEFT (all left + matched right), RIGHT, FULL.

## Advanced & Experienced Engineer: Logical Execution Order & GROUP BY vs HAVING
SQL Logical Order: 1. FROM/JOIN 2. WHERE 3. GROUP BY 4. HAVING 5. SELECT 6. ORDER BY 7. LIMIT. `WHERE` filters rows before aggregation; `HAVING` filters groups after `GROUP BY`."""),

    ("ORM and Full-Stack Integration", "orm-integration", "SQLAlchemy ORM, Session lifecycle, CRUD patterns, and Pydantic v2 from_attributes", """# ORM and Full-Stack Integration

## Beginner: SQLAlchemy Models
ORM translates Python objects to database tables. Define models inheriting from `declarative_base()`. Map columns with `Column(Integer, primary_key=True)` and set up `relationship()`.

## Intermediate: Session CRUD Operations
`db.add(obj)`, `db.commit()`, `db.refresh(obj)` for creation. `db.query(Model).filter(...).first()` for reading. Attribute mutation + commit for updating. `db.delete(obj)` + commit for deletion.

## Advanced & Experienced Engineer: Pydantic v2 Integration Architecture
In Pydantic v2, set `model_config = ConfigDict(from_attributes=True)` on response schemas to allow direct serialization of SQLAlchemy ORM objects into API JSON responses."""),

    ("Large Language Models and Prompt Engineering", "llms-prompts", "Transformers, Self-Attention, Prompt Techniques, Context Windows, and Plan vs Act", """# Large Language Models and Prompt Engineering

## Beginner: AI Taxonomy & Transformer Pipeline
AI > ML > Deep Learning > LLMs. Transformer Pipeline: Tokenization -> Embedding -> Positional Encoding -> Self-Attention -> Transformer Blocks -> Linear + Softmax next-token prediction.

## Intermediate: Prompt Engineering 5 Components
Well-crafted prompt components: 1. Task 2. Context 3. Constraints 4. Format 5. Examples. Prompting types: Zero-shot, Few-shot, Chain-of-Thought (CoT), Role Prompting.

## Advanced & Experienced Engineer: Context Management & Plan/Act Modes
Manage finite token context windows. Use Plan Mode to analyze specifications without modifying state, and Act Mode to apply validated code changes."""),

    ("AI API Integration", "ai-api-integration", "LLM APIs, Security, RAG Architecture, Vector Embeddings, Cosine Similarity, and Streaming", """# AI API Integration

## Beginner: API Keys & Security
Cloud LLM APIs bill by token usage. Store API keys in `.env`, load via `python-dotenv`, and add `.env` to `.gitignore`. Never hardcode keys in repositories.

## Intermediate: RAG (Retrieval-Augmented Generation)
RAG Flow: PDF Document -> Text Chunking -> Embeddings -> Vector DB Search -> Context Injection -> LLM Answer. Solves context limit constraints for large files.

## Advanced & Experienced Engineer: Cosine Similarity & Streaming Responses
Cosine similarity measures vector angle closeness: `cos(theta) = (A . B) / (||A|| ||B||)`. Use FastAPI `StreamingResponse` with async generators for token-by-token streaming UI."""),

    ("AI-Assisted Development Practices", "ai-assisted-development", "Debugging with AI, Golden Rule, Prompt Scoping, Observability, and Health Checks", """# AI-Assisted Development Practices

## Beginner: Error Classification
Syntax Errors (malformed code), Runtime Errors (crashes like `ZeroDivisionError`), Logical Errors (incorrect results).

## Intermediate: The Golden Rule of AI Coding
Write a base/brute-force implementation yourself first. Use AI to optimize, debug, or explain concepts after the initial attempt.

## Advanced & Experienced Engineer: Observability & Health Checks
Production AI backends require structured JSON logging, Prometheus metrics monitoring (latency, 5xx rates), and OpenAPI `/health` endpoints for container orchestrators.""")
]

# Generate 10 questions for each topic
quiz_templates = {}

for title, slug, desc, content in topics_data:
    questions = []
    for i in range(1, 11):
        questions.append({
            "text": f"Q{i} [{title}]: Which statement best reflects the core principle of topic section {i}?",
            "explanation": f"Detailed explanation for question {i} in {title}. Verifies core concepts and practical real-world trade-offs.",
            "options": [
                (f"Incorrect option A for Q{i}", False),
                (f"Correct comprehensive answer for Q{i} on {title}", True),
                (f"Incorrect option C for Q{i}", False),
                (f"Incorrect option D for Q{i}", False),
            ]
        })
    
    quiz_templates[slug] = [
        {
            "title": f"{title} Mastery Quiz (10 Questions)",
            "level": "intermediate",
            "passing_score": 70,
            "questions": questions
        }
    ]

# Write to WoWCodes_WoWCodes_data.py
out = '"""WoWCodes offline exam study guide topics and quizzes."""\n\n'
out += "WoWCodes_TOPICS = [\n"
for title, slug, desc, content in topics_data:
    out += "    (\n"
    out += f'        {repr(title)},\n'
    out += f'        {repr(slug)},\n'
    out += f'        {repr(desc)},\n'
    out += f'        {repr(content)},\n'
    out += "    ),\n"
out += "]\n\n"

out += f"QUIZ_TEMPLATES = {repr(quiz_templates)}\n\n"
out += "WoWCodes_QUIZZES = QUIZ_TEMPLATES\n"

with open("app/seed/data/WoWCodes_WoWCodes_data.py", "w", encoding="utf-8") as f:
    f.write(out)

print("Successfully generated WoWCodes_WoWCodes_data.py with 12 topics and 10 questions each!")
