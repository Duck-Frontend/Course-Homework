from db import Session
from model.task import Task


class TaskController:
    @staticmethod
    def get_all_tasks():
        with Session as session:
            tasks = session.query(Task).all()
            return tasks

    @staticmethod
    def add_task(title, description):
        with Session as session:
            new_task = Task(name=title, description=description)

            session.add(new_task)
            session.commit()
            session.refresh(new_task)

        return new_task.id
