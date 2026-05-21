from Controller.logica import verif_cadastro
import customtkinter as ctk

def app():

    def button_cadastrar_produto():
        produto_dg = cx_produto.get()
        preco_dg = cx_preco.get()
        quantidade_dg = cx_quantidade.get()
        
        if verif_cadastro(produto_dg, preco_dg, quantidade_dg):
            cx_produto.delete(0, 'end')
            cx_preco.delete(0, 'end')
            cx_quantidade.delete(0, 'end')

    interface = ctk.CTk()
    interface.geometry("600x600")
    interface.title("Sistema de gestão")

    painel_lateral = ctk.CTkFrame(interface, width=80)
    painel_lateral.pack_propagate(False)
    painel_lateral.pack(side="left", fill="y")

    button_listar_produtos = ctk.CTkButton(
         painel_lateral, 
         text="", 
         width=40, 
         height=40,
         corner_radius=12, 
         fg_color="#DD8E19", 
         hover_color="#C9831A"
         )
    button_listar_produtos.pack(pady=70)



    frame_menu_principal = ctk.CTkFrame(interface, fg_color="#3083F0", bg_color="#3083F0", width=250, height=80)
    frame_menu_principal.pack_propagate(False)
    frame_menu_principal.pack(side="top", fill="x")

    label_menu_principal = ctk.CTkLabel(frame_menu_principal, text="Sistema de Gestão V-3", font=("Trebuchet MS", 28))
    label_menu_principal.pack(pady=25, padx=10)

    borda_frame = ctk.CTkFrame(interface, fg_color="#2D79DD", bg_color="#3083F0", width=250, height=20)
    borda_frame.pack_propagate(False)
    borda_frame.pack(side="top", fill="x")

    frame_cadastrar_produto = ctk.CTkFrame(interface, corner_radius=20)
    frame_cadastrar_produto.pack(pady=30, padx=20)

    label_cadastrar_produto = ctk.CTkLabel(frame_cadastrar_produto, text="• Cadastrar produto no sistema", font=("Roboto", 18))
    label_cadastrar_produto.pack(pady=15, padx=20)



    cx_produto = ctk.CTkEntry(interface, placeholder_text="Inserir nome do produto", width=200)
    cx_produto.pack(pady=20)

    cx_preco = ctk.CTkEntry(interface, placeholder_text="Inserir preço do produto", width=200)
    cx_preco.pack(pady=20)

    cx_quantidade = ctk.CTkEntry(interface, placeholder_text="Inserir quantidade do produto", width=200)
    cx_quantidade.pack(pady=20)



    button = ctk.CTkButton(interface, text="Cadastrar produto", command=button_cadastrar_produto)
    button.pack(pady=30)

    interface.mainloop()
if __name__ == "__main__":
        app()
