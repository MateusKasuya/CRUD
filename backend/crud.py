from sqlalchemy.orm import Session
from schemas import ProductUpdate, ProductCreate
from models import ProductModel

# get all (select * from)
def get_products(db: Session):
    return db.query(ProductModel).all()

# get where id = 1
def get_product(db: Session, product_id: int):
    return db.query(ProductModel).filter(ProductModel.id==product_id).first()