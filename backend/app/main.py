from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ✅ Import router correctly
from app.routes.auth import router as auth_router

# 🚀 Create app
app = FastAPI(title="Asset Management API")

# 🔥 CORS (allow frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔗 Include auth router
app.include_router(auth_router, prefix="/auth", tags=["Auth"])

# 🏠 Root route
@app.get("/")
def root():
    return {"message": "API is running 🚀"}