from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy import Column, UUID, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column

from site_mgmt.schema import Base


# Database model, database table inferred from class name.
class Customer(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    country: str
    address: str
    postal_code: int
    phone_number: int
    email: str
    first_name: str
    first_name: str
    # reviews: list["Review"] = Relationship(back_populates="customer")
    # reviewedProducts: list["Product"] = Relationship(back_populates="customer")


class CustomerUpdate(Customer):
    first_name: str | None = None  # type: ignore.
    last_name: str | None = None
