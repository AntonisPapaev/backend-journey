from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    title: str
    done: bool = False

# Tasks memory
tasks = []

# Creates tasks
@app.post("/tasks")
def create_task(task: Task):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "done": task.done
    }
    tasks.append(new_task)
    return new_task

# Shows all tasks
@app.get("/tasks")
def get_tasks():
    return tasks

class UpdateTask(BaseModel):
    title: str | None = None
    done: bool | None = None

#Shows tasks that are done
@app.get("/tasks/done")
def done_tasks():
    tasksdone = []
    for t in tasks:
        if (t["done"] == True):
            tasksdone.append(t)
    return tasksdone

# Updates a task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, data: UpdateTask):
    for t in tasks:
        if t["id"] == task_id:
            if data.title is not None:
                t["title"] = data.title
            if data.done is not None:
                t["done"] = data.done
            return t
    return {"error": "Task not found"}

# Deletes a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            return {"message": "Task deleted successfully"}
    return {"error": "Task not found"}


