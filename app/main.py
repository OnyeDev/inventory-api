from fastapi import FastAPI
from routes.user import create, read, update, delete
from routes.data import create, read, update, delete

app = FastAPI()