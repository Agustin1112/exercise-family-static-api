from flask import Flask, request, jsonify
from datastructures import FamilyStructure


app = Flask(__name__)

# Inicio la familia "Jackson"
jackson_family = FamilyStructure('Jackson')

# Miembros iniciales de la familia
jackson_family.add_member({
    'first_name': 'John',
    'age': 33,
    'lucky_numbers': [7, 13, 22]
})
jackson_family.add_member({
    'first_name': 'Jane',
    'age': 35,
    'lucky_numbers': [10, 14, 3]
})
jackson_family.add_member({
    'first_name': 'Jimmy',
    'age': 5,
    'lucky_numbers': [1]
})

@app.route('/members', methods=['GET'])
def get_members():
    try:
        members = jackson_family.get_all_members()
        return jsonify(members), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    try:
        member = jackson_family.get_member(member_id)
        if member:
            return jsonify(member), 200
        else:
            return jsonify({'error': 'Member not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/member', methods=['POST'])
def add_member():
    try:
        member_data = request.get_json()

        # Verifico que los campos necesarios estén en el cuerpo de la solicitud
        if not all(key in member_data for key in ['first_name', 'age', 'lucky_numbers']):
            return jsonify({'error': 'Missing required fields'}), 400

        # Valido que la edad sea mayor a 0
        if member_data['age'] <= 0:
            return jsonify({'error': 'Age must be greater than 0'}), 400

        jackson_family.add_member(member_data)
        return jsonify(member_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    try:
        success = jackson_family.delete_member(member_id)
        if success:
            return jsonify({'done': True}), 200
        else:
            return jsonify({'error': 'Member not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

