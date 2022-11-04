from flask import Flask, request,  jsonify
from flask_cors import CORS

#configure the app
app = Flask(__name__)

CORS(app)


@app.route('/')
def home():
    return "Computation"


@app.route('/api/compute', methods= ['POST'])
def post_computation():
      # Unpacking the data posted to the API
    
    operation_type= request.json['operation_type']
    x =request.json['x']
    y = request.json['y']
      
    result =0
    if operation_type == "minus" or operation_type == "substract" or operation_type == "substraction":
        result = x - y
    if operation_type == "add" or operation_type == "addition":
        result = x + y
    if operation_type == "multiply" or operation_type == "multiplication":
        result = x * y
    return jsonify({
            'slackUsername': 'oluwasube',
            'result': result,
            'tion_type': operation_typeopera
        })
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


