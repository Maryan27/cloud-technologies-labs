class EnergySales:
    def __init__(self, id, station_id, energy_sold, price_per_kWh, timestamp):
        self.id = id
        self.station_id = station_id
        self.energy_sold = energy_sold
        self.price_per_kWh = price_per_kWh
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "id": self.id,
            "station_id": self.station_id,
            "energy_sold": str(self.energy_sold),
            "price_per_kWh": str(self.price_per_kWh),
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
        }
