import sqlite3
import os

db_path = 'wowcodes.db'
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("PRAGMA table_info(certificates)")
    cols = [col[1] for col in cursor.fetchall()]
    if 'student_name' not in cols:
        cursor.execute("ALTER TABLE certificates ADD COLUMN student_name VARCHAR(255)")
        print("Added student_name to certificates")
    if 'grade' not in cols:
        cursor.execute("ALTER TABLE certificates ADD COLUMN grade VARCHAR(100) DEFAULT 'Distinction (Grade A+)'")
        print("Added grade to certificates")
    if 'congrats_quote' not in cols:
        cursor.execute("ALTER TABLE certificates ADD COLUMN congrats_quote VARCHAR(500)")
        print("Added congrats_quote to certificates")

    cursor.execute("PRAGMA table_info(project_submissions)")
    p_cols = [col[1] for col in cursor.fetchall()]
    if 'grade' not in p_cols:
        cursor.execute("ALTER TABLE project_submissions ADD COLUMN grade VARCHAR(100)")
        print("Added grade to project_submissions")
    if 'score' not in p_cols:
        cursor.execute("ALTER TABLE project_submissions ADD COLUMN score FLOAT")
        print("Added score to project_submissions")
    if 'instructor_feedback' not in p_cols:
        cursor.execute("ALTER TABLE project_submissions ADD COLUMN instructor_feedback TEXT")
        print("Added instructor_feedback to project_submissions")
    if 'evaluated_by' not in p_cols:
        cursor.execute("ALTER TABLE project_submissions ADD COLUMN evaluated_by INTEGER")
        print("Added evaluated_by to project_submissions")

    conn.commit()
    conn.close()
    print("Database schema migration completed successfully on wowcodes.db!")
else:
    print("No local wowcodes.db found.")
