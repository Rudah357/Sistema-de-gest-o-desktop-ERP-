from Model.banco import salvar
from tkinter import messagebox

def verif_cadastro(produto, preco_txt, quantidade_txt):

    if produto == "" or preco_txt == "" or quantidade_txt == "":
        return False, messagebox.showwarning("Aviso!", "Os campos não podem ficar vazios!")
    
    try:
        preco = float(preco_txt)
        quantidade = int(quantidade_txt)

    except ValueError:
        return False, messagebox.showerror("Erro!", "Apenas números em preço e quantidade!")
    
    salvar(produto, preco, quantidade)
    return True, messagebox.showinfo("Sucesso!", "Produto cadastrado com sucesso!")
    
