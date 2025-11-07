from flask import Blueprint, request, jsonify
from services.hourly_production_service import HourlyProductionService

def create_hourly_production_controller(mysql):
    hourly_production_controller = Blueprint('hourly_production', __name__)
    service = HourlyProductionService(mysql)

    @hourly_production_controller.route('/hourly_production', methods=['GET'])
    def get_hourly_productions():
        """
        Get list of hourly productions
        ---
        responses:
          200:
            description: A list of hourly productions
        """
        productions = service.get_hourly_productions()
        return jsonify(productions)

    @hourly_production_controller.route('/hourly_production', methods=['POST'])
    def create_hourly_production():
        """
        Create a new hourly production record
        ---
        parameters:
          - in: body
            name: body
            schema:
              type: object
              required:
                - panel_id
                - timestamp
                - energy_produced
              properties:
                panel_id:
                  type: integer
                timestamp:
                  type: string
                  format: date-time
                energy_produced:
                  type: number
        responses:
          201:
            description: Hourly production created successfully
          400:
            description: Invalid input
        """
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
        """
        Update hourly production
        ---
        parameters:
          - in: path
            name: production_id
            type: integer
            required: true
          - in: body
            name: body
            schema:
              type: object
              required:
                - panel_id
                - timestamp
                - energy_produced
              properties:
                panel_id:
                  type: integer
                timestamp:
                  type: string
                  format: date-time
                energy_produced:
                  type: number
        responses:
          200:
            description: Hourly production updated successfully
          400:
            description: Invalid input
        """
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
        """
        Delete hourly production
        ---
        parameters:
          - in: path
            name: production_id
            type: integer
            required: true
        responses:
          200:
            description: Hourly production deleted successfully
        """
        try:
            service.remove_hourly_production(production_id)
            return jsonify({"message": "Hourly production deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return hourly_production_controller

