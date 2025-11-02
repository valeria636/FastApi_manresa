from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from database import engine, get_session
from models import Product, ProductPublic, SQLModel

app = FastAPI()

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.post("/api/product")
def create_product(product: Product, db: Session = Depends(get_session)):
    db.add(product)
    db.commit()
    db.refresh(product)
    return {"message": "Producte afegit correctament"}

@app.get("/api/product", response_model=list[ProductPublic])
def read_products(db: Session = Depends(get_session)):
    products = db.exec(select(Product)).all()
    return products  # secret_code és sensible i no s’envia

@app.get("/api/product/{product_id}", response_model=ProductPublic)
def read_product_by_id(product_id: int, db: Session = Depends(get_session)):
    product = db.get(Product, product_id)
    return product

@app.get("/api/product/filter/{category}", response_model=list[ProductPublic])
def read_product_by_category(category: str, db: Session = Depends(get_session)):
    result = db.exec(select(Product).where(Product.category == category)).all()
    return result

@app.delete("/api/product/delete/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_session)):
    product = db.get(Product, product_id)
    db.delete(product)
    db.commit()
    return {"message": "Producte eliminat correctament"}
