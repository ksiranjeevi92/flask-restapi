from db import db
from sqlalchemy.orm import mapped_column, Mapped, relationship

class StoreModel(db.Model):
    __tablename__="stores"
    
    id:Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name:Mapped[str] = mapped_column(db.String(80), unique=True, nullable=False)
    items= relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")