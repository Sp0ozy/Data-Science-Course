from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

items = [ 
    {"id": 1, "name": "Item One", "description": "first item description"},
    {"id": 2, "name": "Item Two", "description": "second item description"},
]

@app.route("/")
def welcome():  
    return "Welcome to this Flask course"

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "item not found"}), 404
    return jsonify(item)

@app.route("/items", methods=["POST"])
def create_item():
    if not request.json or "name" not in request.json:
        return jsonify({"error": "name is required"}), 400
    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json["name"],
        "description": request.json["description"]
    }
    items.append(new_item)
    return jsonify(new_item)

@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "item not found"}), 404
    item['name']= request.json.get('name', item['name'])
    item['description']= request.json.get('description', item['description'])
    return jsonify(item)

@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result": "item deleted"})

if __name__ == "__main__":
    app.run()