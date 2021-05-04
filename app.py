# from flask import Flask, jsonify, request, render_template

# app = Flask(__name__)


# stores = [
#     {
#         'name': 'My Wonderful Store',
#         'items': [
#             {
#                 'name': 'My Team',
#                 'price': 15.99
#             }
#         ]
#     }
# ]

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/store',methods=['POST'])
# def create_store():
#     request_data = request.get_json()
#     new_store = {
#         'name': request_data['name'],
#         'items': []
#     }
#     stores.append(new_store)
#     return jsonify(new_store)


# @app.route('/store/<string:name>')
# def get_store(name):
#     for store in stores:
#         if store['name'] == name:
#             return jsonify(store)
#     return jsonify({'msg':'store not found'})


# @app.route('/store')
# def get_stores():
#     return jsonify({'stores':stores})


# @app.route('/store/<string:name>/item',methods=['POST'])
# def create_iteams_in_store(name):
#     request_data = request.get_json()
#     for store in stores:
#         if store['name'] == name:
#             new_item = {
#                 'name': request_data['name'],
#                 'price': request_data['price']
#             }
#             store['items'].request_data['name']
#             return jsonify(new_item)
#     return jsonify({'msg':'store not found'})


# @app.route('/store/<string:name>/item')
# def get_items_in_store(name):
#     for store in stores:
#         if store['name'] == name:
#             return jsonify({'items': store['items']})
#     return jsonify({'msg':'store not found'})

# app.run(port=5000)

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self,name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 400

    def post(self,name):
        data = request.get_json() #force=True #silent=True
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {'items':items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)