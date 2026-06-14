import tkinter as tk
from tkinter import messagebox

def adicionar_contato():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    if nome and telefone:
        lista_contatos.insert(tk.END, f"{nome} - {telefone}")
        entry_nome.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Por favor, preencha nome e telefone.")

def remover_contato():
    try:
        # Pega o índice do item selecionado
        indice_selecionado = lista_contatos.curselection()[0]
        lista_contatos.delete(indice_selecionado)
    except IndexError:
        messagebox.showwarning("Aviso", "Por favor, selecione um contato para remover.")

# --- Configuração da Janela ---
janela = tk.Tk()
janela.title("Lista de Contatos")

# --- Frame para os inputs ---
frame_inputs = tk.Frame(janela)
frame_inputs.pack(padx=10, pady=10)

tk.Label(frame_inputs, text="Nome:").grid(row=0, column=0)
entry_nome = tk.Entry(frame_inputs, width=20)
entry_nome.grid(row=0, column=1)

tk.Label(frame_inputs, text="Telefone:").grid(row=1, column=0)
entry_telefone = tk.Entry(frame_inputs, width=20)
entry_telefone.grid(row=1, column=1)

# --- Frame para os botões ---
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=5)

tk.Button(frame_botoes, text="Adicionar", command=adicionar_contato).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botoes, text="Remover", command=remover_contato).pack(side=tk.LEFT, padx=5)

# --- Listbox para exibir os contatos ---
lista_contatos = tk.Listbox(janela, width=40, height=10)
lista_contatos.pack(padx=10, pady=10)

# --- Inicia a Janela ---
janela.mainloop()