from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Adresses(Base):
    __tablename__ = "adresses"

    id: Mapped[int] = mapped_column()
    user_id: Mapped[int] = mapped_column()
    street: Mapped[str] = mapped_column()
    city: Mapped[str] = mapped_column()
    state: Mapped[str] = mapped_column()
    postal_code: Mapped[str] = mapped_column()
    country: Mapped[str] = mapped_column()
    created_at: Mapped[str] = mapped_column()
    updated_at: Mapped[str] = mapped_column()