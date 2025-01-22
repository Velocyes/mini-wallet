from datetime import datetime, timedelta
import uuid
import jwt
from flask import Flask, request, jsonify

app = Flask(__name__)
customers = {}
wallets = {}

SECRET_KEY = "JULO"

def generate_jwt_token(customer_id):
    expiration = datetime.utcnow() + timedelta(hours=1)
    token = jwt.encode({"customer_id": customer_id, "exp": expiration}, SECRET_KEY, algorithm="HS256")
    return token

def decode_jwt_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload['customer_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def _authenticate(token):
    customer_id = decode_jwt_token(token)
    return customer_id is not None


@app.route("/api/v1/init", methods=["POST"])
def initialize_account():
    customer_xid = request.form.get("customer_xid")
    if not customer_xid:
        return jsonify({"status": "fail", "data": {"error": {"customer_xid": ["Missing data for required field."]}}}), 400
    
    token = generate_jwt_token(customer_xid)
    
    customers[customer_xid] = {"wallet_id": None}
    return jsonify({"status": "success", "data": {"token": token}}), 201

@app.route("/api/v1/wallet", methods=["POST"])
def enable_wallet():
    token = request.headers.get("Authorization", "").replace("Token ", "")
    if not token or not _authenticate(token):
        return jsonify({"status": "fail", "data": {"error": "Unauthorized"}}), 401
    
    customer_id = decode_jwt_token(token)
    wallet_id = customers[customer_id].get("wallet_id")

    if wallet_id and wallets[wallet_id]["status"] == "enabled":
        return jsonify({"status": "fail", "data": {"error": "Already enabled"}}), 400

    if not wallet_id:
        wallet_id = uuid.uuid4().hex
        customers[customer_id]["wallet_id"] = wallet_id
        
    enabled_at = datetime.utcnow().isoformat()

    wallets[wallet_id] = {"id": wallet_id, "owned_by": customer_id, "status": "enabled", "enabled_at": enabled_at, "balance": 0}
    return jsonify({"status": "success", "data": {"wallet": wallets[wallet_id]}}), 201

if __name__ == "__main__":
    app.run(debug=True)