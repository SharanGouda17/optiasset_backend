from fastapi import APIRouter, Depends
from app.dependencies import RequirePrivilege

router = APIRouter(prefix="/assets")

@router.delete("/{id}")
def delete_asset(id: int, user=Depends(RequirePrivilege("delete:asset"))):
    return {"message": f"Asset {id} deleted"}