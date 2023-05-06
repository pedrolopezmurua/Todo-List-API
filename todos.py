from flask import Flask, request, jsonify, render_template

todos = [
    {
        "done": True,
        "label": "Sample Todo 1",
        "id": 0
    },
    {
        "done": True,
        "label": "Sample Todo 2",
        "id": 1
    }
]

app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def todos_get():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def todos_post():
    tarea = request.get_json()
    tarea["id"] = len(todos)
    todos.append(tarea)
    return jsonify({"status": "success", "message": "Tarea agregada exitosamente!"})

@app.route('/todos/<int:id>', methods=['DELETE'])
def todos_delete(id):
        for i in range(len(todos)):
            if todos[i]['id'] == id:
                del todos[i]
                return jsonify({"status": "success", "message": f"Tarea con id {id} eliminada exitosamente!"})
        return jsonify({"status": "error", "message": f"No se encontró una tarea con id {id}."})


@app.route('/', methods=['GET'])
def html():
        return render_template('index.html')

if __name__ == '__main__':
    app.run(port="3000")
