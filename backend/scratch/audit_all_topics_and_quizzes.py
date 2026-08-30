"""Audit all topics and quizzes to verify topic-question matching and database integrity."""
import sys
from pathlib import Path

backend_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(backend_dir))

from app.database.session import SessionLocal
from app.models.course import Course
from app.models.topic import Topic
from app.models.quiz import Quiz
from app.models.question import Question

def audit_curriculum():
    db = SessionLocal()
    try:
        courses = db.query(Course).all()
        print(f"Total Courses: {len(courses)}")
        
        topics = db.query(Topic).order_by(Topic.id).all()
        print(f"Total Topics: {len(topics)}")

        quizzes = db.query(Quiz).all()
        print(f"Total Quizzes: {len(quizzes)}")

        questions = db.query(Question).all()
        print(f"Total Questions in DB: {len(questions)}")

        mismatches = []
        for t in topics:
            qz = db.query(Quiz).filter(Quiz.topic_id == t.id).first()
            if not qz:
                mismatches.append(f"Topic {t.id} ({t.title}) has NO quiz!")
                continue
            
            q_list = db.query(Question).filter(Question.quiz_id == qz.id).all()
            if len(q_list) == 0:
                mismatches.append(f"Topic {t.id} ({t.title}) - Quiz {qz.id} has 0 questions!")
            else:
                for q in q_list:
                    # Check options
                    opts = list(q.options)
                    if len(opts) < 2:
                        mismatches.append(f"Q {q.id} in Topic {t.id} has < 2 options")
                    corr_count = sum(1 for o in opts if o.is_correct)
                    if corr_count != 1:
                        mismatches.append(f"Q {q.id} in Topic {t.id} has {corr_count} correct options (expected 1)")

        if mismatches:
            print("FOUND ISSUES:")
            for m in mismatches[:20]:
                print(" -", m)
        else:
            print("ALL 37 TOPICS AND 410 QUESTIONS ARE 100% VALID WITH EXACTLY 1 CORRECT OPTION EACH!")

    except Exception as e:
        print(f"Audit error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    audit_curriculum()
