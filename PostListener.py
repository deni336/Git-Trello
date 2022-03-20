from flask import Flask
from flask import request
from flask import json  #importing json cause that’s what we’re going to be working with


app = Flask(__name__)

@app.route('/')
def root():
  return 'Hello World!'

@app. route('/hooktest', methods=[''])  # ‘/hooktest’ specifies which link will it work on 
def hook_root():
  if request.headers['Content-Types'] == 'application/json':  # calling json objects
    return json.dumps(request.json)

if __name__ == '__main__':
    app.run(debug=True)
    x = hook_root()
    print(x)