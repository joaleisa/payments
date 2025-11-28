from fastapi import FastAPI

app = FastAPI(
    title="Payments API",
    description="track your payments",
    version="0.0.1",
)

#todo: middleware

#todo: routers
# app.include_router(router)

@app.get("/")
def root():
    return {"message": "Hello World"}