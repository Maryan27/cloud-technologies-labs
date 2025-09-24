from models.owner import Owner

class OwnerDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_owners(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM owner")
        rows = cur.fetchall()
        cur.close()
        return [Owner(*row).to_dict() for row in rows]

    def insert_owner(self, owner):
        cur = self.mysql.connection.cursor()
        cur.execute("INSERT INTO owner (name, email) VALUES (%s, %s)", (owner['name'], owner['email']))
        self.mysql.connection.commit()
        cur.close()

    def update_owner(self, owner_id, owner):
        cur = self.mysql.connection.cursor()
        cur.execute("UPDATE owner SET name = %s, email = %s WHERE id = %s", (owner['name'], owner['email'], owner_id))
        self.mysql.connection.commit()
        cur.close()

    def delete_owner(self, owner_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM owner WHERE id = %s", (owner_id,))
        self.mysql.connection.commit()
        cur.close()

    def get_owner_with_households(self, owner_id):
        cur = self.mysql.connection.cursor()
        query = """
            SELECT o.id, o.name, o.email, ho.id, ho.address 
            FROM owner o
            LEFT JOIN household_owner ho ON o.id = ho.owner_id
            WHERE o.id = %s
        """
        cur.execute(query, (owner_id,))
        rows = cur.fetchall()
        cur.close()
        
        owner_data = None
        households = []
        for row in rows:
            if not owner_data:
                owner_data = {
                    "id": row[0],
                    "name": row[1],
                    "email": row[2],
                    "households": []
                }
            if row[3]: 
                households.append({
                    "id": row[3],
                    "address": row[4]
                })
        
        if owner_data:
            owner_data["households"] = households
        return owner_data

    def get_owner_stations(self, owner_id):
        cur = self.mysql.connection.cursor()
        query = """
            SELECT s.id, s.installation_date 
            FROM owner o
            JOIN owner_has_station ohs ON o.id = ohs.owner_id
            JOIN solar_station s ON ohs.station_id = s.id
            WHERE o.id = %s
        """
        cur.execute(query, (owner_id,))
        rows = cur.fetchall()
        cur.close()
        
        return [{"id": row[0], "installation_date": row[1]} for row in rows]
