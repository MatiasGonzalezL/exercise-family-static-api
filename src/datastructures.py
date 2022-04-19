
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": self.last_name,
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        },
        {
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": self.last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        },
        {
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": self.last_name,
            "age": 5,
            "lucky_numbers": [1]
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    #agregar miembro
    def add_member_by_name(self, member):
        self._members.append(member)
        pass

    #borrar miembro
    def delete_member(self, id):
        self._members = [object for object in self._members if object["id"] != int(id)]
        pass

    #obtener miembro
    def get_member(self, id):
        member = [object for object in self._members if object["id"] == id]
        return member

    #todos los miembros
    def get_all_members(self):
        return self._members
