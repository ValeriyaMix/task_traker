import sqlite3 as db


class TaskTracker:
    def __init__(self):
        self.new_tasks = []
        self.in_progress_tasks = []
        self.completed_tasks = []

    def add(self, user_token):
        task = Task(user_token)
        self.new_tasks.append(task)

    def take_to_perform(self, user_token):
        task = Task(user_token)
        self.in_progress_tasks.append(task)

    def mark_accomplishment(self, user_token):
        task = Task(user_token)
        self.completed_tasks.append(task)

    def check_status(self):
        pass



class DatabaseManager:


    def add_task(self, task):
        connection = db.connect("taskandusers")
        cursor = connection.cursor()
        sql = 'INSERT INTO task (status, user_id) values (?, ?)'
        params = (task.status, task.user_token)   #kakie imenno parametri hochy vstavit
        cursor.execute(sql, params)
        connection.commit()
        connection.close()
        return cursor.lastrowid

    def change_status(self, task):
        cursor = self.connection.cursor()
        sql = 'UPDATE task SET status = ? WHERE rowid = ?'
        params = (task.status, task.id)  # kakie imenno parametri hochy vstavit
        cursor.execute(sql, params)


class Task:
    db_manager = DatabaseManager()
    created = 0
    in_progress = 1
    completed = 2

    def __init__(self, user_token, tasks=None):
        self.tasks = tasks
        self.user_token = user_token
        self.status = self.created
        self.id = self.db_manager.add_task(self)

    def get_to_execute(self):
        if self.status == self.in_progress:
            raise ValueError("Status is already in progress")
        elif self.status != self.created:
            raise ValueError("Status should be created")
        else:
            self.status = self.in_progress
            self.db_manager.change_status(self)

    def complete(self):
        if self.status == self.in_progress:
            self.status = self.completed
            self.db_manager.change_status(self)
        else:
            raise ValueError("Incorrect status")

    def get_status(self):
        return self.status


def create_database():
    c = db.connect("taskandusers")
    cu = c.cursor()
    cur = c.cursor()

    try:
        cu.execute("""
            CREATE TABLE task (
              status INT,
              user_id TEXT
            );
    """)
        cur.execute("""    
            CREATE TABLE user (
              id TEXT PRIMARY KEY,
              first_name TEXT,
              last_name TEXT
            );
    """)
    except db.DatabaseError as x:
        print("Ошибка: ", x)
    c.commit()
    c.close()


create_database()
TaskTracker().add(user_token='rrrrr22')


