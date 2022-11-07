from celery.utils.log import get_task_logger
from django.contrib.auth import get_user_model

from config import celery_app
from config.celery_app import app

User = get_user_model()
task_logger = get_task_logger(__name__)


@app.task
def get_users_count():
    """A pointless Celery task to demonstrate usage."""
    task_logger.info("Count user")
    User.objects.filter(id=1).update(first_name="aaaaa")
    return User.objects.count()
