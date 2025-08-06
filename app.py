from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

# CRUD operations
# Create, Read, Update, Delete
tasks = []
task_id_control = 1
@app.route('/tasks', methods=['POST'])
def create_task():
    # Logic to create a new task
    global task_id_control
    data = request.get_json()
    new_tast = Task(id=task_id_control, title=data["title"], 
    description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_tast)
    print(f"Task created: {new_tast}")
    return jsonify({"message":"Nova tarefa criada com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)