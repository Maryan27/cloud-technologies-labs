class HouseholdOwner:
    def __init__(self, id, owner_id, address):
        self.id = id
        self.owner_id = owner_id
        self.address = address

    def to_dict(self):
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            'address': self.address
        }
