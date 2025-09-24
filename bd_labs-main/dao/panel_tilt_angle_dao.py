from models.panel_tilt_angle import PanelTiltAngle

class PanelTiltAngleDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_tilt_angles(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM panel_tilt_angle")
        tilt_angles = cur.fetchall()
        cur.close()
        return [PanelTiltAngle(id=row[0], panel_id=row[1], tilt_angle=row[2], timestamp=row[3]) for row in tilt_angles]

    def insert_tilt_angle(self, tilt_angle):
        cur = self.mysql.connection.cursor()
        cur.execute("INSERT INTO panel_tilt_angle (panel_id, tilt_angle, timestamp) VALUES (%s, %s, %s)", 
                    (tilt_angle['panel_id'], tilt_angle['tilt_angle'], tilt_angle['timestamp']))
        self.mysql.connection.commit()
        cur.close()

    def update_tilt_angle(self, tilt_angle_id, tilt_angle):
        cur = self.mysql.connection.cursor()
        cur.execute("UPDATE panel_tilt_angle SET panel_id = %s, tilt_angle = %s, timestamp = %s WHERE id = %s", 
                    (tilt_angle['panel_id'], tilt_angle['tilt_angle'], tilt_angle['timestamp'], tilt_angle_id))
        self.mysql.connection.commit()
        cur.close()

    def delete_tilt_angle(self, tilt_angle_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM panel_tilt_angle WHERE id = %s", (tilt_angle_id,))
        self.mysql.connection.commit()
        cur.close()
