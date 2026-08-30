import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import { apiClient } from '../../api/apiClient'
import { ENDPOINTS } from '../../api/endpoints'

export const fetchCourses = createAsyncThunk(
  'courses/fetchAll',
  async () => {
    const { data } = await apiClient.get(ENDPOINTS.courses)
    return data
  },
)

const coursesSlice = createSlice({
  name: 'courses',
  initialState: {
    courses: [],
    loading: false,
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchCourses.pending, (state) => {
        state.loading = true
      })
      .addCase(fetchCourses.fulfilled, (state, action) => {
        state.courses = action.payload
        state.loading = false
      })
      .addCase(fetchCourses.rejected, (state, action) => {
        state.loading = false
        state.error = action.error.message
      })
  },
})

export default coursesSlice.reducer
