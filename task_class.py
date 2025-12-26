from datetime import datetime

class Task:
    def __init__(self, id: int, name: str, description: str, status: str = "Not Done"):
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.created_at = datetime.now()
        self.completed_at = None

    def mark_done(self):
        self.status = "Done"
        self.completed_at = datetime.now()

    def mark_not_done(self):
        self.status = "Not Done"
        self.completed_at = None

    def __str__(self):
        return f"Task(name={self.name}, description={self.description}, status={self.status}, created_at={self.created_at}, completed_at={self.completed_at})"