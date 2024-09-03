from fastapi import APIRouter, HTTPException, Header, status
from fastapi.params import Depends
from starlette.responses import RedirectResponse
from app.enums.user import USER_ROLE
from app.schemas.user import user_schema
from app.core.jwt import auth_token
from app.db.base import get_db, session
from app.services import user_service as controller

router = APIRouter(
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

@router.get('/users/getAll')
def get_users(db: session = Depends(get_db)):
    try:
        response = controller.get_all(db)
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error: get all users, detail: {e}",
        )

@router.post('/create/user')
def create_user(
        req: user_schema,
        authorization: str = Header(...),
        db: session = Depends(get_db)):
    try:
        if auth_token(authorization)['role'] != USER_ROLE.ADMIN:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail='Error: Error user not authorized'
            )
        response = controller.create_new_user(db, req)
        return response
    except Exception as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.detail)

@router.put('/update/user/{user_id}')
def update_task(
        req: user_schema,
        user_id: int,
        authorization: str = Header(...),
        db: session = Depends(get_db)):
    try:
        if auth_token(authorization)['role'] != USER_ROLE.ADMIN:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail='Error user not authorized'
            )

        response = controller.update_user(db, user_id, req)
        return response
    except Exception as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.detail)

@router.delete('/delete/user/{user_id}')
def delete_character(
        user_id: int,
        authorization: str = Header(...),
        db: session = Depends(get_db)):
    try:
        if auth_token(authorization)['role'] != USER_ROLE.ADMIN:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail='Error user not authorized'
            )
        user = controller.delete_user(db, user_id)
        return {"message": "User deleted successfully", "user": user}
    except Exception as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.detail)
