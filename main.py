import customtkinter as ctk
from Model.banco import tabela
from Controller.logica import carregar_tema_config
from View.interface import app

ctk.set_appearance_mode(carregar_tema_config())

tabela()

if __name__ == "__main__":
    app()