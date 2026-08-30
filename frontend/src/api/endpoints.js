// API endpoint constants
export const ENDPOINTS = {
  // Auth
  register: '/auth/register',
  login: '/auth/login',
  refresh: '/auth/refresh',
  forgotPassword: '/auth/forgot-password',
  resetPassword: '/auth/reset-password',

  // Users
  me: '/users/me',
  updateMe: '/users/me',
  uploadAvatar: '/users/me/avatar',
  leaderboard: '/users/leaderboard',

  // Courses
  courses: '/courses',
  course: (id) => `/courses/${id}`,

  // Topics
  topicsByCourse: (courseId) => `/topics/course/${courseId}`,
  topic: (id) => `/topics/${id}`,

  // Lessons
  lessonsByTopic: (topicId) => `/lessons/topic/${topicId}`,
  lesson: (id) => `/lessons/${id}`,

  // Quiz
  quizzesByTopic: (topicId) => `/quiz/topic/${topicId}`,
  quiz: (id) => `/quiz/${id}`,
  submitQuiz: (id) => `/quiz/${id}/submit`,
  myResults: '/quiz/results/mine',

  // Progress
  dashboard: '/progress/dashboard',
  progress: '/progress',
  topicProgress: (topicId) => `/progress/topic/${topicId}`,

  // Notes
  notes: '/notes',
  note: (id) => `/notes/${id}`,

  // Bookmarks
  bookmarks: '/bookmarks',
  bookmark: (id) => `/bookmarks/${id}`,

  // Notifications
  notifications: '/notifications',
  notificationRead: (id) => `/notifications/${id}/read`,
  notificationsReadAll: '/notifications/read-all',

  // Certificates
  certificates: '/certificates',
  certificate: (code) => `/certificates/${code}`,

  // Search
  search: (q) => `/search?q=${encodeURIComponent(q)}`,
}
