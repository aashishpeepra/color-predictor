import flask
from flask import request , jsonify
from withoutML1 import predict
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
@app.route('/color',methods=['GET'])
def colorShow():
    if 'color' in request.args:
        colorRaw=request.args['color']
        colorHex=[colorRaw[0:2],colorRaw[2:4],colorRaw[4:]]
        colorUnhexed=[int(each,16) for each in colorHex]
        return str(predict(colorUnhexed))
    else:
        return '<h1>Provide Someting </h1>'


app.run()