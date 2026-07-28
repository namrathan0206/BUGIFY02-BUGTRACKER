from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import random
import traceback
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

# 1. FETCH THE ATLAS STRING FROM .env
MONGO_URI = os.getenv("MONGO_URI")

# 2. DEFINE THE DB VARIABLES GLOBALLY
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
db = client.bugify_db
tickets_col = db.tickets


# 3. TEST THE CONNECTION ON STARTUP
try:
    client.server_info() # This forces a connection check
    print("\n========================================")
    print("✅ DATABASE CONNECTED SUCCESSFULLY")
    print("========================================\n")
except Exception as e:
    print("\n========================================")
    print("❌ DATABASE CONNECTION FAILED!")
    print("Check your MONGO_URI string or your internet connection.")
    print("========================================\n")


@app.route('/')
def home():
    return render_template('dashboard.html')

# --- API ROUTES ---
@app.route('/api/tickets', methods=['GET', 'POST'])
def handle_tickets():
    try:
        if request.method == 'GET':
            tickets = list(tickets_col.find().sort('_id', -1))
            for t in tickets:
                t['_id'] = str(t['_id'])
            return jsonify(tickets), 200

        if request.method == 'POST':
            data = request.json
            data['bug_id'] = f"BUG-{random.randint(1000, 9999)}"
            data['created_at'] = datetime.now().strftime("%b %d, %Y")
            data['updated_at'] = data['created_at']
            
            result = tickets_col.insert_one(data)
            return jsonify({"msg": "Ticket Created", "id": str(result.inserted_id)}), 201
            
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({"error": str(e)}), 500

@app.route('/api/tickets/<id>', methods=['PUT', 'DELETE'])
def modify_ticket(id):
    try:
        if request.method == 'PUT':
            data = request.json
            data['updated_at'] = datetime.now().strftime("%b %d, %Y")
            tickets_col.update_one({"_id": ObjectId(id)}, {"$set": data})
            return jsonify({"msg": "Ticket Updated"}), 200

        if request.method == 'DELETE':
            tickets_col.delete_one({"_id": ObjectId(id)})
            return jsonify({"msg": "Ticket Deleted"}), 200
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # SOLUTION 1 APPLIED: Changed port to 5001 to avoid the binding error
    app.run(debug=True, port=5001)