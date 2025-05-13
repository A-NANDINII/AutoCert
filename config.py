import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
UPLOAD_FOLDER = BASE_DIR / 'app' / 'static' / 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'csv'}

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-123'
    UPLOAD_FOLDER = UPLOAD_FOLDER
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB