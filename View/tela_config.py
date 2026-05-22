import customtkinter as ctk
from Controller.logica import salvar_tema_config

def config():
    
    interface_v5 = ctk.CTkToplevel()
    interface_v5.geometry("700x750")
    interface_v5.title("Configurações")

    interface_v5.focus()
    interface_v5.grab_set()

    frame_menu_principal = ctk.CTkFrame(interface_v5, fg_color="#414141", bg_color="#414141", height=80)
    frame_menu_principal.pack(side="top", fill="x")

    label_menu_principal = ctk.CTkLabel(frame_menu_principal, text="Configurações", font=("Segoe UI", 22), text_color="white")
    label_menu_principal.pack(pady=25, padx=10)

    borda_frame = ctk.CTkFrame(interface_v5, fg_color="#383838", bg_color="#383838", height=10)
    borda_frame.pack(side="top", fill="x")

    def alternar_tema():

        novo_tema = "Light" if ctk.get_appearance_mode() == "Dark" else "Dark"
        btn_tema.configure(text="Ativar Modo Escuro" if novo_tema == "Light" else "Ativar Modo Claro")

        ctk.set_appearance_mode(novo_tema)
        salvar_tema_config(novo_tema)

    frame_opcoes = ctk.CTkFrame(interface_v5, corner_radius=15)
    frame_opcoes.pack(pady=50, padx=30, fill="x")

    texto_inicial = "Ativar Modo Claro" if ctk.get_appearance_mode() == "Dark" else "Ativar Modo Escuro"

    btn_tema = ctk.CTkButton(frame_opcoes, text=texto_inicial, font=("Arial", 14, "bold"), fg_color="#414141", command=alternar_tema)
    btn_tema.pack(pady=(20, 5), padx=20)

    lbl_descricao = ctk.CTkLabel(frame_opcoes, text="Altera a aparência visual do aplicativo e salva suas preferências.", font=("Arial", 12, "italic"), text_color="#777777", wraplength=400)
    lbl_descricao.pack(pady=(0, 20), padx=20)