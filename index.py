from fastapi import FastAPI
from routes.address import address
app = FastAPI()
app.include_router(address)
