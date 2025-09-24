from dao.hourly_production_dao import HourlyProductionDAO

class HourlyProductionService:
    def __init__(self, mysql):
        self.dao = HourlyProductionDAO(mysql)

    def get_hourly_productions(self):
        return self.dao.get_all_hourly_productions()

    def add_hourly_production(self, production):
        return self.dao.insert_hourly_production(production)

    def modify_hourly_production(self, production_id, production):
        return self.dao.update_hourly_production(production_id, production)

    def remove_hourly_production(self, production_id):
        return self.dao.delete_hourly_production(production_id)
