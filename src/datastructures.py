
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class NombreDeLaClase:
    def __init__(self):
        self.nombre_de_la_variable #globales para cualquier parte


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["id"] = self._generateId()
        return self._members.append(member)

    def delete_member(self, id):
            #self._members = list(filter(lambda member: id != member["id"], self._members))
            #self._members = [member for member in self._members if not (member['id'] == id)]
            new_members = list(filter(lambda member: member["id"] != id, self._members))
            self._members = new_members
            return self._members

    def get_member(self, id):
        result = {}
        try:
            for member in self._members:
                if member["id"] == id:
                    result = member
        except Exception as e:
            print(f"get_member: {e}")
        return result

    def get_all_members(self):
        return self._members
