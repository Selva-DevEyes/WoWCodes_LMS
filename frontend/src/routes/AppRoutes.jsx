import { Routes, Route } from 'react-router-dom'
import ProtectedRoute from './ProtectedRoute'
import PublicRoute from './PublicRoute'
import DashboardLayout from '../layouts/DashboardLayout'
import AuthLayout from '../layouts/AuthLayout'
import Login from '../pages/auth/Login'
import Register from '../pages/auth/Register'
import ForgotPassword from '../pages/auth/ForgotPassword'
import ResetPassword from '../pages/auth/ResetPassword'
import Dashboard from '../pages/student/Dashboard'
import Learn from '../pages/student/Learn'
import CourseDetail from '../pages/student/CourseDetail'
import TopicDetail from '../pages/student/TopicDetail'
import QuizPage from '../pages/student/QuizPage'
import QuizResultPage from '../pages/student/QuizResultPage'
import LeaderboardPage from '../pages/student/LeaderboardPage'
import CertificatesPage from '../pages/student/CertificatesPage'
import NotesPage from '../pages/student/NotesPage'
import BookmarksPage from '../pages/student/BookmarksPage'
import ProfilePage from '../pages/student/ProfilePage'
import SettingsPage from '../pages/student/SettingsPage'
import PlaygroundPage from '../pages/student/PlaygroundPage'
import NotFound from '../pages/error/NotFound'

function AppRoutes() {
  return (
    <Routes>
      {/* Public auth routes */}
      <Route element={<AuthLayout />}>
        <Route path="/login" element={<PublicRoute><Login /></PublicRoute>} />
        <Route path="/register" element={<PublicRoute><Register /></PublicRoute>} />
        <Route path="/forgot-password" element={<PublicRoute><ForgotPassword /></PublicRoute>} />
        <Route path="/reset-password" element={<PublicRoute><ResetPassword /></PublicRoute>} />
      </Route>

      {/* Protected dashboard routes */}
      <Route element={<ProtectedRoute><DashboardLayout /></ProtectedRoute>}>
        <Route path="/" element={<Dashboard />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/learn" element={<Learn />} />
        <Route path="/playground" element={<PlaygroundPage />} />
        <Route path="/learn/course/:courseId" element={<CourseDetail />} />
        <Route path="/learn/topic/:topicId" element={<TopicDetail />} />
        <Route path="/quiz/:quizId" element={<QuizPage />} />
        <Route path="/quiz/result/:resultId" element={<QuizResultPage />} />
        <Route path="/leaderboard" element={<LeaderboardPage />} />
        <Route path="/certificates" element={<CertificatesPage />} />
        <Route path="/notes" element={<NotesPage />} />
        <Route path="/bookmarks" element={<BookmarksPage />} />
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="/settings" element={<SettingsPage />} />
      </Route>

      {/* 404 */}
      <Route path="*" element={<NotFound />} />
    </Routes>
  )
}

export default AppRoutes