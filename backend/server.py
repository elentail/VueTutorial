import time
import flask
from flask_cors import CORS
from flask import Flask, render_template, request

app = Flask(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
app.debug = True

        
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



if __name__ == '__main__':
    app.run(threaded=True)