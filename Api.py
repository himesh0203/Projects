pip install fastapi uvicorn pydantic


# models.py
from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: Optional[int] = None  # Auto-generated in a real database
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    category: str



# main.py
from fastapi import FastAPI, HTTPException
from typing import List
from models import Product # Import the Product model

app = FastAPI()

# In a real application, this would be a database
products_db: List[Product] = []
next_product_id = 1

@app.post("/products/", response_model=Product)
async def create_product(product: Product):
    global next_product_id
    product.id = next_product_id
    products_db.append(product)
    next_product_id += 1
    return product

@app.get("/products/", response_model=List[Product])
async def get_products():
    return products_db

@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    for product in products_db:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products_db):
        if product.id == product_id:
            products_db[index] = updated_product
            products_db[index].id = product_id # Ensure ID remains the same
            return products_db[index]
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    global products_db
    initial_len = len(products_db)
    products_db = [product for product in products_db if product.id != product_id]
    if len(products_db) == initial_len:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}






uvicorn main:app --reload






