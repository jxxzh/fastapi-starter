from typing import List

from fastapi import APIRouter, HTTPException, Path
from server.core.logger import logger
from server.schemas.item import Item, ItemCreate

router = APIRouter(
    prefix="/items",
    tags=["items"],
)

# In-memory "database" - in production, this would be replaced with actual database
fake_items_db = [
    {"id": 1, "name": "Ginseng", "price": 50.5, "is_offer": False},
    {"id": 2, "name": "Goji Berry", "price": 65.0, "is_offer": True},
]


@router.get("/", response_model=List[Item])
async def get_items():
    """Retrieve all items."""
    logger.info("Retrieving all items")

    # Early return for empty database
    if not fake_items_db:
        logger.info("No items found in database")
        return []

    # Convert dict to Pydantic models for validation
    items = [Item(**item_data) for item_data in fake_items_db]
    logger.info(f"Successfully retrieved {len(items)} items")
    return items


@router.get("/{item_id}", response_model=Item)
async def get_item(
    item_id: int = Path(..., description="The ID of the item to retrieve", gt=0),
):
    """Retrieve a specific item by ID."""
    logger.info(f"Retrieving item with ID {item_id}")

    # Find item by ID
    item_data = next((item for item in fake_items_db if item["id"] == item_id), None)
    if not item_data:
        logger.warning(f"Item with ID {item_id} not found")
        raise HTTPException(status_code=404, detail="Item not found")

    logger.info(f"Successfully retrieved item with ID {item_id}")
    return Item(**item_data)


@router.post("/", response_model=Item, status_code=201)
async def create_item(item: ItemCreate):
    """Create a new item."""
    logger.info(f"Creating new item with data: {item.model_dump()}")

    # Validation checks
    if not item.name or len(item.name.strip()) < 3:
        logger.warning(f"Invalid item name: {item.name}")
        raise HTTPException(
            status_code=400, detail="Item name must be at least 3 characters"
        )

    if item.price <= 0:
        logger.warning(f"Invalid item price: {item.price}")
        raise HTTPException(status_code=400, detail="Item price must be greater than 0")

    # Check for duplicate names
    existing_item = next(
        (
            item_data
            for item_data in fake_items_db
            if item_data["name"].lower() == item.name.lower()
        ),
        None,
    )
    if existing_item:
        logger.warning(f"Item with name '{item.name}' already exists")
        raise HTTPException(
            status_code=409, detail="Item with this name already exists"
        )

    # Create new item
    new_id = (
        max(item_data["id"] for item_data in fake_items_db) + 1 if fake_items_db else 1
    )
    new_item_data = item.model_dump()
    new_item_data["id"] = new_id

    # Validate with Pydantic model
    new_item = Item(**new_item_data)

    # Add to database
    fake_items_db.append(new_item.model_dump())

    logger.info(f"Successfully created item '{new_item.name}' with ID {new_id}")
    return new_item
