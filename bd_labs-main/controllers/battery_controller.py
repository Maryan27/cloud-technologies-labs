from flask import Blueprint, request, jsonify
from services.battery_service import BatteryService

def create_battery_controller(mysql):
    battery_controller = Blueprint('battery', __name__)
    service = BatteryService(mysql)

    @battery_controller.route('/battery', methods=['GET'])
    def get_batteries():
        batteries = service.get_batteries()
        return jsonify([battery.to_dict() for battery in batteries])

    @battery_controller.route('/battery', methods=['POST'])
    def create_battery():
        data = request.json
        if not data or 'station_id' not in data or 'capacity' not in data or 'installation_date' not in data or 'usage_duration' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.add_battery(data)
            return jsonify({"message": "Battery created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @battery_controller.route('/battery/<int:battery_id>', methods=['PUT'])
    def update_battery(battery_id):
        data = request.json
        if not data or 'station_id' not in data or 'capacity' not in data or 'installation_date' not in data or 'usage_duration' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.modify_battery(battery_id, data)
            return jsonify({"message": "Battery updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @battery_controller.route('/battery/<int:battery_id>', methods=['DELETE'])
    def delete_battery(battery_id):
        try:
            service.remove_battery(battery_id)
            return jsonify({"message": "Battery deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return battery_controller
