class BatteryChargeLevel:
    def __init__(self, id, battery_id, charge_level, timestamp):
        self.id = id
        self.battery_id = battery_id
        self.charge_level = charge_level
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "id": self.id,
            "battery_id": self.battery_id,
            "charge_level": str(self.charge_level),
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
        }
