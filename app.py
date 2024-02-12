

from flask import Flask,request

app = Flask(__name__)


@app.route('/')

def basic():
    return 'api server started'

@app.route('/soil',methods=['get'])
def soil():
    value = request.args.get('soil')
    print(value)
    return{'msg':}

   if __name__=="main_":
    app.run('0.0.0.0',port=5001)