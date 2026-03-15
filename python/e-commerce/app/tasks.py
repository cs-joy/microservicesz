import time
from datetime import datetime
from app.celery_app import celery

@celery.task(name="app.tasks.send_order_confirmation")
def send_order_confirmation(email: str, order_details: str):
    """BACKGROUND JOB: Simulate sending order confirmation email"""
    print(f"[BACKGROUND TASK START] Sending email to {email} | Details: {order_details}")
    time.sleep(5)  # Simulate email/network delay (real app: use SMTP, SendGrid, etc.)
    print(f"[BACKGROUND TASK DONE] ✅ Confirmation email sent to {email}")

@celery.task(name="app.tasks.daily_sales_report")
def daily_sales_report():
    """CRONJOB: Runs periodically (scheduled by Celery Beat)"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[CRONJOB {now}] Generating daily sales report...")
    time.sleep(2)  # Simulate report generation + DB query
    print(f"[CRONJOB {now}] ✅ Report sent to admin@ecommerce.com")