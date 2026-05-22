from Model.banco import salvar
from tkinter import messagebox

def verif_cadastro(produto, preco_txt, quantidade_txt):

    if not produto or not preco_txt or not quantidade_txt:
        messagebox.showwarning("Aviso!", "Os campos não podem ficar vazios!")
        return False
    
    try:
        preco = float(preco_txt)
        quantidade = int(quantidade_txt)

        salvar(produto, preco, quantidade)
        messagebox.showinfo("Sucesso!", "Produto cadastrado com sucesso!")
        return True

    except ValueError:
        messagebox.showerror("Erro!", "Apenas números em preço e quantidade!")
        return False
