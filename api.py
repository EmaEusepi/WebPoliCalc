from flask import Flask, request, jsonify, render_template
from calculator_service import (
    add,
    subtract,
    multiply,
    divide,
    power,
    square_root,
    modulus,
)

app = Flask(__name__, template_folder="templates")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET"])
def add_route():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    result = add(a, b)
    return jsonify(result=result)


@app.route("/subtract", methods=["GET"])
def subtract_route():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    result = subtract(a, b)
    return jsonify(result=result)


@app.route("/multiply", methods=["GET"])
def multiply_route():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    result = multiply(a, b)
    return jsonify(result=result)


@app.route("/divide", methods=["GET"])
def divide_route():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    try:
        result = divide(a, b)
        return jsonify(result=result)
    except ValueError as e:
        return jsonify(error=str(e)), 400


@app.route("/power", methods=["GET"])
def power_route():
    base = float(request.args.get("base", 0))
    exp = float(request.args.get("exp", 0))
    result = power(base, exp)
    return jsonify(result=result)


@app.route("/square-root", methods=["GET"])
def square_root_route():
    num = float(request.args.get("num", 0))
    result = square_root(num)
    return jsonify(result=result)


@app.route("/modulus", methods=["GET"])
def modulus_route():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    result = modulus(a, b)
    return jsonify(result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
