# /src/app.py

from flask import Flask, request, jsonify 
from models import tasks, Task

app = Flask(__name__)

# Rota de @app.route('/')
def home():
    return "<h1>Sistema de Gerenciamento de Tarefas</h1><p>Em construção...</p>"

# Rota para listar todas as tarefas (CRUD - Read)
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

# Rota para criar uma nova tarefa (CRUD - Create)
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    if not title:
        return jsonify({"error": "O título da tarefa é obrigatório"}), 400

    new_task = Task(title, description)
    tasks.append(new_task.__dict__)

    return jsonify(new_task.__dict__), 201

# Rota para atualizar uma tarefa (CRUD - Update)
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task_found = None
    for task in tasks:
        if task['id'] == task_id:
            task_found = task
            break

    if not task_found:
        return jsonify({"error": "Tarefa não encontrada"}), 404

    data = request.get_json()
    task_found['title'] = data.get('title', task_found['title'])
    task_found['description'] = data.get('description', task_found['description'])
    task_found['status'] = data.get('status', task_found['status'])

    return jsonify(task_found)

    # Rota para excluir uma tarefa (CRUD - Delete)
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    # Procura a tarefa pelo ID e a remove da lista
    initial_task_count = len(tasks)
    tasks = [task for task in tasks if task['id'] != task_id]

    if len(tasks) < initial_task_count:
        return jsonify({"message": f"Tarefa com ID {task_id} foi excluída com sucesso"}), 200
    else:
        return jsonify({"error": "Tarefa não encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)