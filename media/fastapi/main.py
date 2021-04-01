from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
import uvicorn
from sql_app import models, schemas, crud
from sql_app.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
	names = {}
	haha = []
	haha.append("jj")
	haha.append("jj")
	haha.append("jj")
	haha.append("jj")
	names['fname'] = haha

	# print(names['fname'])
	return templates.TemplateResponse("index.html",{"request": request, "names": haha})

@app.post("/form", response_model=schemas.UserInfo)
async def form(user: schemas.UserCreate, db: Session = Depends(get_db)):
	user.username = "Jereco"
	user.password = "Piso"
	user.fullname = "Anover"
	print(user.username)
	crud.create_user(db=db, user=user)
	# db_user = crud.get_user_by_username(db, username=user.username)
	# if db_user:
	#     raise HTTPException(status_code=400, detail="Username already registered")
	# return crud.create_user(db=db, user=user)
#username: str = Form(...), password: str = Form(...)