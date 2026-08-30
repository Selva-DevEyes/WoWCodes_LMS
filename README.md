# WoWCodes by SelvamSDE

**Learn • Practice • Build • Crack Interviews**

A production-ready Full Stack Learning Management System (LMS) built with React 19 and FastAPI.

## 🚀 Features

- **Authentication**: Register, Login, Logout, Forgot/Reset Password, JWT with refresh tokens
- **Role-Based Access**: Student, Instructor, Admin
- **Student Dashboard**: Progress tracking, learning paths, quizzes, leaderboard, certificates
- **Learning Content**: 17+ learning paths with topics covering HTML, CSS, JavaScript, React, Redux, Python, FastAPI, SQL, Git, AI, and more
- **Quiz System**: Easy/Medium/Hard quizzes with explanations, scoring, and leaderboard
- **Global Search**: Search across topics, courses, and quizzes
- **Dark/Light Mode**: Fully themeable UI
- **Responsive Design**: Mobile-first Tailwind CSS

## 🛠️ Tech Stack

### Frontend
- React 19 + Vite
- Redux Toolkit
- React Router
- Tailwind CSS
- Axios
- React Icons

### Backend
- Python + FastAPI
- SQLAlchemy ORM
- JWT Authentication
- Passlib (bcrypt)
- SQLite (Dev) / PostgreSQL (Production)

### Deployment
- Frontend: Netlify
- Backend: Render
- Database: SQLite / PostgreSQL / Supabase

## 📁 Project Structure

```
capstone/
├── frontend/          # React 19 + Vite + Tailwind
├── backend/           # FastAPI + SQLAlchemy
├── docker-compose.yml
└── README.md
```

## ⚡ Quick Start

### Backend

```bash
cd backend
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
python -m app.seed.seed   # Seed data (admin + courses)
uvicorn app.main:app --reload --port 8001
```

API will be at `http://localhost:8001`
Swagger docs: `http://localhost:8001/docs`

### Frontend

```bash
cd frontend
npm install
npm run dev
```

App will be at `http://localhost:5173`

### Default Accounts (after seeding)

| Role       | Email                     | Password        |
|------------|---------------------------|-----------------|
| Admin      | admin@wowcodes.com        | admin123        |
| Instructor | instructor@wowcodes.com   | instructor123   |

## 🌐 Deployment

### Frontend → Netlify

1. Push frontend to GitHub
2. In Netlify: **New site from Git**
3. Build command: `npm run build`
4. Publish directory: `dist`
5. Set env var: `VITE_API_URL=https://wowcodes-api.onrender.com/api/v1`

### Backend → Render

1. Push backend to GitHub
2. In Render: **New Web Service**
3. Runtime: Python
4. Build: `pip install -r requirements.txt`
5. Start: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
6. Set env vars: `DATABASE_URL`, `SECRET_KEY`

### Docker (Alternative)

```bash
docker-compose up --build
```

## 🗄️ Database Tables

Users, Roles, Courses, Topics, Lessons, Notes, Quizzes, Questions, Options, Answers, Results, Progress, Bookmarks, Certificates, Notifications

## 🔒 Environment Variables

See `.env.example` in both `frontend/` and `backend/`

## 📄 License

MIT
