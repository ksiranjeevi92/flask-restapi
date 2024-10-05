from db import db
from sqlalchemy.orm import mapped_column, Mapped, relationship

class ItemModel(db.Model):
    __tablename__="items"
    
    id:Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name:Mapped[str] = mapped_column(db.String(80), unique=True, nullable=False)
    price:Mapped[float] = mapped_column(db.Float(precision=2), unique=False, nullable=False)
    store_id:Mapped[int] = mapped_column(db.Integer,db.ForeignKey("stores.id"), unique=False, nullable=False )
    store= relationship("StoreModel", back_populates="items")
    