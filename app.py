from flask import Flask, request, jsonify
import hashlib
import uuid

app = Flask(__name__)
database = {}

@app.route('/activate', methods=['POST'])
def activate():
    data = request.get_json()
    email = data['email']
    key = data['key']

    if key == generate_license_key(email):
        order_id = str(uuid.uuid4())
        license_data = {
            "key": key,
            "order_id": order_id
        }
        database[email] = license_data
        return jsonify(license_data), 200
    return jsonify({"error": "Invalid license key"}), 400

def generate_license_key(email):
    return hashlib.sha256(f"secret-{email}".encode()).hexdigest()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')