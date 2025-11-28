from fastapi import FastAPI
from backend.routers import person_router, payment_method_router, user_router, payment_router

app = FastAPI(
    title="Payments API",
    description="track your payments",
    version="0.0.1",
)

#todo: middleware

#todo: routers
app.include_router(person_router.router)
app.include_router(payment_method_router.router)
app.include_router(user_router.router)
app.include_router(payment_router.router)

@app.get("/")
def root():
    return {"message": "Hello World"}

#todo: tabla personas y pagos