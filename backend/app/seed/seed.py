"""Seed initial data: roles, admin user, courses, topics, lessons, quizzes."""
import os
from datetime import datetime

import httpx
from sqlalchemy.orm import Session

from app.database.session import SessionLocal, init_db
from app.models.role import Role
from app.models.user import User
from app.models.course import Course
from app.models.topic import Topic
from app.models.lesson import Lesson
from app.models.quiz import Quiz
from app.models.question import Question
from app.models.option import Option
from app.security.passwordHashing import hash_password


from app.seed.data.js_data import JS_TOPICS, JS_QUIZZES
from app.seed.data.nodejs_data import NODEJS_TOPICS, NODEJS_QUIZZES
from app.seed.data.express_data import EXPRESS_TOPICS, EXPRESS_QUIZZES
from app.seed.data.database_data import DATABASE_TOPICS, DATABASE_QUIZZES
from app.seed.data.redux_data import REDUX_TOPICS, REDUX_QUIZZES
from app.seed.data.git_ai_data import GIT_AI_TOPICS, GIT_AI_QUIZZES
from app.seed.data.WoWCodes_curriculum_data import WoWCodes_TOPICS as WoWCodes_TOPICS, WoWCodes_QUIZZES as WoWCodes_QUIZZES


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
GOOGLE_GENERATIVE_AI_ENDPOINT = (
    "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
)


def _clean_generated_markdown(text: str) -> str:
    """Normalize markdown returned by the Gemini API."""
    text = (text or "").strip()
    if text.startswith("```markdown"):
        text = text[len("```markdown"):]
    if text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    return text.strip()


def generate_topic_content(title: str, slug: str, description: str, api_key: str | None = None, fallback_content: str | None = None) -> str:
    """Generate topic lesson content using the Google Gemini API."""
    effective_key = api_key or GOOGLE_API_KEY
    prompt = (
        f"Create a detailed Markdown lesson for a learning platform about '{title}'.\n"
        f"Topic slug: {slug}\n"
        f"Short description: {description}\n"
        "Requirements:\n"
        "- Return only markdown content.\n"
        "- Include a clear title, learning objectives, explanation, one or two code examples, key takeaways, and a short practice section.\n"
        "- Keep it concise but educational and suitable for beginners."
    )

    payload = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.3,
            "maxOutputTokens": 1400,
        },
    }

    try:
        response = httpx.post(
            f"{GOOGLE_GENERATIVE_AI_ENDPOINT}?key={effective_key}",
            json=payload,
            timeout=30.0,
        )
        response.raise_for_status()
        result = response.json()
        candidates = result.get("candidates") or []
        if candidates:
            parts = candidates[0].get("content", {}).get("parts", [])
            if parts:
                text = parts[0].get("text", "")
                if text:
                    return _clean_generated_markdown(text)
    except Exception as exc:
        print(f"Google content generation failed for {title}: {exc}")

    return fallback_content or f"# {title}\n\n{description}\n\n## Overview\n\nThis topic introduces {title}."


# Course definitions: (title, slug, description, category, level, icon, color)
COURSES = [
    ("HTML", "html", "Learn the foundation of web development with HTML.", "Frontend", "beginner", "🌐", "bg-blue-100 text-blue-600"),
    ("CSS", "css", "Style your web pages with modern CSS.", "Frontend", "beginner", "🎨", "bg-purple-100 text-purple-600"),
    ("JavaScript", "javascript", "Master the language of the web - JavaScript from basics to advanced.", "Frontend", "intermediate", "⚡", "bg-yellow-100 text-yellow-600"),
    ("React", "react", "Build modern user interfaces with React 19.", "Frontend", "intermediate", "⚛️", "bg-cyan-100 text-cyan-600"),
    ("Redux", "redux", "Manage application state with Redux Toolkit.", "Frontend", "intermediate", "🔄", "bg-violet-100 text-violet-600"),
    ("Python", "python", "Learn Python programming from zero to hero.", "Backend", "beginner", "🐍", "bg-green-100 text-green-600"),
    ("FastAPI", "fastapi", "Build production-ready APIs with FastAPI.", "Backend", "intermediate", "🚀", "bg-teal-100 text-teal-600"),
    ("Node.js Basics", "nodejs", "Master asynchronous server-side JavaScript runtime.", "Backend", "intermediate", "🟢", "bg-emerald-100 text-emerald-600"),
    ("Express.js", "express", "Build fast, flexible web applications and REST APIs.", "Backend", "intermediate", "🚂", "bg-stone-100 text-stone-600"),
    ("Database", "database", "Relational, NoSQL databases, SQL basics, and ORMs.", "Database", "intermediate", "🗄️", "bg-orange-100 text-orange-600"),
    ("SQL", "sql", "Master databases and SQL queries.", "Database", "intermediate", "🗄️", "bg-orange-100 text-orange-600"),
    ("Git & GitHub", "git-github", "Version control and collaboration with Git.", "Tools", "beginner", "🔀", "bg-red-100 text-red-600"),
    ("AI & ML", "ai-ml", "Artificial Intelligence and Machine Learning fundamentals.", "AI", "advanced", "🤖", "bg-indigo-100 text-indigo-600"),
    ("Certificate of Software Development Engineering Program", "WoWCodes", "Comprehensive evaluation study guide covering software development engineering and applied AI.", "Certification", "advanced", "🎓", "bg-indigo-100 text-indigo-600"),
]

# Topics per course: [(title, slug, description, content)]
COURSE_TOPICS = {
    "html": [
        ("Introduction to HTML", "introduction", "What is HTML and basic structure", """# Introduction to HTML

HTML (HyperText Markup Language) is the standard markup language for creating web pages.

## What is HTML?

- HTML describes the structure of a web page
- HTML elements tell the browser how to display content
- HTML consists of a series of elements

## Basic Structure

```html
<!DOCTYPE html>
<html>
<head>
  <title>My Page</title>
</head>
<body>
  <h1>Hello World</h1>
</body>
</html>
```

## Key Concepts

- **Tags**: Elements are defined by tags like `<h1>` and `<p>`
- **Attributes**: Provide additional info like `class` and `id`
- **Nesting**: Elements can be nested inside each other"""),
        ("HTML Tags", "tags", "Common HTML tags and elements", """# HTML Tags

HTML tags are the building blocks of web pages.

## Common Tags

### Headings
```html
<h1>Main Heading</h1>
<h2>Sub Heading</h2>
<h3>Section Heading</h3>
```

### Text
```html
<p>Paragraph text</p>
<strong>Bold text</strong>
<em>Italic text</em>
<br> Line break
```

### Links & Images
```html
<a href="https://example.com">Link</a>
<img src="image.jpg" alt="Description">
```

### Lists
```html
<ul>
  <li>Unordered item</li>
</ul>
<ol>
  <li>Ordered item</li>
</ol>
```

## Practice Tips

- Always close your tags
- Use semantic tags when possible
- Validate your HTML regularly"""),
        ("Forms", "forms", "Building forms with HTML", """# HTML Forms

Forms allow users to input and submit data.

## Form Structure

```html
<form action="/submit" method="POST">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name">
  
  <label for="email">Email:</label>
  <input type="email" id="email" name="email">
  
  <button type="submit">Submit</button>
</form>
```

## Input Types

- `text` - Single line text
- `email` - Email address
- `password` - Masked input
- `number` - Numeric input
- `checkbox` - Multiple selection
- `radio` - Single selection
- `select` - Dropdown list
- `textarea` - Multi-line text

## Form Attributes

- `action` - Where to send data
- `method` - GET or POST
- `required` - Mandatory field
- `placeholder` - Hint text
- `pattern` - Validation pattern"""),
        ("Semantic HTML", "semantic-html", "Semantic elements for accessibility", """# Semantic HTML

Semantic HTML uses meaningful tags that describe their content.

## Semantic Elements

```html
<header>Page header</header>
<nav>Navigation links</nav>
<main>Main content</main>
<article>Self-contained content</article>
<section>Related content group</section>
<aside>Sidebar content</aside>
<footer>Page footer</footer>
```

## Benefits

- **Accessibility**: Screen readers understand the page better
- **SEO**: Search engines rank content better
- **Maintainability**: Code is easier to read and maintain

## Best Practices

- Use one `<h1>` per page
- Use `<nav>` for navigation links
- Use `<article>` for blog posts or news
- Use `<section>` to group related content"""),
        ("HTML Projects", "projects", "Build real HTML projects", """# HTML Projects

Practice your HTML skills with these projects.

## Project 1: Personal Portfolio

Create a personal portfolio page with:
- Header with your name and title
- About section
- Skills list
- Contact form

## Project 2: Blog Layout

Build a blog page with:
- Navigation bar
- Article sections
- Sidebar with categories
- Footer with links

## Project 3: Landing Page

Create a product landing page with:
- Hero section
- Features grid
- Pricing table
- Signup form

## Tips

- Start with a wireframe
- Use semantic HTML
- Validate your code
- Test on different screen sizes"""),
        ("HTML Quiz", "quiz", "Test your HTML knowledge", """# HTML Quiz

Test your knowledge of HTML fundamentals.

## Topics Covered

- Basic structure and tags
- Forms and inputs
- Semantic HTML
- Best practices

## How to Prepare

- Review the HTML introduction
- Practice creating forms
- Study semantic elements
- Build small projects"""),
    ],
    "css": [
        ("Introduction to CSS", "introduction", "What is CSS and how to use it", """# Introduction to CSS

CSS (Cascading Style Sheets) controls the visual presentation of web pages.

## What is CSS?

- CSS describes how HTML elements should be displayed
- CSS saves work by controlling multiple pages at once
- CSS can be inline, internal, or external

## Basic Syntax

```css
selector {
  property: value;
}
```

## Example

```css
h1 {
  color: blue;
  font-size: 24px;
  text-align: center;
}
```

## Ways to Add CSS

1. **External** - `<link rel="stylesheet" href="style.css">`
2. **Internal** - `<style>` in the head
3. **Inline** - `style` attribute on elements"""),
        ("Selectors", "selectors", "CSS selectors and specificity", """# CSS Selectors

Selectors target specific HTML elements to style them.

## Types of Selectors

### Element Selector
```css
p { color: red; }
```

### Class Selector
```css
.highlight { background: yellow; }
```

### ID Selector
```css
#header { font-size: 20px; }
```

### Attribute Selector
```css
input[type="text"] { border: 1px solid gray; }
```

### Pseudo-classes
```css
a:hover { color: green; }
li:first-child { font-weight: bold; }
```

## Specificity

1. Inline styles (highest)
2. IDs
3. Classes, attributes, pseudo-classes
4. Elements, pseudo-elements (lowest)"""),
        ("Box Model", "box-model", "Understanding the box model", """# CSS Box Model

Every element in CSS is a rectangular box.

## Box Model Components

```css
.box {
  width: 300px;
  padding: 20px;    /* Space inside the border */
  border: 2px solid black;
  margin: 10px;     /* Space outside the border */
}
```

## Components

- **Content**: The actual content (text, images)
- **Padding**: Space between content and border
- **Border**: Surrounds the padding
- **Margin**: Space outside the border

## Box Sizing

```css
* {
  box-sizing: border-box;  /* Width includes padding and border */
}
```

## Key Points

- Total width = content + padding + border + margin
- `box-sizing: border-box` makes sizing easier
- Margins can collapse between adjacent elements"""),
        ("Flexbox", "flexbox", "Flexible layouts with Flexbox", """# CSS Flexbox

Flexbox is a one-dimensional layout model for arranging items.

## Flex Container

```css
.container {
  display: flex;
  justify-content: center;  /* Main axis */
  align-items: center;      /* Cross axis */
  gap: 10px;
}
```

## Main Properties

### Container
- `flex-direction`: row | column
- `justify-content`: flex-start | center | space-between
- `align-items`: stretch | center | flex-start
- `flex-wrap`: nowrap | wrap

### Items
- `flex-grow`: How much to grow
- `flex-shrink`: How much to shrink
- `flex-basis`: Initial size
- `order`: Item order

## Example

```css
.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```"""),
        ("Grid", "grid", "Two-dimensional layouts with Grid", """# CSS Grid

Grid is a two-dimensional layout system for complex layouts.

## Grid Container

```css
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: auto;
  gap: 20px;
}
```

## Key Concepts

### Grid Lines
- Horizontal and vertical lines that divide the grid

### Grid Tracks
- The rows and columns between grid lines

### Grid Areas
- Named regions of the grid

## Common Patterns

```css
/* 3-column layout */
.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

/* Sidebar layout */
.layout {
  display: grid;
  grid-template-columns: 250px 1fr;
}
```

## Grid vs Flexbox

- **Grid**: 2D layouts (rows AND columns)
- **Flexbox**: 1D layouts (row OR column)"""),
        ("CSS Projects", "projects", "Build responsive pages", """# CSS Projects

Apply your CSS skills with these projects.

## Project 1: Responsive Navbar

Create a responsive navigation bar with:
- Flexbox layout
- Mobile hamburger menu
- Hover effects

## Project 2: Card Layout

Build a card grid with:
- CSS Grid for layout
- Hover animations
- Responsive breakpoints

## Project 3: Landing Page

Style a landing page with:
- Hero section with gradient
- Feature cards
- Responsive design
- Smooth animations

## Tips

- Use mobile-first approach
- Test at multiple breakpoints
- Use CSS variables for colors
- Keep animations subtle"""),
        ("CSS Quiz", "quiz", "Test your CSS knowledge", """# CSS Quiz

Test your knowledge of CSS fundamentals.

## Topics Covered

- Selectors and specificity
- Box model
- Flexbox and Grid
- Responsive design

## How to Prepare

- Review selector types
- Practice box model calculations
- Build flexbox layouts
- Create grid layouts"""),
    ],
    "javascript": [
        ("Introduction", "introduction", "JavaScript history and setup", """# Introduction to JavaScript

JavaScript is the programming language of the web.

## What is JavaScript?

- JavaScript is a high-level, interpreted language
- It runs in the browser and on servers (Node.js)
- It makes web pages interactive

## Setting Up

```html
<script>
  console.log('Hello, World!');
</script>
```

Or use an external file:
```html
<script src="app.js"></script>
```

## Basic Syntax

```javascript
// Variables
let name = 'John';
const age = 25;

// Functions
function greet() {
  console.log('Hello!');
}

// Output
console.log('Hello, World!');
```

## Where to Run

- Browser console (F12)
- Node.js
- Online editors (CodePen, JSFiddle)"""),
        ("Variables", "variables", "var, let, const and scoping", """# JavaScript Variables

Variables store data values in JavaScript.

## Declaring Variables

```javascript
// var - function scoped (avoid)
var oldWay = 'value';

// let - block scoped, can reassign
let count = 0;
count = 1;

// const - block scoped, cannot reassign
const pi = 3.14;
```

## Scoping Rules

```javascript
// Block scope
{
  let x = 10;
  const y = 20;
  // x and y accessible here
}
// x and y NOT accessible here

// Function scope
function myFunc() {
  var z = 30;
  // z accessible here
}
// z NOT accessible here
```

## Naming Conventions

- Use camelCase: `myVariable`
- Start with letter, _, or $
- Be descriptive: `userName` not `u`
- Constants in UPPER_CASE: `MAX_SIZE`

## Best Practices

- Prefer `const` by default
- Use `let` when you need to reassign
- Avoid `var` in modern code"""),
        ("Data Types", "data-types", "Primitive and reference types", """# JavaScript Data Types

JavaScript has primitive and reference data types.

## Primitive Types

```javascript
// String
let name = 'John';

// Number
let age = 25;
let price = 19.99;

// Boolean
let isActive = true;

// Undefined
let notDefined;

// Null
let empty = null;

// Symbol
let sym = Symbol('id');

// BigInt
let big = 12345678901234567890n;
```

## Reference Types

```javascript
// Object
let person = { name: 'John', age: 25 };

// Array
let fruits = ['apple', 'banana'];

// Function
function greet() { return 'Hello'; }
```

## Type Checking

```javascript
typeof 'hello';  // 'string'
typeof 42;       // 'number'
typeof true;     // 'boolean'
typeof [];       // 'object'
typeof null;     // 'object' (quirk!)
```

## Type Conversion

```javascript
Number('42');    // 42
String(42);      // '42'
Boolean(0);      // false
parseInt('42px'); // 42
"""),
        ("Operators", "operators", "Arithmetic, comparison, logical operators", """# JavaScript Operators

Operators perform operations on values.

## Arithmetic Operators

```javascript
let a = 10;
let b = 3;

a + b;  // 13 (addition)
a - b;  // 7  (subtraction)
a * b;  // 30 (multiplication)
a / b;  // 3.33 (division)
a % b;  // 1  (modulus)
a ** b; // 1000 (exponent)
```

## Comparison Operators

```javascript
10 == '10';   // true (loose)
10 === '10';  // false (strict)
10 != '10';   // false (loose)
10 !== '10';  // true (strict)
5 > 3;        // true
5 < 3;        // false
5 >= 5;       // true
```

## Logical Operators

```javascript
true && false;  // false (AND)
true || false;  // true  (OR)
!true;          // false (NOT)
```

## Assignment Operators

```javascript
let x = 5;
x += 3;  // x = 8
x -= 2;  // x = 6
x *= 2;  // x = 12
x /= 3;  // x = 4
x %= 3;  // x = 1
```

## Ternary Operator

```javascript
let age = 18;
let status = age >= 18 ? 'Adult' : 'Minor';
```"""),
        ("Functions", "functions", "Function declarations, expressions, arrow functions", """# JavaScript Functions

Functions are reusable blocks of code.

## Function Declaration

```javascript
function greet(name) {
  return `Hello, ${name}!`;
}

greet('John');  // 'Hello, John!'
```

## Function Expression

```javascript
const greet = function(name) {
  return `Hello, ${name}!`;
};
```

## Arrow Functions

```javascript
// Single parameter
const double = x => x * 2;

// Multiple parameters
const add = (a, b) => a + b;

// Block body
const greet = (name) => {
  return `Hello, ${name}!`;
};
```

## Parameters & Defaults

```javascript
function greet(name = 'World') {
  return `Hello, ${name}!`;
}

// Rest parameters
function sum(...numbers) {
  return numbers.reduce((a, b) => a + b, 0);
}
```

## Return Values

```javascript
// Implicit return (arrow)
const square = x => x * x;

// Explicit return
function square(x) {
  return x * x;
}

// No return = undefined
function noReturn() {}
```"""),
        ("Arrays", "arrays", "Array methods and iteration", """# JavaScript Arrays

Arrays store ordered collections of data.

## Creating Arrays

```javascript
let fruits = ['apple', 'banana', 'orange'];
let numbers = [1, 2, 3, 4, 5];
let mixed = ['text', 42, true, null];
let empty = [];
```

## Common Methods

```javascript
let arr = [1, 2, 3];

arr.push(4);        // [1, 2, 3, 4] - add to end
arr.pop();          // [1, 2, 3] - remove from end
arr.unshift(0);     // [0, 1, 2, 3] - add to start
arr.shift();        // [1, 2, 3] - remove from start

arr.indexOf(2);     // 1 - find index
arr.includes(3);    // true - check existence
arr.slice(1, 3);    // [2, 3] - copy portion
arr.splice(1, 1);   // remove 1 element at index 1
```

## Iteration Methods

```javascript
let numbers = [1, 2, 3, 4, 5];

// forEach
numbers.forEach(n => console.log(n));

// map - transform
let doubled = numbers.map(n => n * 2);

// filter - select
let evens = numbers.filter(n => n % 2 === 0);

// reduce - aggregate
let sum = numbers.reduce((acc, n) => acc + n, 0);

// find - first match
let first = numbers.find(n => n > 3);
```

## Destructuring

```javascript
let [first, second] = [1, 2, 3];
let [head, ...rest] = [1, 2, 3, 4];
```"""),
        ("Objects", "objects", "Object creation and manipulation", """# JavaScript Objects

Objects store key-value pairs of data.

## Creating Objects

```javascript
// Object literal
let person = {
  name: 'John',
  age: 25,
  greet() {
    return `Hi, I'm ${this.name}`;
  }
};

// Using new
let obj = new Object();

// Computed keys
let key = 'dynamic';
let obj2 = { [key]: 'value' };
```

## Accessing Properties

```javascript
let person = { name: 'John', age: 25 };

person.name;        // 'John' (dot notation)
person['name'];     // 'John' (bracket notation)

let key = 'age';
person[key];        // 25 (dynamic)
```

## Object Methods

```javascript
let person = { name: 'John', age: 25 };

Object.keys(person);    // ['name', 'age']
Object.values(person);  // ['John', 25]
Object.entries(person); // [['name', 'John'], ['age', 25]]

// Spread
let copy = { ...person };
let merged = { ...person, city: 'NYC' };

// Destructuring
let { name, age } = person;
```

## this Keyword

```javascript
const person = {
  name: 'John',
  greet() {
    console.log(`Hello, ${this.name}`);
  }
};
```"""),
        ("DOM", "dom", "Document Object Model basics", """# DOM Basics

The DOM (Document Object Model) represents the page structure.

## What is the DOM?

- The DOM is a tree structure of HTML elements
- JavaScript can access and modify the DOM
- The DOM is created by the browser

## Selecting Elements

```javascript
// Single element
document.getElementById('header');
document.querySelector('.nav-item');

// Multiple elements
document.getElementsByClassName('item');
document.querySelectorAll('p');
```

## Modifying Elements

```javascript
// Text content
element.textContent = 'New text';
element.innerText = 'New text';

// HTML content
element.innerHTML = '<strong>Bold</strong>';

// Attributes
element.setAttribute('class', 'active');
element.getAttribute('class');
element.removeAttribute('disabled');

// Styles
element.style.color = 'red';
element.style.backgroundColor = 'blue';
```

## Creating Elements

```javascript
let div = document.createElement('div');
div.textContent = 'Hello';
document.body.appendChild(div);
```"""),
        ("DOM Manipulation", "dom-manipulation", "Selecting and modifying elements", """# DOM Manipulation

Manipulate the DOM to create dynamic pages.

## Adding Elements

```javascript
// Create and append
let li = document.createElement('li');
li.textContent = 'New item';
list.appendChild(li);

// Insert before
list.insertBefore(li, list.firstChild);

// Insert adjacent
element.insertAdjacentHTML('beforeend', '<p>Text</p>');
```

## Removing Elements

```javascript
// Remove element
element.remove();

// Remove child
parent.removeChild(child);

// Clear all children
element.innerHTML = '';
```

## Class Manipulation

```javascript
element.classList.add('active');
element.classList.remove('active');
element.classList.toggle('active');
element.classList.contains('active');
```

## Traversing

```javascript
element.parentElement;
element.children;
element.firstElementChild;
element.lastElementChild;
element.nextElementSibling;
element.previousElementSibling;
```

## Example: Todo List

```javascript
function addTodo(text) {
  const li = document.createElement('li');
  li.textContent = text;
  li.addEventListener('click', () => li.remove());
  document.querySelector('#todos').appendChild(li);
}
```"""),
        ("Event Handling", "event-handling", "Event listeners and propagation", """# Event Handling

Events make pages interactive.

## Adding Event Listeners

```javascript
// Click event
button.addEventListener('click', () => {
  console.log('Button clicked!');
});

// Multiple events
element.addEventListener('mouseover', handler);
element.addEventListener('mouseout', handler);
```

## Common Events

```javascript
// Mouse events
click, dblclick, mouseover, mouseout, mousemove

// Keyboard events
keydown, keyup, keypress

// Form events
submit, change, focus, blur, input

// Window events
load, resize, scroll
```

## Event Object

```javascript
element.addEventListener('click', (event) => {
  event.target;        // Element clicked
  event.preventDefault();  // Stop default
  event.stopPropagation(); // Stop bubbling
  event.clientX;       // Mouse X position
  event.clientY;       // Mouse Y position
});
```

## Event Delegation

```javascript
// Instead of adding to each item
list.addEventListener('click', (e) => {
  if (e.target.tagName === 'LI') {
    console.log('Item clicked:', e.target.textContent);
  }
});
```

## Form Submission

```javascript
form.addEventListener('submit', (e) => {
  e.preventDefault();
  const data = new FormData(form);
  console.log(Object.fromEntries(data));
});
```"""),
        ("Fetch API", "fetch-api", "Making HTTP requests with fetch", """# Fetch API

Fetch is the modern way to make HTTP requests.

## Basic Fetch

```javascript
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
```

## Async/Await

```javascript
async function getData() {
  try {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error:', error);
  }
}
```

## POST Request

```javascript
fetch('https://api.example.com/users', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    name: 'John',
    email: 'john@example.com'
  })
})
.then(res => res.json())
.then(data => console.log(data));
```

## Response Handling

```javascript
const response = await fetch(url);

response.ok;          // true if 200-299
response.status;      // HTTP status code
response.statusText;  // Status text
response.json();      // Parse JSON
response.text();      // Parse text
```"""),
        ("Promises", "promises", "Promise chains and composition", """# JavaScript Promises

Promises handle asynchronous operations.

## What is a Promise?

A Promise represents a value that may be available now, later, or never.

## Promise States

- **Pending**: Initial state
- **Fulfilled**: Operation completed
- **Rejected**: Operation failed

## Creating Promises

```javascript
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('Success!');
    // or
    // reject(new Error('Failed!'));
  }, 1000);
});
```

## Using Promises

```javascript
promise
  .then(result => console.log(result))
  .catch(error => console.error(error))
  .finally(() => console.log('Done'));
```

## Promise Chaining

```javascript
fetchUser()
  .then(user => fetchPosts(user.id))
  .then(posts => fetchComments(posts[0].id))
  .then(comments => console.log(comments))
  .catch(error => console.error(error));
```

## Promise Methods

```javascript
// All - wait for all
Promise.all([p1, p2, p3]);

// Race - first to settle
Promise.race([p1, p2]);

// All settled - wait for all regardless
Promise.allSettled([p1, p2]);

// Any - first to fulfill
Promise.any([p1, p2]);
```"""),
        ("Async Await", "async-await", "Modern asynchronous JavaScript", """# Async/Await

Async/await makes asynchronous code look synchronous.

## Basic Syntax

```javascript
async function getData() {
  const response = await fetch('https://api.example.com/data');
  const data = await response.json();
  return data;
}
```

## Error Handling

```javascript
async function getData() {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error('Request failed');
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error:', error.message);
  }
}
```

## Parallel Execution

```javascript
// Sequential (slow)
const user = await fetchUser();
const posts = await fetchPosts();

// Parallel (fast)
const [user, posts] = await Promise.all([
  fetchUser(),
  fetchPosts()
]);
```

## Async Functions

```javascript
// Always returns a Promise
async function greet() {
  return 'Hello';
}
greet().then(console.log);  // 'Hello'

// Arrow functions
const getData = async () => {
  return await fetch(url);
};
```

## Best Practices

- Use try/catch for error handling
- Use Promise.all for independent calls
- Avoid await in loops when possible
- Handle errors gracefully"""),
        ("ES6+", "es6-plus", "Modern JavaScript features", """# ES6+ Features

Modern JavaScript features that improve code quality.

## Destructuring

```javascript
// Arrays
const [a, b] = [1, 2];

// Objects
const { name, age } = person;

// Renaming
const { name: userName } = person;

// Defaults
const { city = 'Unknown' } = person;
```

## Template Literals

```javascript
const name = 'John';
const greeting = `Hello, ${name}!`;
const multiLine = `
  Line 1
  Line 2
`;
```

## Spread & Rest

```javascript
// Spread
const arr = [1, 2, 3];
const copy = [...arr];
const merged = [...arr, 4, 5];

const obj = { a: 1, b: 2 };
const objCopy = { ...obj };

// Rest
function sum(...nums) {
  return nums.reduce((a, b) => a + b);
}
```

## Optional Chaining

```javascript
const user = { profile: { name: 'John' } };
user?.profile?.name;      // 'John'
user?.address?.city;      // undefined
```

## Nullish Coalescing

```javascript
const value = null ?? 'default';  // 'default'
const num = 0 ?? 'default';       // 0
```"""),
        ("Modules", "modules", "Import and export systems", """# JavaScript Modules

Modules organize code into separate files.

## Exporting

```javascript
// Named exports
export const name = 'John';
export function greet() { return 'Hello'; }
export class Person {}

// Default export
export default function main() {}

// Export list
const a = 1;
const b = 2;
export { a, b };
```

## Importing

```javascript
// Named imports
import { name, greet } from './module.js';

// Default import
import main from './module.js';

// Rename imports
import { name as userName } from './module.js';

// Import all
import * as utils from './utils.js';
```

## Benefits

- Code organization
- Reusability
- Namespace isolation
- Better maintainability

## CommonJS vs ES Modules

```javascript
// CommonJS (Node.js)
const module = require('./module');
module.exports = { name };

// ES Modules
import { name } from './module.js';
export { name };
```"""),
        ("Projects", "projects", "Build JavaScript projects", """# JavaScript Projects

Apply your JavaScript skills with these projects.

## Project 1: Todo App

Build a todo application with:
- Add and delete todos
- LocalStorage persistence
- Filter by status
- Mark as complete

## Project 2: Quiz App

Create a quiz application with:
- Multiple questions
- Score tracking
- Progress bar
- Results screen

## Project 3: Weather App

Build a weather app with:
- Fetch API integration
- Search by city
- Display temperature
- Error handling

## Project 4: Calculator

Create a calculator with:
- Basic operations
- Keyboard support
- Clear and backspace
- Responsive design

## Tips

- Break problems into small steps
- Use console.log for debugging
- Test edge cases
- Refactor your code"""),
        ("Quiz", "quiz", "Test your JavaScript knowledge", """# JavaScript Quiz

Test your knowledge of JavaScript fundamentals.

## Topics Covered

- Variables and data types
- Functions and scope
- Arrays and objects
- DOM manipulation
- Async programming
- ES6+ features

## How to Prepare

- Review all JavaScript topics
- Practice coding exercises
- Build small projects
- Understand async concepts"""),
    ],
    "react": [
        ("Introduction", "introduction", "React fundamentals and setup", """# Introduction to React

React is a JavaScript library for building user interfaces.

## What is React?

- Component-based architecture
- Declarative UI development
- Virtual DOM for performance
- Unidirectional data flow

## Setting Up

```bash
# Create React App
npx create-react-app my-app

# Vite
npm create vite@latest my-app -- --template react
```

## First Component

```jsx
function App() {
  return (
    <div>
      <h1>Hello, React!</h1>
    </div>
  );
}

export default App;
```

## Key Concepts

- **Components**: Reusable UI pieces
- **JSX**: JavaScript + HTML syntax
- **Props**: Data passed to components
- **State**: Component data that changes"""),
        ("JSX", "jsx", "JSX syntax and rules", """# JSX

JSX is a syntax extension for JavaScript.

## What is JSX?

JSX looks like HTML but is JavaScript.

```jsx
const element = <h1>Hello, World!</h1>;
```

## JSX Rules

### Single Root Element
```jsx
// Correct
return (
  <div>
    <h1>Title</h1>
    <p>Text</p>
  </div>
);

// Also correct (fragment)
return (
  <>
    <h1>Title</h1>
    <p>Text</p>
  </>
);
```

### JavaScript Expressions
```jsx
const name = 'John';
const element = <h1>Hello, {name}!</h1>;
const total = <p>Total: {2 + 3}</p>;
```

### Attributes
```jsx
// className instead of class
<div className="container">

// camelCase for attributes
<button onClick={handleClick}>
<input type="text" maxLength={10}>
```

### Conditional Rendering
```jsx
{isLoggedIn ? <Dashboard /> : <Login />}
{isLoading && <Spinner />}
```

## Comments

```jsx
{/* This is a JSX comment */}
```"""),
        ("Components", "components", "Functional and class components", """# React Components

Components are the building blocks of React apps.

## Functional Components

```jsx
function Welcome({ name }) {
  return <h1>Hello, {name}!</h1>;
}

// Arrow function
const Welcome = ({ name }) => {
  return <h1>Hello, {name}!</h1>;
};
```

## Class Components (Legacy)

```jsx
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}!</h1>;
  }
}
```

## Component Composition

```jsx
function App() {
  return (
    <div>
      <Header />
      <MainContent />
      <Footer />
    </div>
  );
}
```

## Component Types

- **Presentational**: Focus on UI
- **Container**: Handle logic and state
- **Higher-Order**: Wrap other components
- **Controlled**: Form inputs controlled by React

## Best Practices

- Components should be small and focused
- Use descriptive names
- Keep components pure when possible
- Extract reusable pieces"""),
        ("Props", "props", "Passing data with props", """# React Props

Props pass data from parent to child components.

## Passing Props

```jsx
function App() {
  return (
    <UserCard
      name="John"
      age={25}
      isActive={true}
      hobbies={['coding', 'reading']}
    />
  );
}
```

## Receiving Props

```jsx
function UserCard(props) {
  return (
    <div>
      <h2>{props.name}</h2>
      <p>Age: {props.age}</p>
    </div>
  );
}

// Destructuring
function UserCard({ name, age, isActive, hobbies }) {
  return (
    <div>
      <h2>{name}</h2>
      <p>Age: {age}</p>
    </div>
  );
}
```

## Default Props

```jsx
function Button({ text = 'Click me', color = 'blue' }) {
  return <button style={{ color }}>{text}</button>;
}
```

## Children Prop

```jsx
function Card({ children }) {
  return <div className="card">{children}</div>;
}

<Card>
  <h2>Title</h2>
  <p>Content</p>
</Card>
```

## Props are Read-Only

```jsx
// Props cannot be modified
function Bad({ count }) {
  count = count + 1;  // ❌ Don't do this
  return <p>{count}</p>;
}
```"""),
        ("State", "state", "Managing component state", """# React State

State is data that changes over time in a component.

## useState Hook

```jsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </div>
  );
}
```

## State Rules

- State is immutable - always use the setter
- State updates are asynchronous
- State is local to the component

## Updating Objects

```jsx
const [user, setUser] = useState({ name: 'John', age: 25 });

// Correct
setUser({ ...user, age: 26 });

// Wrong
user.age = 26;  // ❌
```

## Updating Arrays

```jsx
const [items, setItems] = useState([]);

// Add
setItems([...items, newItem]);

// Remove
setItems(items.filter(item => item.id !== id));

// Update
setItems(items.map(item =>
  item.id === id ? { ...item, done: true } : item
));
```

## Lazy Initialization

```jsx
const [count, setCount] = useState(() => {
  return expensiveCalculation();
});
```"""),
        ("Hooks", "hooks", "useState, useEffect, custom hooks", """# React Hooks

Hooks let you use state and lifecycle features in functional components.

## Common Hooks

### useState
```jsx
const [count, setCount] = useState(0);
```

### useEffect
```jsx
useEffect(() => {
  // Runs after render
  fetchData();
  
  // Cleanup
  return () => {
    // Cleanup code
  };
}, [dependencies]);
```

### useContext
```jsx
const theme = useContext(ThemeContext);
```

### useRef
```jsx
const inputRef = useRef(null);
inputRef.current.focus();
```

### useMemo
```jsx
const memoized = useMemo(() => compute(a, b), [a, b]);
```

### useCallback
```jsx
const memoizedCallback = useCallback(() => {
  doSomething(a, b);
}, [a, b]);
```

## Custom Hooks

```jsx
function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    return localStorage.getItem(key) || initialValue;
  });

  useEffect(() => {
    localStorage.setItem(key, value);
  }, [key, value]);

  return [value, setValue];
}

// Usage
const [name, setName] = useLocalStorage('name', '');
```

## Rules of Hooks

- Only call hooks at the top level
- Only call hooks from React functions
- Don't call hooks in conditions or loops"""),
        ("Routing", "routing", "React Router for navigation", """# React Router

React Router handles navigation in React apps.

## Setup

```bash
npm install react-router-dom
```

## Basic Setup

```jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/users/:id" element={<UserDetail />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}
```

## Navigation

```jsx
import { Link, useNavigate } from 'react-router-dom';

// Link component
<Link to="/about">About</Link>

// useNavigate hook
const navigate = useNavigate();
navigate('/dashboard');
navigate(-1);  // Go back
```

## URL Parameters

```jsx
import { useParams } from 'react-router-dom';

function UserDetail() {
  const { id } = useParams();
  return <h1>User {id}</h1>;
}
```

## Nested Routes

```jsx
<Route path="/dashboard" element={<DashboardLayout />}>
  <Route index element={<Overview />} />
  <Route path="settings" element={<Settings />} />
</Route>
```

## Protected Routes

```jsx
function ProtectedRoute({ children }) {
  const isAuth = useAuth();
  return isAuth ? children : <Navigate to="/login" />;
}
```"""),
        ("Forms", "forms", "Controlled and uncontrolled forms", """# React Forms

Handle form inputs in React.

## Controlled Components

```jsx
function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log({ email, password });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Email"
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
      />
      <button type="submit">Login</button>
    </form>
  );
}
```

## Multiple Fields

```jsx
const [form, setForm] = useState({
  name: '',
  email: '',
  age: ''
});

const handleChange = (e) => {
  setForm({
    ...form,
    [e.target.name]: e.target.value
  });
};

<input name="name" value={form.name} onChange={handleChange} />
```

## Form Validation

```jsx
const [errors, setErrors] = useState({});

const validate = () => {
  const newErrors = {};
  if (!form.email.includes('@')) {
    newErrors.email = 'Invalid email';
  }
  return newErrors;
};

const handleSubmit = (e) => {
  e.preventDefault();
  const validationErrors = validate();
  if (Object.keys(validationErrors).length > 0) {
    setErrors(validationErrors);
    return;
  }
  // Submit
};
```"""),
        ("API Integration", "api-integration", "Fetching data with Axios", """# API Integration

Fetch data from APIs in React.

## Using Fetch

```jsx
useEffect(() => {
  fetch('https://api.example.com/users')
    .then(res => res.json())
    .then(data => setUsers(data))
    .catch(err => setError(err));
}, []);
```

## Using Axios

```bash
npm install axios
```

```jsx
import axios from 'axios';

useEffect(() => {
  axios.get('https://api.example.com/users')
    .then(res => setUsers(res.data))
    .catch(err => setError(err));
}, []);
```

## Loading States

```jsx
const [loading, setLoading] = useState(true);
const [data, setData] = useState(null);
const [error, setError] = useState(null);

useEffect(() => {
  const loadData = async () => {
    try {
      setLoading(true);
      const res = await axios.get(url);
      setData(res.data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };
  loadData();
}, [url]);

if (loading) return <Spinner />;
if (error) return <Error message={error} />;
return <DataView data={data} />;
```

## POST Requests

```jsx
const handleSubmit = async (formData) => {
  try {
    const res = await axios.post('/api/users', formData);
    console.log('Created:', res.data);
  } catch (err) {
    console.error('Error:', err);
  }
};
```"""),
        ("Projects", "projects", "Build React applications", """# React Projects

Apply your React skills with these projects.

## Project 1: Todo App

Build a todo app with:
- Add, delete, edit todos
- Filter by status
- LocalStorage persistence
- Clean component structure

## Project 2: Weather App

Create a weather app with:
- API integration
- Search functionality
- Loading states
- Error handling

## Project 3: E-commerce Store

Build a store with:
- Product listing
- Shopping cart
- Checkout flow
- Context or Redux state

## Project 4: Chat Application

Create a chat app with:
- Message list
- Input form
- User list
- Real-time updates

## Tips

- Plan component structure first
- Use hooks effectively
- Handle loading and error states
- Write clean, reusable components"""),
        ("Quiz", "quiz", "Test your React knowledge", """# React Quiz

Test your knowledge of React fundamentals.

## Topics Covered

- Components and JSX
- Props and state
- Hooks
- Routing
- Forms and API integration

## How to Prepare

- Review all React topics
- Build components with props
- Practice using hooks
- Create forms and API calls"""),
    ],
    "python": [
        ("Introduction", "introduction", "Python setup and basics", """# Introduction to Python

Python is a versatile, high-level programming language.

## What is Python?

- Easy to read and learn
- Used for web, data science, AI, automation
- Large standard library
- Cross-platform

## Setting Up

```bash
# Check version
python --version

# Run Python
python
# or
python3
```

## First Program

```python
print("Hello, World!")

# Variables
name = "John"
age = 25

# Comments
# This is a comment
```

## Basic Syntax

```python
# No semicolons needed
print("Hello")

# Indentation matters
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

## Key Features

- Dynamic typing
- Automatic memory management
- Rich standard library
- Huge ecosystem of packages"""),
        ("Variables", "variables", "Variables and data types", """# Python Variables

Variables store data in Python.

## Basic Variables

```python
# Numbers
age = 25
price = 19.99
complex_num = 3 + 4j

# Strings
name = "John"
message = 'Hello'
multi_line = '''This is
a multi-line
string'''

# Boolean
is_active = True
is_admin = False

# None
result = None
```

## Type Checking

```python
type(25)        # <class 'int'>
type(19.99)     # <class 'float'>
type("text")    # <class 'str'>
type(True)      # <class 'bool'>
type([1, 2])    # <class 'list'>
type((1, 2))    # <class 'tuple'>
type({"a": 1})  # <class 'dict'>
```

## Type Conversion

```python
int("42")       # 42
float("3.14")   # 3.14
str(42)         # "42"
bool(0)         # False
bool(1)         # True
list("abc")     # ['a', 'b', 'c']
```

## Naming Conventions

- Use snake_case: `my_variable`
- Start with letter or underscore
- Constants in UPPER_CASE: `MAX_SIZE`
- Descriptive names: `user_name` not `u`"""),
        ("Functions", "functions", "Defining and calling functions", """# Python Functions

Functions are reusable blocks of code.

## Defining Functions

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("John"))  # Hello, John!
```

## Parameters

```python
# Default parameters
def greet(name="World"):
    return f"Hello, {name}!"

# Keyword arguments
def create_user(name, age, city="Unknown"):
    return {"name": name, "age": age, "city": city}

create_user("John", 25)
create_user(name="Jane", age=30, city="NYC")

# *args - variable positional
def sum_all(*args):
    return sum(args)

# **kwargs - variable keyword
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

## Return Values

```python
# Single return
def square(x):
    return x * x

# Multiple returns
def get_min_max(numbers):
    return min(numbers), max(numbers)

min_val, max_val = get_min_max([1, 5, 3])
```

## Lambda Functions

```python
# Anonymous functions
square = lambda x: x * x
add = lambda a, b: a + b

# Used with map/filter
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

## Scope

```python
# Global scope
x = 10

def my_func():
    # Local scope
    y = 20
    return x + y  # Can access global

# global keyword
def change_global():
    global x
    x = 100
```"""),
        ("Lists", "lists", "List operations and methods", """# Python Lists

Lists store ordered collections of items.

## Creating Lists

```python
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["text", 42, True, None]
empty = []
```

## Accessing Elements

```python
fruits[0]       # 'apple'
fruits[-1]      # 'orange' (last)
fruits[1:3]     # ['banana', 'orange'] (slice)
fruits[::2]     # ['apple', 'orange'] (step)
```

## List Methods

```python
fruits.append("grape")      # Add to end
fruits.insert(0, "kiwi")    # Insert at index
fruits.remove("banana")     # Remove by value
fruits.pop()                # Remove last
fruits.pop(0)               # Remove at index
fruits.index("apple")       # Find index
fruits.count("apple")       # Count occurrences
fruits.sort()               # Sort in place
fruits.reverse()            # Reverse in place
```

## List Operations

```python
# Concatenation
[1, 2] + [3, 4]     # [1, 2, 3, 4]

# Repetition
[0] * 3             # [0, 0, 0]

# Membership
"apple" in fruits   # True

# Length
len(fruits)         # 3

# Min/Max/Sum
min(numbers)        # 1
max(numbers)        # 5
sum(numbers)        # 15
```

## List Comprehension

```python
# Basic
squares = [x * x for x in range(5)]

# With condition
evens = [x for x in range(10) if x % 2 == 0]

# Nested
matrix = [[x * y for x in range(3)] for y in range(3)]
```"""),
        ("Dictionaries", "dictionaries", "Dictionary operations", """# Python Dictionaries

Dictionaries store key-value pairs.

## Creating Dictionaries

```python
person = {
    "name": "John",
    "age": 25,
    "city": "NYC"
}

# Using dict()
person = dict(name="John", age=25)

# Empty
empty = {}
```

## Accessing Values

```python
person["name"]          # 'John'
person.get("name")      # 'John'
person.get("email", "N/A")  # 'N/A' (default)

# KeyError if missing
# person["email"]  # ❌ KeyError
```

## Modifying

```python
person["age"] = 26          # Update
person["email"] = "j@e.com" # Add
person.pop("city")          # Remove
del person["age"]           # Remove
person.clear()              # Clear all
```

## Dictionary Methods

```python
person.keys()       # dict_keys(['name', 'age'])
person.values()     # dict_values(['John', 25])
person.items()      # dict_items([('name', 'John'), ...])

# Update multiple
person.update({"age": 30, "city": "LA"})

# Merge (Python 3.9+)
merged = {**person, **other}
```

## Iteration

```python
for key in person:
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(f"{key}: {value}")
```

## Dictionary Comprehension

```python
squares = {x: x * x for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```"""),
        ("OOP", "oop", "Classes, objects, inheritance", """# Python OOP

Object-Oriented Programming in Python.

## Classes

```python
class Person:
    # Class attribute
    species = "human"

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def greet(self):
        return f"Hello, I'm {self.name}"

    # String representation
    def __str__(self):
        return f"Person({self.name}, {self.age})"

# Create object
john = Person("John", 25)
print(john.greet())  # Hello, I'm John
```

## Inheritance

```python
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying"

    # Override
    def greet(self):
        return f"Hi, I'm student {self.name}"
```

## Encapsulation

```python
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance  # Protected
        self.__pin = "1234"      # Private

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def get_balance(self):
        return self._balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
```

## Class Methods & Static Methods

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def create_default(cls):
        return cls()
```"""),
        ("Exception Handling", "exception-handling", "Try, except, finally", """# Python Exception Handling

Handle errors gracefully in Python.

## Try/Except

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

## Multiple Exceptions

```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("Invalid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Else and Finally

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
else:
    print("File read successfully!")
finally:
    print("This always runs")
```

## Raising Exceptions

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age < 18:
        raise ValueError("Must be 18+")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(f"Error: {e}")
```

## Custom Exceptions

```python
class CustomError(Exception):
    pass

class ValidationError(Exception):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")

try:
    raise ValidationError("email", "Invalid format")
except ValidationError as e:
    print(f"{e.field}: {e.message}")
```"""),
        ("Modules", "modules", "Importing and creating modules", """# Python Modules

Organize code into modules and packages.

## Importing Modules

```python
# Import entire module
import math
math.sqrt(16)  # 4.0

# Import specific items
from math import sqrt, pi
sqrt(16)  # 4.0

# Import with alias
import numpy as np
import pandas as pd

# Import all (not recommended)
from math import *
```

## Creating Modules

```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

class Calculator:
    def add(self, a, b):
        return a + b

# main.py
import mymodule
print(mymodule.greet("John"))
```

## if __name__ == "__main__"

```python
# mymodule.py
def main():
    print("Running directly")

if __name__ == "__main__":
    main()
```

## Common Standard Modules

```python
import os          # Operating system
import sys         # System-specific
import json        # JSON handling
import datetime    # Dates and times
import random      # Random numbers
import re          # Regular expressions
import collections # Specialized containers
```

## Packages

```python
# Directory structure
# mypackage/
#   __init__.py
#   module1.py
#   module2.py

from mypackage import module1
from mypackage.module1 import function1
```"""),
        ("Projects", "projects", "Build Python projects", """# Python Projects

Apply your Python skills with these projects.

## Project 1: Calculator

Build a calculator with:
- Basic operations
- Error handling
- User input

## Project 2: To-Do List

Create a todo list app with:
- Add, remove, complete tasks
- File storage
- Command-line interface

## Project 3: Web Scraper

Build a web scraper with:
- Requests library
- BeautifulSoup
- Data extraction
- CSV export

## Project 4: Data Analysis

Create a data analysis tool with:
- Pandas
- Matplotlib
- Data cleaning
- Visualization

## Tips

- Start with simple projects
- Use functions to organize code
- Handle errors properly
- Write tests for your code"""),
        ("Quiz", "quiz", "Test your Python knowledge", """# Python Quiz

Test your knowledge of Python fundamentals.

## Topics Covered

- Variables and data types
- Functions
- Lists and dictionaries
- OOP
- Exception handling
- Modules

## How to Prepare

- Review all Python topics
- Practice writing functions
- Build classes and objects
- Handle exceptions properly"""),
    ],
    "fastapi": [
        ("Introduction", "introduction", "FastAPI setup and overview", """# Introduction to FastAPI

FastAPI is a modern web framework for building APIs.

## What is FastAPI?

- High performance
- Automatic API documentation
- Type hints and validation
- Async support

## Installation

```bash
pip install fastapi uvicorn
```

## First API

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/health")
def health():
    return {"status": "healthy"}
```

## Running

```bash
uvicorn main:app --reload
```

## Automatic Docs

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Key Features

- **Type hints**: Automatic validation
- **Pydantic**: Data validation
- **Async**: High performance
- **OpenAPI**: Standard documentation"""),
        ("Routing", "routing", "Path and query parameters", """# FastAPI Routing

Define routes and handle parameters.

## Path Parameters

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/items/{item_id}")
def get_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

## Query Parameters

```python
@app.get("/search")
def search(q: str, limit: int = 10, offset: int = 0):
    return {"query": q, "limit": limit, "offset": offset}

# /search?q=python&limit=5
```

## Path vs Query

```python
# Path: /users/42
@app.get("/users/{user_id}")
def get_user(user_id: int):
    ...

# Query: /users?role=admin
@app.get("/users")
def list_users(role: str = None):
    ...
```

## Parameter Types

```python
@app.get("/items/{item_id}")
def get_item(
    item_id: int,           # Path parameter
    q: str = None,          # Optional query
    skip: int = 0,          # Default value
    limit: int = 10,        # Default value
    tags: list[str] = [],   # List query
):
    return {
        "item_id": item_id,
        "q": q,
        "skip": skip,
        "limit": limit,
        "tags": tags,
    }
```

## Route Order Matters

```python
# Specific routes first
@app.get("/users/me")
def get_me():
    return {"user": "me"}

# Dynamic routes after
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```"""),
        ("Request & Response", "request-response", "Handling requests and responses", """# FastAPI Request & Response

Handle HTTP requests and responses.

## Request Body

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

@app.post("/items/")
def create_item(item: Item):
    return {"item": item, "message": "Created"}
```

## Response Models

```python
class ItemResponse(BaseModel):
    id: int
    name: str
    price: float

@app.post("/items/", response_model=ItemResponse)
def create_item(item: Item):
    # Return only fields in ItemResponse
    return {"id": 1, "name": item.name, "price": item.price}
```

## Status Codes

```python
from fastapi import status

@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    return item

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    return None
```

## Headers & Cookies

```python
from fastapi import Header, Cookie

@app.get("/headers")
def get_headers(
    user_agent: str = Header(None),
    session_id: str = Cookie(None),
):
    return {"user_agent": user_agent, "session_id": session_id}
```

## Response Types

```python
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse

@app.get("/json")
def json_response():
    return JSONResponse({"message": "Hello"})

@app.get("/html")
def html_response():
    return HTMLResponse("<h1>Hello</h1>")

@app.get("/redirect")
def redirect():
    return RedirectResponse("/docs")
```"""),
        ("Dependency Injection", "dependency-injection", "DI in FastAPI", """# FastAPI Dependency Injection

Dependencies make code reusable and testable.

## Basic Dependencies

```python
from fastapi import Depends

def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/items/")
def read_items(commons: dict = Depends(common_parameters)):
    return commons

@app.get("/users/")
def read_users(commons: dict = Depends(common_parameters)):
    return commons
```

## Class Dependencies

```python
class CommonQueryParams:
    def __init__(self, q: str = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit

@app.get("/items/")
def read_items(commons: CommonQueryParams = Depends()):
    return {"q": commons.q, "skip": commons.skip}
```

## Database Dependency

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()
```

## Authentication Dependency

```python
def get_current_user(token: str = Depends(oauth2_scheme)):
    user = verify_token(token)
    if user is None:
        raise HTTPException(status_code=401)
    return user

@app.get("/users/me")
def read_me(current_user: User = Depends(get_current_user)):
    return current_user
```

## Dependency Chaining

```python
def get_current_active_user(
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_active:
        raise HTTPException(status_code=400)
    return current_user
```"""),
        ("Authentication", "authentication", "JWT authentication with FastAPI", """# FastAPI Authentication

Implement JWT authentication.

## Password Hashing

```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)
```

## JWT Tokens

```python
import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=30))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.PyJWTError:
        return None
```

## Login Endpoint

```python
@app.post("/auth/login")
def login(credentials: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == credentials.email).first()
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}
```

## Protected Routes

```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(User).filter(User.id == int(payload["sub"])).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user

@app.get("/users/me")
def read_me(current_user: User = Depends(get_current_user)):
    return current_user
```"""),
        ("Background Tasks", "background-tasks", "Running background tasks", """# FastAPI Background Tasks

Run tasks after returning a response.

## Basic Background Tasks

```python
from fastapi import BackgroundTasks

def write_log(message: str):
    with open("log.txt", "a") as f:
        f.write(f"{message}\n")

@app.post("/send-email/")
def send_email(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, f"Email sent to {email}")
    return {"message": "Email will be sent"}
```

## Multiple Tasks

```python
def send_welcome_email(email: str):
    # Send email logic
    pass

def update_analytics(user_id: int):
    # Update analytics
    pass

@app.post("/register/")
def register(
    user_data: UserCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    user = create_user(db, user_data)
    background_tasks.add_task(send_welcome_email, user.email)
    background_tasks.add_task(update_analytics, user.id)
    return {"message": "User registered", "user_id": user.id}
```

## Use Cases

- Sending emails
- Generating reports
- Processing uploads
- Cleaning up resources
- Webhooks and notifications

## Important Notes

- Tasks run after response is sent
- Tasks share the same process
- For heavy tasks, use a task queue (Celery, RQ)"""),
        ("Projects", "projects", "Build FastAPI applications", """# FastAPI Projects

Apply your FastAPI skills with these projects.

## Project 1: Todo API

Build a todo API with:
- CRUD operations
- Pydantic validation
- SQLite database
- Authentication

## Project 2: Blog API

Create a blog API with:
- Posts and comments
- User authentication
- Categories and tags
- Pagination

## Project 3: E-commerce API

Build an e-commerce API with:
- Products and inventory
- Shopping cart
- Orders
- Payment integration

## Project 4: URL Shortener

Create a URL shortener with:
- Short URL generation
- Redirect handling
- Click tracking
- Analytics

## Tips

- Use Pydantic for validation
- Implement proper error handling
- Add authentication early
- Write API tests"""),
        ("Quiz", "quiz", "Test your FastAPI knowledge", """# FastAPI Quiz

Test your knowledge of FastAPI fundamentals.

## Topics Covered

- Routing and parameters
- Request and response models
- Dependency injection
- Authentication
- Background tasks

## How to Prepare

- Review all FastAPI topics
- Build simple APIs
- Practice with dependencies
- Implement authentication"""),
    ],
}

# Add imported data module topics
COURSE_TOPICS["javascript"] = JS_TOPICS
COURSE_TOPICS["nodejs"] = NODEJS_TOPICS
COURSE_TOPICS["express"] = EXPRESS_TOPICS
COURSE_TOPICS["database"] = DATABASE_TOPICS
COURSE_TOPICS["sql"] = DATABASE_TOPICS
COURSE_TOPICS["redux"] = REDUX_TOPICS
COURSE_TOPICS["git-github"] = GIT_AI_TOPICS["git-github"]
COURSE_TOPICS["ai-ml"] = GIT_AI_TOPICS["ai-ml"]
COURSE_TOPICS["WoWCodes"] = WoWCodes_TOPICS


# Quizzes per topic: (full topic slug, level, title, passing_score, [(question, explanation, [(option, correct)] )])
QUIZ_TEMPLATES = {
    "html-introduction": [
        {
            "level": "easy",
            "title": "HTML Introduction - Easy Quiz",
            "passing_score": 60,
            "questions": [
                {
                    "text": "What does HTML stand for?",
                    "explanation": "HTML stands for HyperText Markup Language.",
                    "options": [("HyperText Markup Language", True), ("HighText Machine Language", False), ("HyperText Making Language", False), ("HyperTool Markup Language", False)],
                },
                {
                    "text": "Which tag is used to create a paragraph in HTML?",
                    "explanation": "The <p> tag defines a paragraph.",
                    "options": [("<para>", False), ("<p>", True), ("<paragraph>", False), ("<text>", False)],
                },
                {
                    "text": "What is the correct HTML element for the largest heading?",
                    "explanation": "<h1> is the largest heading element.",
                    "options": [("<heading>", False), ("<h6>", False), ("<h1>", True), ("<head>", False)],
                },
            ],
        }
    ],
    "html-tags": [
        {
            "level": "easy",
            "title": "HTML Tags - Easy Quiz",
            "passing_score": 60,
            "questions": [
                {
                    "text": "Which tag is used to create a hyperlink?",
                    "explanation": "The <a> tag creates hyperlinks.",
                    "options": [("<link>", False), ("<a>", True), ("<href>", False), ("<url>", False)],
                },
                {
                    "text": "Which attribute specifies an image source?",
                    "explanation": "The src attribute specifies the image source URL.",
                    "options": [("href", False), ("src", True), ("alt", False), ("source", False)],
                },
                {
                    "text": "Which tag creates an unordered list?",
                    "explanation": "<ul> creates an unordered (bulleted) list.",
                    "options": [("<ol>", False), ("<list>", False), ("<ul>", True), ("<li>", False)],
                },
            ],
        }
    ],
    "html-forms": [
        {
            "level": "medium",
            "title": "HTML Forms - Medium Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which input type is used for email addresses?",
                    "explanation": "type='email' validates email format.",
                    "options": [("text", False), ("email", True), ("mail", False), ("address", False)],
                },
                {
                    "text": "Which attribute makes a form field mandatory?",
                    "explanation": "The required attribute makes a field mandatory.",
                    "options": [("mandatory", False), ("required", True), ("validate", False), ("must", False)],
                },
                {
                    "text": "What does the 'action' attribute in a form specify?",
                    "explanation": "The action attribute specifies where to send form data.",
                    "options": [("The form method", False), ("Where to send data", True), ("The form name", False), ("The form style", False)],
                },
            ],
        }
    ],
    "html-semantic-html": [
        {
            "level": "medium",
            "title": "Semantic HTML - Medium Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which element is used for the main navigation links?",
                    "explanation": "The <nav> element is for navigation links.",
                    "options": [("<header>", False), ("<nav>", True), ("<menu>", False), ("<links>", False)],
                },
                {
                    "text": "Which semantic element represents self-contained content?",
                    "explanation": "<article> represents self-contained content like a blog post.",
                    "options": [("<section>", False), ("<article>", True), ("<div>", False), ("<span>", False)],
                },
                {
                    "text": "Why is semantic HTML important for accessibility?",
                    "explanation": "Semantic HTML helps screen readers understand page structure.",
                    "options": [("It makes pages faster", False), ("It helps screen readers understand structure", True), ("It adds more colors", False), ("It reduces file size", False)],
                },
            ],
        }
    ],
    "html-projects": [
        {
            "level": "hard",
            "title": "HTML Projects - Hard Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "What is the first step when building an HTML project?",
                    "explanation": "Planning with a wireframe is the first step.",
                    "options": [("Writing CSS", False), ("Creating a wireframe", True), ("Adding JavaScript", False), ("Deploying", False)],
                },
                {
                    "text": "Which element should contain the main content of a page?",
                    "explanation": "The <main> element contains the primary content.",
                    "options": [("<header>", False), ("<main>", True), ("<footer>", False), ("<aside>", False)],
                },
            ],
        }
    ],
    "html-quiz": [
        {
            "level": "hard",
            "title": "HTML Comprehensive Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "Which HTML element is used to define a table row?",
                    "explanation": "<tr> defines a table row.",
                    "options": [("<td>", False), ("<tr>", True), ("<th>", False), ("<table>", False)],
                },
                {
                    "text": "What is the correct way to comment in HTML?",
                    "explanation": "HTML comments use <!-- --> syntax.",
                    "options": [("// comment", False), ("<!-- comment -->", True), ("/* comment */", False), ("# comment", False)],
                },
                {
                    "text": "Which attribute is used to provide alternative text for an image?",
                    "explanation": "The alt attribute provides alternative text.",
                    "options": [("title", False), ("alt", True), ("text", False), ("desc", False)],
                },
            ],
        }
    ],
    "css-introduction": [
        {
            "level": "easy",
            "title": "CSS Introduction - Easy Quiz",
            "passing_score": 60,
            "questions": [
                {
                    "text": "What does CSS stand for?",
                    "explanation": "CSS stands for Cascading Style Sheets.",
                    "options": [("Computer Style Sheets", False), ("Cascading Style Sheets", True), ("Creative Style Sheets", False), ("Colorful Style Sheets", False)],
                },
                {
                    "text": "Which HTML tag is used to link an external CSS file?",
                    "explanation": "The <link> tag links external stylesheets.",
                    "options": [("<style>", False), ("<link>", True), ("<css>", False), ("<script>", False)],
                },
                {
                    "text": "Which property changes the text color?",
                    "explanation": "The color property changes text color.",
                    "options": [("font-color", False), ("text-color", False), ("color", True), ("font-style", False)],
                },
            ],
        }
    ],
    "css-selectors": [
        {
            "level": "medium",
            "title": "CSS Selectors - Medium Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which selector has the highest specificity?",
                    "explanation": "ID selectors have higher specificity than classes and elements.",
                    "options": [("Element selector", False), ("Class selector", False), ("ID selector", True), ("Universal selector", False)],
                },
                {
                    "text": "How do you select an element with class 'highlight'?",
                    "explanation": "The . prefix selects by class.",
                    "options": [("#highlight", False), (".highlight", True), ("highlight", False), ("*highlight", False)],
                },
                {
                    "text": "What does the :hover pseudo-class do?",
                    "explanation": ":hover applies styles when the mouse is over an element.",
                    "options": [("Styles when clicked", False), ("Styles when hovered", True), ("Styles when focused", False), ("Styles when loaded", False)],
                },
            ],
        }
    ],
    "css-box-model": [
        {
            "level": "medium",
            "title": "CSS Box Model - Medium Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which part of the box model is between content and border?",
                    "explanation": "Padding is between content and border.",
                    "options": [("Margin", False), ("Padding", True), ("Border", False), ("Outline", False)],
                },
                {
                    "text": "What does box-sizing: border-box do?",
                    "explanation": "It includes padding and border in the element's total width.",
                    "options": [("Excludes padding from width", False), ("Includes padding and border in width", True), ("Adds extra margin", False), ("Removes borders", False)],
                },
                {
                    "text": "Which property creates space outside the border?",
                    "explanation": "Margin creates space outside the border.",
                    "options": [("Padding", False), ("Margin", True), ("Spacing", False), ("Gap", False)],
                },
            ],
        }
    ],
    "css-flexbox": [
        {
            "level": "medium",
            "title": "CSS Flexbox - Medium Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which property centers items on the main axis in flexbox?",
                    "explanation": "justify-content aligns items on the main axis.",
                    "options": [("align-items", False), ("justify-content", True), ("align-self", False), ("text-align", False)],
                },
                {
                    "text": "What does display: flex do?",
                    "explanation": "It creates a flex container for one-dimensional layout.",
                    "options": [("Creates a grid layout", False), ("Creates a flex container", True), ("Hides the element", False), ("Makes text bold", False)],
                },
                {
                    "text": "Which property sets the direction of flex items?",
                    "explanation": "flex-direction sets row or column direction.",
                    "options": [("flex-wrap", False), ("flex-direction", True), ("flex-flow", False), ("align-items", False)],
                },
            ],
        }
    ],
    "css-grid": [
        {
            "level": "hard",
            "title": "CSS Grid - Hard Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "Which property defines the columns in a grid?",
                    "explanation": "grid-template-columns defines the grid columns.",
                    "options": [("grid-columns", False), ("grid-template-columns", True), ("grid-gap", False), ("grid-flow", False)],
                },
                {
                    "text": "What does 'repeat(3, 1fr)' mean?",
                    "explanation": "It creates 3 equal-width columns.",
                    "options": [("3 rows of equal height", False), ("3 equal-width columns", True), ("3 pixels gap", False), ("3 grid areas", False)],
                },
                {
                    "text": "When should you use Grid instead of Flexbox?",
                    "explanation": "Grid is best for 2D layouts with rows and columns.",
                    "options": [("For single-row layouts", False), ("For 2D layouts with rows and columns", True), ("For navigation bars", False), ("For text alignment", False)],
                },
            ],
        }
    ],
    "css-projects": [
        {
            "level": "hard",
            "title": "CSS Projects - Hard Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "What is the mobile-first approach?",
                    "explanation": "Design for mobile screens first, then scale up.",
                    "options": [("Design for desktop first", False), ("Design for mobile first, then scale up", True), ("Design for tablets only", False), ("Design without breakpoints", False)],
                },
                {
                    "text": "Which CSS feature helps create responsive designs?",
                    "explanation": "Media queries apply styles based on screen size.",
                    "options": [("Flexbox only", False), ("Media queries", True), ("CSS variables", False), ("Transitions", False)],
                },
            ],
        }
    ],
    "css-quiz": [
        {
            "level": "hard",
            "title": "CSS Comprehensive Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "What is the default value of position property?",
                    "explanation": "The default position value is static.",
                    "options": [("relative", False), ("static", True), ("absolute", False), ("fixed", False)],
                },
                {
                    "text": "Which property creates a smooth transition?",
                    "explanation": "transition creates smooth animations between states.",
                    "options": [("animation", False), ("transition", True), ("transform", False), ("translate", False)],
                },
                {
                    "text": "What does z-index control?",
                    "explanation": "z-index controls the stacking order of elements.",
                    "options": [("Horizontal position", False), ("Stacking order", True), ("Opacity", False), ("Font size", False)],
                },
            ],
        }
    ],
    "javascript-introduction": [
        {
            "level": "easy",
            "title": "JavaScript Introduction - Easy Quiz",
            "passing_score": 60,
            "questions": [
                {
                    "text": "Which tag is used to include JavaScript in HTML?",
                    "explanation": "The <script> tag is used for JavaScript.",
                    "options": [("<js>", False), ("<script>", True), ("<javascript>", False), ("<code>", False)],
                },
                {
                    "text": "How do you write 'Hello World' in the console?",
                    "explanation": "console.log() outputs to the browser console.",
                    "options": [("print('Hello World')", False), ("console.log('Hello World')", True), ("echo 'Hello World'", False), ("log('Hello World')", False)],
                },
                {
                    "text": "JavaScript is a ______ language.",
                    "explanation": "JavaScript is a high-level, interpreted language.",
                    "options": [("compiled", False), ("interpreted", True), ("assembly", False), ("markup", False)],
                },
            ],
        }
    ],
    "javascript-variables": [
        {
            "level": "easy",
            "title": "JavaScript Variables - Easy Quiz",
            "passing_score": 60,
            "questions": [
                {
                    "text": "Which keyword is used to declare a block-scoped variable in JavaScript?",
                    "explanation": "let and const are block-scoped declarations.",
                    "options": [("var", False), ("let", True), ("function", False), ("int", False)],
                },
                {
                    "text": "What is the output of typeof null in JavaScript?",
                    "explanation": "A quirk of JavaScript, typeof null returns 'object'.",
                    "options": [("null", False), ("undefined", False), ("object", True), ("number", False)],
                },
                {
                    "text": "Which keyword declares a constant that cannot be reassigned?",
                    "explanation": "const declares variables that cannot be reassigned.",
                    "options": [("let", False), ("var", False), ("const", True), ("static", False)],
                },
                {
                    "text": "What is the scope of a variable declared with 'let' inside a block?",
                    "explanation": "let is block-scoped, so it's only accessible within the block.",
                    "options": [("Global scope", False), ("Function scope", False), ("Block scope", True), ("Module scope", False)],
                },
            ],
        }
    ],
    "javascript-data-types": [
        {
            "level": "easy",
            "title": "JavaScript Data Types - Easy Quiz",
            "passing_score": 60,
            "questions": [
                {
                    "text": "Which of the following is NOT a primitive data type?",
                    "explanation": "Arrays are reference types, not primitives.",
                    "options": [("String", False), ("Number", False), ("Array", True), ("Boolean", False)],
                },
                {
                    "text": "What is the result of typeof [] ?",
                    "explanation": "Arrays return 'object' in JavaScript.",
                    "options": [("'array'", False), ("'object'", True), ("'list'", False), ("'undefined'", False)],
                },
                {
                    "text": "Which method converts a string to a number?",
                    "explanation": "Number() converts strings to numbers.",
                    "options": [("parseString()", False), ("Number()", True), ("toNumber()", False), ("convert()", False)],
                },
            ],
        }
    ],
    "javascript-operators": [
        {
            "level": "medium",
            "title": "JavaScript Operators - Medium Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What is the result of 10 === '10'?",
                    "explanation": "=== is strict equality, so number 10 is not equal to string '10'.",
                    "options": [("true", False), ("false", True), ("undefined", False), ("NaN", False)],
                },
                {
                    "text": "What does the % operator do?",
                    "explanation": "% returns the remainder of division.",
                    "options": [("Percentage", False), ("Modulus (remainder)", True), ("Division", False), ("Multiplication", False)],
                },
                {
                    "text": "What is the result of true && false?",
                    "explanation": "AND returns true only if both operands are true.",
                    "options": [("true", False), ("false", True), ("undefined", False), ("null", False)],
                },
                {
                    "text": "What does the ?? operator do?",
                    "explanation": "Nullish coalescing returns the right side if left is null/undefined.",
                    "options": [("Logical OR", False), ("Nullish coalescing", True), ("Strict equality", False), ("Assignment", False)],
                },
            ],
        }
    ],
    "javascript-functions": [
        {
            "level": "medium",
            "title": "JavaScript Functions - Medium Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does a function return if no return statement is used?",
                    "explanation": "Functions return undefined by default.",
                    "options": [("null", False), ("undefined", True), ("0", False), ("NaN", False)],
                },
                {
                    "text": "Which is the correct arrow function syntax?",
                    "explanation": "Arrow functions use => syntax.",
                    "options": [("function => {}", False), ("() => {}", True), ("=> function {}", False), ("{} => ()", False)],
                },
                {
                    "text": "What is a function expression?",
                    "explanation": "A function assigned to a variable is a function expression.",
                    "options": [("A function declared with 'function' keyword", False), ("A function assigned to a variable", True), ("An async function", False), ("A generator function", False)],
                },
                {
                    "text": "What are default parameters?",
                    "explanation": "Default parameters have fallback values if no argument is passed.",
                    "options": [("Parameters that are required", False), ("Parameters with fallback values", True), ("Parameters that are optional", False), ("Rest parameters", False)],
                },
            ],
        }
    ],
    "javascript-arrays": [
        {
            "level": "medium",
            "title": "JavaScript Arrays - Medium Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which method adds an element to the end of an array?",
                    "explanation": "push() adds elements to the end.",
                    "options": [("shift()", False), ("push()", True), ("pop()", False), ("unshift()", False)],
                },
                {
                    "text": "Which method creates a new array with transformed elements?",
                    "explanation": "map() transforms each element and returns a new array.",
                    "options": [("forEach()", False), ("map()", True), ("filter()", False), ("reduce()", False)],
                },
                {
                    "text": "What does filter() return?",
                    "explanation": "filter() returns a new array with elements that pass the test.",
                    "options": [("The first matching element", False), ("A new array with matching elements", True), ("A boolean", False), ("The original array", False)],
                },
                {
                    "text": "What is the result of [1, 2, 3].reduce((a, b) => a + b, 0)?",
                    "explanation": "reduce sums all elements: 1 + 2 + 3 = 6.",
                    "options": [("3", False), ("6", True), ("123", False), ("0", False)],
                },
            ],
        }
    ],
    "javascript-objects": [
        {
            "level": "medium",
            "title": "JavaScript Objects - Medium Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "How do you access the 'name' property of object person?",
                    "explanation": "Dot notation accesses object properties.",
                    "options": [("person->name", False), ("person.name", True), ("person[name]", False), ("person::name", False)],
                },
                {
                    "text": "Which method returns an array of an object's keys?",
                    "explanation": "Object.keys() returns an array of keys.",
                    "options": [("Object.values()", False), ("Object.keys()", True), ("Object.entries()", False), ("Object.items()", False)],
                },
                {
                    "text": "What does the spread operator do with objects?",
                    "explanation": "Spread copies properties into a new object.",
                    "options": [("Deletes properties", False), ("Copies properties into a new object", True), ("Sorts properties", False), ("Freezes the object", False)],
                },
            ],
        }
    ],
    "javascript-dom": [
        {
            "level": "medium",
            "title": "JavaScript DOM - Medium Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which method selects an element by its ID?",
                    "explanation": "getElementById() selects by ID.",
                    "options": [("querySelectorAll()", False), ("getElementById()", True), ("getElementsByClass()", False), ("selectById()", False)],
                },
                {
                    "text": "What does the DOM represent?",
                    "explanation": "The DOM is a tree structure of HTML elements.",
                    "options": [("The server database", False), ("A tree structure of HTML elements", True), ("The CSS styles", False), ("The JavaScript code", False)],
                },
                {
                    "text": "Which property changes the text content of an element?",
                    "explanation": "textContent sets or gets the text content.",
                    "options": [("innerHTML", False), ("textContent", True), ("value", False), ("src", False)],
                },
            ],
        }
    ],
    "javascript-dom-manipulation": [
        {
            "level": "medium",
            "title": "JavaScript DOM Manipulation - Medium Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which method creates a new HTML element?",
                    "explanation": "document.createElement() creates new elements.",
                    "options": [("document.newElement()", False), ("document.createElement()", True), ("document.addElement()", False), ("document.makeElement()", False)],
                },
                {
                    "text": "How do you add a class to an element?",
                    "explanation": "classList.add() adds a class.",
                    "options": [("element.class = 'active'", False), ("element.classList.add('active')", True), ("element.addClass('active')", False), ("element.className += 'active'", False)],
                },
                {
                    "text": "Which method removes an element from the DOM?",
                    "explanation": "element.remove() removes the element.",
                    "options": [("element.delete()", False), ("element.remove()", True), ("element.hide()", False), ("element.destroy()", False)],
                },
            ],
        }
    ],
    "javascript-event-handling": [
        {
            "level": "medium",
            "title": "JavaScript Event Handling - Medium Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which method adds an event listener?",
                    "explanation": "addEventListener() attaches event handlers.",
                    "options": [("onClick()", False), ("addEventListener()", True), ("attachEvent()", False), ("listen()", False)],
                },
                {
                    "text": "What does event.preventDefault() do?",
                    "explanation": "It stops the default browser behavior.",
                    "options": [("Stops event propagation", False), ("Stops default browser behavior", True), ("Stops the event loop", False), ("Removes the element", False)],
                },
                {
                    "text": "What is event delegation?",
                    "explanation": "Attaching one listener to a parent to handle child events.",
                    "options": [("Adding multiple listeners to one element", False), ("Attaching one listener to a parent for child events", True), ("Removing all event listeners", False), ("Creating custom events", False)],
                },
            ],
        }
    ],
    "javascript-fetch-api": [
        {
            "level": "hard",
            "title": "JavaScript Fetch API - Hard Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "What does fetch() return?",
                    "explanation": "fetch() returns a Promise.",
                    "options": [("An array", False), ("A Promise", True), ("A string", False), ("An object", False)],
                },
                {
                    "text": "Which method parses a JSON response?",
                    "explanation": "response.json() parses the JSON body.",
                    "options": [("response.parse()", False), ("response.json()", True), ("response.text()", False), ("response.data()", False)],
                },
                {
                    "text": "How do you send a POST request with fetch?",
                    "explanation": "Pass method: 'POST' and body in options.",
                    "options": [("fetch(url, { method: 'POST', body: data })", True), ("fetch.post(url, data)", False), ("fetch(url, 'POST', data)", False), ("post(url, data)", False)],
                },
            ],
        }
    ],
    "javascript-promises": [
        {
            "level": "hard",
            "title": "JavaScript Promises - Hard Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "What are the three states of a Promise?",
                    "explanation": "Pending, fulfilled, and rejected.",
                    "options": [("Start, middle, end", False), ("Pending, fulfilled, rejected", True), ("Open, closed, error", False), ("Waiting, done, failed", False)],
                },
                {
                    "text": "Which method handles promise errors?",
                    "explanation": "catch() handles rejected promises.",
                    "options": [("then()", False), ("catch()", True), ("finally()", False), ("error()", False)],
                },
                {
                    "text": "What does Promise.all() do?",
                    "explanation": "It waits for all promises to resolve.",
                    "options": [("Waits for the first promise", False), ("Waits for all promises", True), ("Cancels all promises", False), ("Runs promises sequentially", False)],
                },
            ],
        }
    ],
    "javascript-async-await": [
        {
            "level": "hard",
            "title": "JavaScript Async/Await - Hard Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "What does the 'async' keyword do?",
                    "explanation": "It makes a function return a Promise.",
                    "options": [("Makes a function synchronous", False), ("Makes a function return a Promise", True), ("Makes a function faster", False), ("Makes a function recursive", False)],
                },
                {
                    "text": "What does 'await' do?",
                    "explanation": "It pauses execution until a Promise resolves.",
                    "options": [("Stops the function", False), ("Pauses until a Promise resolves", True), ("Returns immediately", False), ("Throws an error", False)],
                },
                {
                    "text": "How do you handle errors with async/await?",
                    "explanation": "Use try/catch blocks.",
                    "options": [("With .catch() only", False), ("With try/catch", True), ("With .error()", False), ("With finally only", False)],
                },
            ],
        }
    ],
    "javascript-es6-plus": [
        {
            "level": "hard",
            "title": "JavaScript ES6+ - Hard Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "What is destructuring?",
                    "explanation": "Extracting values from arrays/objects into variables.",
                    "options": [("Deleting variables", False), ("Extracting values into variables", True), ("Creating new objects", False), ("Merging arrays", False)],
                },
                {
                    "text": "What does the spread operator (...) do?",
                    "explanation": "It expands iterables into individual elements.",
                    "options": [("Combines functions", False), ("Expands iterables into elements", True), ("Creates promises", False), ("Sorts arrays", False)],
                },
                {
                    "text": "What is optional chaining (?.)?",
                    "explanation": "It safely accesses nested properties without errors.",
                    "options": [("Chains multiple functions", False), ("Safely accesses nested properties", True), ("Makes properties required", False), ("Combines objects", False)],
                },
            ],
        }
    ],
    "javascript-modules": [
        {
            "level": "hard",
            "title": "JavaScript Modules - Hard Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "Which keyword exports a single value by default?",
                    "explanation": "export default exports a single default value.",
                    "options": [("export default", True), ("export main", False), ("export single", False), ("export only", False)],
                },
                {
                    "text": "How do you import a default export?",
                    "explanation": "Import without curly braces for default exports.",
                    "options": [("import { main } from './module'", False), ("import main from './module'", True), ("import * as main from './module'", False), ("require('./module').main", False)],
                },
                {
                    "text": "What is the benefit of modules?",
                    "explanation": "Modules organize code and prevent global scope pollution.",
                    "options": [("They make code slower", False), ("They organize code and prevent scope pollution", True), ("They remove all errors", False), ("They replace components", False)],
                },
            ],
        }
    ],
    "javascript-projects": [
        {
            "level": "hard",
            "title": "JavaScript Projects - Hard Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "Which API is used to persist data in the browser?",
                    "explanation": "localStorage persists data in the browser.",
                    "options": [("sessionStorage only", False), ("localStorage", True), ("fetch API", False), ("DOM API", False)],
                },
                {
                    "text": "What is the best way to debug JavaScript?",
                    "explanation": "Using console.log and browser dev tools.",
                    "options": [("Guessing the error", False), ("Using console.log and dev tools", True), ("Rewriting the code", False), ("Ignoring errors", False)],
                },
            ],
        }
    ],
    "javascript-quiz": [
        {
            "level": "hard",
            "title": "JavaScript Comprehensive Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "What is the output of console.log(typeof NaN)?",
                    "explanation": "NaN is a number type in JavaScript.",
                    "options": [("'undefined'", False), ("'number'", True), ("'NaN'", False), ("'object'", False)],
                },
                {
                    "text": "Which method converts a JSON string to an object?",
                    "explanation": "JSON.parse() converts JSON strings to objects.",
                    "options": [("JSON.stringify()", False), ("JSON.parse()", True), ("JSON.toObject()", False), ("JSON.convert()", False)],
                },
                {
                    "text": "What is closure in JavaScript?",
                    "explanation": "A function that has access to its outer scope.",
                    "options": [("A function that closes the browser", False), ("A function with access to its outer scope", True), ("A function that returns nothing", False), ("A function that is private", False)],
                },
                {
                    "text": "What does the 'this' keyword refer to in a regular function?",
                    "explanation": "In a regular function, 'this' refers to the calling context.",
                    "options": [("Always the window object", False), ("The calling context", True), ("The function itself", False), ("Undefined always", False)],
                },
            ],
        }
    ],
    "react-introduction": [
        {
            "level": "easy",
            "title": "React Introduction - Easy Quiz",
            "passing_score": 60,
            "questions": [
                {
                    "text": "What is React?",
                    "explanation": "React is a JavaScript library for building user interfaces.",
                    "options": [("A database", False), ("A JavaScript library for building UIs", True), ("A CSS framework", False), ("A server", False)],
                },
                {
                    "text": "What is JSX?",
                    "explanation": "JSX is a syntax extension that looks like HTML in JavaScript.",
                    "options": [("A CSS preprocessor", False), ("A syntax extension for JavaScript", True), ("A database query language", False), ("A testing framework", False)],
                },
                {
                    "text": "What is a component in React?",
                    "explanation": "A component is a reusable piece of UI.",
                    "options": [("A CSS class", False), ("A reusable piece of UI", True), ("A JavaScript variable", False), ("An HTML file", False)],
                },
            ],
        }
    ],
    "react-jsx": [
        {
            "level": "easy",
            "title": "React JSX - Easy Quiz",
            "passing_score": 60,
            "questions": [
                {
                    "text": "Which attribute replaces 'class' in JSX?",
                    "explanation": "className is used instead of class in JSX.",
                    "options": [("class", False), ("className", True), ("classname", False), ("cssClass", False)],
                },
                {
                    "text": "How do you embed a JavaScript expression in JSX?",
                    "explanation": "Use curly braces {expression}.",
                    "options": [("${expression}", False), ("{expression}", True), ("{{expression}}", False), ("(expression)", False)],
                },
                {
                    "text": "What is a fragment in React?",
                    "explanation": "A fragment groups elements without adding a DOM node.",
                    "options": [("A broken component", False), ("Groups elements without a DOM node", True), ("A CSS class", False), ("A type of component", False)],
                },
            ],
        }
    ],
    "react-components": [
        {
            "level": "medium",
            "title": "React Components - Medium Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What is the recommended way to create components today?",
                    "explanation": "Functional components with hooks are recommended.",
                    "options": [("Class components", False), ("Functional components", True), ("Factory functions", False), ("HTML components", False)],
                },
                {
                    "text": "What is component composition?",
                    "explanation": "Combining smaller components to build larger ones.",
                    "options": [("Merging CSS files", False), ("Combining smaller components", True), ("Deleting components", False), ("Renaming components", False)],
                },
                {
                    "text": "What is a presentational component?",
                    "explanation": "A component focused on UI, not logic.",
                    "options": [("A component with complex logic", False), ("A component focused on UI", True), ("A component that fetches data", False), ("A component with state", False)],
                },
            ],
        }
    ],
    "react-props": [
        {
            "level": "medium",
            "title": "React Props - Medium Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "How do you pass data from parent to child?",
                    "explanation": "Data is passed via props.",
                    "options": [("Via state", False), ("Via props", True), ("Via CSS", False), ("Via localStorage", False)],
                },
                {
                    "text": "Can props be modified by the child component?",
                    "explanation": "Props are read-only and cannot be modified.",
                    "options": [("Yes, always", False), ("No, props are read-only", True), ("Only with useState", False), ("Only in class components", False)],
                },
                {
                    "text": "What is the children prop?",
                    "explanation": "It passes content between opening and closing tags.",
                    "options": [("A prop for child components only", False), ("Content between opening and closing tags", True), ("A prop for arrays", False), ("A prop for numbers", False)],
                },
            ],
        }
    ],
    "react-state": [
        {
            "level": "medium",
            "title": "React State - Medium Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which hook manages state in functional components?",
                    "explanation": "useState manages state in functional components.",
                    "options": [("useEffect", False), ("useState", True), ("useRef", False), ("useMemo", False)],
                },
                {
                    "text": "How do you update state?",
                    "explanation": "Use the setter function returned by useState.",
                    "options": [("Directly assign a new value", False), ("Use the setter function", True), ("Reload the page", False), ("Use a global variable", False)],
                },
                {
                    "text": "What is the initial value of useState(0)?",
                    "explanation": "The initial state value is 0.",
                    "options": [("null", False), ("0", True), ("undefined", False), ("false", False)],
                },
            ],
        }
    ],
    "react-hooks": [
        {
            "level": "medium",
            "title": "React Hooks - Medium Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which hook runs side effects?",
                    "explanation": "useEffect runs side effects after render.",
                    "options": [("useState", False), ("useEffect", True), ("useRef", False), ("useContext", False)],
                },
                {
                    "text": "What is the dependency array in useEffect?",
                    "explanation": "It controls when the effect re-runs.",
                    "options": [("It lists CSS classes", False), ("It controls when the effect re-runs", True), ("It stores state values", False), ("It defines component props", False)],
                },
                {
                    "text": "What is a custom hook?",
                    "explanation": "A function that uses other hooks to share logic.",
                    "options": [("A hook from React library", False), ("A function that uses other hooks", True), ("A CSS class", False), ("A type of component", False)],
                },
            ],
        }
    ],
    "react-routing": [
        {
            "level": "medium",
            "title": "React Routing - Medium Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which library handles routing in React?",
                    "explanation": "react-router-dom handles routing.",
                    "options": [("axios", False), ("react-router-dom", True), ("redux", False), ("express", False)],
                },
                {
                    "text": "Which hook gets URL parameters?",
                    "explanation": "useParams gets URL parameters.",
                    "options": [("useNavigate", False), ("useParams", True), ("useLocation", False), ("useRoute", False)],
                },
                {
                    "text": "What does <Link> do?",
                    "explanation": "<Link> navigates without reloading the page.",
                    "options": [("Reloads the page", False), ("Navigates without reloading", True), ("Fetches data", False), ("Renders a component", False)],
                },
            ],
        }
    ],
    "react-forms": [
        {
            "level": "hard",
            "title": "React Forms - Hard Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "What is a controlled component?",
                    "explanation": "Form inputs whose value is controlled by React state.",
                    "options": [("An input without state", False), ("Form inputs controlled by React state", True), ("A component with no props", False), ("A CSS-controlled input", False)],
                },
                {
                    "text": "How do you prevent form submission in React?",
                    "explanation": "Call e.preventDefault() in the submit handler.",
                    "options": [("Return false", False), ("Call e.preventDefault()", True), ("Stop the event loop", False), ("Use preventSubmit()", False)],
                },
                {
                    "text": "What is the onChange handler for?",
                    "explanation": "It updates state when input values change.",
                    "options": [("It changes CSS", False), ("It updates state when input changes", True), ("It submits the form", False), ("It validates the form", False)],
                },
            ],
        }
    ],
    "react-api-integration": [
        {
            "level": "hard",
            "title": "React API Integration - Hard Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "Where should you fetch data in a component?",
                    "explanation": "Inside useEffect to avoid infinite loops.",
                    "options": [("In the render method", False), ("Inside useEffect", True), ("In the JSX", False), ("Outside the component", False)],
                },
                {
                    "text": "What is the loading state pattern?",
                    "explanation": "Track loading with state and show a spinner.",
                    "options": [("Hide the component", False), ("Track loading with state and show a spinner", True), ("Use CSS animations", False), ("Block the page", False)],
                },
                {
                    "text": "Which library is commonly used for HTTP requests in React?",
                    "explanation": "Axios is a popular HTTP client.",
                    "options": [("jQuery", False), ("Axios", True), ("Lodash", False), ("Moment", False)],
                },
            ],
        }
    ],
    "react-projects": [
        {
            "level": "hard",
            "title": "React Projects - Hard Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "What should you plan first when building a React app?",
                    "explanation": "Plan the component structure first.",
                    "options": [("The CSS styles", False), ("The component structure", True), ("The deployment", False), ("The database", False)],
                },
                {
                    "text": "How do you persist data in a React app?",
                    "explanation": "Use localStorage or a backend API.",
                    "options": [("With CSS only", False), ("With localStorage or a backend API", True), ("With JSX only", False), ("With fragments", False)],
                },
            ],
        }
    ],
    "react-quiz": [
        {
            "level": "hard",
            "title": "React Comprehensive Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "What is the Virtual DOM?",
                    "explanation": "A lightweight copy of the real DOM for performance.",
                    "options": [("The real browser DOM", False), ("A lightweight copy of the DOM", True), ("A CSS framework", False), ("A database", False)],
                },
                {
                    "text": "What is the key prop used for?",
                    "explanation": "Keys help React identify items in lists.",
                    "options": [("For styling", False), ("To identify items in lists", True), ("For routing", False), ("For state management", False)],
                },
                {
                    "text": "What is lifting state up?",
                    "explanation": "Moving shared state to a common parent component.",
                    "options": [("Deleting state", False), ("Moving shared state to a common parent", True), ("Creating new state", False), ("Hiding state", False)],
                },
            ],
        }
    ],
    "python-introduction": [
        {
            "level": "easy",
            "title": "Python Introduction - Easy Quiz",
            "passing_score": 60,
            "questions": [
                {
                    "text": "Which command runs a Python file?",
                    "explanation": "python filename.py runs a Python script.",
                    "options": [("run filename.py", False), ("python filename.py", True), ("execute filename.py", False), ("start filename.py", False)],
                },
                {
                    "text": "How do you print output in Python?",
                    "explanation": "print() outputs to the console.",
                    "options": [("echo()", False), ("print()", True), ("console.log()", False), ("output()", False)],
                },
                {
                    "text": "What is Python known for?",
                    "explanation": "Python is known for its readability and simplicity.",
                    "options": [("Being the fastest language", False), ("Readability and simplicity", True), ("Being a markup language", False), ("Running only in browsers", False)],
                },
            ],
        }
    ],
    "python-variables": [
        {
            "level": "easy",
            "title": "Python Variables - Easy Quiz",
            "passing_score": 60,
            "questions": [
                {
                    "text": "Which of these is a valid variable name in Python?",
                    "explanation": "my_var follows snake_case convention.",
                    "options": [("2myvar", False), ("my_var", True), ("my-var", False), ("my var", False)],
                },
                {
                    "text": "What is the type of 3.14?",
                    "explanation": "3.14 is a float.",
                    "options": [("int", False), ("float", True), ("str", False), ("decimal", False)],
                },
                {
                    "text": "How do you convert a string to an integer?",
                    "explanation": "int() converts strings to integers.",
                    "options": [("integer()", False), ("int()", True), ("to_int()", False), ("parse_int()", False)],
                },
            ],
        }
    ],
    "python-functions": [
        {
            "level": "medium",
            "title": "Python Functions - Medium Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which keyword defines a function in Python?",
                    "explanation": "The def keyword defines functions.",
                    "options": [("function", False), ("def", True), ("func", False), ("define", False)],
                },
                {
                    "text": "What is a lambda function?",
                    "explanation": "An anonymous one-line function.",
                    "options": [("A named function", False), ("An anonymous one-line function", True), ("A recursive function", False), ("A class method", False)],
                },
                {
                    "text": "What does *args allow?",
                    "explanation": "It allows a variable number of positional arguments.",
                    "options": [("Keyword arguments only", False), ("A variable number of positional arguments", True), ("Default arguments", False), ("No arguments", False)],
                },
            ],
        }
    ],
    "python-lists": [
        {
            "level": "medium",
            "title": "Python Lists - Medium Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which method adds an item to the end of a list?",
                    "explanation": "append() adds to the end.",
                    "options": [("add()", False), ("append()", True), ("insert()", False), ("push()", False)],
                },
                {
                    "text": "What is list comprehension?",
                    "explanation": "A concise way to create lists.",
                    "options": [("A way to sort lists", False), ("A concise way to create lists", True), ("A way to delete lists", False), ("A way to merge lists", False)],
                },
                {
                    "text": "What is the result of [1, 2, 3][-1]?",
                    "explanation": "Negative indexing starts from the end, so -1 is 3.",
                    "options": [("1", False), ("3", True), ("2", False), ("Error", False)],
                },
            ],
        }
    ],
    "python-dictionaries": [
        {
            "level": "medium",
            "title": "Python Dictionaries - Medium Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which method safely gets a value with a default?",
                    "explanation": "get() returns a default if the key is missing.",
                    "options": [("value()", False), ("get()", True), ("fetch()", False), ("retrieve()", False)],
                },
                {
                    "text": "How do you add a new key-value pair?",
                    "explanation": "Assign to a new key: dict[key] = value.",
                    "options": [("dict.add(key, value)", False), ("dict[key] = value", True), ("dict.insert(key, value)", False), ("dict.push(key, value)", False)],
                },
                {
                    "text": "Which method returns all keys?",
                    "explanation": "keys() returns all dictionary keys.",
                    "options": [("values()", False), ("keys()", True), ("items()", False), ("all()", False)],
                },
            ],
        }
    ],
    "python-oop": [
        {
            "level": "hard",
            "title": "Python OOP - Hard Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "Which keyword defines a class in Python?",
                    "explanation": "The class keyword defines classes.",
                    "options": [("object", False), ("class", True), ("struct", False), ("type", False)],
                },
                {
                    "text": "What is the constructor method called?",
                    "explanation": "__init__ is the constructor method.",
                    "options": [("__construct__", False), ("__init__", True), ("__new__", False), ("init()", False)],
                },
                {
                    "text": "What is inheritance?",
                    "explanation": "A class inheriting attributes from another class.",
                    "options": [("Deleting a class", False), ("A class inheriting from another class", True), ("Creating multiple objects", False), ("Merging two classes", False)],
                },
            ],
        }
    ],
    "python-exception-handling": [
        {
            "level": "hard",
            "title": "Python Exception Handling - Hard Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "Which keyword catches exceptions?",
                    "explanation": "except catches exceptions.",
                    "options": [("catch", False), ("except", True), ("handle", False), ("rescue", False)],
                },
                {
                    "text": "What does finally do?",
                    "explanation": "finally always runs, whether or not an exception occurred.",
                    "options": [("Runs only on success", False), ("Always runs", True), ("Runs only on error", False), ("Never runs", False)],
                },
                {
                    "text": "How do you raise a custom exception?",
                    "explanation": "Use the raise keyword.",
                    "options": [("throw", False), ("raise", True), ("error()", False), ("except", False)],
                },
            ],
        }
    ],
    "python-modules": [
        {
            "level": "hard",
            "title": "Python Modules - Hard Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "Which keyword imports a module?",
                    "explanation": "import brings in modules.",
                    "options": [("include", False), ("import", True), ("require", False), ("use", False)],
                },
                {
                    "text": "How do you import a specific function?",
                    "explanation": "Use 'from module import function'.",
                    "options": [("import function from module", False), ("from module import function", True), ("require function", False), ("use function", False)],
                },
                {
                    "text": "What does if __name__ == '__main__' do?",
                    "explanation": "It runs code only when the file is executed directly.",
                    "options": [("Always runs the code", False), ("Runs only when executed directly", True), ("Never runs the code", False), ("Runs only when imported", False)],
                },
            ],
        }
    ],
    "python-projects": [
        {
            "level": "hard",
            "title": "Python Projects - Hard Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "Which library is used for data analysis?",
                    "explanation": "Pandas is the popular data analysis library.",
                    "options": [("Requests", False), ("Pandas", True), ("Flask", False), ("Django", False)],
                },
                {
                    "text": "What is the best way to organize a Python project?",
                    "explanation": "Use functions and modules to organize code.",
                    "options": [("Put everything in one file", False), ("Use functions and modules", True), ("Avoid functions", False), ("Use global variables", False)],
                },
            ],
        }
    ],
    "python-quiz": [
        {
            "level": "hard",
            "title": "Python Comprehensive Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "What is the output of print(2 ** 3)?",
                    "explanation": "** is exponentiation: 2 to the power of 3 = 8.",
                    "options": [("6", False), ("8", True), ("9", False), ("23", False)],
                },
                {
                    "text": "Which data type is immutable?",
                    "explanation": "Tuples are immutable.",
                    "options": [("List", False), ("Tuple", True), ("Dictionary", False), ("Set", False)],
                },
                {
                    "text": "What does the len() function do?",
                    "explanation": "len() returns the length of a sequence.",
                    "options": [("Sorts a list", False), ("Returns the length", True), ("Deletes items", False), ("Creates a list", False)],
                },
            ],
        }
    ],
    "fastapi-introduction": [
        {
            "level": "easy",
            "title": "FastAPI Introduction - Easy Quiz",
            "passing_score": 60,
            "questions": [
                {
                    "text": "What is FastAPI?",
                    "explanation": "FastAPI is a modern web framework for building APIs.",
                    "options": [("A database", False), ("A modern web framework for APIs", True), ("A CSS framework", False), ("A testing tool", False)],
                },
                {
                    "text": "Which command runs a FastAPI app?",
                    "explanation": "uvicorn main:app --reload runs the server.",
                    "options": [("python main.py", False), ("uvicorn main:app --reload", True), ("npm start", False), ("fastapi run", False)],
                },
                {
                    "text": "Where is the automatic API documentation?",
                    "explanation": "Swagger UI is at /docs.",
                    "options": [("/api-docs", False), ("/docs", True), ("/swagger", False), ("/documentation", False)],
                },
            ],
        }
    ],
    "fastapi-routing": [
        {
            "level": "medium",
            "title": "FastAPI Routing - Medium Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "How do you define a path parameter?",
                    "explanation": "Use curly braces: /users/{user_id}.",
                    "options": [("/users/:user_id", False), ("/users/{user_id}", True), ("/users/<user_id>", False), ("/users?user_id", False)],
                },
                {
                    "text": "What is a query parameter?",
                    "explanation": "Parameters in the URL after ?.",
                    "options": [("Parameters in the path", False), ("Parameters after ? in the URL", True), ("Parameters in the body", False), ("Parameters in headers", False)],
                },
                {
                    "text": "Which decorator handles GET requests?",
                    "explanation": "@app.get() handles GET requests.",
                    "options": [("@app.post()", False), ("@app.get()", True), ("@app.put()", False), ("@app.delete()", False)],
                },
            ],
        }
    ],
    "fastapi-request-response": [
        {
            "level": "medium",
            "title": "FastAPI Request & Response - Medium Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which library is used for data validation in FastAPI?",
                    "explanation": "Pydantic handles data validation.",
                    "options": [("SQLAlchemy", False), ("Pydantic", True), ("Jinja2", False), ("Requests", False)],
                },
                {
                    "text": "What does response_model do?",
                    "explanation": "It defines the response schema and filters fields.",
                    "options": [("It styles the response", False), ("It defines the response schema", True), ("It caches the response", False), ("It logs the response", False)],
                },
                {
                    "text": "How do you set a 201 status code?",
                    "explanation": "Use status_code=201 in the decorator.",
                    "options": [("return 201", False), ("status_code=201", True), ("response=201", False), ("code=201", False)],
                },
            ],
        }
    ],
    "fastapi-dependency-injection": [
        {
            "level": "hard",
            "title": "FastAPI Dependency Injection - Hard Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "Which module provides dependency injection?",
                    "explanation": "fastapi.Depends provides DI.",
                    "options": [("fastapi.Inject", False), ("fastapi.Depends", True), ("fastapi.Use", False), ("fastapi.Require", False)],
                },
                {
                    "text": "What is a common use of dependencies?",
                    "explanation": "Database sessions and authentication.",
                    "options": [("Styling responses", False), ("Database sessions and auth", True), ("Compiling code", False), ("Serving static files", False)],
                },
                {
                    "text": "How do you use a dependency in a route?",
                    "explanation": "Add it as a parameter with Depends().",
                    "options": [("db = Depends(get_db)", True), ("use(get_db)", False), ("inject(get_db)", False), ("require(get_db)", False)],
                },
            ],
        }
    ],
    "fastapi-authentication": [
        {
            "level": "hard",
            "title": "FastAPI Authentication - Hard Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "What does JWT stand for?",
                    "explanation": "JSON Web Token.",
                    "options": [("JavaScript Web Token", False), ("JSON Web Token", True), ("Java Web Token", False), ("JSON Web Tool", False)],
                },
                {
                    "text": "Which library is commonly used for password hashing?",
                    "explanation": "Passlib with bcrypt is common.",
                    "options": [("JWT", False), ("Passlib", True), ("Requests", False), ("Pydantic", False)],
                },
                {
                    "text": "What is OAuth2PasswordBearer used for?",
                    "explanation": "It extracts the bearer token from requests.",
                    "options": [("Hashing passwords", False), ("Extracting bearer tokens", True), ("Creating users", False), ("Sending emails", False)],
                },
            ],
        }
    ],
    "fastapi-background-tasks": [
        {
            "level": "hard",
            "title": "FastAPI Background Tasks - Hard Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "When do background tasks run?",
                    "explanation": "They run after the response is sent.",
                    "options": [("Before the request", False), ("After the response is sent", True), ("During the request", False), ("Never", False)],
                },
                {
                    "text": "Which class manages background tasks?",
                    "explanation": "fastapi.BackgroundTasks.",
                    "options": [("BackgroundTasks", True), ("TaskQueue", False), ("AsyncTasks", False), ("TaskManager", False)],
                },
                {
                    "text": "What is a common use case?",
                    "explanation": "Sending emails after registration.",
                    "options": [("Compiling code", False), ("Sending emails", True), ("Rendering HTML", False), ("Styling pages", False)],
                },
            ],
        }
    ],
    "fastapi-projects": [
        {
            "level": "hard",
            "title": "FastAPI Projects - Hard Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "Which database is easiest to start with in FastAPI?",
                    "explanation": "SQLite is simple and requires no setup.",
                    "options": [("PostgreSQL", False), ("SQLite", True), ("MongoDB", False), ("Redis", False)],
                },
                {
                    "text": "What should you add early in API development?",
                    "explanation": "Authentication should be added early.",
                    "options": [("CSS styles", False), ("Authentication", True), ("Animations", False), ("Static files", False)],
                },
            ],
        }
    ],
    "fastapi-quiz": [
        {
            "level": "hard",
            "title": "FastAPI Comprehensive Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "What is the default port for uvicorn?",
                    "explanation": "uvicorn defaults to port 8000.",
                    "options": [("3000", False), ("8000", True), ("5000", False), ("8080", False)],
                },
                {
                    "text": "Which decorator handles POST requests?",
                    "explanation": "@app.post() handles POST requests.",
                    "options": [("@app.get()", False), ("@app.post()", True), ("@app.put()", False), ("@app.delete()", False)],
                },
                {
                    "text": "What is the lifespan parameter used for?",
                    "explanation": "It runs startup and shutdown code.",
                    "options": [("For styling", False), ("For startup/shutdown code", True), ("For routing", False), ("For validation", False)],
                },
            ],
        }
    ],
}

COURSE_TOPICS["WoWCodes"] = WoWCodes_TOPICS

# Update QUIZ_TEMPLATES with imported quizzes
QUIZ_TEMPLATES.update(JS_QUIZZES)
QUIZ_TEMPLATES.update(NODEJS_QUIZZES)
QUIZ_TEMPLATES.update(EXPRESS_QUIZZES)
QUIZ_TEMPLATES.update(DATABASE_QUIZZES)
QUIZ_TEMPLATES.update(REDUX_QUIZZES)
QUIZ_TEMPLATES.update(GIT_AI_QUIZZES)
QUIZ_TEMPLATES.update(WoWCodes_QUIZZES)



def seed_courses(db: Session) -> None:
    """Create courses and topics."""
    for title, slug, desc, category, level, icon, color in COURSES:
        course = db.query(Course).filter(Course.slug == slug).first()
        if course is None:
            course = Course(
                title=title,
                slug=slug,
                description=desc,
                category=category,
                level=level,
                icon=icon,
                color=color,
                is_published=True,
                order=len(db.query(Course).all()) + 1,
            )
            db.add(course)
            db.flush()
        else:
            course.title = title
            course.description = desc
            course.category = category
            course.level = level
            course.icon = icon
            course.color = color

        # Topics
        for topic_title, topic_slug, topic_desc, topic_content in COURSE_TOPICS.get(slug, []):
            generated_content = generate_topic_content(
                topic_title,
                f"{slug}-{topic_slug}",
                topic_desc,
                fallback_content=topic_content,
            )
            existing = db.query(Topic).filter(Topic.slug == f"{slug}-{topic_slug}").first()
            if existing is None:
                topic = Topic(
                    course_id=course.id,
                    title=topic_title,
                    slug=f"{slug}-{topic_slug}",
                    description=topic_desc,
                    content=generated_content,
                    order=len(db.query(Topic).filter(Topic.course_id == course.id).all()) + 1,
                    estimated_minutes=15,
                )
                db.add(topic)
            else:
                # Update existing topic with new content
                existing.title = topic_title
                existing.description = topic_desc
                existing.content = generated_content
                existing.estimated_minutes = 15

    db.commit()


def seed_lessons(db: Session) -> None:
    """Create lessons for topics."""
    for course_slug, topics in COURSE_TOPICS.items():
        course = db.query(Course).filter(Course.slug == course_slug).first()
        if course is None:
            continue
        for topic_title, topic_slug, topic_desc, topic_content in topics:
            topic = db.query(Topic).filter(Topic.slug == f"{course_slug}-{topic_slug}").first()
            if topic is None:
                continue
            # Check if lessons already exist for this topic
            existing_count = db.query(Lesson).filter(Lesson.topic_id == topic.id).count()
            if existing_count > 0:
                continue

            # Create 2-3 lessons per topic from the content
            lines = topic_content.split("\n")
            lesson_titles = []
            lesson_contents = []

            # Extract sections from markdown content
            sections = []
            current_section = None
            for line in lines:
                if line.startswith("## "):
                    if current_section:
                        sections.append(current_section)
                    current_section = {"title": line[3:].strip(), "content": []}
                elif current_section:
                    current_section["content"].append(line)

            if current_section:
                sections.append(current_section)

            if not sections:
                # Fallback: create a single lesson
                sections = [{"title": topic_title, "content": topic_content.split("\n")}]

            for idx, section in enumerate(sections[:3]):
                lesson = Lesson(
                    course_id=course.id,
                    topic_id=topic.id,
                    title=section["title"],
                    content="\n".join(section["content"]).strip(),
                    order=idx,
                    is_published=True,
                )
                db.add(lesson)

    db.commit()


def seed_quizzes(db: Session) -> None:
    """Create or update quizzes for existing topics with full questions."""
    for topic_slug, quizzes in QUIZ_TEMPLATES.items():
        topic = db.query(Topic).filter(Topic.slug.endswith(topic_slug) | (Topic.slug == topic_slug)).first()
        if topic is None:
            continue
        for quiz_data in quizzes:
            quiz = db.query(Quiz).filter(
                Quiz.topic_id == topic.id,
                Quiz.level == quiz_data["level"],
            ).first()
            if not quiz:
                quiz = Quiz(
                    topic_id=topic.id,
                    title=quiz_data["title"],
                    level=quiz_data["level"],
                    description=f"Test your knowledge of {topic.title}.",
                    passing_score=quiz_data["passing_score"],
                    time_limit_minutes=15,
                )
                db.add(quiz)
                db.flush()
            else:
                quiz.title = quiz_data["title"]
                # Delete any legacy placeholder questions for this quiz
                old_qs = db.query(Question).filter(
                    Question.quiz_id == quiz.id,
                    Question.text.like('%Which statement best reflects%')
                ).all()
                for oq in old_qs:
                    db.query(Option).filter(Option.question_id == oq.id).delete()
                    db.delete(oq)
                db.flush()

            # Ensure all 10 real questions are added
            for q_idx, q in enumerate(quiz_data["questions"]):
                existing_q = db.query(Question).filter(
                    Question.quiz_id == quiz.id,
                    Question.text == q["text"],
                ).first()
                if not existing_q:
                    question = Question(
                        quiz_id=quiz.id,
                        text=q["text"],
                        explanation=q.get("explanation", ""),
                        points=10,
                        order=q_idx,
                    )
                    db.add(question)
                    db.flush()
                    for opt_idx, (text, correct) in enumerate(q["options"]):
                        db.add(Option(
                            question_id=question.id,
                            text=text,
                            is_correct=correct,
                            order=opt_idx,
                        ))
    db.commit()


def seed():
    """Run all seeders."""
    init_db()
    db = SessionLocal()
    try:
        # Roles
        for name, desc in [
            ("student", "Student role"),
            ("instructor", "Instructor role"),
            ("admin", "Administrator role"),
        ]:
            if not db.query(Role).filter(Role.name == name).first():
                db.add(Role(name=name, description=desc))
        db.commit()

        # Admin + Instructor users
        admin_role = db.query(Role).filter(Role.name == "admin").first()
        instructor_role = db.query(Role).filter(Role.name == "instructor").first()

        if admin_role and not db.query(User).filter(User.email == "admin@wowcodes.com").first():
            db.add(User(
                email="admin@wowcodes.com",
                username="admin",
                full_name="Admin User",
                hashed_password=hash_password("admin123"),
                role_id=admin_role.id,
                is_active=True,
                is_verified=True,
            ))
        if instructor_role and not db.query(User).filter(User.email == "instructor@wowcodes.com").first():
            db.add(User(
                email="instructor@wowcodes.com",
                username="instructor",
                full_name="Instructor",
                hashed_password=hash_password("instructor123"),
                role_id=instructor_role.id,
                is_active=True,
                is_verified=True,
            ))
        db.commit()

        # Courses, topics, lessons, quizzes
        seed_courses(db)
        seed_lessons(db)
        seed_quizzes(db)

        print("=" * 50)
        print("Seed data created successfully!")
        print("=" * 50)
        print("Admin login:      admin@wowcodes.com / admin123")
        print("Instructor login: instructor@wowcodes.com / instructor123")
        print("=" * 50)
    finally:
        db.close()


if __name__ == "__main__":
    seed()