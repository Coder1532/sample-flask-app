from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hola')
def hello_world2():
    return 'Hola'

# if __name__ == '__main__':
#     app.run()
