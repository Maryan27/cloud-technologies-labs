from dao.battery_charge_level_dao import BatteryChargeLevelDAO

class BatteryChargeLevelService:
    def __init__(self, mysql):
        self.dao = BatteryChargeLevelDAO(mysql)

    def get_charge_levels(self):
        return self.dao.get_all_charge_levels()

    def add_charge_level(self, charge_level):
        return self.dao.insert_charge_level(charge_level)

    def modify_charge_level(self, charge_level_id, charge_level):
        return self.dao.update_charge_level(charge_level_id, charge_level)

    def remove_charge_level(self, charge_level_id):
        return self.dao.delete_charge_level(charge_level_id)
