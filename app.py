import socket

from flask import Flask, request

app = Flask(__name__)

@app.route('/', defaults={'path': '/'})
@app.route('/<path:path>')
def return_hostname(path):
    return "<h1>Path {} served from host : {}</h1>".format(path, socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, use_debugger=False, use_reloader=True)
