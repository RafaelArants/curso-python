import json, os

def salvarDicionarioJson(dicionario, nome_arquivo='usuarios.json'):
    try:
        with open(nome_arquivo,"w", encoding='utf-8') as arquivo: #r Apenas ler
            json.dump(dicionario, arquivo, indent=4, ensure_ascii=False)
        print("Arquivo salvo com sucesso!")
    except:
        print("Erro ao salvar o arquivo!")

def carregarDicionarioJson(nome_arquivo='usuarios.json'):
    dicionario={}
    if os.path.exists(nome_arquivo):
        try:
            with open(nome_arquivo,"r", encoding='utf-8') as arquivo: #w Ler e alterar
                dicionario = json.load(arquivo)
                novo_dicionario= {}
                for chave,valor in dicionario.items():
                    novo_dicionario[int(chave)] = valor
                dicionario = novo_dicionario
        except:
            print("ERRO - Erro ao ler o arquivo!")
    return dicionario