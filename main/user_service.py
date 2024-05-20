# services.py
from main.user import db, Todo

def add_task(content):
    new_task = Todo(content=content)
    db.session.add(new_task)
    db.session.commit()
    return new_task

def get_all_tasks():
    return Todo.query.order_by(Todo.date_created).all()

def get_task_by_id(task_id):
    return Todo.query.get_or_404(task_id)

def delete_task(task_id):
    task_to_delete = get_task_by_id(task_id)
    db.session.delete(task_to_delete)
    db.session.commit()

def update_task(task_id, content):
    task = get_task_by_id(task_id)
    task.content = content
    db.session.commit()
    return task
