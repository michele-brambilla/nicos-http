import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from nicos.clients.http.backend.src import detectors, devices, setups

log = logging.getLogger(__name__)


app = FastAPI()

origins = ["http://localhost:8080",
           "http://localhost", ]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(devices.router)
app.include_router(setups.router)
app.include_router(detectors.router)


@app.get("/")
async def root():
    return {"message": "Hello, NICOS!"}
