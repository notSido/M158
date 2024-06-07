from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Asset(Base):
    __tablename__ = "assets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    type = Column(String(255), index=True)
    location_id = Column(Integer, ForeignKey('locations.id'), index=True)
    serial_number = Column(String(255), unique=True, index=True)
    purchase_date = Column(Date)
    warranty_expiration = Column(Date)
    status = Column(String(50))
    assigned_to = Column(Integer, ForeignKey('users.id'))
    last_maintenance = Column(Date)
    notes = Column(String(500))

    location = relationship("Location", back_populates="assets")
    user = relationship("User", back_populates="assets")
    maintenance_records = relationship("MaintenanceRecord", back_populates="asset")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)
    department_id = Column(Integer, ForeignKey('departments.id'))

    assets = relationship("Asset", back_populates="user")
    department = relationship("Department", back_populates="users")


class MaintenanceRecord(Base):
    __tablename__ = "maintenance_records"
    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, ForeignKey('assets.id'))
    maintenance_date = Column(Date)
    description = Column(String(500))

    asset = relationship("Asset", back_populates="maintenance_records")


class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    address = Column(String(255))

    assets = relationship("Asset", back_populates="location")


class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)

    users = relationship("User", back_populates="department")
