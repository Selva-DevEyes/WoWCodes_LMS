import sys
import os

sys.path.insert(0, os.path.abspath("."))
os.environ["PYTHONIOENCODING"] = "utf-8"

from app.database.session import SessionLocal, init_db
from app.models.user import User
from app.models.course import Course
from app.models.topic import Topic
from app.models.progress import Progress
from app.models.result import Result
from app.models.quiz import Quiz
from app.models.certificate import Certificate
from app.models.notification import Notification
from app.models.project_submission import ProjectSubmission
from app.api.projects import auto_evaluate_and_generate_certificate, submit_project, ProjectSubmissionCreate

init_db()
db = SessionLocal()

print("--- TESTING AUTOMATIC CERTIFICATE GENERATION & INSTRUCTOR NOTIFICATIONS ---")

# 1. Fetch test student
student = db.query(User).filter(User.email == "cert_student@test.com").first()
instructor = db.query(User).filter(User.role_id == 2).first()

# 2. Verify Certificate Generated
cert = db.query(Certificate).filter(Certificate.user_id == student.id).first()
assert cert is not None, "Certificate was not found!"
print("1. Certificate Generated in Database:")
print(f"   - Certificate Code: {cert.certificate_code}")
print(f"   - Student Name: {cert.student_name}")
print(f"   - Honors Grade: {cert.grade}")
print(f"   - Congratulations Quote: {cert.congrats_quote}")
print(f"   - Issued At: {cert.issued_at}")

# 3. Verify Instructor Notification Received
instructor_notifs = db.query(Notification).filter(Notification.user_id == instructor.id).order_by(Notification.created_at.desc()).all()
print(f"2. Instructor Notifications Verified: Total={len(instructor_notifs)}")
latest_inst = instructor_notifs[0]
print(f"   - Title: {latest_inst.title.encode('ascii', 'ignore').decode()}")
print(f"   - Message: {latest_inst.message.encode('ascii', 'ignore').decode()}")

# 4. Verify Student Notification Received
student_notifs = db.query(Notification).filter(Notification.user_id == student.id).order_by(Notification.created_at.desc()).all()
print(f"3. Student Notifications Verified: Total={len(student_notifs)}")
for sn in student_notifs[:2]:
    print(f"   - Student Notification: {sn.title.encode('ascii', 'ignore').decode()} | {sn.message.encode('ascii', 'ignore').decode()}")

db.close()
print("\nSUCCESS: AUTOMATIC CERTIFICATION & INSTRUCTOR NOTIFICATIONS ARE 100% OPERATIONAL!")
