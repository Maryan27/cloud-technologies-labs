class Panel:
    def __init__(self, id, station_id, panel_type, installation_date, power, usage_duration):
        self.id = id
        self.station_id = station_id
        self.panel_type = panel_type
        self.installation_date = installation_date
        self.power = power
        self.usage_duration = usage_duration

    def to_dict(self):
        return {
            "id": self.id,
            "station_id": self.station_id,
            "panel_type": self.panel_type,
            "installation_date": self.installation_date.isoformat() if self.installation_date else None,
            "power": str(self.power),
            "usage_duration": self.usage_duration
        }
