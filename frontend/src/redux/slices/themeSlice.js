import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  mode: localStorage.getItem('theme') || 'light',
}

const themeSlice = createSlice({
  name: 'theme',
  initialState,
  reducers: {
    setTheme: (state, action) => {
      state.mode = action.payload
      localStorage.setItem('theme', action.payload)
    },
    toggleTheme: (state) => {
      state.mode = state.mode === 'light' ? 'dark' : 'light'
      localStorage.setItem('theme', state.mode)
    },
  },
})

export const { setTheme, toggleTheme } = themeSlice.actions
export const selectTheme = (state) => state.theme.mode
export default themeSlice.reducer
