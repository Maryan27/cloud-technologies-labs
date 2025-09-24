from flask import Blueprint, request, jsonify
from services.panel_service import PanelService

def create_panel_controller(mysql):
    panel_controller = Blueprint('panel', __name__)
    service = PanelService(mysql)

    @panel_controller.route('/panel', methods=['GET'])
    def get_panels():
        panels = service.get_panels()
        return jsonify([panel.to_dict() for panel in panels])

    @panel_controller.route('/panel', methods=['POST'])
    def create_panel():
        data = request.json
        if not data or 'station_id' not in data or 'panel_type' not in data or 'installation_date' not in data or 'power' not in data or 'usage_duration' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.add_panel(data)
            return jsonify({"message": "Panel created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @panel_controller.route('/panel/<int:panel_id>', methods=['PUT'])
    def update_panel(panel_id):
        data = request.json
        if not data or 'station_id' not in data or 'panel_type' not in data or 'installation_date' not in data or 'power' not in data or 'usage_duration' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.modify_panel(panel_id, data)
            return jsonify({"message": "Panel updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @panel_controller.route('/panel/<int:panel_id>', methods=['DELETE'])
    def delete_panel(panel_id):
        try:
            service.remove_panel(panel_id)
            return jsonify({"message": "Panel deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return panel_controller
