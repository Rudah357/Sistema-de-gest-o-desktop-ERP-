import customtkinter as ctk
from Model.banco import tabela
from Controller.logica import carregar_tema_config
from View.interface import app
import os
import sys

def resolver_caminho(caminho_relativo):

    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, caminho_relativo)
    return os.path.join(os.path.abspath("."), caminho_relativo)

ctk.set_appearance_mode(carregar_tema_config())

tabela()

if __name__ == "__main__":
    app()