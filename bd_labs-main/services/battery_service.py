from dao.battery_dao import BatteryDAO

class BatteryService:
    def __init__(self, mysql):
        self.dao = BatteryDAO(mysql)

    def get_batteries(self):
        return self.dao.get_all_batteries()

    def add_battery(self, battery):
        return self.dao.insert_battery(battery)

    def modify_battery(self, battery_id, battery):
        return self.dao.update_battery(battery_id, battery)

    def remove_battery(self, battery_id):
        return self.dao.delete_battery(battery_id)
