from app import app
from flask import request, jsonify


@app.route('/')
def hello():
    return "Hello World"


@app.route('/arithmetic', methods = ['GET','POST'])
def arithmetic():
    num1 = []
    num1 = request.args.get('a')
    num2 = request.args.get('b')
    op = request.args.get('op')
    try:
        if op is '/':
            result = 'The div is :' + str(int(num1)/(int(num2)))
        elif op is '-':
            result = 'The sub is :' + str(int(num1)-(int(num2)))
        elif op is '*':
            result = 'The product is :' + str(int(num1)*(int(num2)))
        else:
            result = 'The sum is :' + str(int(num1)+(int(num2)))
    except ZeroDivisionError:
        result = "Number not divided by zero"


    return jsonify({"result":result})