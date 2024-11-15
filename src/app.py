from flask import Flask, request, jsonify

app = Flask(__name__)

# Miembros iniciales
members = [
    {"first_name": "Tommy", "id": 1, "age": 33, "lucky_numbers": [4, 6, 23]},
    {"first_name": "Jane", "id": 2, "age": 35, "lucky_numbers": [12, 42, 7]},
    {"first_name": "Alice", "id": 3, "age": 25, "lucky_numbers": [34, 65, 23, 4, 6]}
]

# Ruta para obtener todos los miembros
@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(members)

# Ruta para obtener un miembro por ID
@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):
    member = next((m for m in members if m["id"] == id), None)
    if member:
        return jsonify(member)
    else:
        return jsonify({"error": "Member not found"}), 404

# Ruta para agregar un nuevo miembro
@app.route('/member', methods=['POST'])
def add_member():
    new_member = request.get_json()
    members.append(new_member)
    return jsonify(new_member), 201

# Ruta para eliminar un miembro por ID
@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    global members
    member = next((m for m in members if m["id"] == id), None)
    if member:
        members = [m for m in members if m["id"] != id]
        return jsonify({"done": True}), 200
    else:
        return jsonify({"error": "Member not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)






