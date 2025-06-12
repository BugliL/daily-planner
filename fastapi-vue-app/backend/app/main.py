from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router

app = FastAPI(
    title="Daily Planner API",
    description="API for managing daily tasks with a FastAPI backend and NoSQL database.",
    version="1.0.0",
    docs_url="/docs",         # Swagger UI
    redoc_url="/redoc"        # ReDoc UI
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Daily Planner API"}