from flask import Blueprint, request, jsonify
from services.household_owner_service import HouseholdOwnerService

def create_household_owner_controller(mysql):
    household_owner_controller = Blueprint('household_owner', __name__)
    service = HouseholdOwnerService(mysql)

   
    @household_owner_controller.route('/household_owner', methods=['GET'])
    def get_household_owners():
        household_owners = service.get_household_owners()
        return jsonify(household_owners)

    @household_owner_controller.route('/owner/<int:owner_id>/household_owner', methods=['GET'])
    def get_household_owners_by_owner(owner_id):
        household_owners = service.get_household_owners_by_owner(owner_id)
        return jsonify(household_owners)

    
    @household_owner_controller.route('/household_owner', methods=['POST'])
    def create_household_owner():
        data = request.json
        if not data or 'owner_id' not in data or 'address' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.add_household_owner(data)
            return jsonify({"message": "Household Owner created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @household_owner_controller.route('/household_owner/<int:household_owner_id>', methods=['PUT'])
    def update_household_owner(household_owner_id):
        data = request.json
        if not data or 'owner_id' not in data or 'address' not in data:
            return jsonify({"error": "Invalid data"}), 400
        try:
            service.modify_household_owner(household_owner_id, data)
            return jsonify({"message": "Household Owner updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @household_owner_controller.route('/household_owner/<int:household_owner_id>', methods=['DELETE'])
    def delete_household_owner(household_owner_id):
        try:
            service.remove_household_owner(household_owner_id)
            return jsonify({"message": "Household Owner deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return household_owner_controller
