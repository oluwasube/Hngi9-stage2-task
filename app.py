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
    x =int(request.json['x'])
    y = int(request.json['y'])
      
    result =0
    if operation_type == "minus" or operation_type == "subtract" or operation_type == "subtraction":
        result = x - y
    if operation_type == "add" or operation_type == "addition" or operation_type == "plus":
        result = x + y
    if operation_type == "multiply" or operation_type == "multiplication":
        result = x * y
    return jsonify({
            'slackUsername': 'oluwasube',
            'result': result,
            'operation_type': operation_type
        })
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


