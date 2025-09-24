from flask import Blueprint, request, jsonify
from services.solar_station_service import SolarStationService

def create_solar_station_controller(mysql):
    solar_station_controller = Blueprint('solar_station', __name__)
    service = SolarStationService(mysql)

    @solar_station_controller.route('/solar_station', methods=['GET'])
    def get_solar_stations():
        stations = service.get_solar_stations()
        return jsonify([station.to_dict() for station in stations])

    @solar_station_controller.route('/solar_station', methods=['POST'])
    def create_solar_station():
        data = request.json
        if not data or 'household_id' not in data or 'installation_date' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.add_solar_station(data)
            return jsonify({"message": "Solar station created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @solar_station_controller.route('/solar_station/<int:station_id>', methods=['PUT'])
    def update_solar_station(station_id):
        data = request.json
        if not data or 'household_id' not in data or 'installation_date' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.modify_solar_station(station_id, data)
            return jsonify({"message": "Solar station updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @solar_station_controller.route('/solar_station/<int:station_id>', methods=['DELETE'])
    def delete_solar_station(station_id):
        try:
            service.remove_solar_station(station_id)
            return jsonify({"message": "Solar station deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return solar_station_controller
