from flask import Flask, jsonify, session, request, redirect, url_for,send_from_directory, Response
import json
from dataset import *
from input_data import *
from flask_cors import CORS
import psycopg2

app = Flask(__name__)

db_data= DBData()
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

conn = psycopg2.connect(
    host = db_data.host,
    dbname = db_data.dbname,
    user = db_data.user,
    password = db_data.password,
    port = 5432
)
cur = conn.cursor()
print('Connected to the PostgreSQL database')

def collect_data():
    with open("sample_dataset.json") as f:
        input = json.load(f)
    ransomware_data = RansomwareSet(input)    
    return ransomware_data

app = Flask(__name__)



@app.route('/login', methods=['POST'])
def login():
    # Load all data from file
    ransomware_data = collect_data()
    for i in ransomware_data.data:
        query = f"SELECT * FROM ransomware WHERE name = ARRAY {str(i.name).replace('"',"'")} ;"
        cur.execute(query)
        entry = cur.fetchone()
        if entry is not None:
            #print(f"Skipped {i.name}")
            continue
        query="INSERT INTO ransomware (name, extensions, extensionPattern , ransomNoteFilenames , comment ,encryptionAlgorithm ,decryptor, resources ,screenshots ) "
        query+= f" VALUES(ARRAY {str(i.name).replace('"',"'")},'{i.extensions}','{i.extensionPattern}','{i.ransomNoteFilenames}','{i.comment.replace("'","''")}','{i.encryptionAlgorithm}','{i.decryptor}',ARRAY {str(i.resources).replace('"',"'")},'{i.screenshots}');"
        cur.execute(query)
        
    return jsonify({"msg" : "Initialized"}), 200

@app.route('/ransom', methods=['POST'])
def add_entry():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    content = request.json
    data = Ransomware.from_dict(content)
    query = f"SELECT * FROM ransomware WHERE name = ARRAY {str(data.name).replace('"',"'")} ;"
    cur.execute(query)
    entry = cur.fetchone()
    if entry is not None:
        return jsonify({"msg":'Name already exsist '}), 409
    query="INSERT INTO ransomware (name, extensions, extensionPattern , ransomNoteFilenames , comment ,encryptionAlgorithm ,decryptor, resources ,screenshots ) "
    query+= f" VALUES(ARRAY {str(data.name).replace('"',"'")},'{data.extensions}','{data.extensionPattern}','{data.ransomNoteFilenames}','{data.comment.replace("'","''")}','{data.encryptionAlgorithm}','{data.decryptor}',ARRAY {str(data.resources).replace('"',"'")},'{data.screenshots}');"
    print(query)
    cur.execute(query)
    return jsonify({"msg" : "Data added"}), 200

@app.route('/ransoms', methods=['GET'])
def get_all():
    cur.execute("SELECT * FROM ransomware;")
    entries = cur.fetchall()
    return jsonify({"data" : entries}), 200
    
@app.route('/ransom/', methods=['GET'])
def get():
    name_list = request.args.getlist('name')
    query = f"SELECT * FROM ransomware WHERE name = ARRAY{str(name_list).replace('"',"'")};"
    cur.execute(query)
    entry = cur.fetchone()
    if entry is None:
        return jsonify({"data" : "Data not Found"}), 404
    return jsonify({"data" : entry}), 200

@app.route('/ransom/', methods=['DELETE'])
def delete():
    name_list = request.args.getlist('name')
    query = f"DELETE FROM ransomware WHERE name = ARRAY {str(name_list).replace('"',"'")};"
    cur.execute(query)
    return jsonify({"msg" : "Data Deleted"}), 200

@app.route('/ransom/', methods=['PUT'])
def put():
    name_list = request.args.getlist('name')
    content = request.json
    key=list(content.keys())[0]
    query = f"UPDATE ransomware  SET {key} = '{content[key]}' WHERE name = ARRAY {str(name_list).replace('"',"'")};"
    cur.execute(query)
    return jsonify({"msg" : "Data updated"}), 200

if __name__ == "__main__":
    with app.app_context():
        app.run(host='127.0.0.1',port=8000,debug=True)