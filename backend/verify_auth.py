import sys
sys.path.append('.')
from app.database.session import SessionLocal, init_db
from app.api.auth import register
from app.schemas.auth import RegisterRequest

init_db()
db = SessionLocal()
try:
    payload = RegisterRequest(email='newuser123@example.com', username='newuser123', full_name='New User', password='password123')
    print(register(payload, db=db))
except Exception as e:
    import traceback
    traceback.print_exc()
finally:
    db.close()
