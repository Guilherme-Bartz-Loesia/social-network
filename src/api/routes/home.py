from fastapi import APIRouter
from src.datalayer.models.user import UserModel
from typing import Annotated
from fastapi import Depends
from src.api.authentication import verify_token

router = APIRouter(
    prefix="/me",
    tags=["me"],
    responses={404: {"description": "Not found"}},
)

# meu token: cJRy99RJy4ntFpKpfPXFR6T-iBU

@router.post("/")
async def my_informations(current_user: Annotated[UserModel, Depends(verify_token)]):
    return {'user': current_user}