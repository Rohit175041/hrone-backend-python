from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# ✅ Import routes and db using package prefix
from hrone_backend.routes.product_routes import router as product_router
from hrone_backend.routes.order_routes import router as order_router
from hrone_backend.db import connect_db

# Load environment variables from .env
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Connect to MongoDB
db = connect_db()

# Normalize URL paths (e.g. collapse // into /)
@app.middleware("http")
async def normalize_url_middleware(request: Request, call_next):
    scope = request.scope
    scope["path"] = os.path.normpath(scope["path"]).replace("\\", "/")
    return await call_next(request)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

#testing
@app.get("/ping")
def ping():
    return {"message": "ping"}

# Include routers
app.include_router(product_router)
app.include_router(order_router)

# Run manually (for local python run)
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 3000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
