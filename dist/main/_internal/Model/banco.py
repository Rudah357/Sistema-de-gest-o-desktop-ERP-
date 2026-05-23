import sqlite3

def conectar():
    return sqlite3.connect("lista_de_produtos.db")

def tabela():

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                produto TEXT NOT NULL,
                preco REAL NOT NULL,
                quantidade INTEGER NOT NULL
            )
        """)
        conexao.commit()

    except sqlite3.Error as erro:
        print(f"ERRO BANCO DE DADOS: {erro}")

    finally:
        conexao.close()

def salvar(produto, preco, quantidade):

    conexao = conectar()
    cursor = conexao.cursor()

    cmd_sql = "INSERT INTO produtos (produto, preco, quantidade) VALUES (?, ?, ?)"
    cursor.execute(cmd_sql, (produto, preco, quantidade))

    conexao.commit()
    conexao.close()

def listar(pesquisa=""):

    conexao = conectar()
    cursor = conexao.cursor()

    if pesquisa == "":
        cursor.execute("SELECT * FROM produtos")

    else:
        cursor.execute("SELECT * FROM produtos WHERE produto LIKE ?", (f"%{pesquisa}%",))
    lista_produtos = cursor.fetchall()
    conexao.close()
    return lista_produtos

def buscar(id_produto):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id_produto,))
    produto = cursor.fetchone()
    conexao.close()

    return produto

def atualizar(id_produto, produto, preco, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()

    cmd_sql = "UPDATE produtos SET produto = ?, preco = ?, quantidade = ? WHERE id = ?"
    cursor.execute(cmd_sql, (produto, preco, quantidade, id_produto))

    conexao.commit()
    conexao.close()

def excluir(id_produto):
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))

    conexao.commit()
    conexao.close()

def buscar_por_nome(nome_produto):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos WHERE LOWER(produto) = LOWER(?)", (nome_produto,))
    produto = cursor.fetchone()
    
    conexao.close()
    return produto

if __name__ == "__main__":
    tabela()