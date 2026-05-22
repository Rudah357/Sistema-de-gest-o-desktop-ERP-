from Controller.logica import verif_cadastro
from View.interface_secundarias import listar_produtos, atualizar_produtos, grafico, deletar_produto, config
import customtkinter as ctk
from PIL import Image

def app():

    def button_cadastrar_produto():
        produto_dg = cx_produto.get().strip().capitalize()
        preco_dg = cx_preco.get().strip()
        quantidade_dg = cx_quantidade.get().strip()
        
        if verif_cadastro(produto_dg, preco_dg, quantidade_dg) is True:
            cx_produto.delete(0, 'end')
            cx_preco.delete(0, 'end')
            cx_quantidade.delete(0, 'end')

    interface = ctk.CTk()
    interface.geometry("800x800")
    interface.title("Sistema de gestão")

    painel_lateral = ctk.CTkFrame(interface, width=120)
    painel_lateral.pack_propagate(False)
    painel_lateral.pack(side="left", fill="y")


    img_lista = ctk.CTkImage(
    light_image=Image.open("listinha.png"),
    dark_image=Image.open("listinha.png"),
    size=(35, 35)
    )

    button_listar_produtos = ctk.CTkButton(
         painel_lateral, 
         text="",
         image=img_lista, 
         width=40, 
         height=40,
         corner_radius=12, 
         fg_color="#DD8E19", 
         hover_color="#C9831A",
         command=listar_produtos
         )
    button_listar_produtos.pack(side="top", pady=40)

    img_atualizar = ctk.CTkImage(
    light_image=Image.open("atualizar.png"),
    dark_image=Image.open("atualizar.png"),
    size=(30, 30)
    )

    button_atualizar_produtos = ctk.CTkButton(
         painel_lateral, 
         text="",
         image=img_atualizar, 
         width=45, 
         height=40,
         corner_radius=12, 
         fg_color="#1FDB6D", 
         hover_color="#1DBB5F",
         command=atualizar_produtos
         )
    button_atualizar_produtos.pack(side="top", pady=40)

    img_grafico = ctk.CTkImage(
    light_image=Image.open("grafico.png"),
    dark_image=Image.open("grafico.png"),
    size=(30, 30)
    )

    button_grafico = ctk.CTkButton(
         painel_lateral, 
         text="",
         image=img_grafico, 
         width=40, 
         height=40,
         corner_radius=12, 
         fg_color="#DD1974", 
         hover_color="#C91A6B",
         command=grafico
         )
    button_grafico.pack(side="top", pady=40)

    img_deletar = ctk.CTkImage(
    light_image=Image.open("deletar.png"),
    dark_image=Image.open("deletar.png"),
    size=(30, 30)
    )

    button_deletar_produto = ctk.CTkButton(
         painel_lateral, 
         text="",
         image=img_deletar, 
         width=40, 
         height=40,
         corner_radius=12, 
         fg_color="#DA3838", 
         hover_color="#CA2E2E",
         command=deletar_produto
         )
    button_deletar_produto.pack(side="top", pady=40)

    img_config = ctk.CTkImage(
    light_image=Image.open("config.png"),
    dark_image=Image.open("config.png"),
    size=(30, 30)
    )

    button_config = ctk.CTkButton(
         painel_lateral, 
         text="",
         image=img_config,
         width=40, 
         height=40,
         corner_radius=12, 
         fg_color="#D8D8D8", 
         hover_color="#B4B4B4",
         command=config
         )
    button_config.pack(side="bottom", pady=50)



    frame_menu_principal = ctk.CTkFrame(interface, fg_color="#3083F0", bg_color="#3083F0", width=250, height=80)
    frame_menu_principal.pack_propagate(False)
    frame_menu_principal.pack(side="top", fill="x")

    label_menu_principal = ctk.CTkLabel(frame_menu_principal, text="Sistema de Gestão V-3", font=("Segoe UI", 28))
    label_menu_principal.pack(pady=25, padx=10)

    borda_frame = ctk.CTkFrame(interface, fg_color="#2D79DD", bg_color="#3083F0", width=250, height=20)
    borda_frame.pack_propagate(False)
    borda_frame.pack(side="top", fill="x")

    frame_cadastrar_produto = ctk.CTkFrame(interface, corner_radius=20)
    frame_cadastrar_produto.pack(pady=30, padx=20)

    label_cadastrar_produto = ctk.CTkLabel(frame_cadastrar_produto, text="• Cadastrar produto no sistema", font=("Consolas", 18))
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
