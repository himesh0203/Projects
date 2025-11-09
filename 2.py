from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store (for demonstration purposes)
items = [
    {"id": 1, "name": "Item A", "description": "This is item A"},
    {"id": 2, "name": "Item B", "description": "This is item B"}
]

# GET all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# GET a single item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"message": "Item not found"}), 404

# POST (create) a new item
@app.route('/items', methods=['POST'])
def create_item():
    new_item_data = request.get_json()
    if not new_item_data or not 'name' in new_item_data:
        return jsonify({"message": "Name is required"}), 400

    new_id = max([item['id'] for item in items]) + 1 if items else 1
    new_item = {
        "id": new_id,
        "name": new_item_data['name'],
        "description": new_item_data.get('description', '')
    }
    items.append(new_item)
    return jsonify(new_item), 201

# PUT (update) an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({"message": "Item not found"}), 404

    update_data = request.get_json()
    if 'name' in update_data:
        item['name'] = update_data['name']
    if 'description' in update_data:
        item['description'] = update_data['description']
    return jsonify(item)

# DELETE an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    initial_length = len(items)
    items = [item for item in items if item['id'] != item_id]
    if len(items) < initial_length:
        return jsonify({"message": "Item deleted"}), 200
    return jsonify({"message": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
