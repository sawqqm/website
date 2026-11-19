from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Payments(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column()
    order_id: Mapped[int] = mapped_column()
    payment_method: Mapped[str] = mapped_column()
    amount: Mapped[float] = mapped_column()
    status: Mapped[str] = mapped_column()
    created_at: Mapped[str] = mapped_column()
    updated_at: Mapped[str] = mapped_column()