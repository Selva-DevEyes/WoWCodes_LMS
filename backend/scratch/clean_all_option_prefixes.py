"""Strip 'Correct: ' and 'Incorrect: ' prefixes from all database option records."""
import sys
from pathlib import Path

# Add backend directory to sys.path
backend_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(backend_dir))

from app.database.session import SessionLocal
from app.models.option import Option

def clean_prefixes():
    db = SessionLocal()
    try:
        options = db.query(Option).all()
        cleaned_count = 0
        prefixes = ["Correct: ", "Incorrect: ", "Correct choice: ", "Incorrect choice: "]

        for opt in options:
            original_text = opt.text
            for p in prefixes:
                if opt.text.startswith(p):
                    opt.text = opt.text[len(p):].strip()
                    cleaned_count += 1
                    break

        db.commit()
        print(f"Successfully cleaned prefixes from {cleaned_count} option records in DB!")
    except Exception as e:
        db.rollback()
        print(f"Error cleaning option prefixes: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    clean_prefixes()
