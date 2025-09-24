from flask import Blueprint, request, jsonify
from services.hourly_production_service import HourlyProductionService

def create_hourly_production_controller(mysql):
    hourly_production_controller = Blueprint('hourly_production', __name__)
    service = HourlyProductionService(mysql)

    @hourly_production_controller.route('/hourly_production', methods=['GET'])
    def get_hourly_productions():
        productions = service.get_hourly_productions()
        return jsonify([production.to_dict() for production in productions])

    @hourly_production_controller.route('/hourly_production', methods=['POST'])
    def create_hourly_production():
        data = request.json
        if not data or 'panel_id' not in data or 'timestamp' not in data or 'energy_produced' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.add_hourly_production(data)
            return jsonify({"message": "Hourly production created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @hourly_production_controller.route('/hourly_production/<int:production_id>', methods=['PUT'])
    def update_hourly_production(production_id):
        data = request.json
        if not data or 'panel_id' not in data or 'timestamp' not in data or 'energy_produced' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.modify_hourly_production(production_id, data)
            return jsonify({"message": "Hourly production updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @hourly_production_controller.route('/hourly_production/<int:production_id>', methods=['DELETE'])
    def delete_hourly_production(production_id):
        try:
            service.remove_hourly_production(production_id)
            return jsonify({"message": "Hourly production deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return hourly_production_controller
