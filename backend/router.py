from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ProductResponse, ProductUpdate, ProductCreate
from typing import List
from crud import (
    create_product,
    get_products,
    get_product,
    delete_product,
    update_product
)

router = APIRouter()

### criar minha rota de buscar todos os itens
### sempre vamos ter 2 atributos obrigatorios, o PATH e o meu RESPONSE
@router.get("/products/", response_model=List[ProductResponse])
def read_all_products(db: Session = Depends(get_db)):
    products = get_products(db)
    return products

### criar minha rota de buscar 1 item
@router.get("/products/{product_id}", response_model=ProductResponse)
def read_one_product(product_id:int, db : Session = Depends(get_db)):
    db_product = get_product(db = db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="voce ta querendio buscar um produto que nao existe")
    return db_product

### criar minha rota de adicionar um item
@router.post("/products/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    

### criar minha rota de deletar um item
@router.delete

### criar minha rota de fazer update nos itens
@router.put