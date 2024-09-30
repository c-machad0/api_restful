from flask import Flask
from flask_restful import Api

from porders.resources import PurchaseOrders, PurchaseOrdersById

app = Flask(__name__) # Armazena nessa variavel o nome do arquivo
api = Api(app)
    
api.add_resource(PurchaseOrders, '/purchase_orders')
api.add_resource(PurchaseOrdersById, '/purchase_orders/<int:id>')

app.run(port=5000) # Executar nossa aplicação na porta 5000