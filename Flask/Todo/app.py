### Use of Put and Delete
### Working with APIs

from flask import Flask, jsonify, request

app = Flask(__name__)

items = [
    {"id": 1, "title": "Buy groceries", "description": "Milk, Cheese, Pizza, Fruit, Tylenol"},
    {"id": 2, "title": "Learn Python", "description": "Need to find a good Python tutorial on the web"},
    {"id": 3, "title": "Learn Flask", "description": "Need to find a good Flask tutorial on the web"},
]

@app.route('/')
def home():
    return "This is home page"

##Get: Retrieve all the items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

##Get item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"]==item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

##Post: Add a new item
@app.route('/items', methods=['POST'])
def add_item():
    if not request.json or not 'title' in request.json:
        return jsonify({"error": "Invalid input"}), 400
    data = request.get_json()
    new_item = {"id": items[-1]['id'] + 1 if items else 1,
                "title": data['title'],
                "description": data['description']}
    items.append(new_item)
    return jsonify(new_item)

##Put: Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"==item_id]), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    if not request.json:
        return jsonify({"error": "Invalid input"}), 400
    data = request.get_json()
    item["title"] = data.get("title", item["title"])
    item["description"] = data.get("description", item["description"])
    return jsonify(item)

##Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = next((item for item in items if item["id"==item_id]), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    items.remove(item)
    return jsonify({"message": "Item deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)