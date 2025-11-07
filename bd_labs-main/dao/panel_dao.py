from models.panel import Panel

class PanelDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_panels(self):
        cur = self.mysql.connection.cursor()
        cur.execute("""
            SELECT id, station_id, panel_type, power, installation_date
            FROM panel
            ORDER BY id
        """)
        rows = cur.fetchall()
        cur.close()
        return [
            {
                "id": row[0],
                "station_id": row[1],
                "panel_type": row[2],
                "power": row[3],
                "installation_date": row[4]
            }
            for row in rows
        ]

    def insert_panel(self, panel):
        cur = self.mysql.connection.cursor()
        cur.execute("""
            INSERT INTO panel (station_id, panel_type, power, installation_date)
            VALUES (%s, %s, %s, %s)
        """, (
            panel['station_id'],
            panel['panel_type'],
            panel['power'],
            panel['installation_date']
        ))
        self.mysql.connection.commit()
        cur.close()

    def update_panel(self, panel_id, panel):
        cur = self.mysql.connection.cursor()
        cur.execute("""
            UPDATE panel
            SET station_id = %s, panel_type = %s, power = %s, installation_date = %s
            WHERE id = %s
        """, (
            panel['station_id'],
            panel['panel_type'],
            panel['power'],
            panel['installation_date'],
            panel_id
        ))
        self.mysql.connection.commit()
        cur.close()

    def delete_panel(self, panel_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM panel WHERE id = %s", (panel_id,))
        self.mysql.connection.commit()
        cur.close()

