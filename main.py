from fastapi import FastAPI

from fastapi.encoders import jsonable_encoder
from model.model import Task
import model.taskman as taskman

app = FastAPI()

@app.get("/api/tasks")
async def get_tasks():
    """Fetch the list of all tasks."""
    return await taskman.get_tasks()

@app.get("/api/tasks/{id}")
async def get_task(id: int):
    """Fetch the task by id."""
    return await taskman.get_tasks(id)

@app.post("/api/tasks/create")
async def create_task(task: Task):
    """Create a new task and return the details of the task."""
    id = await taskman.create_task(task)
    return {"id": id, "task": task.dict()}

@app.put("/api/tasks/{id}/update")
async def update_task(id: int, task: Task):
    """Update the task by id and return the updated task."""
    await taskman.update_task(id, task)
    return {"id": id, "task": task.dict()}

@app.delete("/api/tasks/{id}/delete")
async def delete_task(id: int):
    """Delete the task by id and return a confirmation of deletion."""
    await taskman.delete_task(id)
    return {"id": id, "message": "Task successfully deleted"}
