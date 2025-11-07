class SolarStation:
    def __init__(self, id, household_id, installation_date):
        self.id = id
        self.household_id = household_id
        self.installation_date = installation_date

    def to_dict(self):
        return {
            "id": self.id,
            "household_id": self.household_id,
            "installation_date": self.installation_date.isoformat() if self.installation_date else None
        }
