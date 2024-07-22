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
    """
    Essa é minha rota de ler todos os produtos do banco de dados
    """
    products = get_products(db)
    return products

### criar minha rota de buscar 1 item
@router.get("/products/{product_id}", response_model=ProductResponse)
def read_one_product(product_id:int, db : Session = Depends(get_db)):
    db_product = get_product(db = db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="voce ta querendo buscar um produto que nao existe")
    return db_product

### criar minha rota de adicionar um item
@router.post("/products/", response_model=ProductResponse)
def create_product_route(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(product=product, db = db)

### criar minha rota de deletar um item
@router.delete("/products/{product_id}", response_model=ProductResponse)
def delete_product_route(product_id: int, db: Session = Depends(get_db)):
    product_db = delete_product(product_id = product_id, db = db)
    if product_db is None:
        raise HTTPException(status_code=404, detail="voce ta querendo deletar um produto que nao existe")
    return product_db

### criar minha rota de fazer update nos itens
@router.put("/products/{product_id}", response_model=ProductResponse)
def atualizar_product_route(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    product_db = update_product(db = db, product_id=product_id, product = product)
    if product_db is None:
        raise HTTPException(status_code=404, detail="voce ta querendo fazer um update de um produto que nao existe")
    return product_db