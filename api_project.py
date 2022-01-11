# importing libraries and classes from the main flask framework
from flask import Flask, json, request, jsonify

# app is an object of a class flask whose constructor is Flask and argument is __name__
app = Flask(__name__)

# default list of contacts 
contacts = [{'id': 1, 'name':u'Mukesh', 'contact':u'9238402142', 'done': False},
            {'id': 2, 'name':u'Shravan', 'contact':u'2039420919', 'done': False}]

# the route for adding the data
@app.route('/add-data', methods = ['POST'])

def add_data():
    # if the request is not in json format then throw error
    if not request.json:
        return jsonify({
            'status': 'error',
            'message': 'please provide data'
        }, 400)

    # basic sturcture or format of adding the contacts
    contact = {
        'id': contacts[-1]['id'] + 1,
        'name': request.json['name'],
        'contact': request.json.get('contact', '  '),
        'done': False
    }

    # appending the newly added contacts to the main list
    contacts.append(contact)

    # returning a success message
    return jsonify({
        'status': 'success',
        'message': 'contact added successfully'
    })

# the route for getting or reading the data on local host 127.0.0.1
@app.route('/get-data')

def get_data():
    # simply returning the complete contacts data
    return jsonify({
        'data': contacts
    })

# typical flask running statement
if __name__ == '__main__':
    app.run(debug = True)