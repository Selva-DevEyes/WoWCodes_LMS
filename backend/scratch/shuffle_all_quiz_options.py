"""Shuffle options order for all questions across all quizzes in the database to randomize the correct option index."""
import sys
import random
from pathlib import Path

backend_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(backend_dir))

from app.database.session import SessionLocal
from app.models.question import Question
from app.models.option import Option

def shuffle_options():
    db = SessionLocal()
    try:
        questions = db.query(Question).all()
        shuffled_q_count = 0
        pos_distribution = {0: 0, 1: 0, 2: 0, 3: 0}

        # Seed random for deterministic reproducible shuffle
        random.seed(42)

        for q in questions:
            opts = list(q.options)
            if len(opts) > 1:
                # Shuffle options list
                random.shuffle(opts)
                
                # Re-assign database order/IDs by deleting and re-inserting or updating attributes
                opt_data = [(o.text, o.is_correct) for o in opts]
                
                # Clear existing option records for this question
                db.query(Option).filter(Option.question_id == q.id).delete(synchronize_session=False)
                db.flush()

                # Re-create options in newly shuffled order
                for idx, (text_val, is_corr) in enumerate(opt_data):
                    new_opt = Option(
                        question_id=q.id,
                        text=text_val,
                        is_correct=is_corr
                    )
                    db.add(new_opt)
                    if is_corr:
                        pos_distribution[idx] = pos_distribution.get(idx, 0) + 1
                
                shuffled_q_count += 1

        db.commit()
        print(f"Successfully shuffled option choices across {shuffled_q_count} questions!")
        print("Correct Option Position Distribution after shuffling:", pos_distribution)
    except Exception as e:
        db.rollback()
        print(f"Error shuffling quiz options: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    shuffle_options()
