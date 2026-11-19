from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Products(Base):
    __tablename__ = "products"
    
    id: Mapped[int] = mapped_column()
    name: Mapped[str] = mapped_column()
    slug: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    price: Mapped[float] = mapped_column()
    created_at: Mapped[datetime] = mapped_column()
    is_active: Mapped[bool] = mapped_column()