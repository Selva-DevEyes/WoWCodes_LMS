import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import { apiClient } from '../../api/apiClient'
import { ENDPOINTS } from '../../api/endpoints'

export const fetchDashboard = createAsyncThunk(
  'progress/dashboard',
  async () => {
    const { data } = await apiClient.get(ENDPOINTS.dashboard)
    return data
  },
)

export const updateTopicProgress = createAsyncThunk(
  'progress/updateTopic',
  async ({ topicId, payload }) => {
    const { data } = await apiClient.post(ENDPOINTS.topicProgress(topicId), payload)
    return data
  },
)

const progressSlice = createSlice({
  name: 'progress',
  initialState: {
    stats: null,
    items: [],
    loading: false,
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchDashboard.pending, (state) => {
        state.loading = true
      })
      .addCase(fetchDashboard.fulfilled, (state, action) => {
        state.stats = action.payload
        state.loading = false
      })
      .addCase(fetchDashboard.rejected, (state, action) => {
        state.loading = false
        state.error = action.error.message
      })
  },
})

export default progressSlice.reducer
