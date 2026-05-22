from Model.banco import listar, buscar
import customtkinter as ctk
from PIL import Image


def listar_produtos():

    interface_v2 = ctk.CTkToplevel()
    interface_v2.geometry("700x750")
    interface_v2.title("Lista de Produtos")

    interface_v2.focus()
    interface_v2.grab_set()

    frame_menu_principal = ctk.CTkFrame(interface_v2, fg_color="#DD8E19", bg_color="#DD8E19", width=250, height=80)
    frame_menu_principal.pack_propagate(False)
    frame_menu_principal.pack(side="top", fill="x")

    label_menu_principal = ctk.CTkLabel(frame_menu_principal, text="Lista de Pordutos", font=("Segoe UI", 28))
    label_menu_principal.pack(pady=25, padx=10)

    borda_frame = ctk.CTkFrame(interface_v2, fg_color="#C9831A", bg_color="#C9831A", width=250, height=20)
    borda_frame.pack_propagate(False)
    borda_frame.pack(side="top", fill="x")

    entry_barra_de_pesquisa = ctk.CTkEntry(interface_v2, placeholder_text="• Procurar produto na lista: ", font=("Roboto", 12), width=400)
    entry_barra_de_pesquisa.pack(pady=40, padx=30)    

    lbl_pesquisa_resultado = ctk.CTkLabel(interface_v2, text="Mostrando todos os produtos", font=("Arial", 13, "italic"), text_color="#777777")
    lbl_pesquisa_resultado.pack(pady=5)

    frame_label_lp = ctk.CTkFrame(interface_v2, corner_radius=20)
    frame_label_lp.pack(pady=20, padx=20)

    label_lista_produtos = ctk.CTkLabel(frame_label_lp, text="• Lista de Produtos:", font=("Consolas", 18))
    label_lista_produtos.pack(pady=15, padx=20)

    frame_produtos = ctk.CTkScrollableFrame(interface_v2, width=500, height=250)
    frame_produtos.pack(pady=25)

    def atualizar_tabela(event=None):

        for widget in frame_produtos.winfo_children():
            widget.destroy()

        termo_pesquisa = entry_barra_de_pesquisa.get()

        if termo_pesquisa:
            lbl_pesquisa_resultado.configure(text=f"Resultados para: '{termo_pesquisa}'")
        else:
            lbl_pesquisa_resultado.configure(text="Mostrando todos os produtos")

        dados_produtos = listar(termo_pesquisa)

        ctk.CTkLabel(frame_produtos, text="ID", font=("Arial", 12, "bold"), width=50, anchor="w").grid(row=0, column=0, padx=10, pady=5)
        ctk.CTkLabel(frame_produtos, text="Produto", font=("Arial", 12, "bold"), width=200, anchor="w").grid(row=0, column=1, padx=10, pady=5)
        ctk.CTkLabel(frame_produtos, text="Preço", font=("Arial", 12, "bold"), width=100, anchor="w").grid(row=0, column=2, padx=10, pady=5)
        ctk.CTkLabel(frame_produtos, text="Qtd.", font=("Arial", 12, "bold"), width=80, anchor="w").grid(row=0, column=3, padx=10, pady=5)

        for index, produto in enumerate(dados_produtos, start=1):
            ctk.CTkLabel(frame_produtos, text=str(produto[0]), width=50, anchor="w").grid(row=index, column=0, padx=10, pady=2)
            ctk.CTkLabel(frame_produtos, text=str(produto[1]), width=200, anchor="w").grid(row=index, column=1, padx=10, pady=2)
            ctk.CTkLabel(frame_produtos, text=f"R$ {produto[2]:.2f}", width=100, anchor="w").grid(row=index, column=2, padx=10, pady=2)
            ctk.CTkLabel(frame_produtos, text=str(produto[3]), width=80, anchor="w").grid(row=index, column=3, padx=10, pady=2)

    entry_barra_de_pesquisa.bind("<KeyRelease>", atualizar_tabela)

    atualizar_tabela()

    dados_produtos = listar()

    lbl_id = ctk.CTkLabel(frame_produtos, text="ID", font=("Arial", 12, "bold"), width=50, anchor="w")
    lbl_id.grid(row=0, column=0, padx=10, pady=5)
    
    lbl_nome = ctk.CTkLabel(frame_produtos, text="Produto", font=("Arial", 12, "bold"), width=200, anchor="w")
    lbl_nome.grid(row=0, column=1, padx=10, pady=5)
    
    lbl_preco = ctk.CTkLabel(frame_produtos, text="Preço", font=("Arial", 12, "bold"), width=100, anchor="w")
    lbl_preco.grid(row=0, column=2, padx=10, pady=5)
    
    lbl_qtd = ctk.CTkLabel(frame_produtos, text="Qtd.", font=("Arial", 12, "bold"), width=80, anchor="w")
    lbl_qtd.grid(row=0, column=3, padx=10, pady=5)

    for index, produto in enumerate(dados_produtos, start=1):

        ctk.CTkLabel(frame_produtos, text=str(produto[0]), width=50, anchor="w").grid(row=index, column=0, padx=10, pady=2)
        ctk.CTkLabel(frame_produtos, text=str(produto[1]), width=200, anchor="w").grid(row=index, column=1, padx=10, pady=2)
        ctk.CTkLabel(frame_produtos, text=f"R$ {produto[2]:.2f}", width=100, anchor="w").grid(row=index, column=2, padx=10, pady=2)
        ctk.CTkLabel(frame_produtos, text=str(produto[3]), width=80, anchor="w").grid(row=index, column=3, padx=10, pady=2)

def atualizar_produtos():

    interface_v3 = ctk.CTkToplevel()
    interface_v3.geometry("700x750")
    interface_v3.title("Atualizar Produtos")

    interface_v3.focus()
    interface_v3.grab_set()

    frame_menu_principal = ctk.CTkFrame(interface_v3, fg_color="#1FDB6D", bg_color="#1FDB6D", width=250, height=80)
    frame_menu_principal.pack_propagate(False)
    frame_menu_principal.pack(side="top", fill="x")

    label_menu_principal = ctk.CTkLabel(frame_menu_principal, text="Atualizar Produtos", font=("Segoe UI", 28))
    label_menu_principal.pack(pady=25, padx=10)

    borda_frame = ctk.CTkFrame(interface_v3, fg_color="#1DBB5F", bg_color="#1DBB5F", width=250, height=20)
    borda_frame.pack_propagate(False)
    borda_frame.pack(side="top", fill="x")

    frame_atualizar_produto = ctk.CTkFrame(interface_v3, corner_radius=20)
    frame_atualizar_produto.pack(pady=30, padx=20)

    label_atualizar_produto = ctk.CTkLabel(frame_atualizar_produto, text="• Atualizar/modificar produto do sistema", font=("Consolas", 18))
    label_atualizar_produto.pack(pady=15, padx=20)

    entry_selecinar_id_produto = ctk.CTkEntry(interface_v3, placeholder_text="Insira o id do produto a ser atualizado", width=350)
    entry_selecinar_id_produto.pack(pady=30)

    def buscar_produto():
        id_digitado = entry_selecinar_id_produto.get().strip()

        if not id_digitado:
            produto_selecionado.configure(text="Aguardando ID...", text_color="#777777")
            return

        try:
            resultado = buscar(id_digitado)

            if resultado:

                nome = resultado[1]
                preco = resultado[2]
                qtd = resultado[3]
                
                produto_selecionado.configure(
                    text=f"Produto Selecionado: {nome} (R$ {preco:.2f} | Qtd: {qtd})",
                    text_color="#1DBB5F"
                )
            else:
                produto_selecionado.configure(
                    text="Produto não encontrado no banco de dados.",
                    text_color="#DA3838"
                )
        except Exception as e:
            produto_selecionado.configure(
                text="Erro ao buscar o ID informado.",
                text_color="#DA3838"
            )

    button_buscar_produto = ctk.CTkButton(
        interface_v3,
        text="Buscar produto",
        fg_color="#1FDB6D", 
        hover_color="#1DBB5F",
        command=buscar_produto
    )
    button_buscar_produto.pack(pady=10)
    
    produto_selecionado = ctk.CTkLabel(interface_v3, text="Aguardando ID...", font=("Arial", 14, "italic"), text_color="#777777")
    produto_selecionado.pack(pady=10)

    entry_produto = ctk.CTkEntry(interface_v3, placeholder_text="Novo nome do produto", width=250)
    entry_produto.pack(pady=20)

    entry_preco = ctk.CTkEntry(interface_v3, placeholder_text="Novo preco do produto", width=250)
    entry_preco.pack(pady=20)

    entry_quantidade = ctk.CTkEntry(interface_v3, placeholder_text="Nova quantidade deste produto", width=250)
    entry_quantidade.pack(pady=20)

    btn_confirmar_atualizacao = ctk.CTkButton(
        interface_v3, 
        text="Salvar Alterações", 
        fg_color="#1FDB6D", 
        hover_color="#1DBB5F"
    )
    btn_confirmar_atualizacao.pack(pady=25)    

def grafico():

    interface_v4 = ctk.CTkToplevel()
    interface_v4.geometry("700x750")
    interface_v4.title("Gráfico do Estoque")

    interface_v4.focus()
    interface_v4.grab_set()

    frame_menu_principal = ctk.CTkFrame(interface_v4, fg_color="#DD1974", bg_color="#DD1974", width=250, height=80)
    frame_menu_principal.pack_propagate(False)
    frame_menu_principal.pack(side="top", fill="x")

    label_menu_principal = ctk.CTkLabel(frame_menu_principal, text="Gráfico do Estoque", font=("Segoe UI", 28))
    label_menu_principal.pack(pady=25, padx=10)

    borda_frame = ctk.CTkFrame(interface_v4, fg_color="#C91A6B", bg_color="#C91A6B", width=250, height=20)
    borda_frame.pack_propagate(False)
    borda_frame.pack(side="top", fill="x")

def deletar_produto():

    interface_v5 = ctk.CTkToplevel()
    interface_v5.geometry("700x750")
    interface_v5.title("Deletar Produto")

    interface_v5.focus()
    interface_v5.grab_set()

    frame_menu_principal = ctk.CTkFrame(interface_v5, fg_color="#DA3838", bg_color="#DA3838", width=250, height=80)
    frame_menu_principal.pack_propagate(False)
    frame_menu_principal.pack(side="top", fill="x")

    label_menu_principal = ctk.CTkLabel(frame_menu_principal, text="Deletar Produto", font=("Segoe UI", 28))
    label_menu_principal.pack(pady=25, padx=10)

    borda_frame = ctk.CTkFrame(interface_v5, fg_color="#CA2E2E", bg_color="#CA2E2E", width=250, height=20)
    borda_frame.pack_propagate(False)
    borda_frame.pack(side="top", fill="x")

def config():

    interface_v5 = ctk.CTkToplevel()
    interface_v5.geometry("700x750")
    interface_v5.title("Configurações")

    interface_v5.focus()
    interface_v5.grab_set()

    frame_menu_principal = ctk.CTkFrame(interface_v5, fg_color="#414141", bg_color="#414141", width=250, height=80)
    frame_menu_principal.pack_propagate(False)
    frame_menu_principal.pack(side="top", fill="x")

    label_menu_principal = ctk.CTkLabel(frame_menu_principal, text="Configurações", font=("Segoe UI", 22))
    label_menu_principal.pack(pady=25, padx=10)

    borda_frame = ctk.CTkFrame(interface_v5, fg_color="#383838", bg_color="#383838", width=250, height=10)
    borda_frame.pack_propagate(False)
    borda_frame.pack(side="top", fill="x")