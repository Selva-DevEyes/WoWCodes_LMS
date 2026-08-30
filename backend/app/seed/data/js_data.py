"""JavaScript course topics and quizzes seed data."""

JS_TOPICS = [
    ("Variables", "variables", "var, let, const, block scope, and temporal dead zone", """# JavaScript Variables

Variables are containers for storing data values. In modern JavaScript, variable declaration is a fundamental concept.

## Declaring Variables

JavaScript provides three keywords to declare variables:

- `const`: Block-scoped. Cannot be reassigned. Use by default.
- `let`: Block-scoped. Can be reassigned. Use when values change.
- `var`: Function-scoped or global. Hoisted with `undefined`. Avoid in modern code.

```javascript
const maxUsers = 100;
let currentScore = 0;
currentScore += 10;

// Re-assigning a const variable throws a TypeError:
// maxUsers = 200; // Error!
```

## Scope and Temporal Dead Zone (TDZ)

`let` and `const` declarations are block-scoped and remain in the **Temporal Dead Zone (TDZ)** from the start of the block until the declaration line is executed.

```javascript
{
  // TDZ for user
  // console.log(user); // ReferenceError
  const user = 'Alice';
  console.log(user); // 'Alice'
}
```

## Best Practices

- Prefer `const` for all declarations unless re-assignment is required.
- Use `let` for loop iterators and mutable accumulators.
- Avoid global variable declarations to prevent namespace pollution.
"""),

    ("Data Types", "data-types", "Primitive vs Reference types, typeof, and type coercion", """# JavaScript Data Types

JavaScript is a dynamically typed language. Types are divided into primitives and objects.

## Primitive Types

Primitives are immutable values passed by value:

- `string`: `"Hello World"`
- `number`: `42`, `3.14`, `NaN`, `Infinity`
- `boolean`: `true` or `false`
- `null`: Intentional absence of value
- `undefined`: Variable declared but not assigned
- `symbol`: Unique identifier (`Symbol('id')`)
- `bigint`: Large integers (`9007199254740991n`)

```javascript
const age = 25;
const name = "John";
const isStudent = true;
const data = null;
let x; // undefined
```

## Reference Types (Objects)

Objects, arrays, and functions are reference types passed by reference:

```javascript
const obj1 = { name: "Alice" };
const obj2 = obj1;
obj2.name = "Bob";
console.log(obj1.name); // "Bob"
```

## Type Checking & Coercion

Use `typeof` to check primitive types. Note that `typeof null === 'object'` is a historical language quirk.

```javascript
typeof "text"; // "string"
typeof 100;    // "number"
typeof true;   // "boolean"
typeof {};     // "object"
typeof [];     // "object" -> use Array.isArray([])
```
"""),

    ("Operators", "operators", "Arithmetic, comparison, logical, and nullish coalescing operators", """# JavaScript Operators

Operators allow you to manipulate variables and values.

## Arithmetic & Assignment Operators

```javascript
let count = 10;
count += 5;   // 15
count *= 2;   // 30
const remainder = count % 4; // 2
const power = 2 ** 3;        // 8
```

## Strict vs Loose Equality

Always use strict equality (`===` and `!==`) to prevent unexpected type coercion.

```javascript
5 == "5";  // true (loose - coerces type)
5 === "5"; // false (strict - checks type and value)
```

## Logical & Nullish Coalescing

- `&&` (AND): Returns first falsy or last truthy value.
- `||` (OR): Returns first truthy or last value.
- `??` (Nullish Coalescing): Returns right-hand value only if left is `null` or `undefined`.

```javascript
const input = "";
const name1 = input || "Guest"; // "Guest" (falsy check)
const name2 = input ?? "Guest"; // "" (nullish check)
```
"""),

    ("Arrays", "arrays", "Array methods: map, filter, reduce, slice, splice", """# JavaScript Arrays

Arrays are ordered collections of values with rich built-in methods.

## Essential Array Methods

```javascript
const numbers = [1, 2, 3, 4, 5];

// map: transform elements
const doubled = numbers.map(num => num * 2); // [2, 4, 6, 8, 10]

// filter: extract matching elements
const evens = numbers.filter(num => num % 2 === 0); // [2, 4]

// reduce: accumulate to single value
const sum = numbers.reduce((acc, curr) => acc + curr, 0); // 15
```

## Mutating vs Non-Mutating Methods

- **Mutating**: `push()`, `pop()`, `shift()`, `unshift()`, `splice()`, `sort()`
- **Non-mutating**: `map()`, `filter()`, `slice()`, `concat()`, `toSorted()`

```javascript
const fruits = ["Apple", "Banana", "Cherry"];

// Immutable slice
const sub = fruits.slice(0, 2); // ["Apple", "Banana"]
console.log(fruits); // Original unchanged
```
"""),

    ("Objects", "objects", "Literals, dynamic keys, destructuring, and Object methods", """# JavaScript Objects

Objects are collections of key-value pairs used to store structured data.

## Creating & Accessing Objects

```javascript
const user = {
  id: 101,
  name: "Sarah",
  role: "Developer",
  greet() {
    return `Hi, I am ${this.name}`;
  }
};

// Bracket notation for dynamic keys
const key = "role";
console.log(user[key]); // "Developer"
```

## Destructuring & Spread

```javascript
const { name, role } = user;
console.log(name, role); // "Sarah", "Developer"

// Object spreading
const updatedUser = { ...user, role: "Senior Developer", active: true };
```

## Useful Object Methods

- `Object.keys(obj)`: Returns array of keys.
- `Object.values(obj)`: Returns array of values.
- `Object.entries(obj)`: Returns key-value pairs array.
- `Object.freeze(obj)`: Prevents mutation.
"""),

    ("Loops", "loops", "for, while, for...of, and for...in loops", """# JavaScript Loops

Loops execute a code block repeatedly until a specified condition is met.

## Standard for and while Loops

```javascript
for (let i = 0; i < 5; i++) {
  console.log(`Index: ${i}`);
}

let count = 3;
while (count > 0) {
  console.log(`Countdown: ${count}`);
  count--;
}
```

## for...of vs for...in

- `for...of`: Iterates over iterable values (Arrays, Strings, Sets, Maps).
- `for...in`: Iterates over enumerable object keys.

```javascript
const colors = ["Red", "Green", "Blue"];
for (const color of colors) {
  console.log(color); // "Red", "Green", "Blue"
}

const person = { name: "Alex", age: 30 };
for (const prop in person) {
  console.log(`${prop}: ${person[prop]}`);
}
```
"""),

    ("Functions", "functions", "Declarations, expressions, default and rest parameters", """# JavaScript Functions

Functions are building blocks of code that execute reusable operations.

## Declarations vs Expressions

```javascript
// Function Declaration (Hoisted)
function add(a, b) {
  return a + b;
}

// Function Expression (Not hoisted)
const multiply = function(a, b) {
  return a * b;
};
```

## Default & Rest Parameters

```javascript
// Default parameters
function greet(name = "Guest") {
  return `Hello, ${name}!`;
}

// Rest parameters (...args)
function sumAll(...numbers) {
  return numbers.reduce((total, n) => total + n, 0);
}

console.log(sumAll(10, 20, 30)); // 60
```
"""),

    ("Arrow Functions", "arrow-functions", "Syntax, implicit returns, and lexical this binding", """# Arrow Functions

Arrow functions provide a concise syntax introduced in ES6.

## Syntax Comparison

```javascript
// Standard function
const square1 = function(n) {
  return n * n;
};

// Arrow function (implicit return)
const square2 = n => n * n;
```

## Lexical `this` Binding

Arrow functions do NOT have their own `this`. They inherit `this` from their enclosing execution context.

```javascript
const timer = {
  seconds: 0,
  start() {
    setInterval(() => {
      this.seconds++; // Inherits 'this' from timer object
      console.log(this.seconds);
    }, 1000);
  }
};
```

## When NOT to use Arrow Functions

- Object methods requiring `this` binding.
- Constructor functions (arrow functions cannot be called with `new`).
- Event listeners where `this` should point to the DOM element.
"""),

    ("Scope", "scope", "Global, function, block, and lexical scope", """# JavaScript Scope

Scope determines the accessibility and visibility of variables in your code.

## Types of Scope

1. **Global Scope**: Accessible everywhere.
2. **Function Scope**: Variables declared inside a function with `var`.
3. **Block Scope**: Variables declared inside `{}` with `let` or `const`.
4. **Lexical Scope**: Inner functions can access variables from outer functions.

```javascript
const globalVar = "I am global";

function outer() {
  const outerVar = "I am outer";

  function inner() {
    const innerVar = "I am inner";
    console.log(globalVar, outerVar, innerVar); // All accessible
  }

  inner();
}
```
"""),

    ("Hoisting", "hoisting", "Hoisting behavior of var, let, const, and function declarations", """# JavaScript Hoisting

Hoisting is JavaScript's default behavior of moving declarations to the top of their current scope during compilation.

## Function Hoisting

Function declarations are completely hoisted, allowing them to be invoked before their definition in code.

```javascript
sayHello(); // Works!

function sayHello() {
  console.log("Hello from hoisted function!");
}
```

## Variable Hoisting

- `var`: Hoisted and initialized with `undefined`.
- `let` and `const`: Hoisted but NOT initialized (Temporal Dead Zone).

```javascript
console.log(a); // undefined
var a = 10;

// console.log(b); // ReferenceError! (TDZ)
let b = 20;
```
"""),

    ("Closures", "closures", "Lexical environment retention, data privacy, and practical patterns", """# JavaScript Closures

A closure is a function that retains access to its lexical scope even when the function is executed outside that scope.

## How Closures Work

```javascript
function createCounter() {
  let count = 0; // Private state

  return {
    increment() {
      count++;
      return count;
    },
    decrement() {
      count--;
      return count;
    },
    getCount() {
      return count;
    }
  };
}

const counter = createCounter();
console.log(counter.increment()); // 1
console.log(counter.increment()); // 2
console.log(counter.getCount());   // 2
```

## Practical Uses of Closures

- Private data encapsulation.
- Function currying & memoization.
- Event handler configuration.
"""),

    ("Callbacks", "callbacks", "Higher-order functions, async callbacks, and callback hell", """# JavaScript Callbacks

A callback is a function passed as an argument to another function to be executed later.

## Synchronous vs Asynchronous Callbacks

```javascript
// Synchronous callback
const nums = [1, 2, 3];
nums.forEach(n => console.log(n * 2));

// Asynchronous callback
setTimeout(() => {
  console.log("Executed after 1 second");
}, 1000);
```

## Callback Hell & Error-First Pattern

Node.js traditionally uses error-first callbacks: `(err, data) => {}`. Nesting multiple async callbacks leads to unmaintainable code known as **Callback Hell**, which is solved using Promises.
"""),

    ("Promises", "promises", "Promise states, chaining, and static methods", """# JavaScript Promises

A Promise represents the eventual completion (or failure) of an asynchronous operation and its resulting value.

## Promise States

- **Pending**: Initial state, neither fulfilled nor rejected.
- **Fulfilled**: Operation completed successfully (`resolve()`).
- **Rejected**: Operation failed (`reject()`).

```javascript
const fetchData = new Promise((resolve, reject) => {
  setTimeout(() => {
    const success = true;
    if (success) {
      resolve({ id: 1, name: "Data" });
    } else {
      reject(new Error("Fetch failed"));
    }
  }, 1000);
});

fetchData
  .then(data => console.log(data))
  .catch(err => console.error(err.message))
  .finally(() => console.log("Done"));
```

## Promise Methods

- `Promise.all([p1, p2])`: Fails fast if any promise rejects.
- `Promise.allSettled([p1, p2])`: Waits for all promises to finish regardless of outcome.
- `Promise.race([p1, p2])`: Resolves/rejects with the first settled promise.
"""),

    ("async/await", "async/await", "Syntactic sugar for Promises, try/catch error handling", """# async/await in JavaScript

`async` and `await` enable asynchronous, promise-based code to be written in a clean, synchronous-looking style.

## Basic Syntax

```javascript
async function getUserData(userId) {
  try {
    const response = await fetch(`https://api.example.com/users/${userId}`);
    if (!response.ok) {
      throw new Error(`HTTP Error: ${response.status}`);
    }
    const user = await response.json();
    return user;
  } catch (error) {
    console.error("Failed to fetch user:", error.message);
    throw error;
  }
}
```

## Parallel Execution with `Promise.all`

Avoid sequential `await` calls when requests are independent:

```javascript
// Parallel execution
const [user, posts] = await Promise.all([
  fetchUser(id),
  fetchPosts(id)
]);
```
"""),

    ("ES6+ Features", "es6-plus", "Destructuring, spread operator, optional chaining, nullish coalescing", """# ES6+ Modern Features

Modern JavaScript offers elegant syntax additions that make code cleaner and more resilient.

## Destructuring & Rest/Spread

```javascript
const user = { name: "Emma", age: 28, city: "London" };
const { name, ...rest } = user; // rest = { age: 28, city: "London" }

const arr1 = [1, 2];
const arr2 = [...arr1, 3, 4]; // [1, 2, 3, 4]
```

## Optional Chaining (`?.`) & Nullish Coalescing (`??`)

```javascript
const response = {
  user: {
    profile: {
      avatar: "avatar.jpg"
    }
  }
};

// Safe deep property access
const avatar = response?.user?.profile?.avatar ?? "default.jpg";
console.log(avatar); // "avatar.jpg"
```
"""),

    ("Modules", "modules", "ES Modules (import/export), default vs named exports", """# JavaScript Modules

Modules break up code into reusable, isolated files.

## Exporting & Importing

```javascript
// math.js - Named exports
export const add = (a, b) => a + b;
export const multiply = (a, b) => a * b;

// logger.js - Default export
export default function log(msg) {
  console.log(`[LOG]: ${msg}`);
}
```

```javascript
// main.js - Importing
import log from './logger.js';
import { add, multiply as mult } from './math.js';

log(`Result: ${add(5, 10)}`);
```
"""),

    ("Error Handling", "error-handling", "try...catch...finally, custom Error classes", """# JavaScript Error Handling

Robust applications handle runtime exceptions gracefully without crashing.

## The try...catch...finally Block

```javascript
try {
  const data = JSON.parse("{ invalid json }");
} catch (error) {
  console.error("JSON Parsing failed:", error.name, error.message);
} finally {
  console.log("Cleanup executed regardless of error");
}
```

## Creating Custom Errors

```javascript
class ValidationError extends Error {
  constructor(message) {
    super(message);
    this.name = "ValidationError";
  }
}

function validateAge(age) {
  if (age < 0) {
    throw new ValidationError("Age cannot be negative");
  }
}
```
"""),

    ("DOM & Event Handling", "dom", "DOM selection, manipulation, addEventListener, bubbling", """# DOM & Event Handling

The Document Object Model (DOM) represents web pages as a tree structure of objects.

## Selecting & Modifying Elements

```javascript
const title = document.querySelector("#main-title");
title.textContent = "Updated Page Title";
title.classList.add("highlight");
```

## Event Listeners & Event Delegation

```javascript
const button = document.querySelector("#btn");
button.addEventListener("click", (event) => {
  event.preventDefault();
  console.log("Button clicked!");
});

// Event Delegation on parent
const list = document.querySelector("#item-list");
list.addEventListener("click", (e) => {
  if (e.target.tagName === "LI") {
    console.log("Clicked item:", e.target.textContent);
  }
});
```
""")
]

JS_QUIZZES = {
    "javascript-variables": [
        {
            "level": "easy",
            "title": "JavaScript Variables Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which variable declaration keyword creates a block-scoped variable that CANNOT be reassigned?",
                    "explanation": "const creates block-scoped variables that cannot be reassigned.",
                    "options": [("let", False), ("var", False), ("const", True), ("def", False)],
                },
                {
                    "text": "What happens if you access a let variable before its declaration in its block?",
                    "explanation": "Accessing let or const before declaration throws a ReferenceError due to the Temporal Dead Zone (TDZ).",
                    "options": [("Returns undefined", False), ("Throws a ReferenceError", True), ("Returns null", False), ("Returns 0", False)],
                },
                {
                    "text": "What scope do variables declared with 'var' possess?",
                    "explanation": "var variables are function-scoped or globally scoped, but NOT block-scoped.",
                    "options": [("Block scope", False), ("Function or Global scope", True), ("Module scope only", False), ("Package scope", False)],
                },
            ],
        }
    ],
    "javascript-data-types": [
        {
            "level": "easy",
            "title": "Data Types Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does typeof null evaluate to in JavaScript?",
                    "explanation": "typeof null returns 'object', which is a famous historical bug in JavaScript.",
                    "options": [("'null'", False), ("'undefined'", False), ("'object'", True), ("'boolean'", False)],
                },
                {
                    "text": "Which of the following is a primitive data type in JavaScript?",
                    "explanation": "Symbol is a primitive data type along with string, number, boolean, null, undefined, and bigint.",
                    "options": [("Array", False), ("Symbol", True), ("Object", False), ("Date", False)],
                },
                {
                    "text": "How should you correctly check if a value 'arr' is an Array?",
                    "explanation": "Array.isArray(arr) is the reliable standard way to check if a value is an array.",
                    "options": [("typeof arr === 'array'", False), ("arr.type === 'array'", False), ("Array.isArray(arr)", True), ("arr instanceof String", False)],
                },
            ],
        }
    ],
    "javascript-operators": [
        {
            "level": "medium",
            "title": "JavaScript Operators Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What is the result of 5 === '5'?",
                    "explanation": "Strict equality (===) checks both value and data type without implicit conversion, so number 5 is not equal to string '5'.",
                    "options": [("true", False), ("false", True), ("undefined", False), ("TypeError", False)],
                },
                {
                    "text": "What does the Nullish Coalescing Operator (??) check for?",
                    "explanation": "?? returns the right-hand operand only when the left-hand operand is null or undefined.",
                    "options": [("Falsy values (0, '', false)", False), ("null or undefined only", True), ("Empty arrays", False), ("Boolean values", False)],
                },
                {
                    "text": "What is the value of: const x = '' || 'Default'?",
                    "explanation": "Logical OR (||) treats empty string '' as falsy, returning 'Default'.",
                    "options": [("''", False), ("'Default'", True), ("null", False), ("false", False)],
                },
            ],
        }
    ],
    "javascript-arrays": [
        {
            "level": "medium",
            "title": "JavaScript Arrays Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which array method creates a NEW array populated with the results of calling a provided function on every element?",
                    "explanation": "map() returns a new array transformed by the callback function.",
                    "options": [("forEach()", False), ("map()", True), ("filter()", False), ("reduce()", False)],
                },
                {
                    "text": "Does slice() mutate the original array?",
                    "explanation": "No, slice() returns a shallow copy of a portion of the array without modifying the original.",
                    "options": [("Yes, always", False), ("No, slice() is immutable", True), ("Only when removing elements", False), ("Only in strict mode", False)],
                },
                {
                    "text": "What does array.reduce((acc, curr) => acc + curr, 0) calculate for an array of numbers?",
                    "explanation": "It sums up all elements in the array starting from initial value 0.",
                    "options": [("The average", False), ("The sum of all numbers", True), ("The largest number", False), ("Filter even numbers", False)],
                },
            ],
        }
    ],
    "javascript-objects": [
        {
            "level": "medium",
            "title": "JavaScript Objects Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which Object method returns an array of a given object's own enumerable property names?",
                    "explanation": "Object.keys(obj) returns an array containing the keys of the object.",
                    "options": [("Object.values()", False), ("Object.keys()", True), ("Object.entries()", False), ("Object.getNames()", False)],
                },
                {
                    "text": "How do you dynamically access an object property stored in a variable `key`?",
                    "explanation": "Bracket notation `obj[key]` evaluates the variable `key` dynamically.",
                    "options": [("obj.key", False), ("obj[key]", True), ("obj->key", False), ("obj::key", False)],
                },
            ],
        }
    ],
    "javascript-loops": [
        {
            "level": "easy",
            "title": "Loops Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which loop statement is specifically designed to iterate over iterable values like Arrays?",
                    "explanation": "for...of loops iterate over iterable objects such as Arrays, Strings, Maps, and Sets.",
                    "options": [("for...in", False), ("for...of", True), ("while", False), ("do...while", False)],
                },
                {
                    "text": "What is the key difference between a while loop and a do...while loop?",
                    "explanation": "A do...while loop always executes its body at least once before testing the condition.",
                    "options": [("while runs at least once", False), ("do...while runs at least once", True), ("They are identical", False), ("for...of is faster", False)],
                },
            ],
        }
    ],
    "javascript-functions": [
        {
            "level": "easy",
            "title": "Functions Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "How do you define rest parameters in a function signature?",
                    "explanation": "Rest parameters use three dots prefixing an array name, e.g., ...args.",
                    "options": [("args[]", False), ("...args", True), ("*args", False), ("&args", False)],
                },
                {
                    "text": "What is a pure function?",
                    "explanation": "A pure function given the same inputs always returns the same output without causing side effects.",
                    "options": [("A function with no arguments", False), ("A function with no side effects that returns deterministic output", True), ("An arrow function", False), ("A function inside an object", False)],
                },
            ],
        }
    ],
    "javascript-arrow-functions": [
        {
            "level": "medium",
            "title": "Arrow Functions Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "How do arrow functions handle the 'this' keyword?",
                    "explanation": "Arrow functions do not have their own 'this'; they lexically inherit 'this' from the outer scope.",
                    "options": [("They bind 'this' to window always", False), ("They lexically inherit 'this' from enclosing scope", True), ("They reset 'this' to undefined", False), ("They dynamically bind 'this'", False)],
                },
                {
                    "text": "Can an arrow function be called with the 'new' keyword as a constructor?",
                    "explanation": "No, arrow functions lack [[Construct]] internal method and cannot be constructors.",
                    "options": [("Yes", False), ("No, it throws a TypeError", True), ("Only if uppercase", False), ("Only in Node.js", False)],
                },
            ],
        }
    ],
    "javascript-scope": [
        {
            "level": "medium",
            "title": "Scope Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which declarations create block-scoped variables in JavaScript?",
                    "explanation": "let and const create block-scoped variables restricted to their enclosing block {}.",
                    "options": [("var and let", False), ("let and const", True), ("var only", False), ("const and var", False)],
                },
                {
                    "text": "What is Lexical Scope?",
                    "explanation": "Lexical scope means variable access is determined by physical position in source code at compile time.",
                    "options": [("Runtime dynamic scope", False), ("Scope determined by physical code structure", True), ("Global scope only", False), ("Browser-only scope", False)],
                },
            ],
        }
    ],
    "javascript-hoisting": [
        {
            "level": "medium",
            "title": "Hoisting Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What value does a hoisted 'var' variable have before initialization?",
                    "explanation": "var declarations are hoisted and initialized with 'undefined'.",
                    "options": [("null", False), ("undefined", True), ("0", False), ("ReferenceError", False)],
                },
                {
                    "text": "What is the Temporal Dead Zone (TDZ)?",
                    "explanation": "The TDZ is the period between entering scope and reaching line of declaration for let/const variables.",
                    "options": [("A garbage collection process", False), ("The state where let/const exist but cannot be accessed", True), ("An asynchronous wait time", False), ("A memory leak state", False)],
                },
            ],
        }
    ],
    "javascript-closures": [
        {
            "level": "hard",
            "title": "Closures Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "What is a closure in JavaScript?",
                    "explanation": "A closure is a function combined with references to its surrounding lexical environment.",
                    "options": [("A loop that never terminates", False), ("A function that retains access to its outer scope variables", True), ("A method to close browser tabs", False), ("A database transaction", False)],
                },
                {
                    "text": "Which common pattern relies on closures for data encapsulation?",
                    "explanation": "Module patterns and private variables rely heavily on closures.",
                    "options": [("Singleton pattern", False), ("Module pattern with private state", True), ("Prototype pattern", False), ("Factory pattern only", False)],
                },
            ],
        }
    ],
    "javascript-callbacks": [
        {
            "level": "medium",
            "title": "Callbacks Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What is Callback Hell?",
                    "explanation": "Callback Hell describes deeply nested asynchronous callbacks making code hard to read and maintain.",
                    "options": [("A runtime syntax error", False), ("Deeply nested asynchronous callbacks", True), ("A missing return statement", False), ("An infinite loop", False)],
                },
                {
                    "text": "What is the standard error-first callback signature in Node.js?",
                    "explanation": "The convention is (err, result) where error is passed as the first parameter.",
                    "options": [("(result, err)", False), ("(err, result)", True), ("(data)", False), ("(status, err)", False)],
                },
            ],
        }
    ],
    "javascript-promises": [
        {
            "level": "medium",
            "title": "Promises Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which method is used to handle rejections in a Promise chain?",
                    "explanation": ".catch() handles errors and rejected promises in a chain.",
                    "options": [(".then()", False), (".catch()", True), (".finally()", False), (".reject()", False)],
                },
                {
                    "text": "What does Promise.all() do when ONE promise in the array rejects?",
                    "explanation": "Promise.all() rejects immediately (fast-fails) with the reason of the first rejected promise.",
                    "options": [("Ignores the error", False), ("Rejects immediately with that error", True), ("Waits for remaining promises", False), ("Returns null", False)],
                },
            ],
        }
    ],
    "javascript-async-await": [
        {
            "level": "hard",
            "title": "async/await Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "What type of value does an async function ALWAYS return?",
                    "explanation": "An async function implicitly wraps return values in a Promise.",
                    "options": [("The raw value", False), ("A Promise", True), ("undefined", False), ("A callback", False)],
                },
                {
                    "text": "How should errors be caught inside an async function?",
                    "explanation": "Using try...catch blocks around await calls.",
                    "options": [("With if/else", False), ("Using try...catch blocks", True), ("With onError listeners", False), ("Using process.catch", False)],
                },
            ],
        }
    ],
    "javascript-es6-plus": [
        {
            "level": "medium",
            "title": "ES6+ Features Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does optional chaining (`obj?.prop`) prevent?",
                    "explanation": "It short-circuits and returns undefined instead of throwing a TypeError if obj is null or undefined.",
                    "options": [("Syntax errors", False), ("TypeError when evaluating null or undefined properties", True), ("Memory leaks", False), ("Infinite recursion", False)],
                },
            ],
        }
    ],
    "javascript-modules": [
        {
            "level": "easy",
            "title": "Modules Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "How many default exports can a single JavaScript module file have?",
                    "explanation": "A module can have at most ONE default export.",
                    "options": [("Multiple", False), ("Exactly one", True), ("Zero only", False), ("Unlimited", False)],
                },
            ],
        }
    ],
    "javascript-error-handling": [
        {
            "level": "medium",
            "title": "Error Handling Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Does the 'finally' block execute if an error is thrown and caught in 'try...catch'?",
                    "explanation": "Yes, the finally block ALWAYS executes regardless of whether an error occurred or was caught.",
                    "options": [("No, only on success", False), ("Yes, finally always executes", True), ("Only if re-thrown", False), ("Only in Node.js", False)],
                },
            ],
        }
    ],
    "javascript-dom": [
        {
            "level": "medium",
            "title": "DOM & Events Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What is Event Delegation?",
                    "explanation": "Attaching a single event listener to a parent element to handle events on descendant elements via event bubbling.",
                    "options": [("Removing event listeners", False), ("Attaching a single listener to a parent to manage child events", True), ("Preventing event bubbling", False), ("Triggering fake events", False)],
                },
            ],
        }
    ],
}
