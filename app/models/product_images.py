from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class ProductImage(Base):
    __tablename__ = "product_images"
    
    id: Mapped[int] = mapped_column()
    product_id: Mapped[int] = mapped_column()
    image_url: Mapped[str] = mapped_column()
    is_primary: Mapped[bool] = mapped_column()