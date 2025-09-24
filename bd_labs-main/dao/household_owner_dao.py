# household_owner_dao.py
from models.household_owner import HouseholdOwner

class HouseholdOwnerDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    # Метод для отримання всіх household_owners
    def get_all_household_owners(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM household_owner")
        rows = cur.fetchall()
        cur.close()
        return [HouseholdOwner(*row).to_dict() for row in rows]

    # Метод для отримання household owners за owner_id
    def get_household_owners_by_owner(self, owner_id):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM household_owner WHERE owner_id = %s", (owner_id,))
        rows = cur.fetchall()
        cur.close()
        return [HouseholdOwner(*row).to_dict() for row in rows]

    # Метод для вставки нового household_owner
    def insert_household_owner(self, household_owner):
        cur = self.mysql.connection.cursor()
        cur.execute(
            "INSERT INTO household_owner (owner_id, address) VALUES (%s, %s)", 
            (household_owner['owner_id'], household_owner['address'])
        )
        self.mysql.connection.commit()
        cur.close()

    # Метод для оновлення даних household_owner
    def update_household_owner(self, household_owner_id, household_owner):
        cur = self.mysql.connection.cursor()
        cur.execute(
            "UPDATE household_owner SET owner_id = %s, address = %s WHERE id = %s", 
            (household_owner['owner_id'], household_owner['address'], household_owner_id)
        )
        self.mysql.connection.commit()
        cur.close()

    # Метод для видалення household_owner за ID
    def delete_household_owner(self, household_owner_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM household_owner WHERE id = %s", (household_owner_id,))
        self.mysql.connection.commit()
        cur.close()


