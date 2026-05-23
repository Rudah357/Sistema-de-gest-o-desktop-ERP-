import customtkinter as ctk
from tkinter import messagebox
from Controller.logica import buscar_produto_por_id, processar_exclusao

def deletar_produto():

    interface_v5 = ctk.CTkToplevel()
    interface_v5.geometry("700x750")
    interface_v5.title("Deletar Produto")

    interface_v5.focus()
    interface_v5.grab_set()

    produto_para_deletar = {"id": None}

    frame_menu_principal = ctk.CTkFrame(interface_v5, fg_color="#DA3838", bg_color="#DA3838", height=80)
    frame_menu_principal.pack(side="top", fill="x")

    label_menu_principal = ctk.CTkLabel(frame_menu_principal, text="Deletar Produto", font=("Segoe UI", 28), text_color="white")
    label_menu_principal.pack(pady=25, padx=10)

    borda_frame = ctk.CTkFrame(interface_v5, fg_color="#CA2E2E", bg_color="#CA2E2E", height=20)
    borda_frame.pack(side="top", fill="x")

    entry_id_deletar = ctk.CTkEntry(interface_v5, placeholder_text="Insira o ID do produto para exclusão", width=350)
    entry_id_deletar.pack(pady=30)

    lbl_produto_encontrado = ctk.CTkLabel(interface_v5, text="Aguardando ID...", font=("Arial", 14, "italic"), text_color="#777777")
    lbl_produto_encontrado.pack(pady=10)

    def buscar_deletar():

        id_digitado = entry_id_deletar.get().strip()
        resposta = buscar_produto_por_id(id_digitado)

        if resposta["sucesso"]:

            res = resposta["dados"]
            produto_para_deletar["id"] = id_digitado
            lbl_produto_encontrado.configure(
                text=f"Produto Encontrado: {res[1]} (R$ {res[2]:.2f} | Qtd: {res[3]})",
                text_color="#DA3838"
            )

        else:
            lbl_produto_encontrado.configure(text=resposta.get("mensagem", "Erro"), text_color="#777777")
            produto_para_deletar["id"] = None

    btn_buscar = ctk.CTkButton(interface_v5, text="Buscar Produto", fg_color="#414141", command=buscar_deletar)
    btn_buscar.pack(pady=10)

    def confirmar_exclusao():
        if produto_para_deletar["id"] is None or entry_id_deletar.get().strip() != produto_para_deletar["id"]:
            messagebox.showwarning("Aviso", "Busque e selecione um produto válido antes!")
            return
        
        if messagebox.askyesno("Confirmar", f"Deseja permanentemente excluir o ID {produto_para_deletar['id']}?"):
            if processar_exclusao(produto_para_deletar["id"]):
                entry_id_deletar.delete(0, "end")
                lbl_produto_encontrado.configure(text="Aguardando ID...", text_color="#777777")
                produto_para_deletar["id"] = None

    btn_deletar = ctk.CTkButton(interface_v5, text="Excluir Produto", fg_color="#DA3838", font=("Arial", 14, "bold"), command=confirmar_exclusao)
    btn_deletar.pack(pady=40)
    