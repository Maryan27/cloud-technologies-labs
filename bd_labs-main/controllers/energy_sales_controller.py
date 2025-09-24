from flask import Blueprint, request, jsonify
from services.energy_sales_service import EnergySalesService

def create_energy_sales_controller(mysql):
    energy_sales_controller = Blueprint('energy_sales', __name__)
    service = EnergySalesService(mysql)

    @energy_sales_controller.route('/energy_sales', methods=['GET'])
    def get_energy_sales():
        sales = service.get_energy_sales()
        return jsonify([sale.to_dict() for sale in sales])

    @energy_sales_controller.route('/energy_sales', methods=['POST'])
    def create_energy_sales():
        data = request.json
        if not data or 'station_id' not in data or 'energy_sold' not in data or 'price_per_kWh' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.add_energy_sales(data)
            return jsonify({"message": "Energy sale created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @energy_sales_controller.route('/energy_sales/<int:sale_id>', methods=['PUT'])
    def update_energy_sales(sale_id):
        data = request.json
        service.modify_energy_sales(sale_id, data)
        return jsonify({"message": "Energy sale updated"})

    @energy_sales_controller.route('/energy_sales/<int:sale_id>', methods=['DELETE'])
    def delete_energy_sales(sale_id):
        service.remove_energy_sales(sale_id)
        return jsonify({"message": "Energy sale deleted"})

    return energy_sales_controller
