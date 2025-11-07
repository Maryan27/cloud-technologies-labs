class OwnerHasStation:
    def __init__(self, owner_id, station_id):
        self.owner_id = owner_id
        self.station_id = station_id

    def to_dict(self):
        return {
            "owner_id": self.owner_id,
            "station_id": self.station_id,
        }
