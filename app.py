
from flask import Flask, jsonify, make_response, request
import json

app = Flask(__name__, static_url_path='/home/ubuntu/psp-test/static/')

from flask import make_response

import requests
import json, csv
import pymongo
import urllib

mongo_uri = "mongodb+srv://dbuser:" + urllib.parse.quote("xyzabc") + "@cluster0.pibqa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongo_uri)
current_db = client.psp


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


members = [
    {
        'id': 1,
        'name': u'John Tan',
        'ward': u'AMK',
        'done': False
    },
    {
        'id': 2,
        'name': u'Florence Lee',
        'ward': u'West Coast',
        'done': False
    }
]


@app.route('/')
def root():
	return app.send_static_file('index.html')

@app.route('/members/<id>/', methods=['GET'])
def get_task(id):
    id = int(id)
    return jsonify({'member': members[id]})



@app.route('/members/', methods=['GET'])
def get_tasks():
    _cursor = current_db.members.find({}, {'_id': False})
    print (dir(_cursor))
    _members = list(_cursor)
    return jsonify({'members':_members})

@app.route('/viz/', methods=['GET'])
def do_viz():
    _cursor = current_db.members.find({}, {'_id': False})

    _members = list(_cursor)
    doc = []
    for m in _members:
        doc.append(m.get("form_response").get('answers')[1].get('choice').get('label'))
    print (doc)
    return jsonify({'survey':doc})





@app.route('/addmember/', methods=['POST'])
def create_task():







    #if not request.json or not 'title' in request.json:
    #    abort(400)
    #task = {
    #    'id': tasks[-1]['id'] + 1,
    #    'title': request.json['title'],
    #    'description': request.json.get('description', ""),
    #    'done': False
    #}
    #tasks.append(task)
    data = request.json
    print (data)



    l1 = data
    #f = db.members.insert_many(l)
    f = current_db.members.insert_one(l1)
    print (f)

    '''
    with open("/home/ubuntu/psp-test/myfile.txt", "a+") as fo:
        fo.write(json.dumps(data))
        fo.write('\n')
    '''

    return 'ok', 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)
