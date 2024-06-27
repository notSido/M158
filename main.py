from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas, crud
from app.database import SessionLocal, engine

# Create all tables in the database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Department endpoints
@app.post("/departments/", response_model=schemas.Department)
def create_department(department: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    return crud.create_department(db=db, department=department)

@app.get("/departments/", response_model=List[schemas.Department])
def read_departments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    departments = crud.get_departments(db, skip=skip, limit=limit)
    return departments

@app.get("/departments/{department_id}", response_model=schemas.Department)
def read_department(department_id: int, db: Session = Depends(get_db)):
    db_department = crud.get_department(db, department_id=department_id)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return db_department

@app.put("/departments/{department_id}", response_model=schemas.Department)
def update_department(department_id: int, department: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    db_department = crud.update_department(db, department_id, department)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return db_department

@app.delete("/departments/{department_id}", response_model=schemas.Department)
def delete_department(department_id: int, db: Session = Depends(get_db)):
    db_department = crud.delete_department(db, department_id)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return db_department

# User endpoints
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.update_user(db, user_id, user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Asset endpoints
@app.post("/assets/", response_model=schemas.Asset)
def create_asset(asset: schemas.AssetCreate, db: Session = Depends(get_db)):
    return crud.create_asset(db=db, asset=asset)

@app.get("/assets/", response_model=List[schemas.Asset])
def read_assets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    assets = crud.get_assets(db, skip=skip, limit=limit)
    return assets

@app.get("/assets/{asset_id}", response_model=schemas.Asset)
def read_asset(asset_id: int, db: Session = Depends(get_db)):
    db_asset = crud.get_asset(db, asset_id=asset_id)
    if db_asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return db_asset

@app.put("/assets/{asset_id}", response_model=schemas.Asset)
def update_asset(asset_id: int, asset: schemas.AssetCreate, db: Session = Depends(get_db)):
    db_asset = crud.update_asset(db, asset_id, asset)
    if db_asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return db_asset

@app.delete("/assets/{asset_id}", response_model=schemas.Asset)
def delete_asset(asset_id: int, db: Session = Depends(get_db)):
    db_asset = crud.delete_asset(db, asset_id)
    if db_asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return db_asset
