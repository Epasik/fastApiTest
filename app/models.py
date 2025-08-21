from sqlalchemy import Column, Integer, String, Float, Boolean, Numeric
from app.database import Base

# SQLAlchemy модели, которые создадут таблицу в PostgreSQL
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True,)
    description = Column(String,nullable=True)
    price = Column(Numeric(10,2), nullable=False)
    in_stock = Column(Boolean, default=True)