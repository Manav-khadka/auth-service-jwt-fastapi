from fastapi import FastAPI
import model
from routes import router
from database import engine
app = FastAPI()
model.Base.metadata.create_all(bind=engine)

app.include_router(router)

    