from fastapi import APIRouter, HTTPException, status
from app.schemas.todos import TodoCreate, TodoUpdate, TodoResponse
from app.db.models import Todo
from typing import List

router = APIRouter()

async def get_todo_or_404(todo_id: int) -> Todo:
    todo = await Todo.get_or_none(id=todo_id)
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return todo


@router.post("/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoCreate):
    new_todo = await Todo.create(**todo.dict())
    return TodoResponse.model_validate(new_todo)


@router.get("/", response_model=List[TodoResponse])
async def list_todos():
    todos = await Todo.all()
    return [TodoResponse.model_validate(todo) for todo in todos]


@router.get("/{todo_id}", response_model=TodoResponse)
async def get_todo(todo_id: int):
    todo = await get_todo_or_404(todo_id)
    return TodoResponse.model_validate(todo)


@router.put("/{todo_id}", response_model=TodoResponse)
async def update_todo(todo_id: int, todo_update: TodoUpdate):
    todo = await get_todo_or_404(todo_id)
    await todo.update_from_dict(todo_update.dict(exclude_unset=True))
    await todo.save()
    return TodoResponse.model_validate(todo)


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int):
    todo = await get_todo_or_404(todo_id)
    await todo.delete()
    return None
