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

@app.route('/tasks', methods=['GET'])
def get_tasks():
    # Logic to get all tasks
    task_list = [task.to_dict() for task in tasks] # Convert Task objects to dictionaries
    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
            }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    # Logic to get a specific task by ID
    task = None
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks/<int:id>', methods=["PUT"])
def update_task(id):
  task = None
  for t in tasks:
    if t.id == id:
      task = t
  if task == None:
    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

  data = request.get_json()
  task.title = data['title']
  task.description = data['description']
  task.completed = data['completed']
  return jsonify({"message": "Tarefa atualizada com sucesso"})

if __name__ == "__main__":
    app.run(debug=True)