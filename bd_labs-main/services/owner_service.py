# owner_service.py
from dao.owner_dao import OwnerDAO

class OwnerService:
    def __init__(self, mysql):
        self.dao = OwnerDAO(mysql)

    # Метод для отримання всіх власників
    def get_owners(self):
        return self.dao.get_all_owners()

    # Метод для додавання нового власника
    def add_owner(self, owner):
        return self.dao.insert_owner(owner)

    # Метод для оновлення даних власника
    def modify_owner(self, owner_id, owner):
        return self.dao.update_owner(owner_id, owner)

    # Метод для видалення власника
    def remove_owner(self, owner_id):
        return self.dao.delete_owner(owner_id)

    # Новий метод для отримання owner з його household_owners (зв'язок M:1)
    def get_owner_with_households(self, owner_id):
        return self.dao.get_owner_with_households(owner_id)

    # Новий метод для отримання всіх станцій для owner (зв'язок M:M)
    def get_owner_stations(self, owner_id):
        return self.dao.get_owner_stations(owner_id)




