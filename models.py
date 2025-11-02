from sqlmodel import SQLModel, Field
from typing import Optional

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    stock: int
    category: str
    provider: str
    secret_code: str  # dada sensible

# Model sense dades sensibles
class ProductPublic(SQLModel):
    id: int
    name: str
    price: float
    stock: int
    category: str

