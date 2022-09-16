import requests
from tkinter import *


def get_cotacoes():
    cotacoes = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotacoes_dict = cotacoes.json()
    cotacoes_dolar = cotacoes_dict['USDBRL']['bid']
    cotacoes_euro = cotacoes_dict['EURBRL']['bid']
    cotacoes_btc = cotacoes_dict['BTCBRL']['bid']
    texto_quotations['text'] = f"""
    Dólar: R$ {cotacoes_dolar}
    Euro:  R$ {cotacoes_euro}
    BitCoin: R$ {cotacoes_btc}
    """


janela = Tk()

janela.title("Cotações de Moedas")
janela.geometry("300x200")
texto = Label(janela, text="Clique para exibir as cotações das moedas.")
texto.grid(column=0, row=0, padx=40, pady=10)

botao = Button(janela, text="Buscar cotações", command=get_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_quotations = Label(janela, text="")
texto_quotations.grid(column=0, row=2, padx=0, pady=5)

janela.mainloop()
