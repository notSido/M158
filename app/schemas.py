from pydantic import BaseModel

class AssetBase(BaseModel):
    name: str
    type: str
    location: str

class AssetCreate(AssetBase):
    pass

class Asset(AssetBase):
    id: int

    class Config:
        orm_mode = True
