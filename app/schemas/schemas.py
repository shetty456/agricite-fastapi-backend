from pydantic import BaseModel, EmailStr
from typing import List, Optional

# --- User Authentication and Registration ---

# Login Schema
class LoginRequestSchema(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True

# Register Schema
class RegisterRequestSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True

# User Response Schema
class UserResponseSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    is_active: bool
    is_superuser: bool
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True

# --- Modules and Categories ---

# Module Response Schema
class ModuleResponseSchema(BaseModel):
    id: int
    module_name: str
    module_desc: str
    module_image: Optional[str] = None
    tags: List[str]

    class Config:
        orm_mode = True

# Get Modules Request (with Filtering by Tags)
class GetModulesRequestSchema(BaseModel):
    tag: Optional[str] = None  # Filter by tag, if provided

    class Config:
        orm_mode = True

# Content Response Schema
class ContentResponseSchema(BaseModel):
    id: int
    name: str
    description: str
    image_urls: Optional[List[str]] = None
    module_name: str

    class Config:
        orm_mode = True

# --- Questions ---

# Question Response Schema
class QuestionResponseSchema(BaseModel):
    id: int
    question: str
    question_desc: Optional[str] = None
    image_url: Optional[str] = None
    options: List[str]  # List of option content
    module_name: str

    class Config:
        orm_mode = True

# --- Test Series ---

# Test Series Response Schema
class TestSeriesResponseSchema(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    created_at: str
    updated_at: str
    questions: List[QuestionResponseSchema]

    class Config:
        orm_mode = True

# --- Score ---

# Score Response Schema
class ScoreResponseSchema(BaseModel):
    id: int
    user_id: int
    test_series_id: int
    score: int
    total_score: int
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True

# Create Score Request Schema (For User Submission)
class CreateScoreRequestSchema(BaseModel):
    user_id: int
    test_series_id: int
    score: int
    total_score: int

    class Config:
        orm_mode = True

# --- Tag ---

# Tag Response Schema
class TagResponseSchema(BaseModel):
    id: int
    tag_name: str

    class Config:
        orm_mode = True

# --- Other Generic Schemas ---

# Generic Response Schema for Success/Error
class SuccessResponseSchema(BaseModel):
    message: str

    class Config:
        orm_mode = True
