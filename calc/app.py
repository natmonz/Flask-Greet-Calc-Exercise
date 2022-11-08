# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)


@app.route('/add')
def add_calc():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    result = add(a, b)
    return str(result)


@app.route('/sub')
def sub_calc():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    result = sub(a, b)
    return str(result)


@app.route('/mult')
def mult_calc():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    result = mult(a, b)
    return str(result)


@app.route('/div')
def div_calc():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    result = div(a, b)
    return str(result)

    # FURTHER STUDY
# create a dict of operations
operators = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div,
}


@app.route('/math/<math_op>')
def math_operation(math_op):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    op_result = operators[math_op](a, b)

    return str(op_result)
