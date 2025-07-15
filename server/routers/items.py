from http import HTTPStatus

from fastapi import APIRouter
from server.core.decorators import response_wrapper
from server.schemas.api import APIError, APIResponseModel
from server.schemas.item import Item, ItemCreate
from starlette.requests import Request

router = APIRouter()


# 模拟一个数据库或服务层
fake_items_db = {
    1: {"id": 1, "name": "Foo", "price": 50.2, "is_offer": False},
    2: {"id": 2, "name": "Bar", "price": 65.2, "is_offer": True},
}


@router.get("", response_model=APIResponseModel[list[Item]])  # 修正 response_model
@response_wrapper
async def read_items(request: Request, skip: int = 0, limit: int = 100):
    """
    获取项目列表
    """
    return list(fake_items_db.values())[skip : skip + limit]


@router.post(
    "", response_model=APIResponseModel[Item], status_code=201
)  # 修正 response_model
@response_wrapper
async def create_item(request: Request, item: ItemCreate):
    """
    创建一个新项目
    """
    item_id = max(fake_items_db.keys()) + 1
    new_item = Item(id=item_id, **item.model_dump())
    fake_items_db[item_id] = new_item.model_dump()
    return new_item


@router.get("/{item_id}", response_model=APIResponseModel[Item])  # 修正 response_model
@response_wrapper
async def read_item(request: Request, item_id: int):
    """
    根据 ID 获取单个项目
    - **item_id**: 项目的 ID
    """
    if item_id not in fake_items_db:
        raise APIError(
            status_code=HTTPStatus.NOT_FOUND.value,
            message=f"ID 为 {item_id} 的项目不存在",
        )
    return fake_items_db[item_id]
