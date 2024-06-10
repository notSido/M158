from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)

    users = relationship("User", back_populates="department")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    username = Column(String(10), index=True)
    department_id = Column(Integer, ForeignKey('departments.id'), index=True)

    department = relationship("Departent", back_populates="users")
    assets = relationship("Asset", back_populates="user")

class Asset(Base):
    __tablename__ = "assets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    type = Column(String(255), index=True)
    serial_nr = Column(String(255), unique=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)

    user = relationship("User", back_populates="assets")
