from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/bank/user/<user_id>')
def bank_home(user_id):
    user = requests.get(f'http://192.168.0.107:5001/user/{user_id}').json()
    txn  = requests.get(f'http://192.168.0.102:5002/txn/{user_id}').json()

    return jsonify({
        "user": user,
        "transaction": txn
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
