class HourlyProduction:
    def __init__(self, id, panel_id, timestamp, energy_produced):
        self.id = id
        self.panel_id = panel_id
        self.timestamp = timestamp
        self.energy_produced = energy_produced

    def to_dict(self):
        return {
            "id": self.id,
            "panel_id": self.panel_id,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
            "energy_produced": str(self.energy_produced)
        }
