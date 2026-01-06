from flask import Flask, jsonify, request
app = Flask(__name__)
items = [
    {'id': 1, 'nombre': 'Zapatos', 'precio': 59.99},
    {'id': 2, 'nombre': 'Camisa', 'precio': 29.99},
    {'id': 3, 'nombre': 'Cinturon', 'precio': 19.99}
    ]
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({'message': 'Item no encontrado'}), 404

@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.get_json()
    new_item={
        'id': new_item['id'],
        'nombre': new_item['nombre'],
        'precio': new_item['precio']
    }
    items.append(new_item)
    return jsonify(new_item), 201

# metodo actualizar
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        data = request.get_json()
        item['nombre'] = data.get('nombre', item['nombre'])
        item['precio'] = data.get('precio', item['precio'])
        return jsonify(item)
    return jsonify({'message': 'Item no encontrado'}), 404
# metodo eliminar
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item eliminado'})

if __name__ == '__main__':
    app.run(debug=True)
