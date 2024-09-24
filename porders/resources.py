from flask import jsonify
from flask_restful import Resource, reqparse

purchase_orders = [
    {
    'id': 1,
    'description': 'Pedido de de Compra 1',
    'items': [
        {
            'id': 1,
            'description': 'Item do pedido 1',
            'price': 20.99
        }
    ]
    }
]

class PurchaseOrders(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        'id',
        type=int,
        required=True, # se é obrigatorio ou nao
        help='Informe um id' # mensagem caso o parametro seja incorreto ou nao seja preenchido
    )

    parser.add_argument(
        'description',
        type=str,
        required=True,
        help='Informe uma descrição'
    )

    def get(self):
        return jsonify(purchase_orders)
    
    def post(self):
        request_data = PurchaseOrders().parser.parse_args()
        purchase_order = {
            'id': request_data['id'],
            'description': request_data['description'],
            'items': []
        }

        purchase_orders.append(purchase_order)

        return jsonify(purchase_order)