from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.core.database import engine, get_db
from app.models import base
from app.core.database import Base
from app.models.user import User
from app.models.financial import BankAccount, Category, Transaction

import uvicorn

# Create database tables
#Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Financial Dashboard API",
    description="API for financial dashboard with bank statement processing",
    version="0.1.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Financial Dashboard API", "version": "0.1.0"}

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    return {"status": "healthy", "database": "connected"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)