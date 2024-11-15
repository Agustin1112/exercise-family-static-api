class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1  # ID inicial
        self._members = []  # Lista de miembros

    # Método para generar IDs únicos
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    # Método para agregar un nuevo miembro
    def add_member(self, member):
        member['id'] = self._generate_id()  # Asigno un ID único al miembro
        member['last_name'] = self.last_name  # Aseguro que el apellido sea el correcto
        self._members.append(member)  # Agrego el miembro a la lista

    # Método para eliminar un miembro
    def delete_member(self, id):
        for member in self._members:
            if member['id'] == id:
                self._members.remove(member)  # Elimino el miembro de la lista
                return True  # Retorno True si se eliminó correctamente
        return False  # Retorno False si no encuentro el miembro

    # Método para obtener un miembro específico
    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                return member  # Devuelvo el miembro si lo encuentro
        return None  # Retorno None si no lo encuentro

    # Método para obtener todos los miembros
    def get_all_members(self):
        return self._members  # Devuelvo la lista de todos los miembros


