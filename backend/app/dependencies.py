from fastapi import Depends, HTTPException
from app.auth import get_current_user

def RequirePrivilege(permission: str):
    def checker(user=Depends(get_current_user)):
        if "permissions" not in user or permission not in user["permissions"]:
            raise HTTPException(status_code=403, detail="Not allowed")
        return user
    return checker