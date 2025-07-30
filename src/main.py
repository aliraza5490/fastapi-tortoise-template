from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from src.lifespan import lifespan
from src.routes import api_router
from src.settings import settings
from tortoise.contrib.fastapi import tortoise_exception_handlers
from pydantic import BaseModel
from inspirational_quotes import quote

app = FastAPI(title="FastAPI Template", description="API documentation", version="1.0.0", lifespan=lifespan, exception_handlers=tortoise_exception_handlers())

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.all_cors_origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


class Health(BaseModel): 
    message: str
    quote: str

@app.get("/", tags=["health"], response_model=Health, summary="Health Route", description="This is a health route for checking server status.")
def read_root():
    qt = quote()
    return {"message": "Hello World!", "quote": qt.get("quote", "No quote available")}

app.include_router(api_router)