from flask import Flask, request
from flask_restful import Api, Resource
from models import Task
from app import app, db

api = Api(app)

class TaskList(Resource):
    def get(self):
        tasks = Task.query.all()
        return [{'id': task.id, 'title': task.title, 'description': task.description, 'completed': task.completed} for task in tasks]

    def post(self):
        data = request.get_json()
        task = Task(title=data['title'], description=data['description'])
        db.session.add(task)
        db.session.commit()
        return {'id': task.id, 'title': task.title, 'description': task.description, 'completed': task.completed}, 201

class TaskDetail(Resource):
    def get(self, task_id):
        task = Task.query.get(task_id)
        if task:
            return {'id': task.id, 'title': task.title, 'description': task.description, 'completed': task.completed}
        return {'message': 'Task not found'}, 404

    def put(self, task_id):
        task = Task.query.get(task_id)
        if task:
            data = request.get_json()
            task.title = data['title']
            task.description = data['description']
            task.completed = data['completed']
            db.session.commit()
            return {'id': task.id, 'title': task.title, 'description': task.description, 'completed': task.completed}
        return {'message': 'Task not found'}, 404

    def delete(self, task_id):
        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return {'message': 'Task deleted'}
        return {'message': 'Task not found'}, 404

api.add_resource(TaskList, '/tasks')
api.add_resource(TaskDetail, '/tasks/<int:task_id>')

if __name__ == '__main__':
    app.run(debug=True)