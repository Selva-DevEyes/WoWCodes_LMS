"""Express.js course topics and quizzes seed data."""

EXPRESS_TOPICS = [
    ("Creating a server", "creating-a-server", "Setting up Express server with app.listen and HTTP handlers", """# Creating an Express.js Server

Express is a fast, unopinionated, minimalist web framework for Node.js.

## Server Setup

```javascript
const express = require('express');
const app = express();
const PORT = process.env.PORT || 5000;

// Basic route handler
app.get('/', (req, res) => {
  res.send('Welcome to Express.js API Server!');
});

// Start listening for HTTP requests
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
```

## Key Components

- `express()`: Function that initializes an Express application instance.
- `app.listen()`: Binds and listens for connections on the specified port.
- Route methods (`app.get`, `app.post`): Match incoming HTTP requests.
"""),

    ("Routing", "routing", "HTTP methods, route parameters, query strings, and express.Router", """# Express Routing

Routing defines how an application responds to a client request to a particular endpoint (URI and HTTP method).

## Route Methods & Parameters

```javascript
// Dynamic route parameters (req.params)
app.get('/users/:userId/posts/:postId', (req, res) => {
  const { userId, postId } = req.params;
  res.send(`User: ${userId}, Post: ${postId}`);
});

// Query parameters (req.query: /search?term=react&page=2)
app.get('/search', (req, res) => {
  const { term, page } = req.query;
  res.json({ term, page });
});
```

## Modular Routers with express.Router()

Organize endpoints into dedicated route modules:

```javascript
// routes/userRoutes.js
const express = require('express');
const router = express.Router();

router.get('/', (req, res) => res.send('All Users'));
router.get('/:id', (req, res) => res.send(`User ${req.params.id}`));

module.exports = router;

// server.js
const userRoutes = require('./routes/userRoutes');
app.use('/api/v1/users', userRoutes);
```
"""),

    ("Request and response objects", "request-response", "req.body, req.params, res.json, status codes, and headers", """# Request and Response Objects

Express wraps Node.js native HTTP request and response objects with powerful utility methods.

## Request (`req`) Properties

- `req.params`: Object containing parameters mapped from URL path variables.
- `req.query`: Object containing parsed query string key-value pairs.
- `req.body`: Object containing key-value pairs submitted in the request body (requires body-parser middleware).
- `req.headers`: Headers sent by the client.

## Response (`res`) Methods

```javascript
app.post('/api/items', (req, res) => {
  // Set HTTP status code 201 Created and return JSON
  res.status(201).json({
    success: true,
    data: req.body
  });
});

// Other common response methods:
// res.send('Text or HTML')
// res.sendFile('/path/to/file.pdf')
// res.redirect('/login')
```
"""),

    ("Middleware", "middleware", "Execution order, next(), built-in middleware, and custom loggers", """# Express Middleware

Middleware functions are functions that have access to the request object (`req`), the response object (`res`), and the `next` function in the application's request-response cycle.

## How Middleware Works

```javascript
// Custom Logger Middleware
const logger = (req, res, next) => {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
  next(); // Pass control to the next middleware in the pipeline!
};

// Register globally
app.use(logger);

// Built-in body parsing middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
```

## Critical Rule

If a middleware function does NOT end the request-response cycle (e.g. by sending `res.json()`), it MUST call `next()` to pass execution to the next handler; otherwise the request hangs!
"""),

    ("Error middleware", "error-middleware", "4-parameter error signature, next(err), and global error handlers", """# Error Handling Middleware in Express

Error-handling middleware functions are defined with **FOUR parameters**: `(err, req, res, next)`.

## Defining Error Handlers

```javascript
// Triggering error in a route
app.get('/broken', (req, res, next) => {
  const error = new Error('Database connection failed');
  error.statusCode = 500;
  next(error); // Pass error to global error handler
});

// Centralized Error Handling Middleware (must be registered LAST)
app.use((err, req, res, next) => {
  const statusCode = err.statusCode || 500;
  res.status(statusCode).json({
    status: 'error',
    message: err.message || 'Internal Server Error',
    stack: process.env.NODE_ENV === 'development' ? err.stack : undefined
  });
});
```
"""),

    ("Static files", "static-files", "express.static, path.join, and virtual path prefixes", """# Serving Static Files in Express

Express provides the built-in `express.static` middleware to serve static assets like images, CSS, JavaScript, and HTML.

## Basic Usage

```javascript
const path = require('path');

// Serve files directly from 'public' directory
app.use(express.static(path.join(__dirname, 'public')));
```

With the code above, files inside `public/` are accessible via URL:
- `public/images/logo.png` -> `http://localhost:5000/images/logo.png`

## Virtual Path Prefix

```javascript
// Prefix static asset URLs with '/static'
app.use('/static', express.static(path.join(__dirname, 'public')));
// Accessible via http://localhost:5000/static/images/logo.png
```
"""),

    ("REST API", "rest-api", "REST design principles, HTTP verbs, and standard response formats", """# Building RESTful APIs with Express

REST (Representational State Transfer) is an architectural style for designing networked applications using HTTP protocols.

## Core REST Principles

1. **Statelessness**: Every request contains all necessary credentials and data.
2. **Resource-Based URIs**: Use nouns, not verbs (e.g. `/api/v1/users` instead of `/getUsers`).
3. **Standard HTTP Verbs**:
   - `GET`: Retrieve resource(s).
   - `POST`: Create a new resource.
   - `PUT`: Replace an existing resource completely.
   - `PATCH`: Partially update an existing resource.
   - `DELETE`: Remove a resource.

## Standard JSON Response Format

```json
{
  "success": true,
  "data": { "id": 1, "name": "John" },
  "message": "Resource created successfully"
}
```
"""),

    ("CRUD operations", "crud-operations", "Implementing Full Create, Read, Update, Delete routes", """# Implementing CRUD Operations in Express

A complete example of building a CRUD API for a `courses` resource:

```javascript
const express = require('express');
const app = express();
app.use(express.json());

let courses = [
  { id: 1, title: 'JavaScript Basics', level: 'Beginner' }
];

// READ All
app.get('/api/courses', (req, res) => {
  res.json(courses);
});

// READ Single
app.get('/api/courses/:id', (req, res) => {
  const course = courses.find(c => c.id === parseInt(req.params.id));
  if (!course) return res.status(404).json({ message: 'Course not found' });
  res.json(course);
});

// CREATE
app.post('/api/courses', (req, res) => {
  const newCourse = { id: courses.length + 1, ...req.body };
  courses.push(newCourse);
  res.status(201).json(newCourse);
});

// UPDATE (PATCH)
app.patch('/api/courses/:id', (req, res) => {
  const course = courses.find(c => c.id === parseInt(req.params.id));
  if (!course) return res.status(404).json({ message: 'Course not found' });
  Object.assign(course, req.body);
  res.json(course);
});

// DELETE
app.delete('/api/courses/:id', (req, res) => {
  courses = courses.filter(c => c.id !== parseInt(req.params.id));
  res.status(204).send();
});
```
"""),

    ("MVC pattern", "mvc-pattern", "Model-View-Controller architecture in Express projects", """# Model-View-Controller (MVC) Pattern

The MVC pattern separates application logic into three interconnected components.

## Directory Structure

```
project/
├── controllers/
│   └── courseController.js
├── models/
│   └── courseModel.js
├── routes/
│   └── courseRoutes.js
└── server.js
```

## Controller Example (`controllers/courseController.js`)

```javascript
const Course = require('../models/courseModel');

exports.getAllCourses = async (req, res, next) => {
  try {
    const courses = await Course.find();
    res.json({ success: true, data: courses });
  } catch (err) {
    next(err);
  }
};
```

## Routes Example (`routes/courseRoutes.js`)

```javascript
const express = require('express');
const router = express.Router();
const courseController = require('../controllers/courseController');

router.get('/', courseController.getAllCourses);

module.exports = router;
```
""")
]

EXPRESS_QUIZZES = {
    "express-creating-a-server": [
        {
            "level": "easy",
            "title": "Creating an Express Server Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which function initializes an Express application instance?",
                    "explanation": "const app = express() creates the Express application object.",
                    "options": [("express.createServer()", False), ("express()", True), ("new Express()", False), ("express.init()", False)],
                },
            ],
        }
    ],
    "express-routing": [
        {
            "level": "medium",
            "title": "Express Routing Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "How do you access path variables defined like '/users/:userId'?",
                    "explanation": "Route parameters are accessible via req.params object (req.params.userId).",
                    "options": [("req.query.userId", False), ("req.params.userId", True), ("req.body.userId", False), ("req.headers.userId", False)],
                },
                {
                    "text": "Which Express class is used to create modular, mountable route handlers?",
                    "explanation": "express.Router() creates isolated sub-routers for modular endpoint organization.",
                    "options": [("express.Route()", False), ("express.Router()", True), ("express.Module()", False), ("express.Path()", False)],
                },
            ],
        }
    ],
    "express-request-response": [
        {
            "level": "easy",
            "title": "Request and Response Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which res method sets the HTTP status code and sends a JSON payload?",
                    "explanation": "res.status(code).json(payload) sets status and formats response as JSON.",
                    "options": [("res.sendJSON()", False), ("res.status(code).json(payload)", True), ("res.output()", False), ("res.body()", False)],
                },
            ],
        }
    ],
    "express-middleware": [
        {
            "level": "medium",
            "title": "Middleware Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What must a custom middleware function call to pass control to the next handler?",
                    "explanation": "Calling next() passes execution to the next middleware in the stack.",
                    "options": [("res.continue()", False), ("next()", True), ("app.next()", False), ("return true", False)],
                },
                {
                    "text": "Which built-in middleware parses incoming JSON request bodies?",
                    "explanation": "express.json() parses incoming requests with JSON payloads.",
                    "options": [("express.parse()", False), ("express.json()", True), ("express.bodyParser()", False), ("express.data()", False)],
                },
            ],
        }
    ],
    "express-error-middleware": [
        {
            "level": "hard",
            "title": "Error Middleware Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "How many arguments must an Express error-handling middleware function accept?",
                    "explanation": "Error middleware MUST accept exactly 4 arguments: (err, req, res, next).",
                    "options": [("2: (req, res)", False), ("3: (req, res, next)", False), ("4: (err, req, res, next)", True), ("1: (err)", False)],
                },
            ],
        }
    ],
    "express-static-files": [
        {
            "level": "easy",
            "title": "Static Files Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which built-in middleware serves static assets like images and CSS?",
                    "explanation": "express.static() serves static assets from a specified directory.",
                    "options": [("express.files()", False), ("express.static()", True), ("express.assets()", False), ("express.public()", False)],
                },
            ],
        }
    ],
    "express-rest-api": [
        {
            "level": "medium",
            "title": "REST API Design Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which HTTP status code signifies that a new resource was created successfully?",
                    "explanation": "201 Created is the standard HTTP status code for successful creation.",
                    "options": [("200 OK", False), ("201 Created", True), ("204 No Content", False), ("302 Found", False)],
                },
            ],
        }
    ],
    "express-crud-operations": [
        {
            "level": "medium",
            "title": "CRUD Operations Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What is the standard HTTP status code returned when a requested item is not found?",
                    "explanation": "404 Not Found indicates that the target resource does not exist.",
                    "options": [("400 Bad Request", False), ("404 Not Found", True), ("500 Server Error", False), ("403 Forbidden", False)],
                },
            ],
        }
    ],
    "express-mvc-pattern": [
        {
            "level": "medium",
            "title": "MVC Pattern Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "In MVC architecture, which component contains the application's business logic and handles HTTP requests?",
                    "explanation": "Controllers handle incoming HTTP requests, interact with models, and return responses.",
                    "options": [("Model", False), ("View", False), ("Controller", True), ("Router only", False)],
                },
            ],
        }
    ],
}
