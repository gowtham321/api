from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime


class Admin(BaseModel):
    name: str
    type: Literal["admin", "doctor", "patient"]
    user_id: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "name": "admin 1",
                "type": "admin",
                "user_id": "admin001",
                "password": "Password@123"
            }
        }

class Doctor(BaseModel):
    name: str
    type: Literal["admin", "doctor", "patient"]
    user_id: str
    password: str
    patients: list

    class Config:
        schema_extra = {
            "example": {
                "name": "doctor 1",
                "type": "doctor",
                "user_id": "doctor001",
                "password": "Password@123",
                "patients": ["13234", "341324"]
            }
        }

class Patient(BaseModel):
    name: str
    type: Literal["admin", "doctor", "patient"]
    user_id: str
    password: str
    data: list
    videos: list
    doctor: str


    class Config:
        schema_extra = {
            "example": {
                "name": "patien 1",
                "type": "patient",
                "user_id": "patient001",
                "password": "Password@123",
                "data": ["data1", "data2"],
                "videos": [],
                "doctor": "doctor001"
                
            }
        }
