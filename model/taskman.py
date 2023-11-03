from model.model import Task, TaskList
import json
from pydantic import parse_file_as
from typing import List, Optional, Dict, Union

filepath = "data/tasks.json"

async def data_to_json(data: List[TaskList]):
    """Write a list of tasks to a JSON file."""
    data = json.dumps([task.dict() for task in data])
    with open(filepath, "w") as file:
        file.write(data)

async def get_tasks(id: Optional[int] = 0) -> Union[Dict[int, dict], dict]:
    """Fetch tasks by ID or return all tasks if ID is not provided."""
    tasks = parse_file_as(List[TaskList], "data/tasks.json")
    data = {task.id: task.dict() for task in tasks}
    response = data if id == 0 else data.get(id)
    return response

async def create_task(new_task: Task) -> int:
    """Create a new task and add it to the list of tasks, then update the JSON file."""
    tasks = parse_file_as(List[TaskList], "data/tasks.json")
    id = max([task.id for task in tasks]) + 1
    tasks.append(TaskList(id=id, task=new_task))
    await data_to_json(tasks)
    return id

async def delete_task(id: int) -> int:
    """Delete a task by ID and update the JSON file."""
    tasks = parse_file_as(List[TaskList], "data/tasks.json")
    tasks = [task for task in tasks if task.id != id]
    await data_to_json(tasks)
    return id

async def update_task(id: int, new_task: Task) -> int:
    """Update a task by ID with new task details and update the JSON file."""
    tasks = parse_file_as(List[TaskList], "data/tasks.json")
    for task in tasks:
        if task.id == id:
            task.task = new_task
    await data_to_json(tasks)
    return id
