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


from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity

from security import authenticate, identity

app = Flask(__name__)
#JWT
app.secret_key = 'jose'
api = Api(app)
jwt = JWT(app, authenticate, identity)

items = []

class Item(Resource):
    @jwt_required()
    def get(self,name):
        item = next(filter(lambda x: x['name'] == name, items),None)
        # for item in items:
        #     if item['name'] == name:
        #         return item
        return {'item': None}, 200 if item else 404

    def post(self,name):
        if next(filter(lambda x: x['name'] == name, items),None):
            return{'message': "An item with name '{}' already exists.".format(name)},400
        data = request.get_json() #force=True #silent=True
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201


    def delete(self,name):
        global items
        items = list(filter(lambda x:x['name'] != name, items))
        return {'message': 'Item deleted'}

    
    def put(self,name):
        # data = request.get_json()
        parser = reqparse.RequestParser()
        parser.add_argument(
            "price",
            type=float,
            required=True,
            help="This field can't be left blank!"
        )
        data = parser.parse_args()

        item = next(filter(lambda x:x['name'] == name, items),None)
        if item in None:
            item = {
                'name':name,
                'price':data['price']
            }
        else:
            item.update(date)
        return item



class ItemList(Resource):
    def get(self):
        return {'items':items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)