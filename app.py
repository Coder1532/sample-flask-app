from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# CORS(app, resources={r"/api/":{"origins":"https://sample-api-call.gowrisivaramp.repl.co"}})
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/api/hola', methods=['GET'])
def hello_world2():
    return 'Hola'

# if __name__ == '__main__':
#     app.run()
