from pydantic import BaseModel, Field


class Item(BaseModel):
    id: int
    name: str = Field(min_length=3, max_length=50)
    price: float = Field(gt=0)
    is_offer: bool | None = None


class ItemCreate(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    price: float = Field(gt=0)
    is_offer: bool | None = None
