from flask import Blueprint, request, jsonify
from services.owner_has_station_service import OwnerHasStationService

def create_owner_has_station_controller(mysql):
    owner_has_station_controller = Blueprint('owner_has_station', __name__)
    service = OwnerHasStationService(mysql)

   
    @owner_has_station_controller.route('/owner_has_station', methods=['GET'])
    def get_owners_stations():
        owners_stations = service.get_owner_stations()
        return jsonify([os.to_dict() for os in owners_stations])

    @owner_has_station_controller.route('/owner_has_station', methods=['POST'])
    def create_owner_station():
        data = request.json
        if not data or 'owner_id' not in data or 'station_id' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.add_owner_station(data)
            return jsonify({"message": "Owner has station created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @owner_has_station_controller.route('/owner_has_station', methods=['DELETE'])
    def delete_owner_station():
        data = request.json
        if not data or 'owner_id' not in data or 'station_id' not in data:
            return jsonify({"error": "Invalid data"}), 400

        service.remove_owner_station(data['owner_id'], data['station_id'])
        return jsonify({"message": "Owner has station deleted"})

    @owner_has_station_controller.route('/owner/<int:owner_id>/solar_station', methods=['GET'])
    def get_stations_for_owner(owner_id):
        try:
            stations = service.get_stations_for_owner(owner_id)  
            return jsonify([station.to_dict() for station in stations])  
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return owner_has_station_controller
