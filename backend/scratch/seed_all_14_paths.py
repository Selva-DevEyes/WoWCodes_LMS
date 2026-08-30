import os
import sys

# Add backend directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.database.session import SessionLocal, init_db
from app.models.course import Course
from app.models.topic import Topic
from app.models.lesson import Lesson
from app.models.quiz import Quiz
from app.models.question import Question
from app.models.option import Option

def generate_10_employer_questions(topic_title):
    return [
        {
            "text": f"Q1 [{topic_title} - Employer Perspective]: Which architectural design pattern or practice best optimizes high-throughput production workloads in {topic_title}?",
            "explanation": f"Detailed production rationale for {topic_title}. Explains memory efficiency, non-blocking execution, and enterprise fault-tolerance.",
            "options": [
                (f"Synchronous blocking loops with global mutable state in {topic_title}", False),
                (f"Decoupled, event-driven architecture with explicit state management and validation in {topic_title}", True),
                (f"Ignoring error handling and logging in {topic_title}", False),
                (f"Hardcoding configuration values directly inside function bodies", False),
            ]
        },
        {
            "text": f"Q2 [{topic_title} - Code Performance]: What is the primary time or space complexity trade-off when implementing core operations in {topic_title}?",
            "explanation": f"Evaluates algorithmic complexity in {topic_title}. Trade-offs between memory footprint and execution speed.",
            "options": [
                (f"O(n^2) time complexity with unindexed full table scans", False),
                (f"Optimal O(1) or O(log n) time complexity using proper indexing or hash maps in {topic_title}", True),
                (f"O(n!) factorial complexity", False),
                (f"Infinite recursive call stack depth", False),
            ]
        },
        {
            "text": f"Q3 [{topic_title} - Production Security]: Which security measure is critical to prevent vulnerabilities in {topic_title}?",
            "explanation": f"Security guidelines for {topic_title}. Input sanitization, parameterization, and secret protection.",
            "options": [
                (f"Storing secret credentials directly in public Git repositories", False),
                (f"Strict input validation, parameterized queries, and environment variable protection in {topic_title}", True),
                (f"Disabling CORS and SSL/TLS encryption entirely", False),
                (f"Trusting all unvalidated client inputs", False),
            ]
        },
        {
            "text": f"Q4 [{topic_title} - Code Reliability]: How should exception handling and error boundary recovery be structured in {topic_title}?",
            "explanation": f"Error handling best practices for {topic_title}. Defensive programming and graceful degradation.",
            "options": [
                (f"Swallowing exceptions silently with empty try/catch blocks", False),
                (f"Centralized error handling with structured logging and standard HTTP error codes in {topic_title}", True),
                (f"Crashing the application process on any warning", False),
                (f"Returning empty 200 OK responses on failure", False),
            ]
        },
        {
            "text": f"Q5 [{topic_title} - Industry Standards]: Which coding convention or style rule is recommended for maintaining enterprise codebases in {topic_title}?",
            "explanation": f"Clean code and maintainability principles for {topic_title}.",
            "options": [
                (f"Using single-letter variable names globally without comments", False),
                (f"Following PEP 8 / Clean Code standards with clear naming and modular functions in {topic_title}", True),
                (f"Writing 5,000-line monolithic files", False),
                (f"Mixing inconsistent formatting and indentation styles", False),
            ]
        },
        {
            "text": f"Q6 [{topic_title} - Testing Strategy]: What testing strategy provides maximum coverage and regression safety in {topic_title}?",
            "explanation": f"Automated testing methodologies including unit, integration, and end-to-end testing for {topic_title}.",
            "options": [
                (f"Testing code only manually in production", False),
                (f"Automated unit tests, integration tests, and CI/CD automated pipeline execution for {topic_title}", True),
                (f"Deleting failing unit tests to make builds pass", False),
                (f"Writing tests after releasing to production without staging", False),
            ]
        },
        {
            "text": f"Q7 [{topic_title} - Scalability]: How do system resources scale horizontally when workload increases in {topic_title}?",
            "explanation": f"Scalability patterns, stateless service design, and database read replica distribution for {topic_title}.",
            "options": [
                (f"Storing sticky state in process memory prohibiting multi-node deployment", False),
                (f"Stateless service architecture with caching and distributed worker queues in {topic_title}", True),
                (f"Increasing single server CPU indefinitely without horizontal scaling", False),
                (f"Hardcoding server IP addresses", False),
            ]
        },
        {
            "text": f"Q8 [{topic_title} - Observability]: Which metric or logging practice is essential for monitoring production systems in {topic_title}?",
            "explanation": f"Observability metrics (latency, error rates, throughput) and structured JSON logging for {topic_title}.",
            "options": [
                (f"Printing unformatted text to console without timestamps", False),
                (f"Structured JSON logging, Prometheus metrics, and distributed tracing for {topic_title}", True),
                (f"Disabling all logs to save disk space", False),
                (f"Logging passwords and API keys in plain text", False),
            ]
        },
        {
            "text": f"Q9 [{topic_title} - API Contract]: How should API contracts and interface definitions be managed in {topic_title}?",
            "explanation": f"API versioning, OpenAPI schema documentation, and backward compatibility in {topic_title}.",
            "options": [
                (f"Breaking API response fields without versioning or notice", False),
                (f"Versioning APIs (/api/v1) with OpenAPI documentation and backward compatibility in {topic_title}", True),
                (f"Deleting API endpoints without deprecation warnings", False),
                (f"Returning different data structures randomly", False),
            ]
        },
        {
            "text": f"Q10 [{topic_title} - Senior Leadership]: As a Senior Software Engineer leading a team working on {topic_title}, how do you evaluate technical debt?",
            "explanation": f"Technical debt management, refactoring strategies, and continuous integration practices for {topic_title}.",
            "options": [
                (f"Ignoring technical debt until system crashes completely", False),
                (f"Balancing feature velocity with planned refactoring sprints and architectural reviews in {topic_title}", True),
                (f"Rewriting entire codebase from scratch every month", False),
                (f"Forcing junior developers to work without code reviews", False),
            ]
        }
    ]

# Generate 50 High-Stakes Questions for Final Evaluation Exam (100 Marks)
def generate_50_final_exam_questions():
    questions = []
    modules = [
        "Module 1: Front-End & Node Runtime",
        "Module 2: Python & Data Structures",
        "Module 3: FastAPI Backend & APIs",
        "Module 4: Git Version Control & DevOps",
        "Module 5: Databases & ORM Integration",
        "Module 6: LLMs & Applied AI Engineering"
    ]
    for i in range(1, 51):
        mod = modules[(i - 1) % len(modules)]
        questions.append({
            "text": f"Q{i} [Final Certification Exam - {mod}]: Which enterprise principle or algorithm implementation best demonstrates mastery in {mod}?",
            "explanation": f"Comprehensive evaluation explanation for Q{i} ({mod}). Verifies employer-side technical competencies and system design capability.",
            "options": [
                (f"Incorrect candidate option A for Q{i}", False),
                (f"Mastery technical choice for Q{i} on {mod} (2 Marks)", True),
                (f"Incorrect candidate option C for Q{i}", False),
                (f"Incorrect candidate option D for Q{i}", False),
            ]
        })
    return questions

def seed_database():
    init_db()
    db = SessionLocal()

    # Clear existing courses to ensure clean 14-path structure
    db.query(Option).delete()
    db.query(Question).delete()
    db.query(Quiz).delete()
    db.query(Lesson).delete()
    db.query(Topic).delete()
    db.query(Course).delete()
    db.commit()

    print("Cleared old database tables successfully.")

    # 14 Learning Paths
    courses_data = [
        ("HTML", "html", "Learn semantic markup, WCAG accessibility, forms, and HTML5 layout.", "Frontend", "beginner", "🌐", "bg-blue-100 text-blue-600"),
        ("CSS", "css", "Master CSS Box Model, Flexbox, CSS Grid, positioning, and responsive design.", "Frontend", "beginner", "🎨", "bg-purple-100 text-purple-600"),
        ("JavaScript", "javascript", "Master ES6+, dynamic typing, DOM, async/await, closures, and event loop.", "Frontend", "intermediate", "⚡", "bg-yellow-100 text-yellow-600"),
        ("React", "react", "Build modern user interfaces with React 19, hooks, virtual DOM, and JSX.", "Frontend", "intermediate", "⚛️", "bg-cyan-100 text-cyan-600"),
        ("Redux", "redux", "Manage global application state with Redux Toolkit and async thunks.", "Frontend", "intermediate", "🔄", "bg-violet-100 text-violet-600"),
        ("Python", "python", "Learn Python programming from syntax basics to memory optimization.", "Backend", "beginner", "🐍", "bg-green-100 text-green-600"),
        ("FastAPI", "fastapi", "Build high-performance asynchronous REST APIs with FastAPI & Pydantic.", "Backend", "intermediate", "🚀", "bg-teal-100 text-teal-600"),
        ("SQL", "sql", "Master SQL DDL/DML/DQL, complex joins, aggregation, and query optimization.", "Database", "intermediate", "🗄️", "bg-orange-100 text-orange-600"),
        ("Git & GitHub", "git-github", "Distributed version control, branching strategies, rebase, and code reviews.", "Tools", "beginner", "🔀", "bg-red-100 text-red-600"),
        ("AI & ML", "ai-ml", "Artificial Intelligence, Machine Learning pipelines, and Deep Learning.", "AI", "advanced", "🤖", "bg-indigo-100 text-indigo-600"),
        ("Node.js Basics", "nodejs", "Asynchronous server-side JavaScript runtime, streams, and native modules.", "Backend", "intermediate", "🟢", "bg-emerald-100 text-emerald-600"),
        ("Express.js", "express", "Build fast, flexible web applications, REST routes, and middleware pipelines.", "Backend", "intermediate", "🚂", "bg-stone-100 text-stone-600"),
        ("Database", "database", "Relational databases, NoSQL systems, indexing, and ORM abstractions.", "Database", "intermediate", "🗄️", "bg-orange-100 text-orange-600"),
        (
            "Final Evaluation of Software Engineering Program",
            "final-evaluation-sde",
            "Structured 6-Module Program covering Front-End, Python/DSA, FastAPI, DevOps, Databases, and LLM Engineering with 100-Mark Certification Exam.",
            "Certification",
            "advanced",
            "🎓",
            "bg-gradient-to-r from-indigo-500 to-purple-600 text-white"
        )
    ]

    for order_idx, (title, slug, desc, category, level, icon, color) in enumerate(courses_data, 1):
        course = Course(
            title=title,
            slug=slug,
            description=desc,
            category=category,
            level=level,
            icon=icon,
            color=color,
            is_published=True,
            order=order_idx,
        )
        db.add(course)
        db.flush()

        if slug == "final-evaluation-sde":
            # Seed 6 Structured Modules with Topics & Quizzes
            modules_structure = [
                ("Module 1: Front-End Web Development", [
                    ("HTML & Semantic Web", "mod1-html", "Semantic HTML5, ARIA, and Accessibility"),
                    ("CSS & Responsive Layouts", "mod1-css", "Box Model, Flexbox 1D, CSS Grid 2D"),
                    ("JavaScript Core", "mod1-js", "ES6+, Event Loop, Microtask Queue"),
                    ("React 19 Framework", "mod1-react", "Components, Hooks, Virtual DOM"),
                    ("Redux Toolkit", "mod1-redux", "Global State, Slices, Async Thunks"),
                    ("Front-End JS & DOM", "mod1-fe-js", "DOM Selection, Event Delegation"),
                    ("Node.js Runtime", "mod1-nodejs", "V8, Event Loop, File System, Streams"),
                    ("Express.js APIs", "mod1-express", "REST Routes, Middleware Pipeline"),
                ]),
                ("Module 2: Python & Data Structures", [
                    ("Python Fundamentals", "mod2-python", "Dynamic Typing, Syntax, Collections"),
                    ("Python Programming Core", "mod2-python-core", "Control Flow, Generators, Decorators"),
                    ("Data Structures & Algorithms", "mod2-dsa", "Insertion Sort, Binary Search, Timsort"),
                ]),
                ("Module 3: FastAPI Backend & APIs", [
                    ("FastAPI Backend", "mod3-fastapi", "ASGI Uvicorn, Path & Query Parameters"),
                    ("SQL Querying", "mod3-sql", "DDL/DML/DQL, WHERE Safety, Joins"),
                    ("FastAPI Architecture", "mod3-fastapi-arch", "Pydantic v2 Validators, Background Tasks"),
                    ("Client-Server APIs", "mod3-apis", "HTTP Methods, Status Codes, Fetch API"),
                ]),
                ("Module 4: Version Control & DevOps", [
                    ("Git & GitHub Enterprise", "mod4-git", "DVCS, Branching, Rebase vs Merge"),
                    ("Version Control Systems", "mod4-vcs", "Conflict Resolution, Secret Safety"),
                ]),
                ("Module 5: Databases & ORM Integration", [
                    ("Databases & SQL Engineering", "mod5-db-sql", "Relational vs NoSQL, Indexing"),
                    ("Relational & NoSQL Systems", "mod5-nosql", "ACID, Normalization, Polyglot Storage"),
                    ("ORM Full-Stack Integration", "mod5-orm", "SQLAlchemy ORM, Pydantic Bridge"),
                ]),
                ("Module 6: LLMs & Applied AI Engineering", [
                    ("LLMs & Prompt Engineering", "mod6-llms", "Transformers, Self-Attention, CoT"),
                    ("AI API & RAG Integration", "mod6-rag", "RAG Architecture, Embeddings, Streaming"),
                    ("AI-Assisted Engineering", "mod6-ai-dev", "Golden Rule, Observability, Health Checks"),
                ]),
            ]

            for mod_title, topics in modules_structure:
                for t_title, t_slug, t_desc in topics:
                    full_t_title = f"{mod_title} — {t_title}"
                    topic = Topic(
                        course_id=course.id,
                        title=full_t_title,
                        slug=f"final-sde-{t_slug}",
                        description=t_desc,
                        order=len(db.query(Topic).filter(Topic.course_id == course.id).all()) + 1,
                    )
                    db.add(topic)
                    db.flush()

                    # Add Lesson
                    lesson = Lesson(
                        course_id=course.id,
                        topic_id=topic.id,
                        title=f"{full_t_title} - Engineering Masterclass",
                        content=f"# {full_t_title}\n\n## Beginner: Core Concepts\nDetailed masterclass covering fundamentals.\n\n## Intermediate: Implementation\nProduction engineering patterns.\n\n## Advanced: Architecture\nScalability, security, and performance optimizations.",
                        order=0,
                        is_published=True,
                    )
                    db.add(lesson)

                    # Add 10-Question Employer Perspective Quiz
                    quiz = Quiz(
                        topic_id=topic.id,
                        title=f"{t_title} Employer Evaluation Quiz (10 Questions)",
                        level="intermediate",
                        description=f"Employer-side technical evaluation quiz for {t_title}.",
                        passing_score=70,
                        time_limit_minutes=15,
                    )
                    db.add(quiz)
                    db.flush()

                    questions_data = generate_10_employer_questions(t_title)
                    for q_idx, q in enumerate(questions_data):
                        question = Question(
                            quiz_id=quiz.id,
                            text=q["text"],
                            explanation=q["explanation"],
                            points=10,
                            order=q_idx,
                        )
                        db.add(question)
                        db.flush()
                        for opt_idx, (text, correct) in enumerate(q["options"]):
                            db.add(Option(
                                question_id=question.id,
                                text=text,
                                is_correct=correct,
                                order=opt_idx,
                            ))

            # Add Final Comprehensive Evaluation Exam (100 Marks, 50 Questions + Project Submission)
            exam_topic = Topic(
                course_id=course.id,
                title="FINAL CERTIFICATION EXAM (100 MARKS & PROJECT SUBMISSION)",
                slug="final-sde-certification-exam",
                description="Final Comprehensive Software Engineering Exam (50 Questions / 100 Marks) & Practical Project Submission Portal.",
                order=99,
            )
            db.add(exam_topic)
            db.flush()

            exam_lesson = Lesson(
                course_id=course.id,
                topic_id=exam_topic.id,
                title="Final Program Evaluation Instructions",
                content="# Final Evaluation of Software Development Engineering Program\n\n## Certification Requirements:\n1. Achieve score >= 70% on the 50-Question Certification Exam (100 Marks Total).\n2. Submit your Practical Capstone Project (GitHub Repository + Live Demo URL).\n3. Upon successful evaluation, your official Software Development Engineering Certification Certificate will be auto-generated!",
                order=0,
                is_published=True,
            )
            db.add(exam_lesson)

            exam_quiz = Quiz(
                topic_id=exam_topic.id,
                title="Final Evaluation Exam (50 Questions - 100 Marks)",
                level="hard",
                description="Final 50-Question Comprehensive Employer Certification Exam.",
                passing_score=70,
                time_limit_minutes=60,
            )
            db.add(exam_quiz)
            db.flush()

            exam_questions = generate_50_final_exam_questions()
            for q_idx, q in enumerate(exam_questions):
                question = Question(
                    quiz_id=exam_quiz.id,
                    text=q["text"],
                    explanation=q["explanation"],
                    points=2,
                    order=q_idx,
                )
                db.add(question)
                db.flush()
                for opt_idx, (text, correct) in enumerate(q["options"]):
                    db.add(Option(
                        question_id=question.id,
                        text=text,
                        is_correct=correct,
                        order=opt_idx,
                    ))

        else:
            # Standalone Learning Path - Add topic with 10 questions each
            topic = Topic(
                course_id=course.id,
                title=f"{title} Complete Curriculum",
                slug=f"{slug}-complete",
                description=f"Complete professional study guide for {title}.",
                order=1,
            )
            db.add(topic)
            db.flush()

            lesson = Lesson(
                course_id=course.id,
                topic_id=topic.id,
                title=f"{title} Engineering Guide",
                content=f"# {title} Engineering Masterclass\n\n## Beginner\nFoundations and syntax.\n\n## Intermediate\nImplementation and state management.\n\n## Advanced\nPerformance, security, and scalability.",
                order=0,
                is_published=True,
            )
            db.add(lesson)

            quiz = Quiz(
                topic_id=topic.id,
                title=f"{title} Technical Mastery Quiz (10 Questions)",
                level="intermediate",
                description=f"Employer-side evaluation quiz for {title}.",
                passing_score=70,
                time_limit_minutes=15,
            )
            db.add(quiz)
            db.flush()

            questions_data = generate_10_employer_questions(title)
            for q_idx, q in enumerate(questions_data):
                question = Question(
                    quiz_id=quiz.id,
                    text=q["text"],
                    explanation=q["explanation"],
                    points=10,
                    order=q_idx,
                )
                db.add(question)
                db.flush()
                for opt_idx, (text, correct) in enumerate(q["options"]):
                    db.add(Option(
                        question_id=question.id,
                        text=text,
                        is_correct=correct,
                        order=opt_idx,
                    ))

    db.commit()
    print("Database seeding completed successfully! All 14 learning paths, 6 modules, 10-question topic quizzes, and 50-question final exam are live!")

if __name__ == "__main__":
    seed_database()
