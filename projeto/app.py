import json, os
from flask import Flask, render_template, request, redirect, url_for
from ferramentas.ferramentas import * #Se colocar "*" ela importa tudo que estiver dentro
from ferramentas.apis import *
from datetime import datetime
#pip install datetime

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', users=users)

def recuperaInfo():
    dados = {}
    if request != None:
        dados = {
            'nome': request.form.get('nome', '').strip(),
            'sobrenome': request.form.get('sobrenome', '').strip(),
            'email': request.form.get('email', '').strip(),
            'data_nascimento': request.form.get('data_nascimento', '').strip(),
            'cep': request.form.get('cep', '').strip(),
            'endereco': request.form.get('endereco', '').strip(),
            'numero': request.form.get('numero', '').strip(),
            'complemento': request.form.get('complemento', '').strip(),
            'bairro': request.form.get('bairro', '').strip(),
            'cidade': request.form.get('cidade', '').strip(),
            'estado': request.form.get('estado', '').strip()            
        }
    return dados

@app.route('/gerenciar_usuario', methods=['GET', 'POST'])
def gerenciar_usuario():

    user_id = request.args.get('user_id', type=int)

    if user_id is not None and user_id not in users:
        return redirect(url_for('usuarios'))
    
    user = users.get(user_id)

    if request.method == "POST":
        dados_usuario = recuperaInfo()

        if "buscar_cep" in request.form:
            if user is None:
                user = dados_usuario
            retorno = buscarEndereco(request.form['cep'])
            if retorno:
                user.update({
                    'endereco': retorno.get('logradouro', '').strip(),
                    'bairro': retorno.get('bairro', '').strip(),
                    'complemento': retorno.get('complemento', '').strip(),
                    'estado': retorno.get('estado', '').strip(),
                    'cidade': retorno.get('localidade', '').strip(),
                    'cep': retorno.get('cep', '').strip()
                })
            return render_template('gerenciar_usuario.html', user=user, user_id=user_id)

        #Editar
        if user_id is not None and user_id in users:
            users[user_id] = dados_usuario
        else: #Inserir
            id = max(users.keys(), default=0) + 1
            users[id] = dados_usuario

        return redirect(url_for('usuarios'))

    return render_template('gerenciar_usuario.html', user = user, user_id = user_id)

@app.route('/excluir_usuario/<int:user_id>')
def excluir_usuario(user_id):
    return redirect(url_for('usuarios'))

@app.route('/api', methods=['GET', 'POST'])
def api():
    context = {}

    if request.method == "POST":
        if "consulta_cep" in request.form:
            cep = request.form["cep"]
            context["api_cep"] = buscarEndereco(cep)
        elif "consulta_moeda" in request.form:
            selecao = request.form["moedas"]
            resposta = cotacaoMoedas(selecao)
            retorno = {}
            if type(resposta) is dict:
                moeda = request.form['moedas'].replace("-", "")
                moeda_dados = resposta[moeda]
                retorno['nome'] = moeda_dados['name']
                retorno['compra'] = formatar_reais(moeda_dados['bid'])
                retorno['venda'] = formatar_reais(moeda_dados['ask'])
                retorno['data'] = datetime.strptime(moeda_dados['create_date'], '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')
            else:
                retorno['mensagem'] = "Erro ao consultar"
            context["api_moedas"] = retorno


    return render_template('api.html', context=context)

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
        elif "convert_temp" in request.form:
            temp = float(request.form["temp"])
            escala = request.form["escala"]
            context["temp_result"] = calcTemp(temp,escala)

    return render_template('ferramentas.html', context=context)
    

if __name__ == '__main__':
    app.run(debug=True)