from flask import Blueprint, request, jsonify
from services.energy_sales_service import EnergySalesService

def create_energy_sales_controller(mysql):
    energy_sales_controller = Blueprint('energy_sales', __name__)
    service = EnergySalesService(mysql)

    @energy_sales_controller.route('/energy_sales', methods=['GET'])
    def get_energy_sales():
        """
        Get list of energy sales
        ---
        responses:
          200:
            description: A list of energy sales
        """
        sales = service.get_energy_sales()
        return jsonify(sales)

    @energy_sales_controller.route('/energy_sales', methods=['POST'])
    def create_energy_sales():
        """
        Create a new energy sale
        ---
        parameters:
          - in: body
            name: body
            required: true
            schema:
                type: object
                properties:
                    station_id:
                        type: integer
                    energy_sold:
                        type: number
                    price_per_kWh:
                        type: number
                    timestamp:
                        type: string
                        format: date-time
        responses:
          201:
            description: Energy sale created successfully
          400:
            description: Invalid input
        """
        data = request.json
        if not data or 'station_id' not in data or 'energy_sold' not in data or 'price_per_kWh' not in data or 'timestamp' not in data:
            return jsonify({"error": "Invalid data"}), 400
        try:
            service.add_energy_sales(data)
            return jsonify({"message": "Energy sale created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @energy_sales_controller.route('/energy_sales/<int:sale_id>', methods=['PUT'])
    def update_energy_sales(sale_id):
        """
        Update an energy sale
        ---
        parameters:
          - name: sale_id
            in: path
            type: integer
            required: true
          - in: body
            name: body
            required: true
            schema:
                type: object
                properties:
                    station_id:
                        type: integer
                    energy_sold:
                        type: number
                    price_per_kWh:
                        type: number
                    timestamp:
                        type: string
                        format: date-time
        responses:
          200:
            description: Energy sale updated successfully
          400:
            description: Invalid input
        """
        data = request.json
        try:
            service.modify_energy_sales(sale_id, data)
            return jsonify({"message": "Energy sale updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @energy_sales_controller.route('/energy_sales/<int:sale_id>', methods=['DELETE'])
    def delete_energy_sales(sale_id):
        """
        Delete an energy sale
        ---
        parameters:
          - name: sale_id
            in: path
            type: integer
            required: true
        responses:
          200:
            description: Energy sale deleted successfully
        """
        try:
            service.remove_energy_sales(sale_id)
            return jsonify({"message": "Energy sale deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return energy_sales_controller

