import { configureStore } from '@reduxjs/toolkit'
import authReducer from '../slices/authSlice'
import themeReducer from '../slices/themeSlice'
import coursesReducer from '../slices/coursesSlice'
import topicsReducer from '../slices/topicsSlice'
import quizReducer from '../slices/quizSlice'
import progressReducer from '../slices/progressSlice'
import notificationsReducer from '../slices/notificationsSlice'

export const store = configureStore({
  reducer: {
    auth: authReducer,
    theme: themeReducer,
    courses: coursesReducer,
    topics: topicsReducer,
    quiz: quizReducer,
    progress: progressReducer,
    notifications: notificationsReducer,
  },
})
