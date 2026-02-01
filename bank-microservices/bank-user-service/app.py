from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/user/<user_id>')
def user(user_id):
    return jsonify({
        "user_id": user_id,
        "name": "Silambarasan Sethuraman",
        "acc_no": "2323****3344"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
