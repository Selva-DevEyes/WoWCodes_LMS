"""Clean 'Correct: ' and 'Incorrect: ' from seed_final_exam_50_questions.py."""
import re
from pathlib import Path

target_file = Path(__file__).resolve().parent / "seed_final_exam_50_questions.py"
content = target_file.read_text(encoding="utf-8")
cleaned = re.sub(r'\"(Incorrect|Correct):\s*', '"', content)
target_file.write_text(cleaned, encoding="utf-8")
print("Cleaned seeder script successfully!")
