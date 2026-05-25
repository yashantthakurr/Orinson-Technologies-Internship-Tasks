
from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate

# CREATE A NEW TASK
def create_task(db: Session, task: TaskCreate):
    db_task = Task(name= task.name, description=task.description, status=task.status)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# GET ALL TASKS
def get_tasks(db: Session):
    return db.query(Task).all()

# GET TASK BY ID
def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

# UPDATE TASK
def update_task(db: Session, task_id: int, updated_task: TaskCreate):
    task = get_task(db, task_id)

    if not task:
        return None

    task.name = updated_task.name
    task.description = updated_task.description
    task.status = updated_task.status

    db.commit()
    db.refresh(task)
    return task

# DELETE TASK
def delete_task(db: Session, task_id: int):
    task = get_task(db, task_id)

    if not task:
        return None

    db.delete(task)
    db.commit()
    return task
