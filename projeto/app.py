import json, os
from flask import Flask, render_template, request, redirect, url_for
from ferramentas.ferramentas import calcular #Se colocar "*" ela importa tudo que estiver dentro

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculadora', methods=['GET', 'POST'])
def calculadora():
    result = None

    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operacao = request.form["operacao"]
        result = calcular(num1,num2,operacao)

    return render_template('calculadora.html', result=result)

@app.route('/ferramentas', methods=['GET', 'POST'])
def ferramentas():
    context = {}
    return render_template('ferramentas.html', context=context)
    

if __name__ == '__main__':
    app.run(debug=True)