import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import { apiClient } from '../../api/apiClient'
import { ENDPOINTS } from '../../api/endpoints'

export const fetchTopics = createAsyncThunk(
  'topics/fetchByCourse',
  async (courseId) => {
    const { data } = await apiClient.get(ENDPOINTS.topicsByCourse(courseId))
    return data
  },
)

const topicsSlice = createSlice({
  name: 'topics',
  initialState: {
    topics: [],
    loading: false,
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchTopics.pending, (state) => {
        state.loading = true
      })
      .addCase(fetchTopics.fulfilled, (state, action) => {
        state.topics = action.payload
        state.loading = false
      })
      .addCase(fetchTopics.rejected, (state, action) => {
        state.loading = false
        state.error = action.error.message
      })
  },
})

export default topicsSlice.reducer
