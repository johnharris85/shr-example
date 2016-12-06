import socket

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def return_hostname():
    return "<h1>Page served from host : {}</h1>".format(socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, use_debugger=False, use_reloader=True)
