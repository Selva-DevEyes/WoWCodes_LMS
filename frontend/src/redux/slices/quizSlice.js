import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import { apiClient } from '../../api/apiClient'
import { ENDPOINTS } from '../../api/endpoints'

export const fetchQuizzes = createAsyncThunk(
  'quiz/fetchByTopic',
  async (topicId) => {
    const { data } = await apiClient.get(ENDPOINTS.quizzesByTopic(topicId))
    return data
  },
)

export const submitQuiz = createAsyncThunk(
  'quiz/submit',
  async ({ quizId, payload }) => {
    const { data } = await apiClient.post(ENDPOINTS.submitQuiz(quizId), payload)
    return data
  },
)

const quizSlice = createSlice({
  name: 'quiz',
  initialState: {
    quizzes: [],
    currentQuiz: null,
    result: null,
    loading: false,
    error: null,
  },
  reducers: {
    setCurrentQuiz: (state, action) => {
      state.currentQuiz = action.payload
    },
    clearResult: (state) => {
      state.result = null
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchQuizzes.pending, (state) => {
        state.loading = true
      })
      .addCase(fetchQuizzes.fulfilled, (state, action) => {
        state.quizzes = action.payload
        state.loading = false
      })
      .addCase(fetchQuizzes.rejected, (state, action) => {
        state.loading = false
        state.error = action.error.message
      })
      .addCase(submitQuiz.fulfilled, (state, action) => {
        state.result = action.payload
        state.loading = false
      })
  },
})

export const { setCurrentQuiz, clearResult } = quizSlice.actions
export default quizSlice.reducer
