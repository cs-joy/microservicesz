from fastapi import FastAPI
from pydantic import BaseModel
from app.tasks import send_order_confirmation

app = FastAPI(
    title="E-commerce Order Microservice",
    description="FastAPI + Celery example (Background Tasks + Cronjobs)",
    version="1.0.0"
)

class OrderCreate(BaseModel):
    product_id: int
    quantity: int
    user_email: str

@app.post("/orders/", status_code=201)
def create_order(order: OrderCreate):
    """Create order → triggers BACKGROUND TASK"""
    order_id = 1001 + len(order.user_email)  # Simulate ID
    details = f"Order #{order_id} - {order.quantity}x Product #{order.product_id}"

    # Fire background job (non-blocking)
    send_order_confirmation.delay(order.user_email, details)

    return {
        "message": "Order created successfully!",
        "order_id": order_id,
        "note": "Confirmation email is being processed in the background by Celery Worker"
    }

@app.get("/")
def root():
    return {
        "status": "✅ E-commerce Order Microservice is running",
        "docs": "/docs",
        "services": ["API", "Celery Worker (background)", "Celery Beat (cron)"]
    }