import customtkinter as ctk # alias - apelido

def calcular():
    num1 = float(entrada_num1.get())
    num2 = float(entrada_num2.get())
    op = operacao.get()

app = ctk.CTk() # Tela Principal

app.title("Calculadora CTK") # Titulo tela
app.geometry("400x300") # Tamanho tela

label_num1 = ctk.CTkLabel(app, text="Primeiro número:")
label_num1.pack(pady=5) 

entrada_num1 = ctk.CTkEntry(app, placeholder_text="Digite o primeiro número", width=200)
entrada_num1.pack(pady=5)

label_num2 = ctk.CTkLabel(app, text="Segundo número:")
label_num2.pack(pady=5) 

entrada_num2 = ctk.CTkEntry(app, placeholder_text="Digite o segundo número", width=200)
entrada_num2.pack(pady=5)

label_operacao = ctk.CTkLabel(app, text="Escolha a operação desejada:")
label_operacao.pack(pady=5) 

operacao = ctk.CTkOptionMenu(app, values=["+","-","*","/"])
operacao.set("+")
operacao.pack(pady=5)

botao_calcular = ctk.CTkButton(app, text="Calcular", command=calcular).pack()
#botao_calcular.pack(pady=5)















app.mainloop()