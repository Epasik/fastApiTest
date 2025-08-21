from fastapi import FastAPI, Depends, Query, Path, status, HTTPException
from typing import Optional
from sqlalchemy.orm import Session
from app import schemas, crud, database

app = FastAPI(
    title="Test FastAPI CRUD Project",
    description="Проект для тестового задания (CRUD с PostgreSQL)",
    version="1.0.0"
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get(
    "/",
    summary="Root endpoint",
    description="Простейший эндпоинт, возвращающий приветственное сообщение",
    response_model=dict,
    status_code=status.HTTP_200_OK
)
def root():
    return {"message": "Hello!"}


@app.post(
    "/products/",
    summary="Создание продукта",
    description="Создает новый продукт в базе данных",
    response_model=schemas.ProductBase,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"description": "Ошибка валидации данных"},
        409: {"description": "Продукт с таким именем уже существует"}
    }
)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)


@app.get(
    "/products/",
    summary="Получить список продуктов",
    description="Возвращает список продуктов с возможностью фильтрации по имени и лимиту",
    response_model=list[schemas.ProductResponse],
    status_code=status.HTTP_200_OK,
)
def read_products(
    limit: int = Query(10, description="Максимальное количество полученных элементов"),
    name: Optional[str] = Query(None, description="Фильтр по имени продукта"),
    db: Session = Depends(get_db)
):
    return crud.get_products(db, limit=limit, name=name)


@app.get(
    "/product/",
    summary="Получить продукт по ID",
    description="Возвращает один продукт по его ID",
    response_model=schemas.ProductResponse,
    status_code=status.HTTP_200_OK,
    responses={404: {"description": "Продукт не найден"}}
)
def read_product(
    product_id: int = Query(..., description="ID продукта для поиска"),
    db: Session = Depends(get_db)
):
    return crud.get_product(db, product_id=product_id)


@app.get(
    "/products/{name}",
    summary="Поиск продуктов по имени",
    description="Возвращает список продуктов, которые содержат указанное имя",
    response_model=list[schemas.ProductResponse],
    status_code=status.HTTP_200_OK
)
def read_products_by_name(
    name: str = Path(..., description="Имя продукта для поиска"),
    db: Session = Depends(get_db)
):
    return crud.list_products(db, name=name)


@app.put("/products/{product_id}", response_model=schemas.ProductResponse,
         summary="Обновление продукта целиком",
         description="Обновляет все поля продукта по его ID")
def update_product(
    product_id: int,
    product_update: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    existing_product = crud.get_product(db, product_id=product_id)
    if not existing_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Продукт c таким ID не найден")
    
    updated_product = crud.update_product(db, product_id=product_id, product_update=product_update)
    return updated_product


@app.delete(
    "/product_delete/",
    summary="Удаление продукта",
    description="Удаляет продукт по его ID",
    response_model=schemas.ProductResponse,
    status_code=status.HTTP_200_OK,
    responses={404: {"description": "Продукт не найден"}}
)
def delete_product(
    product_id: int = Query(..., description="ID продукта для удаления"),
    db: Session = Depends(get_db)
):
    return crud.delete_product(db, product_id=product_id)
