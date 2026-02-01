from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/txn/<user_id>')
def txn(user_id):
    return jsonify({
        "user_id": user_id,
        "name": "Silambarasan Sethuraman",
        "last_txn": {
            "date": "2026-02-02",
            "amount": 500,
            "type": "Debit"
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
