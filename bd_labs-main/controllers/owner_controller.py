from flask import Blueprint, request, jsonify
from services.owner_service import OwnerService

def create_owner_controller(mysql):
    owner_controller = Blueprint('owner', __name__)
    service = OwnerService(mysql)

    @owner_controller.route('/owner', methods=['GET'])
    def get_owners():
        owners = service.get_owners()
        return jsonify(owners)

    @owner_controller.route('/owner', methods=['POST'])
    def create_owner():
        data = request.json
        if not data or 'name' not in data or 'email' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.add_owner(data)
            return jsonify({"message": "Owner created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @owner_controller.route('/owner/<int:owner_id>', methods=['PUT'])
    def update_owner(owner_id):
        data = request.json
        if not data or 'name' not in data or 'email' not in data:
            return jsonify({"error": "Invalid data"}), 400
        try:
            service.modify_owner(owner_id, data)
            return jsonify({"message": "Owner updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @owner_controller.route('/owner/<int:owner_id>', methods=['DELETE'])
    def delete_owner(owner_id):
        try:
            service.remove_owner(owner_id)
            return jsonify({"message": "Owner deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @owner_controller.route('/owner/<int:owner_id>/households', methods=['GET'])
    def get_owner_with_households(owner_id):
        try:
            owner_with_households = service.get_owner_with_households(owner_id)
            return jsonify(owner_with_households)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @owner_controller.route('/owner/<int:owner_id>/stations', methods=['GET'])
    def get_owner_stations(owner_id):
        try:
            stations = service.get_owner_stations(owner_id)
            return jsonify(stations)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return owner_controller

