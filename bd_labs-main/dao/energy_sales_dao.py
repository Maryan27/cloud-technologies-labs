from models.energy_sales import EnergySales

class EnergySalesDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_energy_sales(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM energy_sales")
        sales = cur.fetchall()
        cur.close()
        return [EnergySales(id=row[0], station_id=row[1], energy_sold=row[2], price_per_kWh=row[3], timestamp=row[4]) for row in sales]

    def insert_energy_sales(self, sale):
        cur = self.mysql.connection.cursor()
        cur.execute("INSERT INTO energy_sales (station_id, energy_sold, price_per_kWh, timestamp) VALUES (%s, %s, %s, %s)", 
                    (sale['station_id'], sale['energy_sold'], sale['price_per_kWh'], sale['timestamp']))
        self.mysql.connection.commit()
        cur.close()

    def update_energy_sales(self, sale_id, sale):
        cur = self.mysql.connection.cursor()
        cur.execute("UPDATE energy_sales SET station_id = %s, energy_sold = %s, price_per_kWh = %s, timestamp = %s WHERE id = %s", 
                    (sale['station_id'], sale['energy_sold'], sale['price_per_kWh'], sale['timestamp'], sale_id))
        self.mysql.connection.commit()
        cur.close()

    def delete_energy_sales(self, sale_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM energy_sales WHERE id = %s", (sale_id,))
        self.mysql.connection.commit()
        cur.close()
