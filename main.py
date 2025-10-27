import os
from fastapi import FastAPI, Depends
from dotenv import load_dotenv
from sqlmodel import create_engine, Session, SQLModel, select
from models.User import User, UserRequest, UserResponse


load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)


SQLModel.metadata.cretae_all(engine)


def get_bd():
   db = Session(engine)
   try:
       yield db
   finally:
       db.close()


@app.post("/user", response_model=dict, tags=["CREATE"])
def addUser(user: UserRequest, db: Session = Depends(get_db)):
   #Convertir les dades del client a un model
   insert_user = User.model_validate(user)
   user(json)User(sql)
   db.add(insert_user)
   db.commit()
   return{"msg:""afegit usuari correctament"}


'''
from fastapi import FatAPI, Depends
from dotenv import load_dotenv
from sqlmodel import create_engine, Sessions, SQLModel, select
from .models.User import User, UserRequest, UserResponse
'''
