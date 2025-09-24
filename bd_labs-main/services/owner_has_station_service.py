from dao.owner_has_station_dao import OwnerHasStationDAO

class OwnerHasStationService:
    def __init__(self, mysql):
        self.dao = OwnerHasStationDAO(mysql)

    def get_owner_stations(self):
        return self.dao.get_all_owners_stations()

    def add_owner_station(self, owner_station):
        return self.dao.insert_owner_station(owner_station)

    def remove_owner_station(self, owner_id, station_id):
        return self.dao.delete_owner_station(owner_id, station_id)

    def get_stations_for_owner(self, owner_id):
        return self.dao.get_stations_for_owner(owner_id)


