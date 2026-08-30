import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import { apiClient } from '../../api/apiClient'
import { ENDPOINTS } from '../../api/endpoints'

export const fetchNotifications = createAsyncThunk(
  'notifications/fetchAll',
  async () => {
    const { data } = await apiClient.get(ENDPOINTS.notifications)
    return data
  },
)

export const markAllRead = createAsyncThunk(
  'notifications/markAllRead',
  async () => {
    const { data } = await apiClient.post(ENDPOINTS.notificationsReadAll)
    return data
  },
)

const notificationsSlice = createSlice({
  name: 'notifications',
  initialState: {
    items: [],
    loading: false,
    error: null,
  },
  reducers: {
    markRead: (state, action) => {
      const note = state.items.find((n) => n.id === action.payload)
      if (note) {
        note.is_read = true
      }
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchNotifications.pending, (state) => {
        state.loading = true
      })
      .addCase(fetchNotifications.fulfilled, (state, action) => {
        state.items = action.payload
        state.loading = false
      })
      .addCase(fetchNotifications.rejected, (state, action) => {
        state.loading = false
        state.error = action.error.message
      })
  },
})

export const { markRead } = notificationsSlice.actions
export default notificationsSlice.reducer
