from sqlalchemy import BigInteger, Integer, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class SaleItem(Base):
    __tablename__ = "sale_items"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True
    )
    sale_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("sales.id"),
        nullable=False,
    )
    product_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("products.id"),
        nullable=False,
    )
    quantity: Mapped[int] = mapped_column(
        Integer, nullable=False
    )
    unit_price: Mapped[float] = mapped_column(
        Numeric(12, 2), nullable=False
    )