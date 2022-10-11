# This Python file uses the following encoding: utf-8

# -------------------- #
#    Documentation     #
# -------------------- #

"""
NOME:
    quotations.py

DESCRIÇÃO:
    Programa que irá obter os valores das cotações do dólar, do euro e do bitcoin e irá imprimir em uma janela.

AUTOR:
    R. K. O. Silva, <rodolpho_kades@hotmail.com>
"""


import requests
from datetime import datetime
from tkinter import *


def get_cotacoes():
    """
    def get_cotacoes():
    Esta função é responsável por utilizar a biblioteca requests, obter as cotações pela API e retornar uma string com
    os valores das cotações.
    :return: str
    """
    cotacoes = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotacoes_dict = cotacoes.json()                  # Dicionário (json) de informações obtidas
    cotacoes_dolar = cotacoes_dict['USDBRL']['bid']  # Cotação dólar
    cotacoes_euro = cotacoes_dict['EURBRL']['bid']   # Cotação euro
    cotacoes_btc = cotacoes_dict['BTCBRL']['bid']    # Cotação bitcoin

    texto_quotations = f"""
    Dólar: R$ {cotacoes_dolar}
    Euro:  R$ {cotacoes_euro}
    BitCoin: R$ {cotacoes_btc}
    """
    return texto_quotations


#  Configurações da janela do Tkinter:
background = "#e99142"  # Cor de fundo da janela
font_color = "#7c1c14"  # Cor da fonte do texto escrito na janela

janela = Tk()
janela.title("Cotações de Moedas")      # Título da janela
janela.geometry("300x190+1150+80")      # Tamanho e posição da janela
janela.wm_attributes("-topmost", True)  # Mantem esta janela acima de todas as outras. False para desligar essa opção.
janela.config(bg=background)            # Define a cor de fundo
texto = Label(janela, text="As cotações das moedas Dólar, Euro e BitCoin:", fg="black", bg=background)
texto.grid(column=0, row=0, padx=20, pady=5)


def main():
    # Exibindo as cotações:
    texto_quotations = Label(janela, text=get_cotacoes(), fg=font_color, bg=background)
    texto_quotations.grid(column=0, row=1, padx=0, pady=1)

    texto2 = Label(janela, text="Última atualização: ", fg="black", bg=background)
    texto2.grid(column=0, row=2, padx=0, pady=1)

    # Data da última atualização dia-mês-ano
    data = datetime.now().strftime("%d-%m-%Y")
    data_label = Label(janela, text=f"Data: {data}", fg=font_color, bg=background)
    data_label.grid(column=0, row=3, padx=0, pady=1)

    # Horário da última atualização hora:minuto:segundo
    hora = datetime.now().strftime("%H:%M:%S")
    hora_label = Label(janela, text=f"Hora: {hora}", fg=font_color, bg=background)
    hora_label.grid(column=0, row=4, padx=0, pady=1)

    janela.after(30000, lambda: main())
    janela.mainloop()


if __name__ == "__main__":
    main()
