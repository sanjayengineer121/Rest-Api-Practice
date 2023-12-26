from flask import Flask, render_template,jsonify,request
import json
from tabulate import tabulate

app = Flask(__name__)


def load_data():
    try:
        with open('books.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"books": {"person": []}}

data = load_data()

def display_data_in_terminal():
    table_data = []
    for person in data['books']['person']:
        table_data.append([person['id'], person['name'], person['age'], person['gender']])

    headers = ["ID", "Name", "Age", "Gender"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
@app.route('/')
def home():

    content = """
Home Page:
    Endpoint: /
    Description: Provides information about REST API calling.

Endpoint for Retrieving All Persons:
    Endpoint: /persons
    Description: Returns all information in tabular format for persons. Output is in the Command Line Interface (CLI).

Endpoint for Retrieving User Information:
    Endpoint: /api/books/person
    Description: Returns user information in REST API format.

Endpoint for Retrieving Specific User Information:
    Endpoint: /api/books/person/<int:id>
    Description: Returns information for a specific user identified by the provided `id`.

Endpoint for Posting User Information:
    Endpoint: /api/books/person
    Method: POST
    Description: Allows posting user information in JSON format. Sample JSON data:
        {
            "name": "monika",
            "age": 23,
            "gender": "female"
        }

Endpoint for Updating User Information:
    Endpoint: /api/books/person/<int:id>
    Method: PUT
    Description: Updates information for a specific user identified by the provided `id`. Example curl command:
        curl -X PUT -H "Content-Type: application/json" -d "{\"id\": 1, \"title\": \"Updated Title\", \"author\": \"Updated Author\"}" http://127.0.0.1:5000/api/books

Endpoint for Deleting Specific User Information:
    Endpoint: /api/books/person/<int:id>
    Method: DELETE
    Description: Deletes information for a specific user identified by the provided `id`.
"""

    print(content)

    return render_template('h.html')

@app.route('/persons', methods=['GET'])
def show_persons():
    display_data_in_terminal()
    return render_template('books.html', persons=data['books']['person'])

# Load initial data from a JSON file
def load_data():
    try:
        with open('books.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"books": {"person": []}}

# Save data to the JSON file
def save_data(data):
    with open('books.json', 'w') as file:
        json.dump(data, file, indent=2)

data = load_data()

@app.route('/api/books/person', methods=['GET'])
def get_persons():
    return jsonify(data['books']['person'])

@app.route('/api/books/person/<int:person_id>', methods=['GET'])
def get_person(person_id):
    person = next((person for person in data['books']['person'] if person['id'] == person_id), None)
    if person is None:
        return jsonify({'error': 'Person not found'}), 404
    return jsonify({'person': person})

@app.route('/api/books/person', methods=['POST'])
def create_person():
    data_from_request = request.get_json()
    new_person = {
        'id': len(data['books']['person']) + 1,
        'name': data_from_request['name'],
        'age': data_from_request['age'],
        'gender': data_from_request['gender']
    }
    data['books']['person'].append(new_person)
    
    # Save updated data to the JSON file
    save_data(data)
    
    return jsonify({'message': 'Person created', 'person': new_person}), 201

@app.route('/api/books/person/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    person = next((person for person in data['books']['person'] if person['id'] == person_id), None)
    if person is None:
        return jsonify({'error': 'Person not found'}), 404

    data_from_request = request.get_json()
    person['name'] = data_from_request.get('name', person['name'])
    person['age'] = data_from_request.get('age', person['age'])
    person['gender'] = data_from_request.get('gender', person['gender'])

    # Save updated data to the JSON file
    save_data(data)

    return jsonify({'message': 'Person updated', 'person': person})

@app.route('/api/books/person/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    person = next((person for person in data['books']['person'] if person['id'] == person_id), None)
    if person is None:
        return jsonify({'error': 'Person not found'}), 404

    data['books']['person'].remove(person)

    # Save updated data to the JSON file
    save_data(data)

    return jsonify({'message': 'Person deleted', 'person': person})
# Additional routes (update_person, delete_person) can be modified similarly

if __name__ == '__main__':
    app.run(debug=True)
