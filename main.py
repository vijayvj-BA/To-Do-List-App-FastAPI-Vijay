from fastapi import FastAPI
from task_class import Task
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


tasks_list = []

task1 = Task(id = 1, name="Pay Credit card bills", description="Pay all the three credit card bills before due date")
task2 = Task(id = 2, name="Read books", description="Should complete the book of Think and Grow Rich")

tasks_list.append(task1)
tasks_list.append(task2)

@app.get("/")
def read_root():
    return {"This is a basic to-do list application developed by Vijay Kothawar"}

@app.get("/active-tasks")
def read_active_tasks():
    return [task for task in tasks_list if task.status != "Done"]

@app.get("/completed-tasks")
def read_completed_tasks():
    return [task for task in tasks_list if task.status == "Done"]

@app.get("/all-tasks")
def read_all_tasks():
    return tasks_list

@app.post("/add-task/")
def add_task(request : dict):
    try:
        new_task = Task(id=len(tasks_list)+1, name=request["name"], description=request["description"])
        tasks_list.append(new_task)
        return {"message": "Task added successfully", "task": new_task}
    except Exception as e:
        return {"error": str(e)}
    
@app.post("/mark-done/")
def mark_task_done(request : dict):
    try:
        task_id = request["id"]
        for task in tasks_list:
            if task.id == task_id:
                task.mark_done()
                return {"message": "Task marked as done", "task": task}
        return {"error": "Task not found"}
    except Exception as e:
        return {"error": str(e)}