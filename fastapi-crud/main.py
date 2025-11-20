from fastapi import FastAPI

app = FastAPI()

# Tasks memory
tasks = []

@app.post("/tasks")
def create_task(title: str):
    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "done": False
    }
    tasks.append(new_task)
    return new_task

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/pending")
def pending_tasks():
    pending = []
    for t in tasks:
        if (t["done"] == False):
            pending.append(t)
    return pending

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for t in tasks:
        if (t["id"] == task_id):
            return t
    return {"error": "Task not found"}

@app.put("/tasks/{task_id}")
def update_task(task_id: int , title: str = None , done: bool = None):
    for t in tasks:
        if (t["id"] == task_id):
            if (title is not None):
                t["title"] = title
            if (done is not None):
                t["done"] = done
            return t
    return {"error": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for t in tasks:
        if (t["id"] == task_id):
            tasks.remove(t)
            return {"message": "Task deleted successfully"}
    return {"error": "Task not found"}
