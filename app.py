from flask import Flask, request, jsonify
from app.order_validator import OrderValidator
from app.order_service import OrderService

app = Flask(__name__)


@app.route('/api/orders', methods=['POST'])
def process_order():
    data = request.get_json()

    # 檢查訂單
    validator = OrderValidator()
    if not validator.validate(data):
        return jsonify({'error': 'Invalid order format'}), 400

    # 轉換訂單
    service = OrderService()
    try:
        transformed_order = service.transform(data)
        return jsonify(transformed_order), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
