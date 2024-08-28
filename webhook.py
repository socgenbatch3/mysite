from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_request():
    if request.method == 'GET':
        return jsonify({"message": "Hello, world!"})
    elif request.method == 'POST':
        print(request.json)
        return jsonify({"message": "POST request received", "data": request.json})
    elif request.method == 'PUT':
        return jsonify({"message": "PUT request received"})
    elif request.method == 'DELETE':
        return jsonify({"message": "DELETE request received"})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
#create venv
mkdir venv 
python3 -m venv venv
pip3 install flask
#  run program
python3 webhook.py

