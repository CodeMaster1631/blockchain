from flask import Flask, jsonify, request
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/chain", methods=["GET"])
def get_chain():
    """Returns the full blockchain."""
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(
            {
                "index": block.index,
                "timestamp": block.timestamp,
                "data": block.data,
                "previous_hash": block.previous_hash,
                "hash": block.hash,
            }
        )
    return jsonify({"length": len(blockchain.chain), "chain": chain_data})


@app.route("/add_block", methods=["POST"])
def add_block():
    """Adds a new block with given data."""
    data = request.json.get("data")
    if not data:
        return jsonify({"error": "Missing data"}), 400

    blockchain.add_block(data)
    return jsonify({"message": "Block added successfully!"})


@app.route("/validate", methods=["GET"])
def validate_chain():
    """Checks if the blockchain is valid."""
    is_valid = blockchain.is_chain_valid()
    return jsonify({"valid": is_valid})


if __name__ == "__main__":
    app.run(debug=True)
