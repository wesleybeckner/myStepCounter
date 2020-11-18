from flask import Flask, request
from flask_cors import CORS
import numpy as np
from engine import *

app = Flask(__name__) # create the Flask app
CORS(app) # allow requests from other domains

@app.route('/')
def check_working():
    return "Hello world"

@app.route('/steps', methods=['GET', 'POST'])
def img_url():
    if request.method == 'POST':
        url = request.get_json()
        steps = count_steps(url)
        return "{}".format(steps)
        print(steps)
    elif request.method == 'GET':
        return "Hello again"

if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000
