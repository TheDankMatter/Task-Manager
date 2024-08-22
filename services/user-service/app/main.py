from fastapi import FastAPI
from app.api import users, health 

app = FastAPI(
    title="User Service API",
    description="API for managing users within the Task Management Application",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(health.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)