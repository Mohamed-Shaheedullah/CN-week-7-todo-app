from flask import Flask, Blueprint, render_template, request, redirect, url_for

from .models import Todo
from . import db
my_view = Blueprint("my_view", __name__)

@my_view.route("/")
def home():
    todo_list = Todo.query.all()    # returns list of objects
    # print(todo_list)
    er_message = request.args.get("er_message", None)
    return render_template("index.html", todo_list = todo_list, er_message=er_message)

# add task
# enable form
@my_view.route("/add", methods = ["POST"])
def add():
    try:
        # request form contents by 'name' of form - task
        task = request.form.get("task")
        # left task represents var declared in above line , right task represents contents of form ?
        new_todo = Todo(task=task)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for("my_view.home"))
    except:
        er_message = "There was an error adding your task"
        return redirect(url_for("my_view.home", er_message=er_message))


@my_view.route("/update/<todo_id>", methods=["GET", "POST"])
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    # toggle
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("my_view.home", er_message="              " ))

# delete
@my_view.route("/delete/<todo_id>", methods=["GET", "POST"])
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("my_view.home", er_message="              "))
