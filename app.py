from flask import Flask, render_template, request
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
import json
from db import db
from flask import make_response
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app, supports_credentials=True)


@app.after_request
def af_request(resp):
    """
     #请求钩子，在所有的请求发生后执行，加入headers。
    :param resp:
    :return:
    """
    resp = make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp



@app.route('/index')
def index():
    db.db_in()

    return render_template('index.html')



@app.route('/weather',methods=['POST','GET'])
def weather():
    ret = db.db_read()
    wendu = []
    shidu = []
    for i in ret:

        wendu.append(i[0])
        shidu.append(i[1])
    data = json.dumps({'wendu': wendu, 'shidu': shidu})
    return data


if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 5000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
