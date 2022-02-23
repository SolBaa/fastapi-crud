from fastapi import FastAPI
from typing import Optional
from routes.user import user

app = FastAPI()

app.include_router(user)
