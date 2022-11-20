import os
from dotenv import load_dotenv
from .celery import app as celery_app

PROJECT_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(PROJECT_BASE_DIR)
load_dotenv(os.path.join(PROJECT_BASE_DIR, ".env"))

__all__ = ("celery_app",)
