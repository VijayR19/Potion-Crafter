from typing import Union
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from routes import discovery_route, user_route

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routes
app.include_router(discovery_route.router)
app.include_router(user_route.router)

# Exception handler
@app.exception_handler(Exception)
async def internal_server_error_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message":"An internal server error occurred."}
    )