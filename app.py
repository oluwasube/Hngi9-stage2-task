from flask import Flask, request,  jsonify
from flask_cors import CORS

#configure the app
app = Flask(__name__)

CORS(app, resources={r'/api/*':{'origins':'*'}})


@app.route('/api/v1/compute', methods= ['POST'])
def post_computation():
      # Unpacking the data posted to the API
    request_json = request.get_json()
    operation_type= request_json('operation_type')
    x = request_json('x')
    y = request_json('y')
      
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
            'operation_type': operation_type
        })
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


