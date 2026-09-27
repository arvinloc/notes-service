from fastapi import Depends, HTTPException, Request
from app.services.keycloak_client import KeyCloakClient

def get_keycloak_client(request:Request) -> KeyCloakClient:
    return request.app.state.keycloak_client

async def get_token_from_cookie(request: Request) -> str | None:
    return request.cookies.get("access_token")



# получение пользователя из cookie
async def get_current_user(
    token: str = Depends(get_token_from_cookie),
    keycloak: KeyCloakClient = Depends(get_keycloak_client),
) -> dict:
    if not token:
        raise HTTPException(status_code=401, detail="Unauthorized: No access token")

    try:
        user_info = await keycloak.get_user_info(token)
        return user_info
    except HTTPException:
        raise HTTPException(status_code=401, detail="Invalid token")