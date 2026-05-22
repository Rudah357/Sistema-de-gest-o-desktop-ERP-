import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Controller.logica import obter_dados_grafico

def grafico():

    interface_v4 = ctk.CTkToplevel()
    interface_v4.geometry("700x750")
    interface_v4.title("Gráfico do Estoque")

    interface_v4.focus()
    interface_v4.grab_set()

    frame_menu_principal = ctk.CTkFrame(interface_v4, fg_color="#DD1974", bg_color="#DD1974", height=80)
    frame_menu_principal.pack(side="top", fill="x")

    label_menu_principal = ctk.CTkLabel(frame_menu_principal, text="Gráfico do Estoque", font=("Segoe UI", 28), text_color="white")
    label_menu_principal.pack(pady=25, padx=10)

    borda_frame = ctk.CTkFrame(interface_v4, fg_color="#C91A6B", bg_color="#C91A6B", height=20)
    borda_frame.pack(side="top", fill="x")

    categorias, valores = obter_dados_grafico()

    if not valores:
        lbl_aviso = ctk.CTkLabel(interface_v4, text="Nenhum produto cadastrado para exibir.", font=("Arial", 14))
        lbl_aviso.pack(pady=50)
        return

    cor_fundo = "white" if ctk.get_appearance_mode() == "Light" else "#111111"
    cor_texto = "black" if ctk.get_appearance_mode() == "Light" else "white"

    figura, ax = plt.subplots(figsize=(6, 5), dpi=100, facecolor=cor_fundo)
    ax.set_facecolor(cor_fundo)

    cores_fatias = ["#DD1974", "#FF52A3", "#A3004C", "#FF85C2", "#700032", "#FFB8DC"]

    wedges, texts, autotexts = ax.pie(
        valores, labels=categorias, autopct="%1.1f%%", startangle=90,      
        colors=cores_fatias[:len(categorias)], textprops={'fontsize': 10, 'color': cor_texto}
    )
    
    for autotext in autotexts:
        autotext.set_color(cor_texto)

    ax.set_title("Proporção de Produtos em Estoque", fontsize=14, pad=20, color=cor_texto)
    plt.tight_layout()

    canvas = FigureCanvasTkAgg(figura, interface_v4)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=30, fill="both", expand=True)