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