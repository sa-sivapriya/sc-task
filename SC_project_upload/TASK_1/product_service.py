from flask import Flask, jsonify, session, request, redirect, url_for,send_from_directory
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
import psycopg2
from input_data import *
from flask_cors import CORS
from helper import *
import jwt

app = Flask(__name__)

db_data= DBData()
access_data= AccessData()

products = {

}

app.config['SECRET_KEY'] = access_data.secret_key
app.config["JWT_SECRET_ADMIN_KEY"] = access_data.jwt_secret_admin_key
app.config["JWT_SECRET_KEY"] = access_data.jwt_secret_key
app.config['JWT_TOKEN_LOCATION'] = access_data.jwt_token_location
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

conn = psycopg2.connect(
    host = db_data.host,
    dbname = db_data.dbname,
    user = db_data.user,
    password = db_data.password,
    port = 5432
)
#jwt = JWTManager(app)

cur = conn.cursor()
print('Connected to the PostgreSQL database')

@app.route('/')
def home():
    return "Hello world"

@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    cur.execute(f"SELECT * FROM login_details where username = '{username}' ;")
    user = cur.fetchall()
    
    if len(user) < 1 or user[0][1] != password :
        return jsonify({"msg": "Invalid username or password"}), 401

    payload = {
                    'name': user[0][0],
                    'admin': user[0][2]
                    }
    if user[0][2] :
        
        access_token= jwt.encode(payload,app.config.get('JWT_SECRET_ADMIN_KEY'),algorithm='HS256')
        #access_token = create_access_token(identity=username)
    else:
        access_token= jwt.encode(payload,app.config.get('JWT_SECRET_KEY'),algorithm='HS256')

    return jsonify({"access_token" : access_token}), 200


@app.route('/products', methods=['GET'])
def get_all_products(): 
    return jsonify(products), 200

@app.route('/products/<product_name>', methods=['GET'])
def get_product(product_name):
    if product_name not in products:
        return jsonify({"msg": f"Product {product_name} not found"}), 404
    return jsonify({product_name : products[product_name]}), 200

@app.route('/products', methods=['POST'])
def post_product():
    content = request.json
    access_token = content["access_token"]
    debug = decode_auth_token(access_token,app.config.get('JWT_SECRET_ADMIN_KEY'))
    if debug != 'success' :
        return jsonify({"msg": debug}), 401
    if content["product_name"] in products:
        return jsonify({"msg":'Product already exsist '}), 409
    products[content["product_name"] ]= content["product_desc"]
    return 'Product added successfully', 200

if __name__ == "__main__":
    with app.app_context():
        app.run(host='127.0.0.1',port=8000,debug=True)