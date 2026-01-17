from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Configure SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Task Model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0) # 0 for incomplete, 1 for done
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database within the application context
with app.app_context():
    db.create_all()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        if task_content:
            new_task = Todo(content=task_content)
            try:
                db.session.add(new_task)
                db.session.commit()
                return redirect('/')
            except:
                return 'There was an issue adding your task'
    
    # Sort tasks so incomplete ones appear at the top
    tasks = Todo.query.order_by(Todo.completed, Todo.date_created).all()
    return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>')
def update(id):
    task = Todo.query.get_or_404(id)
    try:
        # Toggle completion status
        task.completed = 1 if task.completed == 0 else 0
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue updating your task'

if __name__ == "__main__":
    app.run(debug=True)