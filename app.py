
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


@app.route('/dapo-deals', methods=['GET'])
def get_trello_cards():
    import requests

    # Required variables
    TRELLO_KEY = "c611d1b1dd04272aa836a448757305bc"
    TRELLO_TOKEN = "832d493718c3689b5d0b2cc70ed43eb5c45ff2b15e7db32f9a0ad3427978ec40"

    # Trello related variables - get cards only in a specific list
    trello_api_url = 'https://api.trello.com'
    list_id = '5f5bad694e5dea1cec83b4ad' # Deal List
    card_list_filter = 'open'

    cards_url =  '{trello_api_url}/1/lists/{list_id}/cards?key={YourAPIKey}&token={TrelloToken}&filter={card_list_filter}'.format(trello_api_url=trello_api_url, list_id=list_id, YourAPIKey=TRELLO_KEY, TrelloToken=TRELLO_TOKEN, card_list_filter=card_list_filter)


    def parse_trello_response(json_response):
        card_data_list = []
        for card in json_response:
            card_dict = {}
            card_labels = []
            card_dict['name'] = card.get('name')

            if card.get('labels'):
                for label in card.get('labels'):
                    _label_dict = {}
                    _label_dict['color'] = label.get('color')
                    _label_dict['name'] = label.get('name')
                    card_labels.append(_label_dict)
            card_dict['labels'] = card_labels
            card_data_list.append(card_dict)

        return card_data_list


    # Call Trello API
    req = requests.get(cards_url)
    req_text = False
    try:
        req_text = json.loads(req.text)
        req_text = parse_trello_response(req_text)
    except Exception as e:
        print("Error parsing response as JSON: {}, Response: {}".format(e, req.text))
        return make_response(jsonify({'error': req.text}), 500)

    return jsonify({'cards':req_text})

@app.route('/dapo/')
def deals():
    return app.send_static_file('deals.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)
