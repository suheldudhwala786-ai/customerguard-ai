from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.models.base_mixin import BaseMixin

class Organization(Base, BaseMixin):
    __tablename__ = "organizations"

    name = Column(String(255), nullable=False, index=True)
    subscription_plan = Column(String(50), default="free")
    
    # Relationships
    users = relationship("User", back_populates="organization", cascade="all, delete-orphan")
    customers = relationship("Customer", back_populates="organization", cascade="all, delete-orphan")
    models = relationship("Model", back_populates="organization", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Organization(name='{self.name}', plan='{self.subscription_plan}')>"
