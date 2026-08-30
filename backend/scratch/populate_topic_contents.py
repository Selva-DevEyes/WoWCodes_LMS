"""Populate rich technical masterclass study guide content for all 24 database topics."""
from app.database.session import SessionLocal
from app.models.topic import Topic

TOPIC_CONTENTS = {
    14: """# Module 1: HTML & Semantic Web Engineering

## 1. Semantic HTML5 & Document Architecture
Semantic HTML provides meaning to web page content rather than just defining its presentation. Using semantic tags improves SEO rankings, screen reader accessibility, and maintainability.

### Core Semantic Elements:
- `<header>`: Contains introductory content, site titles, or primary navigation links.
- `<nav>`: Wraps primary site navigation menus.
- `<main>`: Specifies the unique dominant content of the document. Only one `<main>` element should exist per page.
- `<article>`: Represents a self-contained composition (e.g., blog post, forum card, news article).
- `<section>`: Groups related thematic content with a heading.
- `<aside>`: Contains tangential content (e.g., sidebars, callout boxes).
- `<footer>`: Contains author information, copyright data, and footer navigation.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Enterprise E-Commerce Platform</title>
</head>
<body>
  <header>
    <h1>WoWCodes Portal</h1>
    <nav>
      <ul>
        <li><a href="/courses">Courses</a></li>
        <li><a href="/dashboard">Dashboard</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <article>
      <h2>Full-Stack Software Development</h2>
      <p>Master modern web architectures and production software engineering.</p>
    </article>
  </main>

  <footer>
    <p>&copy; 2026 WoWCodes LMS Inc. All rights reserved.</p>
  </footer>
</body>
</html>
```

---

## 2. Web Accessibility (a11y) & ARIA Guidelines
Accessibility ensures that websites can be navigated by individuals using assistive technology such as screen readers.

### ARIA (Accessible Rich Internet Applications) Attributes:
- `aria-label`: Provides an accessible invisible label for icon-only buttons.
- `aria-expanded`: Indicates whether a collapsible container or dropdown menu is open (`true`/`false`).
- `aria-live`: Notifies screen readers of dynamic content updates (`polite`/`assertive`).

```html
<!-- Icon-only button with accessible label -->
<button aria-label="Close dialog modal" onclick="closeModal()">
  <svg class="icon-close" viewBox="0 0 24 24"></svg>
</button>
```

---

## 3. Advanced HTML5 Forms & Input Validation
HTML5 provides built-in client-side validation using attributes such as `required`, `minlength`, `maxlength`, and `pattern`.

```html
<form action="/api/v1/auth/register" method="POST">
  <fieldset>
    <legend>User Credentials</legend>

    <label for="email">Email Address:</label>
    <input type="email" id="email" name="email" required placeholder="user@company.com">

    <label for="password">Password (Min 8 chars, 1 number):</label>
    <input 
      type="password" 
      id="password" 
      name="password" 
      required 
      pattern="^(?=.*[A-Za-z])(?=.*\\d)[A-Za-z\\d]{8,}$"
      title="Must contain at least 8 characters including 1 letter and 1 number"
    >

    <button type="submit">Create Account</button>
  </fieldset>
</form>
```
""",

    15: """# Module 1: CSS & Responsive Layout Architecture

## 1. The CSS Box Model
Every element in CSS is represented as a rectangular box comprising four distinct layers:

1. **Content**: The actual text, image, or child element.
2. **Padding**: Transparent area surrounding the content inside the border.
3. **Border**: The outline surrounding padding and content.
4. **Margin**: Transparent space outside the border separating adjacent elements.

### Critical Property: `box-sizing: border-box`
By default (`content-box`), adding padding or borders increases the total rendered width of an element. Using `border-box` forces `width` to include padding and border.

```css
/* Universal Border-Box Reset */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card {
  width: 300px;
  padding: 20px;
  border: 2px solid #6366f1;
  /* Total width remains exactly 300px because of border-box */
}
```

---

## 2. Flexible Box Layout (Flexbox) - 1D Layouts
Flexbox is designed for 1-dimensional component alignment along a main axis or cross axis.

```css
.flex-container {
  display: flex;
  flex-direction: row;          /* Main axis horizontal */
  justify-content: space-between;/* Main axis alignment */
  align-items: center;          /* Cross axis alignment */
  gap: 1.5rem;                  /* Spacing between items */
}

.flex-item {
  flex: 1 1 0%;                 /* flex-grow, flex-shrink, flex-basis */
}
```

---

## 3. CSS Grid Layout - 2D Grid Systems
CSS Grid provides precise control over 2-dimensional columns and rows simultaneously.

```css
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
}
```

---

## 4. Mobile-First Media Queries
Designing mobile-first means writing baseline styles for small screens, then layering enhancements using `@media (min-width: ...)` breakpoints.

```css
/* Mobile baseline styles */
.container {
  width: 100%;
  padding: 1rem;
}

/* Tablet & Up */
@media (min-width: 768px) {
  .container {
    max-width: 720px;
    margin: 0 auto;
  }
}

/* Desktop & Up */
@media (min-width: 1024px) {
  .container {
    max-width: 960px;
  }
}
```
""",

    16: """# Module 1: JavaScript Core Execution & V8 Architecture

## 1. V8 Engine Execution Context & Event Loop
JavaScript is a single-threaded, non-blocking asynchronous language powered by the V8 runtime engine.

### Key Components:
- **Call Stack**: Executes synchronous stack frames in Last-In, First-Out (LIFO) order.
- **Web APIs**: Handles browser background tasks (timer intervals, fetch requests, DOM events).
- **Microtask Queue**: Holds Promise callbacks (`.then()`, `await`) and `queueMicrotask()`. Microtasks execute immediately after the current call stack clears before any Macrotask.
- **Macrotask Queue**: Holds `setTimeout`, `setInterval`, and I/O callbacks.

```javascript
console.log('1: Synchronous Start');

setTimeout(() => {
  console.log('4: Macrotask Callback');
}, 0);

Promise.resolve().then(() => {
  console.log('3: Microtask Promise');
});

console.log('2: Synchronous End');

// Execution Output Order:
// 1: Synchronous Start
// 2: Synchronous End
// 3: Microtask Promise
// 4: Macrotask Callback
```

---

## 2. Closures & Lexical Scope
A closure is the combination of a function bundled together with references to its surrounding lexical state. Closures give functions access to their outer scope even after the outer function has returned.

```javascript
function createCounter(initialValue = 0) {
  let count = initialValue; // Enclosed private variable

  return {
    increment: () => ++count,
    decrement: () => --count,
    getValue: () => count,
  };
}

const counter = createCounter(10);
console.log(counter.increment()); // 11
console.log(counter.getValue());   // 11
```

---

## 3. Asynchronous Async/Await & Promise API
`async/await` syntax provides syntactic sugar over native Promises, simplifying asynchronous control flow.

```javascript
async function fetchUserData(userId) {
  try {
    const response = await fetch(`https://api.wowcodes.com/users/${userId}`);
    if (!response.ok) {
      throw new Error(`HTTP Error Status: ${response.status}`);
    }
    const user = await response.json();
    return user;
  } catch (error) {
    console.error('Failed to fetch user:', error.message);
    throw error;
  }
}
```
""",

    17: """# Module 1: React 19 Framework & Modern Component Design

## 1. Virtual DOM & Fiber Reconciliation
React uses an in-memory lightweight representation of the real DOM called the **Virtual DOM**. When component state changes:

1. React creates a new Virtual DOM tree.
2. The **Fiber reconciler** compares the new tree with the previous tree (diffing algorithm).
3. React computes the minimal set of real DOM mutations required and applies them efficiently in a batch.

---

## 2. Core React Hooks

### `useState` & `useEffect`
```jsx
import { useState, useEffect } from 'react';

function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let isMounted = true;
    async function loadData() {
      const data = await fetchUser(userId);
      if (isMounted) {
        setUser(data);
        setLoading(false);
      }
    }
    loadData();
    return () => { isMounted = false; }; // Cleanup function
  }, [userId]);

  if (loading) return <div>Loading Profile...</div>;
  return <h1 className="text-xl font-bold">{user.name}</h1>;
}
```

### Performance Hooks: `useMemo` & `useCallback`
- `useMemo`: Caches the calculated result of an expensive calculation across re-renders.
- `useCallback`: Caches a function definition between renders to prevent unnecessary child re-renders.

```jsx
const memoizedValue = useMemo(() => computeExpensiveValue(data), [data]);
const handleClick = useCallback(() => performAction(id), [id]);
```
""",

    18: """# Module 1: Redux Toolkit (RTK) Global State Management

## 1. Redux Unidirectional Data Flow
Redux enforces predictable state mutation through a strict unidirectional cycle:

1. **View**: User triggers an action (e.g., clicks "Add to Cart").
2. **Action**: An object specifying type and payload is dispatched.
3. **Reducer**: Pure function receives `(previousState, action)` and computes the new state.
4. **Store**: Global single source of truth holds application state.
5. **View Re-renders**: Subscribed components re-render with updated state.

---

## 2. Redux Toolkit `createSlice` Architecture

```javascript
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

// Async Thunk
export const fetchCourses = createAsyncThunk(
  'courses/fetchCourses',
  async (_, { rejectWithValue }) => {
    try {
      const response = await fetch('/api/v1/courses');
      return await response.json();
    } catch (err) {
      return rejectWithValue(err.message);
    }
  }
);

const coursesSlice = createSlice({
  name: 'courses',
  initialState: { items: [], status: 'idle', error: null },
  reducers: {
    clearCourses: (state) => {
      state.items = [];
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchCourses.pending, (state) => {
        state.status = 'loading';
      })
      .addCase(fetchCourses.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.items = action.payload;
      })
      .addCase(fetchCourses.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.payload;
      });
  },
});

export const { clearCourses } = coursesSlice.actions;
export default coursesSlice.reducer;
```
""",

    19: """# Module 1: Front-End JavaScript & DOM Security

## 1. Event Bubbling & Delegation
Event delegation uses event bubbling to handle events at a parent level rather than attaching listeners to individual child elements.

```javascript
const listContainer = document.querySelector('#item-list');

listContainer.addEventListener('click', (event) => {
  // Check if click target matches button
  if (event.target.matches('.delete-btn')) {
    const itemId = event.target.dataset.id;
    deleteItem(itemId);
  }
});
```

---

## 2. Cross-Site Scripting (XSS) Prevention
XSS vulnerabilities occur when untrusted user inputs are executed directly as HTML scripts in the browser.

### Prevention Best Practices:
1. Always sanitize user HTML input before insertion.
2. Avoid dangerous DOM APIs like `element.innerHTML = userInput`. Use `textContent` or `setAttribute`.
3. Set `HttpOnly` flags on sensitive authentication cookies.

```javascript
// Safe Insertion
const userBioElement = document.getElementById('user-bio');
userBioElement.textContent = userInputString; // Prevents HTML tag execution
```
""",

    20: """# Module 1: Node.js Asynchronous Server Architecture

## 1. Event Loop & Thread Pool
Node.js uses a single-threaded event loop built on Libuv for non-blocking I/O operations, utilizing a thread pool for heavy OS operations.

```javascript
const fs = require('fs');
const http = require('http');

const server = http.createServer((req, res) => {
  if (req.url === '/api/health' && req.method === 'GET') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ status: 'healthy', timestamp: new Date() }));
  }
});

server.listen(8001, () => {
  console.log('Node.js server listening on port 8001');
});
```
""",

    21: """# Module 1: Express.js REST Framework & Middleware Pipeline

## 1. Express Middleware Stack
Middleware functions access the request object (`req`), response object (`res`), and next middleware callback (`next`).

```javascript
const express = require('express');
const app = express();

// Body Parser Middleware
app.use(express.json());

// Logger Middleware
app.use((req, res, next) => {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
  next();
});

// REST Endpoint Handler
app.post('/api/v1/courses', (req, res) => {
  const { title, slug } = req.body;
  if (!title) {
    return res.status(400).json({ error: 'Title field is required' });
  }
  res.status(201).json({ id: 101, title, slug });
});

// Centralized Error Handling Middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Internal Server Exception' });
});
```
""",

    22: """# Module 2: Python Fundamentals & Memory Reference Model

## 1. Mutable vs Immutable Objects
In Python, integers, floats, strings, tuples, and frozensets are **immutable**. Lists, dictionaries, and sets are **mutable**.

```python
# Immutable String Mutation creates a new object ID
s1 = "hello"
print(id(s1))
s1 += " world"
print(id(s1))  # Different memory address

# Mutable List Mutation retains the same object ID
lst = [1, 2, 3]
print(id(lst))
lst.append(4)
print(id(lst))  # Same memory address
```

---

## 2. List & Dictionary Comprehensions
Comprehensions provide concise syntax for filtering and transforming iterables.

```python
# List Comprehension with filtering
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x**2 for x in numbers if x % 2 == 0]
# Output: [4, 16, 36, 64, 100]

# Dict Comprehension
users = [("u1", "Alice"), ("u2", "Bob")]
user_dict = {user_id: name for user_id, name in users}
```
""",

    23: """# Module 2: Python Core Operators, Generators & Decorators

## 1. Bitwise Binary Operators
Bitwise operators act directly on the binary representation of integers.

- Left Shift (`x << n`): Shifts bits left, multiplying $x$ by $2^n$.
- Right Shift (`x >> n`): Shifts bits right, dividing $x$ by $2^n$.

```python
x = 5  # Binary: 0101
print(x << 1)  # Output: 10 (Binary: 1010)
print(x >> 1)  # Output: 2  (Binary: 0010)
```

---

## 2. Generators & Lazy Evaluation
Generators return an iterator using the `yield` keyword, yielding items one at a time to preserve system memory.

```python
def stream_large_dataset(limit):
    num = 0
    while num < limit:
        yield f"Record_{num}"
        num += 1

gen = stream_large_dataset(1000000)
print(next(gen))  # Record_0
print(next(gen))  # Record_1
```
""",

    24: """# Module 2: Data Structures & Algorithmic Problem Solving

## 1. Big O Time & Space Complexity
Algorithmic efficiency is classified by worst-case growth rates:

- $O(1)$: Constant time (Dictionary key lookup, Array index access).
- $O(\log n)$: Logarithmic time (Binary Search).
- $O(n)$: Linear time (Unsorted Linear Search).
- $O(n \log n)$: Linearithmic time (Timsort, Merge Sort).
- $O(n^2)$: Quadratic time (Nested loop comparison).

---

## 2. Binary Search Implementation ($O(\log n)$)

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

# Requires sorted input array
sorted_list = [10, 20, 30, 40, 50, 60, 70]
print(binary_search(sorted_list, 40))  # Output: 3
```
""",

    25: """# Module 3: FastAPI Backend & Asynchronous Web Services

## 1. FastAPI Uvicorn Architecture
FastAPI is built on top of Starlette (for web routing) and Pydantic (for data validation), running asynchronously over Uvicorn ASGI server.

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="WoWCodes API", version="1.0.0")

class CourseCreate(BaseModel):
    title: str
    slug: str
    description: str

@app.post("/api/v1/courses", status_code=status.HTTP_201_CREATED)
async def create_course(course: CourseCreate):
    if not course.title:
        raise HTTPException(status_code=400, detail="Title cannot be empty")
    return {"message": "Course created", "course": course}
```
""",

    26: """# Module 3: SQL Database Querying & Joins

## 1. SQL Logical Execution Order
Queries are evaluated in a specific sequence:
1. `FROM` & `JOIN`: Source tables compiled.
2. `WHERE`: Filters individual rows.
3. `GROUP BY`: Aggregates rows into groups.
4. `HAVING`: Filters aggregated groups.
5. `SELECT`: Computes expressions & columns.
6. `ORDER BY`: Sorts output dataset.

```sql
SELECT c.category, COUNT(t.id) AS topic_count
FROM courses c
INNER JOIN topics t ON c.id = t.course_id
WHERE c.is_published = 1
GROUP BY c.category
HAVING COUNT(t.id) >= 3
ORDER BY topic_count DESC;
```
""",

    27: """# Module 3: FastAPI Advanced Architecture & Dependency Injection

## 1. Dependency Injection with `Depends()`

```python
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.user import User

app = FastAPI()

def get_current_user(db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == 1).first()
    return user

@app.get("/api/v1/users/me")
def read_current_user(current_user: User = Depends(get_current_user)):
    return {"id": current_user.id, "email": current_user.email}
```
""",

    28: """# Module 3: Client-Server APIs & HTTP Specifications

## 1. HTTP Verbs & Status Code Matrix
- `200 OK`: Successful retrieval or execution.
- `201 Created`: Resource successfully created.
- `400 Bad Request`: Invalid client request format.
- `401 Unauthorized`: Missing or invalid authentication token.
- `403 Forbidden`: Authenticated user lacks permission.
- `404 Not Found`: Target resource does not exist.
- `422 Unprocessable Entity`: Schema validation failed (Pydantic).
- `500 Internal Server Error`: Unhandled server exception.

```javascript
async function submitProject(payload) {
  const response = await fetch('/api/v1/projects/submit', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Failed to submit project');
  }

  return await response.json();
}
```
""",

    29: """# Module 4: Git & GitHub Enterprise Workflows

## 1. Distributed Version Control Architecture
Git tracks snapshot history using objects:
- **Blob**: File contents.
- **Tree**: Directories and filenames.
- **Commit**: Snapshot pointer with metadata and parent references.

```bash
# Branch setup and tracking
git checkout -b feature/auth-flow
git add .
git commit -m "feat(auth): add JWT token refresh endpoint"
git push -u origin feature/auth-flow
```
""",

    30: """# Module 4: Version Control Systems & Merge Conflicts

## 1. Merge Conflict Resolution
Merge conflicts occur when changes are made to the same lines of a file across different branches.

```git
<<<<<<< HEAD
const API_URL = "http://localhost:8001/api/v1";
=======
const API_URL = "https://api.wowcodes.com/v1";
>>>>>>> feature/production-config
```

### Resolution Steps:
1. Identify conflicting files using `git status`.
2. Open files and select desired code blocks.
3. Remove conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
4. Stage resolved files with `git add <file>` and run `git commit`.
""",

    31: """# Module 5: Databases & SQL Performance Engineering

## 1. Table Lifecycle Commands: DELETE vs TRUNCATE vs DROP
- `DELETE`: DML operation. Removes rows one by one. Slow, allows `WHERE` clause, triggers logging.
- `TRUNCATE`: DDL operation. Deallocates data pages instantly. Extremely fast, resets auto-increment counter.
- `DROP`: DDL operation. Removes both table data and schema definition completely from database catalog.

```sql
-- DML Row Deletion
DELETE FROM audit_logs WHERE created_at < '2026-01-01';

-- DDL Page Deallocation
TRUNCATE TABLE temp_analytics_buffer;

-- DDL Schema Removal
DROP TABLE legacy_user_imports;
```
""",

    32: """# Module 5: Relational & NoSQL Database Systems

## 1. Database Normalization Forms
- **1NF**: Atomic values (no repeating groups/arrays in columns).
- **2NF**: In 1NF and no partial dependencies (non-key attributes depend on the full primary key).
- **3NF**: In 2NF and no transitive dependencies (non-key attributes depend only on the primary key).

---

## 2. Polyglot Persistence Architecture
Modern applications use specialized databases for targeted workloads:
- **PostgreSQL**: Transactional user accounts and financial records (ACID).
- **MongoDB**: Flexible JSON document catalog (Flexible Schema).
- **Redis**: In-memory caching and session state (Sub-millisecond latency).
""",

    33: """# Module 5: ORM & Full-Stack Integration

## 1. SQLAlchemy ORM Model Mapping

```python
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.session import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    slug = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # One-to-Many Relationship
    topics = relationship("Topic", back_populates="course", cascade="all, delete-orphan")
```
""",

    34: """# Module 6: Large Language Models & Prompt Engineering

## 1. Transformer Neural Architecture
Transformers process sequential textual data using parallel self-attention.

### 6-Step Transformer Execution Pipeline:
1. **Tokenization**: Splitting text into sub-word tokens (e.g. `BPE`, `WordPiece`).
2. **Token Embedding**: Mapping token IDs to dense high-dimensional vectors.
3. **Positional Encoding**: Adding positional math vectors to represent word order.
4. **Self-Attention**: Computing attention weights $\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$.
5. **Feed-Forward Layers**: Transforming representations through non-linear layers.
6. **Softmax Output**: Computing output probability distribution across vocabulary.

---

## 2. The 5 Core Prompt Engineering Components
A production-grade prompt consists of:
1. **Role/Persona**: Defines system identity (e.g. "You are an expert Senior Python Architect").
2. **Context**: Background details and domain constraints.
3. **Instruction**: Clear actionable task command.
4. **Input Data**: The target text, snippet, or query to process.
5. **Output Format**: Expected response format (e.g., JSON schema, Markdown table).
""",

    35: """# Module 6: AI API & RAG Architecture Integration

## 1. Retrieval-Augmented Generation (RAG) Architecture
RAG connects Large Language Models to custom private data sources.

### RAG Pipeline Flow:
1. **Document Processing**: Ingestion of PDFs, Markdown, or Database records.
2. **Chunking**: Dividing text into semantic chunks (e.g. 500 tokens with 50-token overlap).
3. **Vector Embedding**: Converting text chunks into vector embeddings via models.
4. **Vector Storage**: Storing vectors in databases (Chroma, PGVector, Pinecone).
5. **Cosine Similarity Search**: Finding top $K$ relevant chunks matching a user query:
$$\\cos(\\theta) = \\frac{\\mathbf{A} \\cdot \\mathbf{B}}{\\|\\mathbf{A}\\| \\|\\mathbf{B}\\|}$$
6. **Context Injection**: Augmenting the LLM prompt with retrieved chunks.
""",

    36: """# Module 6: AI-Assisted Engineering & Observability

## 1. Error Taxonomy & AI Debugging
Software engineering errors fall into three core categories:
- **Syntax Errors**: Invalid language grammar caught by parser/compiler.
- **Runtime Exceptions**: Execution failures occurring at runtime (e.g. `AttributeError`, `ZeroDivisionError`).
- **Logical/Algorithmic Errors**: Code runs cleanly but produces incorrect business results.

---

## 2. The Golden Rule of AI Engineering
*NEVER diagnose a runtime error or test failure without reading un-truncated authority logs first. Base all code fixes strictly on empirical log tracebacks.*

---

## 3. Production Health Monitoring
Every production service must expose health endpoints:

```python
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "WoWCodes Backend", "db": "connected"}
```
""",

    37: """# Certificate of Software Development Engineering - Final Capstone Exam

## 1. Examination Structure
The Final Evaluation Examination tests your engineering capabilities across all 6 core modules:
- **Total Marks**: 100 Marks
- **Total Questions**: 50 High-Stakes Employer Technical Questions (2 Marks per question)
- **Passing Threshold**: 70% Score Required for Certification Eligibility

---

## 2. Practical Capstone Project Guidelines
To complete your certification, submit your capstone project details in the form above:
- **Project Title**: Name of your full-stack application.
- **GitHub Repository URL**: Link to your public GitHub code repository.
- **Live Demo URL**: Deployed application link (Vercel, Render, AWS, Netlify).
- **Architecture Notes**: Summary of backend frameworks, database schemas, and AI integrations.

---

## 3. Automated Certificate Issuance
Upon achieving $\\ge 70\\%$ on the exam and submitting your project details, your verified **Software Development Engineering Certificate** (`SDE-AI-CERT-XXXXX`) will be issued instantly!
"""
}

def seed_contents():
    db = SessionLocal()
    try:
        updated_count = 0
        for topic_id, content_markdown in TOPIC_CONTENTS.items():
            topic = db.query(Topic).filter(Topic.id == topic_id).first()
            if topic:
                topic.content = content_markdown.strip()
                updated_count += 1
        db.commit()
        print(f"Successfully populated rich technical study content for {updated_count} topics!")
    except Exception as e:
        db.rollback()
        print(f"Error seeding topic contents: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_contents()
