from datetime import datetime, timedelta
import uuid
import jwt
from flask import Flask, request, jsonify

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)