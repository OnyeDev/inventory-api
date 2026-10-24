from fastapi import FastAPI
from app.routes.data import d_create, d_read, d_update, d_delete
from app.routes.user import u_create, u_read, u_update, u_delete

app = FastAPI(
  title = "Inventory Api",
  version = "1.0.0.0"
)