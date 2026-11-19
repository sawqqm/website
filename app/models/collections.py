from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Collections(Base):
    __tablename__ = "collections"

    name: Mapped[str] = mapped_column()
    slug: Mapped[str]
    description: Mapped[str]
    is_active: Mapped[bool] = mapped_column()
    image_url: Mapped[str] = mapped_column()