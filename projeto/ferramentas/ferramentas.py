def calcular(num1,num2,operacao):
    if operacao == "soma":
        return f"{num1} + {num2} = {num1+num2}"
    elif operacao == "subtracao":
        return f"{num1} - {num2} = {num1-num2}"
    elif operacao == "multiplicacao":
        return f"{num1} * {num2} = {num1*num2}"
    elif operacao == "divisao":
        if num2 > 0:
            return f"{num1} / {num2} = {num1/num2}"
        else:
            return f"ERRO! - Divisão de {num1} por 0"
    elif operacao == "divisao_inteira":
        if num2 > 0:
            return f"{num1} // {num2} = {num1//num2}"
        else:
            return f"ERRO! - Divisão de {num1} por 0"
    elif operacao == "potencia":
        return f"{num1} ** {num2} = {num1**num2}"
    elif operacao == "modulo":
        return f"{num1} % {num2} = {num1%num2}"
    else:
        return "Operação Inválida!"

def parImpar(num):
    if num%2==0:
        return f"O número {num} é Par!"
    else:
        return f"O número {num} é Impar!"

def calcImc(peso,altura):
    imc = round(peso / (altura * altura),2)
    if imc < 16:
        return f"O seu IMC é de {imc}, e está classificado como Magreza Grave!"
    elif imc >= 16 and imc < 17:
        return f"O seu IMC é de {imc}, e está classificado como Magreza Moderada!"        
    elif imc >= 17 and imc < 18.5:
        return f"O seu IMC é de {imc}, e está classificado como Magreza Leve!"        
    elif imc >= 18.5 and imc < 25:
        return f"O seu IMC é de {imc}, e está classificado como Saudável!"       
    elif imc >= 25 and imc < 30:
        return f"O seu IMC é de {imc}, e está classificado como Sobrepeso!"        
    elif imc >= 30 and imc < 35:
        return f"O seu IMC é de {imc}, e está classificado como Obesidade Grau I!"        
    elif imc >= 35 and imc < 40:
        return f"O seu IMC é de {imc}, e está classificado como Obesidade Grau II!"    
    elif imc >= 40:
        return f"O seu IMC é de {imc}, e está classificado como Obesidade Grau III!"        
    else:
        return f"Valor inválido!"

def calcTabuada(num):
    resultado = []
    for i in range(1,11):
        resultado.append(f"{num} x {i} = {num*i}")
    return resultado

def calcPotencia(base,expoente):
    return f"O {base} elevado a {expoente} é {base ** expoente}"

def calcCombustivel(etanol,gasolina):
    combustivel = etanol / gasolina
    if combustivel <= 0.7:
        return f"Com base nos preços informados, será mais econômico abastecer com Etanol!"
    else:
        return f"Com base nos preços informados, será mais econômico abastecer com Gasolina!"

def calcTemp(temp,escala):
    if escala == "celsius":
        return f"A temperatura {temp}ºF convertido Celsius é {round((temp - 32)/1.8,2)}ºC"
    else:
        return f"A temperatura {temp}ºC convertido é Fahrenheit {round(temp * 1.8 + 32,2)}ºF"
    