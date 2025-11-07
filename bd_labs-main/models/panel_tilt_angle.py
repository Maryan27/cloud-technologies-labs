class PanelTiltAngle:
    def __init__(self, id, panel_id, tilt_angle, timestamp):
        self.id = id
        self.panel_id = panel_id
        self.tilt_angle = tilt_angle
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "id": self.id,
            "panel_id": self.panel_id,
            "tilt_angle": str(self.tilt_angle),
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
        }
