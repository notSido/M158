from pydantic import BaseModel
from typing import List, Optional

class AssetBase(BaseModel):
    name: str
    type: str
    serial_nr: str

class AssetCreate(AssetBase):
    user_id: int

class Asset(AssetBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    username: str

class UserCreate(UserBase):
    department_id: int

class User(UserBase):
    id: int
    department_id: int
    assets: List[Asset] = []

    class Config:
        orm_mode = True

class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id: int
    users: List[User] = []

    class Config:
        orm_mode = True
