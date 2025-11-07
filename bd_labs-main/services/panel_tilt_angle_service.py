from dao.panel_tilt_angle_dao import PanelTiltAngleDAO

class PanelTiltAngleService:
    def __init__(self, mysql):
        self.dao = PanelTiltAngleDAO(mysql)

    def get_tilt_angles(self):
        return self.dao.get_all_tilt_angles()

    def add_tilt_angle(self, tilt_angle):
        return self.dao.insert_tilt_angle(tilt_angle)

    def modify_tilt_angle(self, tilt_angle_id, tilt_angle):
        return self.dao.update_tilt_angle(tilt_angle_id, tilt_angle)

    def remove_tilt_angle(self, tilt_angle_id):
        return self.dao.delete_tilt_angle(tilt_angle_id)
