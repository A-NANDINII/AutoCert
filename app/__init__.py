from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Add this to ensure the allowed extensions are available
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'csv'}

# Create upload directory if it doesn't exist
import os
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

from app import routes