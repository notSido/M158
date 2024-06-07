from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class AssetBase(BaseModel):
    name: str
    type: str
    location_id: int
    serial_number: str
    purchase_date: date
    warranty_expiration: date
    status: str
    assigned_to: Optional[int] = None
    last_maintenance: Optional[date] = None
    notes: Optional[str] = None

class AssetCreate(AssetBase):
    pass

class Asset(AssetBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str
    department_id: int

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    assets: List[Asset] = []

    class Config:
        orm_mode = True

class MaintenanceRecordBase(BaseModel):
    asset_id: int
    maintenance_date: date
    description: str

class MaintenanceRecordCreate(MaintenanceRecordBase):
    pass

class MaintenanceRecord(MaintenanceRecordBase):
    id: int

    class Config:
        orm_mode = True

class LocationBase(BaseModel):
    name: str
    address: str

class LocationCreate(LocationBase):
    pass

class Location(LocationBase):
    id: int
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
