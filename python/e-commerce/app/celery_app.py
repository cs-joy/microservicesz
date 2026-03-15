from celery import Celery
from datetime import timedelta

celery = Celery("ecommerce")

# Redis configuration (matches docker-compose service name)
celery.conf.broker_url = "redis://redis:6379/0"
celery.conf.result_backend = "redis://redis:6379/1"

# Task routing + Beat schedule (cronjob)
celery.conf.task_routes = {
    "app.tasks.*": {"queue": "ecommerce-tasks"}
}

celery.conf.beat_schedule = {
    "daily-sales-report": {                  # ← CRONJOB
        "task": "app.tasks.daily_sales_report",
        "schedule": timedelta(seconds=30),   # Demo: every 30s. Change to crontab(hour=0) for daily midnight
        # "schedule": crontab(hour=0, minute=0),  # Uncomment for real daily cron
    },
}

# Auto-discover tasks
celery.autodiscover_tasks(["app.tasks"])

print("Celery configured with Broker/Backend + Beat schedule")