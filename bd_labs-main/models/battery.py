class Battery:
    def __init__(self, id, station_id, capacity, installation_date, usage_duration):
        self.id = id
        self.station_id = station_id
        self.capacity = capacity
        self.installation_date = installation_date
        self.usage_duration = usage_duration

    def to_dict(self):
        return {
            "id": self.id,
            "station_id": self.station_id,
            "capacity": str(self.capacity),
            "installation_date": self.installation_date.isoformat() if self.installation_date else None,
            "usage_duration": self.usage_duration
        }
