from models.owner_has_station import OwnerHasStation
from models.solar_station import SolarStation 

class OwnerHasStationDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_owners_stations(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM owner_has_station")
        owners_stations = cur.fetchall()
        cur.close()
        return [OwnerHasStation(owner_id=row[0], station_id=row[1]) for row in owners_stations]

    def insert_owner_station(self, owner_station):
        cur = self.mysql.connection.cursor()
        cur.execute("INSERT INTO owner_has_station (owner_id, station_id) VALUES (%s, %s)", 
                    (owner_station['owner_id'], owner_station['station_id']))
        self.mysql.connection.commit()
        cur.close()

    def delete_owner_station(self, owner_id, station_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM owner_has_station WHERE owner_id = %s AND station_id = %s", (owner_id, station_id))
        self.mysql.connection.commit()
        cur.close()

    def get_stations_for_owner(self, owner_id):
        cur = self.mysql.connection.cursor()
        cur.execute("""
            SELECT s.id, s.household_id, s.installation_date
            FROM solar_station s
            JOIN owner_has_station o ON s.id = o.station_id
            WHERE o.owner_id = %s
        """, (owner_id,))
        stations = cur.fetchall()
        cur.close()
        
        return [SolarStation(id=row[0], household_id=row[1], installation_date=row[2]) for row in stations]


