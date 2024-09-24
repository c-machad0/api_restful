from flask import Flask
from flask_restful import Api

from porders.resources import PurchaseOrders

app = Flask(__name__) # Armazena nessa variavel o nome do arquivo
api = Api(app)
    
api.add_resource(PurchaseOrders, '/purchase_orders')

app.run(port=5000) # Executar nossa aplicação na porta 5000