from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return "Hello, World!"

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    #server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    app.run(debug=True)