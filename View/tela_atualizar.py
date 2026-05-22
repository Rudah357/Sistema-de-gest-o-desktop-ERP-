import customtkinter as ctk
from tkinter import messagebox
from Controller.logica import buscar_produto_por_id, processar_atualizacao

def atualizar_produtos():

    interface_v3 = ctk.CTkToplevel()
    interface_v3.geometry("700x750")
    interface_v3.title("Atualizar Produtos")
    
    interface_v3.focus()
    interface_v3.grab_set()

    produto_original = {"id": None, "nome": "", "preco": "", "qtd": ""}

    frame_menu_principal = ctk.CTkFrame(interface_v3, fg_color="#1FDB6D", bg_color="#1FDB6D", height=80)
    frame_menu_principal.pack(side="top", fill="x")

    label_menu_principal = ctk.CTkLabel(frame_menu_principal, text="Atualizar Produtos", font=("Segoe UI", 28), text_color="white")
    label_menu_principal.pack(pady=25, padx=10)

    borda_frame = ctk.CTkFrame(interface_v3, fg_color="#1DBB5F", bg_color="#1DBB5F", height=20)
    borda_frame.pack(side="top", fill="x")

    entry_selecinar_id_produto = ctk.CTkEntry(interface_v3, placeholder_text="Insira o id do produto a ser atualizado", width=350)
    entry_selecinar_id_produto.pack(pady=30)

    def buscar_produto():

        id_digitado = entry_selecinar_id_produto.get().strip()
        resposta = buscar_produto_por_id(id_digitado)

        if resposta["sucesso"]:

            res = resposta["dados"]
            produto_original["id"] = id_digitado
            produto_original["nome"] = str(res[1]).strip()
            produto_original["preco"] = f"{res[2]:.2f}"
            produto_original["qtd"] = str(res[3]).strip()
            
            produto_selecionado.configure(
                text=f"Selecionado: {produto_original['nome']} (R$ {produto_original['preco']} | Qtd: {produto_original['qtd']})",
                text_color="#1DBB5F"
            )
            limpar_campos()
            entry_produto.insert(0, produto_original["nome"])
            entry_preco.insert(0, produto_original["preco"])
            entry_quantidade.insert(0, produto_original["qtd"])

        else:
            produto_selecionado.configure(text=resposta.get("mensagem", "Erro"), text_color="#DA3838")
            limpar_campos()
            produto_original["id"] = None

    def limpar_campos():
        entry_produto.delete(0, "end")
        entry_preco.delete(0, "end")
        entry_quantidade.delete(0, "end")

    button_buscar_produto = ctk.CTkButton(interface_v3, text="Buscar produto", fg_color="#1FDB6D", hover_color="#1DBB5F", command=buscar_produto)
    button_buscar_produto.pack(pady=10)
    
    produto_selecionado = ctk.CTkLabel(interface_v3, text="Aguardando ID...", font=("Arial", 14, "italic"), text_color="#777777")
    produto_selecionado.pack(pady=10)

    entry_produto = ctk.CTkEntry(interface_v3, placeholder_text="Novo nome do produto", width=250)
    entry_produto.pack(pady=15)

    entry_preco = ctk.CTkEntry(interface_v3, placeholder_text="Novo preço", width=250)
    entry_preco.pack(pady=15)

    entry_quantidade = ctk.CTkEntry(interface_v3, placeholder_text="Nova quantidade", width=250)
    entry_quantidade.pack(pady=15)

    def confirmar_alteracao():

        if produto_original["id"] is None:
            messagebox.showwarning("Aviso", "Busque um produto válido primeiro!")
            return

        resultado = processar_atualizacao(
            produto_original["id"], entry_produto.get().strip(),
            entry_preco.get().strip(), entry_quantidade.get().strip(), produto_original
        )

        if resultado:

            produto_selecionado.configure(
                text=f"Atualizado: {resultado['nome']} (R$ {resultado['preco']} | Qtd: {resultado['qtd']})",
                text_color="#1DBB5F"
            )
            
            limpar_campos()
            produto_original["nome"] = resultado["nome"]
            produto_original["preco"] = resultado["preco"]
            produto_original["qtd"] = resultado["qtd"]

    btn_confirmar_atualizacao = ctk.CTkButton(interface_v3, text="Salvar Alterações", fg_color="#1FDB6D", hover_color="#1DBB5F", command=confirmar_alteracao)
    btn_confirmar_atualizacao.pack(pady=25)