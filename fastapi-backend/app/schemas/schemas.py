from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# User Schemas
class UserBase(BaseModel):
    """Base user schema with common attributes."""
    email: EmailStr
    username: str


class UserCreate(UserBase):
    """Schema for creating a new user."""
    password: str


class UserUpdate(BaseModel):
    """Schema for updating a user."""
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None


class UserInDB(UserBase):
    """Schema for user in database."""
    id: int
    is_active: bool
    is_superuser: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = {"from_attributes": True}


class User(UserInDB):
    """Schema for user response."""
    pass


# Item Schemas
class ItemBase(BaseModel):
    """Base item schema with common attributes."""
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    """Schema for creating a new item."""
    pass


class ItemUpdate(BaseModel):
    """Schema for updating an item."""
    title: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None


class ItemInDB(ItemBase):
    """Schema for item in database."""
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = {"from_attributes": True}


class Item(ItemInDB):
    """Schema for item response."""
    pass


# Token Schemas
class Token(BaseModel):
    """Schema for authentication token."""
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Schema for token data."""
    username: Optional[str] = None
