from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.lib.db import get_session
from src.models.user import UserPublic
from src.services.users import list_users

router = APIRouter(tags=["users"])


@router.get("/users", response_model=list[UserPublic])
async def get_users(session: AsyncSession = Depends(get_session)) -> list[UserPublic]:
    rows = await list_users(session)
    return [UserPublic.model_validate(row) for row in rows]
