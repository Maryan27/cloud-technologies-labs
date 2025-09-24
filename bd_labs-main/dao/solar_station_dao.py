from models.solar_station import SolarStation

class SolarStationDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_solar_stations(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM solar_station")
        stations = cur.fetchall()
        cur.close()
        return [SolarStation(id=row[0], household_id=row[1], installation_date=row[2]) for row in stations]

    def insert_solar_station(self, solar_station):
        cur = self.mysql.connection.cursor()
        cur.execute("INSERT INTO solar_station (household_id, installation_date) VALUES (%s, %s)", 
                    (solar_station['household_id'], solar_station['installation_date']))
        self.mysql.connection.commit()
        cur.close()

    def update_solar_station(self, station_id, solar_station):
        cur = self.mysql.connection.cursor()
        cur.execute("UPDATE solar_station SET household_id = %s, installation_date = %s WHERE id = %s", 
                    (solar_station['household_id'], solar_station['installation_date'], station_id))
        self.mysql.connection.commit()
        cur.close()

    def delete_solar_station(self, station_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM solar_station WHERE id = %s", (station_id,))
        self.mysql.connection.commit()
        cur.close()
