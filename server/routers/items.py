from fastapi import APIRouter
from server.core.logger import logger
from server.schemas.item import Item, ItemCreate

router = APIRouter(
    prefix="/items",
    tags=["items"],
)

# In-memory "database"
fake_items_db = [
    {"id": 1, "name": "Ginseng", "price": 50.5, "is_offer": False},
    {"id": 2, "name": "Goji Berry", "price": 65.0, "is_offer": True},
]


@router.get("/", response_model=list[Item])
async def read_items():
    """Retrieve all items."""
    logger.info("Retrieving all items")
    return fake_items_db


@router.post("/", response_model=Item, status_code=201)
async def create_item(item: ItemCreate):
    """Create a new item."""
    logger.info(f"Creating new item with data: {item.model_dump()}")
    new_id = max(i["id"] for i in fake_items_db) + 1 if fake_items_db else 1
    new_item_data = item.model_dump()
    new_item_data["id"] = new_id
    new_item = Item(**new_item_data)
    fake_items_db.append(new_item.model_dump())
    logger.info(f"Successfully created item '{new_item.name}' with ID {new_id}")
    return new_item
