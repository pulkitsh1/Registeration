from flask import Flask,jsonify
from function import sign_up,sign_in,update,fetch,delete

app = Flask(__name__)

@app.route('/', methods=['POST'])
def add():
    response = sign_up.registeration()
    return jsonify(response[0]),response[1]
    
@app.route('/login', methods=['POST'])
def login():
    response = sign_in.login()
    return jsonify(response[0]),response[1]
    
@app.route("/updateName", methods=['POST'])
def updateName():
    response = update.updateName()
    return jsonify(response[0]),response[1]

@app.route('/display_info', methods=['GET'])
def display_info():
    response = fetch.display_info()
    return jsonify(response[0]),response[1]

@app.route('/delete', methods=['POST'])
def remove_user():
    response = delete.delete()
    return jsonify(response[0]),response[1]
    

if __name__ == '__main__':
    app.run(debug=True)
