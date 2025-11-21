from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

class Task(BaseModel):
    title: str = Field(min_length=3)
    done: bool = False


tasks: list[dict] = []

class TaskResponse(BaseModel):
    id: int
    title: str
    done: bool

@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(task: Task):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "done": task.done
    }
    tasks.append(new_task)
    return new_task

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    for t in tasks:
        if t["id"] == task_id:
            return t
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found"
    )
