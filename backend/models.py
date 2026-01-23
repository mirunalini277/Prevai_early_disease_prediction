from sqlalchemy import Column, Integer, String, Date
from backend.database import Base
from sqlalchemy import Column, Integer, String, Text, Enum, TIMESTAMP
import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    role = Column(String(50))
    region = Column(String(100))

class HospitalRecord(Base):
    __tablename__ = "hospital_records"

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    region = Column(String(100))
    syndrome = Column(String(100))
    disease = Column(String(100))
    admissions = Column(Integer)
    icu_occupancy = Column(Integer)


class PressRelease(Base):
    __tablename__ = "press_releases"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    content = Column(Text)
    risk = Column(Enum("High","Medium","Normal"))
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)

