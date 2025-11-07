from dao.energy_sales_dao import EnergySalesDAO

class EnergySalesService:
    def __init__(self, mysql):
        self.dao = EnergySalesDAO(mysql)

    def get_energy_sales(self):
        return self.dao.get_all_energy_sales()

    def add_energy_sales(self, sale):
        return self.dao.insert_energy_sales(sale)

    def modify_energy_sales(self, sale_id, sale):
        return self.dao.update_energy_sales(sale_id, sale)

    def remove_energy_sales(self, sale_id):
        return self.dao.delete_energy_sales(sale_id)
