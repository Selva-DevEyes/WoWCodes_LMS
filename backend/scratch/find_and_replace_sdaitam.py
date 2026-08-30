"""Replace all occurrences of WoWCodes, WoWCodes, WoWCodes, and WoWCodes across code files and database records with WoWCodes."""
import re
import sys
from pathlib import Path

lms_root = Path(__file__).resolve().parent.parent.parent
backend_dir = lms_root / "backend"
sys.path.insert(0, str(backend_dir))

from app.database.session import SessionLocal
from app.models.course import Course
from app.models.topic import Topic
from app.models.quiz import Quiz
from app.models.question import Question
from app.models.option import Option

def replace_in_db():
    db = SessionLocal()
    try:
        # Update Courses
        courses = db.query(Course).all()
        c_count = 0
        for c in courses:
            new_title = re.sub(r'WoWCodes[-\s]*WoWCodes[-\s]*\d*', 'WoWCodes', c.title, flags=re.IGNORECASE)
            new_title = re.sub(r'WoWCodes', 'WoWCodes', new_title, flags=re.IGNORECASE)
            new_title = re.sub(r'WoWCodes', 'WoWCodes', new_title, flags=re.IGNORECASE)
            if new_title != c.title:
                c.title = new_title
                c_count += 1

            new_slug = c.slug.replace('WoWCodes', 'wowcodes-sde-cert').replace('WoWCodes', 'wowcodes')
            if new_slug != c.slug:
                c.slug = new_slug

        # Update Topics
        topics = db.query(Topic).all()
        t_count = 0
        for t in topics:
            new_title = re.sub(r'WoWCodes[-\s]*WoWCodes[-\s]*\d*', 'WoWCodes', t.title, flags=re.IGNORECASE)
            new_title = re.sub(r'WoWCodes', 'WoWCodes', new_title, flags=re.IGNORECASE)
            new_title = re.sub(r'WoWCodes', 'WoWCodes', new_title, flags=re.IGNORECASE)
            if new_title != t.title:
                t.title = new_title
                t_count += 1

            if t.content:
                new_content = re.sub(r'WoWCodes[-\s]*WoWCodes[-\s]*\d*', 'WoWCodes', t.content, flags=re.IGNORECASE)
                new_content = re.sub(r'WoWCodes', 'WoWCodes', new_content, flags=re.IGNORECASE)
                new_content = re.sub(r'WoWCodes', 'WoWCodes', new_content, flags=re.IGNORECASE)
                t.content = new_content

            new_slug = t.slug.replace('WoWCodes', 'wowcodes-sde-cert').replace('WoWCodes', 'wowcodes')
            if new_slug != t.slug:
                t.slug = new_slug

        # Update Quizzes
        quizzes = db.query(Quiz).all()
        for qz in quizzes:
            new_title = re.sub(r'WoWCodes[-\s]*WoWCodes[-\s]*\d*', 'WoWCodes', qz.title, flags=re.IGNORECASE)
            new_title = re.sub(r'WoWCodes', 'WoWCodes', new_title, flags=re.IGNORECASE)
            new_title = re.sub(r'WoWCodes', 'WoWCodes', new_title, flags=re.IGNORECASE)
            qz.title = new_title

        # Update Questions
        questions = db.query(Question).all()
        for q in questions:
            new_text = re.sub(r'WoWCodes[-\s]*WoWCodes[-\s]*\d*', 'WoWCodes', q.text, flags=re.IGNORECASE)
            new_text = re.sub(r'WoWCodes', 'WoWCodes', new_text, flags=re.IGNORECASE)
            new_text = re.sub(r'WoWCodes', 'WoWCodes', new_text, flags=re.IGNORECASE)
            q.text = new_text

        db.commit()
        print(f"Updated DB records! Courses: {c_count}, Topics: {t_count}")
    except Exception as e:
        db.rollback()
        print(f"DB replacement error: {e}")
    finally:
        db.close()

def replace_in_files():
    file_count = 0
    extensions = {'.py', '.jsx', '.js', '.json', '.md', '.html', '.css', '.txt'}

    for path in lms_root.rglob('*'):
        if path.is_file() and path.suffix.lower() in extensions:
            # Skip venv, git, node_modules
            if any(part in path.parts for part in ['.venv', 'node_modules', '.git', '__pycache__', '.pytest_cache']):
                continue
            
            try:
                content = path.read_text(encoding='utf-8')
                new_content = re.sub(r'WoWCodes[-\s]*WoWCodes[-\s]*\d*', 'WoWCodes', content, flags=re.IGNORECASE)
                new_content = re.sub(r'WoWCodes', 'WoWCodes', new_content, flags=re.IGNORECASE)
                new_content = re.sub(r'WoWCodes', 'WoWCodes', new_content, flags=re.IGNORECASE)

                if new_content != content:
                    path.write_text(new_content, encoding='utf-8')
                    file_count += 1
                    print(f"Updated file: {path.name}")
            except Exception as e:
                pass

    print(f"Updated {file_count} project files!")

if __name__ == "__main__":
    replace_in_db()
    replace_in_files()
