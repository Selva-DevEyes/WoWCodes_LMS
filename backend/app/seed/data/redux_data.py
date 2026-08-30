"""Redux course topics and quizzes seed data."""

REDUX_TOPICS = [
    ("Redux Fundamentals", "redux-fundamentals", "Three principles of Redux, store, actions, and pure reducers", """# Redux Fundamentals

Redux is a predictable state container for JavaScript applications.

## Three Core Principles

1. **Single Source of Truth**: The global state of your application is stored in an object tree within a single store.
2. **State is Read-Only**: The only way to change state is to dispatch an action object describing what happened.
3. **Changes are Made with Pure Functions**: Reducers are pure functions that take previous state and an action, returning new state.

```javascript
// Action object
const incrementAction = { type: 'counter/increment', payload: 1 };

// Pure Reducer function
function counterReducer(state = { value: 0 }, action) {
  switch (action.type) {
    case 'counter/increment':
      return { ...state, value: state.value + action.payload };
    default:
      return state;
  }
}
```
"""),

    ("Redux Toolkit", "redux-toolkit", "configureStore, createSlice, and Immer mutable-style syntax", """# Redux Toolkit (RTK)

Redux Toolkit is the official, opinionated, batteries-included toolset for efficient Redux development.

## Why Use Redux Toolkit?

- Simplifies store setup with `configureStore()`.
- Eliminates boilerplate using `createSlice()`.
- Uses **Immer** library to allow safe, "mutable-style" logic inside reducers.

```javascript
import { createSlice, configureStore } from '@reduxjs/toolkit';

const counterSlice = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: {
    increment: (state) => {
      // Immer handles immutability under the hood!
      state.value += 1;
    },
    incrementByAmount: (state, action) => {
      state.value += action.payload;
    }
  }
});

export const { increment, incrementByAmount } = counterSlice.actions;

export const store = configureStore({
  reducer: {
    counter: counterSlice.reducer
  }
});
```
"""),

    ("Store & Slices", "store-slices", "Structuring state into domain slices and combining reducers", """# Redux Store & Slices

In modern Redux, application state is split into modular slice files representing distinct feature domains.

## Modular Slice Example (`features/auth/authSlice.js`)

```javascript
import { createSlice } from '@reduxjs/toolkit';

const authSlice = createSlice({
  name: 'auth',
  initialState: { user: null, token: null, isAuthenticated: false },
  reducers: {
    setCredentials: (state, action) => {
      state.user = action.payload.user;
      state.token = action.payload.token;
      state.isAuthenticated = true;
    },
    logout: (state) => {
      state.user = null;
      state.token = null;
      state.isAuthenticated = false;
    }
  }
});

export const { setCredentials, logout } = authSlice.actions;
export default authSlice.reducer;
```
"""),

    ("useSelector & useDispatch", "redux-hooks", "React-Redux hooks for reading state and dispatching actions", """# React-Redux Hooks

React applications interact with Redux stores using hooks provided by `react-redux`.

## Core Hooks

- `useSelector(selectorFn)`: Reads data from the store state and subscribes to updates.
- `useDispatch()`: Returns the store's dispatch function to trigger actions.

```javascript
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { increment, logout } from './authSlice';

export function UserHeader() {
  const dispatch = useDispatch();
  const { user, isAuthenticated } = useSelector((state) => state.auth);

  if (!isAuthenticated) return <p>Please log in</p>;

  return (
    <div>
      <p>Welcome, {user.name}!</p>
      <button onClick={() => dispatch(logout())}>Log Out</button>
    </div>
  );
}
```
"""),

    ("Async Thunks", "async-thunks", "createAsyncThunk, extraReducers, and handling pending/fulfilled states", """# Async Logic with Redux Thunks

`createAsyncThunk` handles asynchronous data fetching pipelines in Redux Toolkit.

## Creating an Async Thunk

```javascript
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

export const fetchCourses = createAsyncThunk(
  'courses/fetchCourses',
  async (_, thunkAPI) => {
    const response = await fetch('/api/v1/courses');
    return await response.json();
  }
);

const coursesSlice = createSlice({
  name: 'courses',
  initialState: { items: [], loading: false, error: null },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchCourses.pending, (state) => {
        state.loading = true;
      })
      .addCase(fetchCourses.fulfilled, (state, action) => {
        state.loading = false;
        state.items = action.payload;
      })
      .addCase(fetchCourses.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message;
      });
  }
});

export default coursesSlice.reducer;
```
""")
]

REDUX_QUIZZES = {
    "redux-redux-fundamentals": [
        {
            "level": "medium",
            "title": "Redux Fundamentals Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What is the ONLY way to trigger a state change in a Redux store?",
                    "explanation": "State is read-only; the only way to trigger a state change is to dispatch an action object.",
                    "options": [("Mutating state directly", False), ("Dispatching an action object", True), ("Calling store.setState()", False), ("Modifying the reducer file", False)],
                },
            ],
        }
    ],
    "redux-redux-toolkit": [
        {
            "level": "medium",
            "title": "Redux Toolkit Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which internal library enables writing 'mutable-style' code inside RTK createSlice reducers?",
                    "explanation": "Immer wraps state updates in a Proxy to produce immutable copies automatically.",
                    "options": [("Lodash", False), ("Immer", True), ("RxJS", False), ("Axios", False)],
                },
            ],
        }
    ],
    "redux-store-slices": [
        {
            "level": "medium",
            "title": "Store & Slices Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does RTK's createSlice automatically generate for you?",
                    "explanation": "createSlice automatically generates action creators and reducer functions based on your reducer object.",
                    "options": [("React components", False), ("Action creators and reducer function", True), ("Database models", False), ("Express routes", False)],
                },
            ],
        }
    ],
    "redux-redux-hooks": [
        {
            "level": "easy",
            "title": "React-Redux Hooks Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which React-Redux hook is used to extract data from the Redux store state?",
                    "explanation": "useSelector extracts slice state from the Redux store.",
                    "options": [("useDispatch", False), ("useSelector", True), ("useStore", False), ("useReduxState", False)],
                },
            ],
        }
    ],
    "redux-async-thunks": [
        {
            "level": "hard",
            "title": "Async Thunks Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "Which property in createSlice handles action types generated outside the slice, such as async thunks?",
                    "explanation": "extraReducers handles external actions like createAsyncThunk lifecycle states.",
                    "options": [("reducers", False), ("extraReducers", True), ("asyncReducers", False), ("middlewares", False)],
                },
            ],
        }
    ],
}
