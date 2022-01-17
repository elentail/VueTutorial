import time
import flask
from flask_cors import CORS
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
        
def generator_stream():
    for i in range(50):
        time.sleep(1)
        yield  "data: {}\n\n".format(i)

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/api/stream')
def stream():
    #return flask.Response(event_stream(), mimetype="text/event-stream")
    return flask.Response(generator_stream(), mimetype="text/event-stream")

@app.route('/codes')
def codes():
    tf_code = "\nimport tensorflow as tf\nimport numpy as np"
    torch_code = "\nimport torch\nimport torch.nn as nn"
    return jsonify(tf_code=tf_code, torch_code=torch_code)

@app.route('/api/chart')
def chart():
    ret_dict ={
        'labels': ['one', 'two'],
        'datasets': [
            {
                'label': 'Data One',
                'backgroundColor': '#f87979',
                'data': [20, 50, 80, 90, 30]
            },
            {
                'label': 'Data One',
                'backgroundColor': '#f85979',
                'data': [30, 40, 30]
            },
        ]}
    return ret_dict

@app.route('/api/chart2')
def chart2():
    ret_dict ={
        'labels': ['one', 'two', 'three'],
        'datasets': [
            {
                'label': 'Data One',
                'backgroundColor': '#f87979',
                'data': [20, 50, 80, 90, 30]
            },
            {
                'label': 'Data One',
                'backgroundColor': '#f85979',
                'data': [30, 40, 30]
            },
            {
                'label': 'Data One',
                'backgroundColor': '#f47949',
                'data': [20, 50, 80, 90, 30]
            },
        ]}
    return ret_dict


if __name__ == '__main__':
    app.run(threaded=True)
