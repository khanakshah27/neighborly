from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Item(Base):
    __tablename__="items"
    id = Column(Integer, primary_key=True, index=True)
    title=Column(String,nullable=False)
    description=Column(String)
    category=Column(String)
    is_available=Column(Boolean, default=True)
    owner_id=Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")
    
class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    items = relationship("Item", back_populates="owner")

class Booking(Base):
    __tablename__="bookings"
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    borrower_id = Column(Integer, ForeignKey("users.id"))
    start_date = Column(String)
    end_date = Column(String)
    item = relationship("Item")
    borrower = relationship("User")
    
