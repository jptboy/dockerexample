from flask import Flask
from flask import request
from flask import jsonify
from pymongo import MongoClient
import datetime
import json
import os
from flask_cors import CORS
import unittest
app = Flask(__name__)
CORS(app)

@app.route("/gettasks",methods = ['GET'])
def getTasks():
    coll = connectDb()
    cursor = coll.find({})
    q = []
    for c in cursor:
        obj = {}
        for key in c.keys():
            if key != "_id":
                obj[key] = c[key]
        q.append(obj)
    ret = jsonify(q)
    return ret,200

@app.route("/puttask",methods = ['POST'])
def putTask():
    tasks = connectDb()
    data = request.data.decode('utf-8')
    datadict = json.loads(data)
    datadict["Time"] = str(datetime.datetime.now())
    tasks.insert_one(datadict)
    return ('',204)
@app.route("/deltask",methods = ['DELETE'])
def delTask():
    data = request.data.decode('utf-8')
    datadict = json.loads(data)
    name = datadict["Name"]

    coll = connectDb()
    try:
        qret = coll.delete_one({"Name":name})
        if qret.deleted_count == 0:
            return ("Nothing was deleted")
    except:
        return ("Failure",500)

    return ("Success",200)
def connectDb():
    client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)
    db = client.flaskdb
    return db.tasks
if __name__ == "__main__":
    app.run(port=8080,host="0.0.0.0")