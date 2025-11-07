from dao.solar_station_dao import SolarStationDAO

class SolarStationService:
    def __init__(self, mysql):
        self.dao = SolarStationDAO(mysql)

    def get_solar_stations(self):
        return self.dao.get_all_solar_stations()

    def add_solar_station(self, solar_station):
        return self.dao.insert_solar_station(solar_station)

    def modify_solar_station(self, station_id, solar_station):
        return self.dao.update_solar_station(station_id, solar_station)

    def remove_solar_station(self, station_id):
        return self.dao.delete_solar_station(station_id)
