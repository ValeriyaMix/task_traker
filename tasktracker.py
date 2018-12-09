import sqlite as db


class TaskTracker:
    def __init__(self):
        self.new_tasks = []
        self.in_progress_tasks = []
        self.completed_task = []

    def add(self, user_token):
        task = Task(user_token)
        if task:
            self.new_tasks.append(task)

    def take_to_perform(self, user_token):
        task = Task(user_token)
        if task:
            self.in_progress_tasks.append(task)

    def mark_accomplishment(self):
        pass

    def check_status(self):
        pass


class Task:

    created = 0
    in_progress = 1
    completed = 2

    def __init__(self, user_token, tasks=None):
        self.tasks = tasks
        self.user_token = user_token
        self.status = self.created

    def get_to_execute(self):
        if self.status == self.in_progress:
            raise ValueError("Status is already in progress")
        elif self.status != self.created:
            raise ValueError("Status should be created")
        else:
            self.status = self.in_progress

    def complete(self):
        if self.status == self.in_progress:
            self.status = self.completed
        else:
            raise ValueError("Incorrect status")

    def get_status(self):
        return self.status


def create_database():
    c = db.connect(datebase="tasksandusers")
    cu = c.cursor()
    try:
        cu.execute("""
            CREATE TABLE taskuser (
              task STRING,
              user CHAR(20)
            );
    """)
    except db.DatabaseError as x:
        print("Ошибка: ", x)
    c.commit()
    c.close()




