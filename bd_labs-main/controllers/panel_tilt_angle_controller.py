from flask import Blueprint, request, jsonify
from services.panel_tilt_angle_service import PanelTiltAngleService

def create_panel_tilt_angle_controller(mysql):
    panel_tilt_angle_controller = Blueprint('panel_tilt_angle', __name__)
    service = PanelTiltAngleService(mysql)

    @panel_tilt_angle_controller.route('/panel_tilt_angle', methods=['GET'])
    def get_tilt_angles():
        tilt_angles = service.get_tilt_angles()
        return jsonify([tilt_angle.to_dict() for tilt_angle in tilt_angles])

    @panel_tilt_angle_controller.route('/panel_tilt_angle', methods=['POST'])
    def create_tilt_angle():
        data = request.json
        if not data or 'panel_id' not in data or 'tilt_angle' not in data or 'timestamp' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.add_tilt_angle(data)
            return jsonify({"message": "Tilt angle created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @panel_tilt_angle_controller.route('/panel_tilt_angle/<int:tilt_angle_id>', methods=['PUT'])
    def update_tilt_angle(tilt_angle_id):
        data = request.json
        if not data or 'panel_id' not in data or 'tilt_angle' not in data or 'timestamp' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.modify_tilt_angle(tilt_angle_id, data)
            return jsonify({"message": "Tilt angle updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @panel_tilt_angle_controller.route('/panel_tilt_angle/<int:tilt_angle_id>', methods=['DELETE'])
    def delete_tilt_angle(tilt_angle_id):
        try:
            service.remove_tilt_angle(tilt_angle_id)
            return jsonify({"message": "Tilt angle deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return panel_tilt_angle_controller
