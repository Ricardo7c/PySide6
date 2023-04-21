with open("Exemplos/Pokedex/Pokedex.qss", "r") as arquivo:
    qss = arquivo.read()

janela.setStyleSheet(qss)