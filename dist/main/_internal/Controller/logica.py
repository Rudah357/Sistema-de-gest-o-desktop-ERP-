import os
from tkinter import messagebox
from Model.banco import salvar, buscar, atualizar, excluir, listar, buscar_por_nome

ARQUIVO_CONFIG = "config_tema.txt"

# Cadastro ----------------------------------------------------------------------
def verif_cadastro(produto, preco_txt, quantidade_txt):
    if not produto or not preco_txt or not quantidade_txt:
        messagebox.showwarning("Aviso!", "Os campos não podem ficar vazios!")
        return False
    
    produto_formatado = produto.strip().capitalize()
    produto_existente = buscar_por_nome(produto_formatado)

    if produto_existente:
        messagebox.showwarning("Produto Duplicado", f"O produto '{produto_formatado}' já está cadastrado no sistema!")
        return False
    
    try:

        preco = float(preco_txt.replace(",", "."))
        quantidade = int(quantidade_txt)

        salvar(produto, preco, quantidade)
        messagebox.showinfo("Sucesso!", "Produto cadastrado com sucesso!")
        return True

    except ValueError:
        messagebox.showerror("Erro!", "Apenas números em preço e quantidade!")
        return False

# Config ----------------------------------------------------------------------

def salvar_tema_config(tema):
    with open(ARQUIVO_CONFIG, "w") as f:
        f.write(tema)

def carregar_tema_config():
    if os.path.exists(ARQUIVO_CONFIG):
        with open(ARQUIVO_CONFIG, "r") as f:
            tema = f.read().strip()
            if tema in ["Light", "Dark"]:
                return tema
    return "Dark"

# Gerenciamento de produtos ----------------------------------------------------------------------

def buscar_produto_por_id(id_produto):
    if not id_produto:
        return {"sucesso": False, "mensagem": "Aguardando ID..."}
    try:
        resultado = buscar(id_produto)
        if resultado:
            return {"sucesso": True, "dados": resultado}
        
        else:
            return {"sucesso": False, "mensagem": "Produto não encontrado no banco."}
        
    except Exception:
        return {"sucesso": False, "mensagem": "Erro ao buscar o ID informado."}

def processar_atualizacao(id_produto, novo_nome, novo_preco, nova_qtd, original):

    if not novo_nome or not novo_preco or not nova_qtd:
        messagebox.showwarning("Campos Vazios", "Todos os campos devem estar preenchidos!")
        return False

    if novo_nome == original["nome"] and novo_preco == original["preco"] and nova_qtd == original["qtd"]:
        
        messagebox.showwarning("Nenhuma Alteração", "Nenhuma mudança foi detectada.")
        return False

    try:
        preco_float = float(novo_preco.replace(",", "."))
        qtd_int = int(nova_qtd)
        
        atualizar(id_produto, novo_nome, preco_float, qtd_int)
        messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
        return {"nome": novo_nome, "preco": f"{preco_float:.2f}", "qtd": str(qtd_int)}
    
    except ValueError:
        messagebox.showerror("Erro de Formato", "Preço ou quantidade inválidos!")
        return False
    
    except Exception as e:
        messagebox.showerror("Erro no Banco", f"Não foi possível salvar:\n{e}")
        return False

def processar_exclusao(id_produto):

    try:
        excluir(id_produto)
        messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
        return True
    
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível excluir o produto:\n{e}")
        return False

def obter_dados_grafico():

    dados = listar()
    categorias = [prod[1] for prod in dados]
    valores = [prod[3] for prod in dados]
    return categorias, valores

def obter_lista_produtos(pesquisa=""):

    return listar(pesquisa)
