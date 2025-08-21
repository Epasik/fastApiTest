from sqlalchemy.orm import Session
from app import models, schemas

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.model_dump())  # распаковываем поля Pydantic в модель SQLAlchemy
    db.add(db_product)  
    db.commit()         
    db.refresh(db_product)  
    return db_product

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def get_products(db: Session, limit: int = 10, name: str = None):
    query = db.query(models.Product)
    if name:
        query = query.filter(models.Product.name.ilike(f"%{name}%"))
    return query.limit(limit).all()

def list_products(db: Session, name: str = None):
    query = db.query(models.Product)
    if name:
        query = query.filter(models.Product.name.ilike(f"%{name}%"))  # фильтр по имени
    return query.all()


def update_product(db: Session, product_id: int, product_update: schemas.ProductCreate):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        return None
    
    update_data = product_update.model_dump()
    for key, value in update_data.items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        return None
    db.delete(db_product)
    db.commit()
    return db_product