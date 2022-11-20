import os
from dotenv import load_dotenv
from .celery import app as celery_app

PROJECT_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(PROJECT_BASE_DIR, ".env"))

__all__ = ("celery_app",)
