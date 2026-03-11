from flask import Flask, request, jsonify
from checker import check_account

app = Flask(__name__)


@app.route("/")
def index():
    email = request.args.get("email")
    password = request.args.get("pass")
    proxy = request.args.get("proxy")

    if not email or not password:
        return jsonify({"status": "ERROR", "message": "Missing email or pass parameter"}), 400

    try:
        result = check_account(email, password, proxy)
        if result is None:
            return jsonify({"status": "ERROR", "message": "No result returned"})
        return jsonify(result)
    except Exception:
        return jsonify({"status": "ERROR", "message": "Internal server error"}), 500
