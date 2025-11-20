from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

class Task(BaseModel):
    title: str
    done: bool = False

class UpdateTask(BaseModel):
    title: str | None = None
    done: bool | None = None

tasks: list[dict] = []

# Creates a new task
@router.post("/")
def create_task(task: Task):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "done": task.done
    }
    tasks.append(new_task)
    return new_task

# Displays tasks
@router.get("/")
def get_tasks(done: bool | None = None):
    if (done is None):
        return tasks
    return [t for t in tasks if t["done"] == done]

# Displays a specific task
@router.get("/{task_id}")
def get_task(task_id: int):
    for t in tasks:
        if t["id"] == task_id:
            return t
    return {"error": "Task not found"}


@router.put("/{task_id}")
def update_task(task_id: int, data: UpdateTask):
    for t in tasks:
        if t["id"] == task_id:
            if data.title is not None:
                t["title"] = data.title
            if data.done is not None:
                t["done"] = data.done
            return t
    return {"error": "Task not found"}


@router.delete("/{task_id}")
def delete_task(task_id: int):
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            return {"message": "Task deleted successfully"}
    return {"error": "Task not found"}
