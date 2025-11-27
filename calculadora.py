import customtkinter as ctk # alias - apelido

app = ctk.CTk() # Tela Principal

app.title("Calculadora CTK") # Titulo tela
app.geometry("400x300") # Tamanho tela

label_num1 = ctk.CTkLabel(app, text="Primeiro Número:")
label_num1.pack(pady=10) 














app.mainloop()