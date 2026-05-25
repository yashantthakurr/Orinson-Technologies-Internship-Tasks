
from crudoperations import tasks_crud
from database import engine
from dependencies import get_db
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import models, schemas

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix='/tasks', tags=['Tasks API Routes'])

# CREATE A NEW TASK
@router.post('', response_model=schemas.TaskCreate)
def create_new_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return tasks_crud.create_task(db, task)

# GET TASK BY ID
@router.get('/{task_id}', response_model=schemas.TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = tasks_crud.get_task(db, task_id)
    if not task:
        raise HTTPException(404, "Task not found!")
    return task

# GET ALL TASKS
@router.get('')
def read_tasks(db: Session = Depends(get_db)):
    return tasks_crud.get_tasks(db)

# UPDATE TASK
@router.put('/{task_id}', response_model=schemas.TaskResponse)
def update_existing_task(task_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    updated_task = tasks_crud.update_task(db, task_id, task)
    if not updated_task:
        raise HTTPException(404, "Task not found!")
    return updated_task

# DELETE TASK
@router.delete('/{task_id}')
def delete_existing_task(task_id: int, db: Session = Depends(get_db)):
    deleted_task = tasks_crud.delete_task(db, task_id)

    if not deleted_task:
        raise HTTPException(404, "Task not found!")

    return {'message': "Task deleted successfully!"}
