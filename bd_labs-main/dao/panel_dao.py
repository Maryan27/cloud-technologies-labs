from models.panel import Panel

class PanelDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_panels(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM panel")
        panels = cur.fetchall()
        cur.close()
        return [Panel(id=row[0], station_id=row[1], panel_type=row[2], 
                      installation_date=row[3], power=row[4], usage_duration=row[5]) for row in panels]

    def insert_panel(self, panel):
        cur = self.mysql.connection.cursor()
        cur.execute("INSERT INTO panel (station_id, panel_type, installation_date, power, usage_duration) VALUES (%s, %s, %s, %s, %s)", 
                    (panel['station_id'], panel['panel_type'], panel['installation_date'], panel['power'], panel['usage_duration']))
        self.mysql.connection.commit()
        cur.close()

    def update_panel(self, panel_id, panel):
        cur = self.mysql.connection.cursor()
        cur.execute("UPDATE panel SET station_id = %s, panel_type = %s, installation_date = %s, power = %s, usage_duration = %s WHERE id = %s", 
                    (panel['station_id'], panel['panel_type'], panel['installation_date'], panel['power'], panel['usage_duration'], panel_id))
        self.mysql.connection.commit()
        cur.close()

    def delete_panel(self, panel_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM panel WHERE id = %s", (panel_id,))
        self.mysql.connection.commit()
        cur.close()
