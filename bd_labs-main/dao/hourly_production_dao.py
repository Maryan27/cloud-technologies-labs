from models.hourly_production import HourlyProduction

class HourlyProductionDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_hourly_productions(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM hourly_production")
        productions = cur.fetchall()
        cur.close()
        return [HourlyProduction(id=row[0], panel_id=row[1], timestamp=row[2], 
                                 energy_produced=row[3]) for row in productions]

    def insert_hourly_production(self, production):
        cur = self.mysql.connection.cursor()
        cur.execute("INSERT INTO hourly_production (panel_id, timestamp, energy_produced) VALUES (%s, %s, %s)", 
                    (production['panel_id'], production['timestamp'], production['energy_produced']))
        self.mysql.connection.commit()
        cur.close()

    def update_hourly_production(self, production_id, production):
        cur = self.mysql.connection.cursor()
        cur.execute("UPDATE hourly_production SET panel_id = %s, timestamp = %s, energy_produced = %s WHERE id = %s", 
                    (production['panel_id'], production['timestamp'], production['energy_produced'], production_id))
        self.mysql.connection.commit()
        cur.close()

    def delete_hourly_production(self, production_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM hourly_production WHERE id = %s", (production_id,))
        self.mysql.connection.commit()
        cur.close()
