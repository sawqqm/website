from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Cart(Base):
    __tablename__ = "carts"

    id: Mapped[int] = mapped_column()
    user_id: Mapped[int] = mapped_column()
    created_at: Mapped[str] = mapped_column()
    updated_at: Mapped[str] = mapped_column()

class CartItem(Base):
    __tablename__ = "cart_items"

    id: Mapped[int] = mapped_column()
    cart_id: Mapped[int] = mapped_column()
    product_id: Mapped[int] = mapped_column()
    quantity: Mapped[int] = mapped_column()
    created_at: Mapped[str] = mapped_column()
    updated_at: Mapped[str] = mapped_column()