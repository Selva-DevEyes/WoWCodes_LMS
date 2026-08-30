# Profile Image Upload Setup & Configuration

## Overview
This document explains the profile image upload system that persists images to the file system and stores references in the database.

## System Architecture

### Frontend (React + Vite)
- **Location**: `frontend/src/pages/student/ProfilePage.jsx`
- **API Endpoint**: `/users/me/avatar`
- **Accepted Formats**: PNG, JPEG, WebP
- **Max Size**: 5 MB
- **Method**: POST with multipart/form-data

### Backend (FastAPI)
- **Location**: `backend/app/api/users.py`
- **Storage**: `/backend/uploads/avatars/`
- **Database**: `users.avatar_url` (String field)
- **File Naming**: `user-{user_id}-{uuid}.{ext}`
- **URL Pattern**: `{base_url}/uploads/avatars/user-{user_id}-{uuid}.{ext}`

### Database Schema
```sql
-- User table (relevant fields)
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    avatar_url VARCHAR(500),  -- Full URL to the uploaded image
    ...
);
```

## Configuration Files

### 1. Frontend Vite Config (`frontend/vite.config.js`)
```javascript
server: {
  port: 5173,
  proxy: {
    '/api': {
      target: process.env.VITE_PROXY_TARGET || 'http://localhost:8000',  // ✅ FIXED: was 8001
      changeOrigin: true,
    },
  },
},
```

### 2. Backend Main App (`backend/app/main.py`)
```python
# Static files are served from /uploads directory
uploads_dir = Path(__file__).resolve().parents[1] / "uploads"
uploads_dir.mkdir(parents=True, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=uploads_dir), name="uploads")
```

### 3. Backend Upload Endpoint (`backend/app/api/users.py`)
- Validates file type and size
- Creates upload directory if missing
- Saves file with unique name
- Stores full URL in database
- Includes comprehensive error handling
- Rolls back database on file save failure

## Running the Application

### Start Backend (Port 8000)
```bash
cd backend
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Start Frontend (Port 5173)
```bash
cd frontend
npm install
npm run dev
```

### Access Points
- Frontend: `http://localhost:5173`
- API: `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`
- Uploaded Images: `http://localhost:8000/uploads/avatars/{filename}`

## Database Persistence

### How Images Are Stored
1. **File Storage**: Binary image data saved to `/backend/uploads/avatars/`
2. **Database Record**: User's `avatar_url` field updated with full URL
3. **Recovery**: Images persist even after server restart

### Image URL Format
```
http://localhost:8000/uploads/avatars/user-{user_id}-{uuid}.{ext}
```

Example:
```
http://localhost:8000/uploads/avatars/user-42-a1b2c3d4e5f6.jpg
```

## Troubleshooting

### Issue: "Failed to upload profile image"

**Solution 1: Check Proxy Port**
- Ensure backend is running on port 8000
- Verify `vite.config.js` has `target: 'http://localhost:8000'`
- Clear browser cache and restart frontend

**Solution 2: Check Uploads Directory**
```bash
# Windows
dir backend\uploads\avatars

# Linux/Mac
ls -la backend/uploads/avatars/
```

**Solution 3: Check Backend Logs**
- Look for error messages in terminal running backend
- Check for permission issues with uploads directory
- Verify database connection is working

**Solution 4: Check Frontend Console**
- Open DevTools (F12) → Console
- Look for detailed error messages
- Check Network tab to see API response

### Issue: Image Uploads but Doesn't Display

**Check:**
1. Database was updated: Query `SELECT avatar_url FROM users WHERE id = ?`
2. File exists: Check `/backend/uploads/avatars/` directory
3. File URL is accessible: Try opening the URL directly in browser
4. CORS is configured: Backend CORS middleware should allow image requests

## Database Queries

### View User Avatar URL
```sql
SELECT id, username, avatar_url FROM users WHERE id = 1;
```

### Update Avatar (Manual)
```sql
UPDATE users SET avatar_url = 'http://localhost:8000/uploads/avatars/filename.jpg' WHERE id = 1;
```

### Clear Avatar (Manual)
```sql
UPDATE users SET avatar_url = NULL WHERE id = 1;
```

## Production Deployment

For production, consider:

1. **Cloud Storage**: Use S3, Azure Blob, or GCP Cloud Storage
2. **Database Only**: Store base64-encoded images in database
3. **CDN**: Serve images through CDN for faster delivery
4. **Image Processing**: Add thumbnail generation, compression, etc.

### Example: Storing in Database (SQLAlchemy)
```python
from sqlalchemy import LargeBinary

class User(Base):
    image_data: Mapped[bytes] = mapped_column(LargeBinary, nullable=True)
    image_mime_type: Mapped[str] = mapped_column(String(50), nullable=True)
```

## Performance Optimization

### Current Setup
- Files stored on local file system
- URLs stored in database
- Good for development and small deployments

### For Better Performance
1. Add image compression before saving
2. Generate thumbnails for profile previews
3. Implement image lazy-loading on frontend
4. Cache images in CDN
5. Add image metadata (dimensions, size) to database

## Security Considerations

### Currently Implemented
- ✅ File type validation (PNG, JPEG, WebP only)
- ✅ File size limit (5 MB max)
- ✅ Authentication required (JWT token)
- ✅ User-specific directory isolation

### Recommended Additional Measures
- Scan images for malware before storing
- Validate image MIME type (not just extension)
- Implement rate limiting on upload endpoint
- Add virus scanning for production
- Store files outside web root for production
- Use secure file storage with encryption

## Testing the Upload

### Manual Test Steps
1. Go to `http://localhost:5173/profile`
2. Click "Upload image" button
3. Select a PNG/JPEG/WebP image (< 5 MB)
4. Verify success message appears
5. Refresh page and confirm image persists
6. Check backend console for any errors
7. Verify file exists in `/backend/uploads/avatars/`

### Automated Test
```python
# In backend tests
import pytest
from fastapi.testclient import TestClient

def test_upload_avatar(client, current_user_token):
    with open("test_image.jpg", "rb") as img:
        response = client.post(
            "/api/v1/users/me/avatar",
            files={"image": img},
            headers={"Authorization": f"Bearer {current_user_token}"}
        )
    assert response.status_code == 200
    assert "uploads/avatars" in response.json()["avatar_url"]
```

## Recent Fixes (v1.1)

### Fixed Issues
- ✅ Proxy port corrected from 8001 to 8000
- ✅ Enhanced error handling in upload endpoint
- ✅ Added database transaction safety (rollback on failure)
- ✅ Improved error messages in frontend
- ✅ Added console logging for debugging

### Changes Made
1. `frontend/vite.config.js` - Fixed proxy target port
2. `backend/app/api/users.py` - Enhanced upload endpoint with better error handling
3. `frontend/src/pages/student/ProfilePage.jsx` - Improved error messages and logging

## Next Steps

1. Test the upload functionality
2. Verify images persist after server restart
3. Check database for avatar_url entries
4. Monitor backend logs for any warnings
5. Consider adding image optimization pipeline
