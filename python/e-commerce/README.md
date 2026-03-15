**Complete Example: E-commerce Order Microservice with FastAPI + Celery**

This is a **production-ready microservices architecture** example using:
- **FastAPI** as the API service (handles HTTP requests, e.g., creating orders).
- **Celery Worker** as the background job service (asynchronous tasks like sending order confirmation emails).
- **Celery Beat** as the cronjob scheduler service (periodic tasks like daily sales reports).
- **Redis** as the message broker/result backend (connects the services).

This demonstrates real microservices separation:
- API service (scalable horizontally).
- Background worker service (heavy async work).
- Scheduler (cron) service.
- Shared Redis.

**E-commerce context**: When a customer places an order → background task sends confirmation email. Every 30 seconds (demo) or daily (production) → cronjob generates/sends sales report.

---

### 1. Project Structure
