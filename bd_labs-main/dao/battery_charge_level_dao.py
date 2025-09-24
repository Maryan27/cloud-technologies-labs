from models.battery_charge_level import BatteryChargeLevel

class BatteryChargeLevelDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_charge_levels(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM battery_charge_level")
        charge_levels = cur.fetchall()
        cur.close()
        return [BatteryChargeLevel(id=row[0], battery_id=row[1], charge_level=row[2], timestamp=row[3]) for row in charge_levels]

    def insert_charge_level(self, charge_level):
        cur = self.mysql.connection.cursor()
        cur.execute("INSERT INTO battery_charge_level (battery_id, charge_level, timestamp) VALUES (%s, %s, %s)", 
                    (charge_level['battery_id'], charge_level['charge_level'], charge_level['timestamp']))
        self.mysql.connection.commit()
        cur.close()

    def update_charge_level(self, charge_level_id, charge_level):
        cur = self.mysql.connection.cursor()
        cur.execute("UPDATE battery_charge_level SET battery_id = %s, charge_level = %s, timestamp = %s WHERE id = %s", 
                    (charge_level['battery_id'], charge_level['charge_level'], charge_level['timestamp'], charge_level_id))
        self.mysql.connection.commit()
        cur.close()

    def delete_charge_level(self, charge_level_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM battery_charge_level WHERE id = %s", (charge_level_id,))
        self.mysql.connection.commit()
        cur.close()
