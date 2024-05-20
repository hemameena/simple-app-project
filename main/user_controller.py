# app.py
from flask import Flask, render_template, request, redirect
from main.user import db
import main.user_service as services

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Hema098@localhost/dbname'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['POST', 'GET'])
def ind():
    if request.method == 'POST':
        task_content = request.form['content']
        try:
            services.add_task(task_content)
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        tasks = services.get_all_tasks()
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    try:
        services.delete_task(id)
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = services.get_task_by_id(id)

    if request.method == 'POST':
        task_content = request.form['content']
        try:
            services.update_task(id, task_content)
            return redirect('/')
        except:
            return 'There was an issue updating your task'
    else:
        return render_template('update.html', task=task)

if __name__ == "__main__":
    app.run(debug=True)
