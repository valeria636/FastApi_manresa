import os
from typing import List
from fastapi import FastAPI, Depends
from dotenv import load_dotenv
from sqlalchemy.sql.functions import user
from sqlmodel import create_engine, Session, SQLModel, select

from database import get_session
from models import Product, ProductPublic, SQLModel

from models import Product

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)


SQLModel.metadata.create_all(engine)


app = FastAPI()


@app.post("/api/product")
def create_product(product: Product, db: Session = Depends(get_session)):
    db.add(product)
    db.commit()
    db.refresh(product)
    return {"message": "Producte afegit correctament"}

@app.get("/api/product", response_model=list[ProductPublic])
def read_products(db: Session = Depends(get_session)):
    products = db.exec(select(Product)).all()
    return products

@app.get("/api/product/{product_id}", response_model=ProductPublic)
def read_product_by_id(product_id: int, db: Session = Depends(get_session)):
    product = db.get(Product, product_id)
    return product

@app.get("/api/product/filter/{category}", response_model=list[ProductPublic])
def read_product_by_category(category: str, db: Session = Depends(get_session)):
    result = db.exec(select(Product).where(Product.category == category)).all()
    return result

def delete_product(product_id: int, db: Session = Depends(get_session)):
    product = db.get(Product, product_id)
    db.delete(product)
    db.commit()
    return {"message": "Producte eliminat correctament"}

