"""End-to-end API test for WoWCodes backend."""
from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)

# 1. Register test student (idempotent)
client.post("/api/v1/auth/register", json={
    "email": "student@test.com",
    "username": "student1",
    "full_name": "Test Student",
    "password": "password123",
})

# 2. Login
login = client.post("/api/v1/auth/login", json={
    "email": "student@test.com",
    "password": "password123",
})
assert login.status_code == 200, f"Login failed: {login.status_code}"
print("0. Register + Login OK")
token = login.json()["access_token"]
headers = {"Authorization": f"Bearer {token}"}
print("1. Login OK")

# 2. Dashboard stats
stats = client.get("/api/v1/progress/dashboard", headers=headers)
assert stats.status_code == 200, f"Dashboard failed: {stats.status_code}"
print("2. Dashboard stats:", stats.json())

# 3. Get JavaScript course
courses = client.get("/api/v1/courses").json()
js = next((c for c in courses if c["slug"] == "javascript"), None)
assert js is not None, "JavaScript course not found"
print("3. JS course found:", js["id"])

# 4. Get topics for JS course
topics = client.get(f"/api/v1/topics/course/{js['id']}").json()
assert len(topics) > 0, "No topics found"
print("4. JS topics:", len(topics))

# 5. Get quiz for variables topic and submit
var_topic = next((t for t in topics if "variables" in t["slug"]), None)
if var_topic:
    quizzes = client.get(f"/api/v1/quiz/topic/{var_topic['id']}").json()
    print("5. Quizzes for variables:", len(quizzes))
    if quizzes:
        quiz_id = quizzes[0]["id"]
        quiz_detail = client.get(f"/api/v1/quiz/{quiz_id}").json()
        print("   Quiz questions:", len(quiz_detail["questions"]))
        answers = []
        for q in quiz_detail["questions"]:
            correct = next(o for o in q["options"] if o["is_correct"])
            answers.append({
                "question_id": q["id"],
                "selected_option_id": correct["id"],
            })
        result = client.post(
            f"/api/v1/quiz/{quiz_id}/submit",
            headers=headers,
            json={"quiz_id": quiz_id, "time_taken_seconds": 60, "answers": answers},
        )
        print("   Quiz submit:", result.status_code, result.json().get("percentage"))
else:
    print("5. Variables topic not found, skipping quiz test")

# 6. Notes CRUD
note = client.post("/api/v1/notes", headers=headers, json={
    "topic_id": topics[0]["id"],
    "title": "Test Note",
    "content": "Hello world",
})
assert note.status_code == 201, f"Note create failed: {note.status_code}"
notes = client.get("/api/v1/notes", headers=headers)
assert len(notes.json()) > 0, "Notes list is empty"
print("6. Notes CRUD OK")

# 7. Search
search = client.get("/api/v1/search", params={"q": "React"})
assert search.status_code == 200, "Search failed"
print("7. Search React:", len(search.json()), "results")

# 8. Leaderboard
lb = client.get("/api/v1/users/leaderboard")
assert lb.status_code == 200, "Leaderboard failed"
print("8. Leaderboard:", len(lb.json()), "entries")

# 9. Progress update
progress = client.post(
    f"/api/v1/progress/topic/{topics[0]['id']}",
    headers=headers,
    json={"is_completed": True},
)
assert progress.status_code == 200, f"Progress update failed: {progress.status_code}"
print("9. Progress update OK")

# 10. Notifications
notifs = client.get("/api/v1/notifications", headers=headers)
assert notifs.status_code == 200, "Notifications failed"
unread = client.get("/api/v1/notifications/unread-count", headers=headers)
print("10. Notifications:", len(notifs.json()), "total,", unread.json()["count"], "unread")

print("\n[OK] ALL TESTS PASSED!")