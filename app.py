from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data['title'], desccription=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso!"}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }

    return jsonify(output), 200

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict()), 200
    return jsonify({"message": "Tarefa não encontrada!"}), 404

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None 
    for t in tasks:
        if t.id == id:
            task = t
            break

    print(task)
    if task is None:
        return jsonify({"message": "Não foi possível encontrar a tarefa!"}), 404
    
    data = request.get_json()
    task.title = data["title"]
    task.description = data["description"]
    task.completed = data["completed"]
    print(task)
    return jsonify({"message": "Tarefa atualizada com sucesso!", "data": task.to_dict()}), 200

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    if task is None:
        return jsonify({"message": "Nao foi possível encontrar a tarefa!"}), 404
    
    if task in tasks:
            tasks.remove(task)
            return jsonify({"message": "Tarefa deletada com sucesso!"}), 200
    

#garante que somente quando execute o servidor de forma manual, execute em modo debug
if __name__ == "__main__":
    app.run(debug=True) #apenas para dev