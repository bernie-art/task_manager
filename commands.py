import db

def save_task(task):
    # Save task in database
    db.tasks.insert_one(task)
    # Return task
    return True

def delete_task(id):
    # Delete task from database
    db.tasks.delete_one({"_id": id})
    # Return response
    return True

def get_tasks():
    # Get all task from database
    all_tasks = db.tasks.find()
    # Return task
    return all_tasks

def update_task(task, update):
    # Update task in database
    # Return task
    return True