from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from .core.config import settings
from .database import connect_to_mongo, close_mongo_connection
from .api.routes import auth, predict, dashboard

app = FastAPI(title=settings.PROJECT_NAME)

# Setup CORS — allow localhost for dev and all Vercel domains for production
origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://localhost",
    "https://mindcare1-self.vercel.app",  # Production Vercel URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_origin_regex=r"https://.*\.vercel\.app",  # Allows all Vercel preview & production URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(predict.router, prefix="/api/predict", tags=["predict"])
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["dashboard"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Mental Health Prediction API"}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
