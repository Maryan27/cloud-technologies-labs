from flask import Blueprint, request, jsonify
from services.panel_tilt_angle_service import PanelTiltAngleService

def create_panel_tilt_angle_controller(mysql):
    panel_tilt_angle_controller = Blueprint('panel_tilt_angle', __name__)
    service = PanelTiltAngleService(mysql)

    @panel_tilt_angle_controller.route('/panel_tilt_angle', methods=['GET'])
    def get_tilt_angles():
        """
        Get list of panel tilt angles
        ---
        responses:
          200:
            description: A list of panel tilt angles
        """
        tilt_angles = service.get_tilt_angles()
        return jsonify(tilt_angles)

    @panel_tilt_angle_controller.route('/panel_tilt_angle', methods=['POST'])
    def create_tilt_angle():
        """
        Create a new panel tilt angle
        ---
        parameters:
          - in: body
            name: body
            required: true
            schema:
              type: object
              properties:
                panel_id:
                  type: integer
                tilt_angle:
                  type: number
                timestamp:
                  type: string
                  format: date-time
        responses:
          201:
            description: Tilt angle created successfully
          400:
            description: Invalid input
        """
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
        """
        Update panel tilt angle
        ---
        parameters:
          - name: tilt_angle_id
            in: path
            type: integer
            required: true
          - in: body
            name: body
            required: true
            schema:
              type: object
              properties:
                panel_id:
                  type: integer
                tilt_angle:
                  type: number
                timestamp:
                  type: string
                  format: date-time
        responses:
          200:
            description: Tilt angle updated successfully
          400:
            description: Invalid input
        """
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
        """
        Delete panel tilt angle
        ---
        parameters:
          - name: tilt_angle_id
            in: path
            type: integer
            required: true
        responses:
          200:
            description: Tilt angle deleted successfully
        """
        try:
            service.remove_tilt_angle(tilt_angle_id)
            return jsonify({"message": "Tilt angle deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return panel_tilt_angle_controller

