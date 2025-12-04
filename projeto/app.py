import json, os
from flask import Flask, render_template, request, redirect, url_for
from ferramentas.ferramentas import * #Se colocar "*" ela importa tudo que estiver dentro

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

    if request.method == "POST":
        if "verificar_par_impar" in request.form:
            num = int(request.form["num"])
            context["par_impar_result"] = parImpar(num)
        elif "calc_imc" in request.form:
            peso = float(request.form["peso"])
            altura = float(request.form["altura"])
            context["imc_result"] = calcImc(peso,altura)
        elif "gerar_tabuada" in request.form:
            num = int(request.form["num"])
            context["tabuada_result"] = calcTabuada(num)
        elif "calc_potencia" in request.form:
            base = float(request.form["base"])
            expoente = int(request.form["expoente"])
            context["potencia_result"] = calcPotencia(base,expoente)
        elif "calc_combustivel" in request.form:
            etanol = float(request.form["etanol"])
            gasolina = float(request.form["gasolina"])
            context["combustivel_result"] = calcCombustivel(etanol,gasolina)
        #elif "convert_temp" in request.form:
         #   temp = float(request.form["temp"])
          #  escala = request.form["escala"]
           # context["temp_result"] = calcTemp(temp,escala)

    return render_template('ferramentas.html', context=context)
    

if __name__ == '__main__':
    app.run(debug=True)