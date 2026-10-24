from sqlalchemy import BigInteger, String, Numeric, Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True
    )
    name: Mapped[str] = mapped_column(
        String(150), nullable=False
    )
    price: Mapped[float] = mapped_column(
        Numeric(12, 2), nullable=False
    )
    stock_quantity: Mapped[int] = mapped_column(
        Integer, nullable=False, default=0
    )
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )