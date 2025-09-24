from models.battery import Battery

class BatteryDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_batteries(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM battery")
        batteries = cur.fetchall()
        cur.close()
        return [Battery(id=row[0], station_id=row[1], capacity=row[2], 
                        installation_date=row[3], usage_duration=row[4]) for row in batteries]

    def insert_battery(self, battery):
        cur = self.mysql.connection.cursor()
        cur.execute("INSERT INTO battery (station_id, capacity, installation_date, usage_duration) VALUES (%s, %s, %s, %s)", 
                    (battery['station_id'], battery['capacity'], battery['installation_date'], battery['usage_duration']))
        self.mysql.connection.commit()
        cur.close()

    def update_battery(self, battery_id, battery):
        cur = self.mysql.connection.cursor()
        cur.execute("UPDATE battery SET station_id = %s, capacity = %s, installation_date = %s, usage_duration = %s WHERE id = %s", 
                    (battery['station_id'], battery['capacity'], battery['installation_date'], battery['usage_duration'], battery_id))
        self.mysql.connection.commit()
        cur.close()

    def delete_battery(self, battery_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM battery WHERE id = %s", (battery_id,))
        self.mysql.connection.commit()
        cur.close()
