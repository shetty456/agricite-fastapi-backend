from typing import List, Optional
from fastapi import APIRouter, HTTPException
from app.db.models import Module, Tag, Content, Question, Series
from app.schemas.schemas import (
    ContentResponseSchema,
    GetModulesRequestSchema,
    ModuleResponseSchema,
    QuestionResponseSchema,
)

router = APIRouter()


# /auth/login - Placeholder for future implementation
@router.post("/auth/login")
async def login():
    return {"message": "Login endpoint - Implement auth logic"}


# /auth/register - Placeholder for future implementation
@router.post("/auth/register")
async def register():
    return {"message": "Register endpoint - Implement auth logic"}


@router.get("/get_modules/", response_model=List[ModuleResponseSchema])
async def get_modules(query: GetModulesRequestSchema):
    if query.tag:
        modules = await Module.filter(tags__icontains=query.tag)
    else:
        modules = await Module.all()
    return modules


@router.get("/content", response_model=List[ContentResponseSchema])
async def get_content(
    module_name: Optional[str] = None, module_id: Optional[int] = None
):
    if module_name:
        content = await Content.filter(module_name=module_name)
    elif module_id:
        content = await Content.filter(module_id=module_id)
    else:
        content = await Content.all()
    return content


@router.get("/questions", response_model=List[QuestionResponseSchema])
async def get_questions(
    module_name: Optional[str] = None, module_id: Optional[int] = None
):
    if module_name:
        questions = await Question.filter(module_name=module_name)
    elif module_id:
        questions = await Question.filter(module_id=module_id)
    else:
        questions = await Question.all()
    return questions
