from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column()
    user_id: Mapped[int] = mapped_column()
    total_amount: Mapped[float] = mapped_column()
    status: Mapped[str] = mapped_column()
    created_at: Mapped[str] = mapped_column()
    updated_at: Mapped[str] = mapped_column()
    
class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column()
    order_id: Mapped[int] = mapped_column()
    product_id: Mapped[int] = mapped_column()
    quantity: Mapped[int] = mapped_column()
    price: Mapped[float] = mapped_column()
    created_at: Mapped[str] = mapped_column()
    updated_at: Mapped[str] = mapped_column()