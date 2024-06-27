from sqlalchemy.orm import Session
from . import models, schemas

# Asset CRUD Operations

def get_asset(db: Session, asset_id: int):
    return db.query(models.Asset).filter(models.Asset.id == asset_id).first()

def get_assets(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Asset).offset(skip).limit(limit).all()

def create_asset(db: Session, asset: schemas.AssetCreate):
    db_asset = models.Asset(**asset.dict())
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset

def update_asset(db: Session, asset_id: int, asset: schemas.AssetCreate):
    db_asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if db_asset:
        for key, value in asset.dict().items():
            setattr(db_asset, key, value)
        db.commit()
        db.refresh(db_asset)
    return db_asset

def delete_asset(db: Session, asset_id: int):
    db_asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if db_asset:
        db.delete(db_asset)
        db.commit()
    return db_asset

# User CRUD Operations

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        for key, value in user.dict().items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

# Department CRUD Operations

def get_department(db: Session, department_id: int):
    return db.query(models.Department).filter(models.Department.id == department_id).first()

def get_departments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Department).offset(skip).limit(limit).all()

def create_department(db: Session, department: schemas.DepartmentCreate):
    db_department = models.Department(**department.dict())
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department

def update_department(db: Session, department_id: int, department: schemas.DepartmentCreate):
    db_department = db.query(models.Department).filter(models.Department.id == department_id).first()
    if db_department:
        for key, value in department.dict().items():
            setattr(db_department, key, value)
        db.commit()
        db.refresh(db_department)
    return db_department

def delete_department(db: Session, department_id: int):
    db_department = db.query(models.Department).filter(models.Department.id == department_id).first()
    if db_department:
        db.delete(db_department)
        db.commit()
    return db_department
