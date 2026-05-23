import customtkinter as ctk
from Controller.logica import obter_lista_produtos

def listar_produtos():

    interface_v2 = ctk.CTkToplevel()
    interface_v2.geometry("700x750")
    interface_v2.title("Lista de Produtos")

    interface_v2.focus()
    interface_v2.grab_set()

    frame_menu_principal = ctk.CTkFrame(interface_v2, fg_color="#DD8E19", bg_color="#DD8E19", height=80)
    frame_menu_principal.pack(side="top", fill="x")

    label_menu_principal = ctk.CTkLabel(frame_menu_principal, text="Lista de Produtos", font=("Segoe UI", 28), text_color="white")
    label_menu_principal.pack(pady=25, padx=10)

    borda_frame = ctk.CTkFrame(interface_v2, fg_color="#C9831A", bg_color="#C9831A", height=20)
    borda_frame.pack(side="top", fill="x")

    entry_barra_de_pesquisa = ctk.CTkEntry(interface_v2, placeholder_text="• Procurar produto na lista: ", font=("Roboto", 12), width=400)
    entry_barra_de_pesquisa.pack(pady=40, padx=30)    

    lbl_pesquisa_resultado = ctk.CTkLabel(interface_v2, text="Mostrando todos os produtos", font=("Arial", 13, "italic"), text_color="#777777")
    lbl_pesquisa_resultado.pack(pady=5)

    frame_produtos = ctk.CTkScrollableFrame(interface_v2, width=540, height=350)
    frame_produtos.pack(pady=25)

    def atualizar_tabela(event=None):
        
        for widget in frame_produtos.winfo_children():
            widget.destroy()

        termo_pesquisa = entry_barra_de_pesquisa.get().strip()
        lbl_pesquisa_resultado.configure(text=f"Resultados para: '{termo_pesquisa}'" if termo_pesquisa else "Mostrando todos os produtos")

        dados_produtos = obter_lista_produtos(termo_pesquisa)

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