import os
from dotenv import load_dotenv

load_dotenv()

# WhatsApp
WHATSAPP_API_TOKEN = os.getenv("WHATSAPP_API_TOKEN")
WHATSAPP_PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID")
WHATSAPP_BUSINESS_ACCOUNT_ID = os.getenv("WHATSAPP_BUSINESS_ACCOUNT_ID")
WHATSAPP_WEBHOOK_TOKEN = os.getenv("WHATSAPP_WEBHOOK_TOKEN")
WHATSAPP_API_URL = "https://graph.instagram.com/v18.0"

# Redis
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# Database
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./bot_jobs.db")

# App
APP_DEBUG = os.getenv("APP_DEBUG", "True") == "True"
APP_HOST = os.getenv("APP_HOST", "127.0.0.1")
APP_PORT = int(os.getenv("APP_PORT", "8000"))

# Storage
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./storage/uploads")
RESULT_DIR = os.getenv("RESULT_DIR", "./storage/results")

# Create storage directories if not exist
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(RESULT_DIR, exist_ok=True)

# Celery
CELERY_BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = REDIS_URL

# File limits
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB
SUPPORTED_FILE_TYPES = [".docx", ".xlsx", ".pdf", ".txt", ".csv"]

# Job history limit
MAX_JOBS_HISTORY = 50
