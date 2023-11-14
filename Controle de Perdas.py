import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk

valores = []

def salvar_valores():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de texto", "*.txt")])
    if filename:
        with open(filename, "w") as file:
            for valor_ean, valor_qtd in valores:
                file.write(f"{valor_ean};{valor_qtd}\n")
            label_status.configure(text=f"Valores salvos em {filename}")
        valores.clear()
        root.after(3000, limpar_status)

def adicionar_valor():
    valor_ean = entry_ean.get()
    valor_qtd = entry_qtd.get()
    
    if len(valor_ean) < 13:
        valor_ean = "0" * (13 - len(valor_ean)) + valor_ean
    elif len(valor_ean) > 13:
        label_status.configure(text="Código com mais de 13 dígitos.")
        label_status.configure(font=("Arial", 18, "bold"))
        root.after(3000, limpar_status)  
        return

    if len(valor_qtd) < 6:
        valor_qtd = "0" * (6- len(valor_qtd)) + valor_qtd
    elif len(valor_qtd) > 6:
        label_status.configure(text="Quantidade absurda. Verifique.")
        label_status.configure(font=("Arial", 18, "bold",))
        root.after(3000, limpar_status)  
        return

    if valor_ean.isdigit() and valor_qtd.isdigit():
        valores.append((valor_ean, valor_qtd))
        entry_ean.delete(0, 'end')  
        entry_qtd.delete(0, 'end')
        entry_ean.focus_set()  # Retorna o foco para a primeira caixa de texto

def limpar_status():
    label_status.configure(text="")

root = ctk.CTk()
root.title("TÍTULO DO SEU PROGRAMA AQUI")
root.geometry("400x400")
ctk.set_appearance_mode("dark")

# Rótulo
label_ean = ctk.CTkLabel(root, text="Digite o código EAN:")
label_ean.pack(pady=10)
label_ean.configure(font=("Arial", 14, "bold"))

entry_ean = ctk.CTkEntry(root)
entry_ean.pack(pady=10, padx=25)

label_qtd = ctk.CTkLabel(root, text="Digite a quantidade:")
label_qtd.pack(pady=10)
label_qtd.configure(font=("Helvetica", 14, "bold"))

entry_qtd = ctk.CTkEntry(root)
entry_qtd.pack(pady=10)

botao_adicionar = ctk.CTkButton(root, text="Adicionar Produto", command=adicionar_valor)
botao_adicionar.pack(side=tk.TOP, padx=10, pady=10)

botao_salvar = ctk.CTkButton(root, text="Salvar Valores", command=salvar_valores)
botao_salvar.pack(side=tk.TOP, padx=10, pady=10)

label_status = ctk.CTkLabel(root, text="")
label_status.pack(pady=10)

entry_ean.bind('<Tab>', lambda e: entry_qtd.focus_set())
entry_qtd.bind('<Tab>', lambda e: entry_ean.focus_set())

# Associar a tecla "Enter" para mover do entry_ean para entry_qtd
entry_ean.bind('<Return>', lambda e: entry_qtd.focus_set())
# Associar a tecla "Enter" na segunda caixa de texto para adicionar o valor
entry_qtd.bind('<Return>', lambda e: adicionar_valor())

root.mainloop()
