from flask import Flask

#create application
app = Flask(__name__)

# load the views
@app.route('/')
def hello():
    return 'Hello World!'

# run flask application
if __name__ == '__main__':
    app.run()
