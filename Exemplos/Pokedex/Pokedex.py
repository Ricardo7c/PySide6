from PySide6.QtWidgets import QApplication, QGridLayout, QWidget,\
      QLineEdit, QPushButton, QLabel, QGroupBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import requests

app = QApplication()
janela = QWidget()
layout = QGridLayout()
layout2 = QGridLayout()
Grupo = QGroupBox('Habilidades')
Grupo.setLayout(layout2)

def pegar_imagem(nome):
    url_api = f"https://pokeapi.co/api/v2/pokemon/{nome}" 
    #Extrai os dados da API
    dados_api = requests.get(url_api)
    if dados_api.status_code == 200:     
        # Busca a imagem dentro dos dados da api em formato de Json
        url_imagem = dados_api.json()['sprites']['other']['home']['front_default']
        # Faz o download da imagem do Pokémon
        imagem_baixada = requests.get(url_imagem).content
        # Salva a imagem em um arquivo local
        with open("Exemplos/Pokedex/imagem.png", "wb") as file:
            file.write(imagem_baixada)
        # Atualiza a imagem pela imagem baixada!
        pixmap = QPixmap('Exemplos/Pokedex/imagem.png')
        imagem.setPixmap(pixmap)
    else:
        caixa_texto.clear()
        caixa_texto.setPlaceholderText('Não encontrado!')
        pixmap = QPixmap('Exemplos/Pokedex/pokebola.png').scaled(415,450)
        imagem.setPixmap(pixmap)

def textBox():
    if caixa_texto.text() == '':
        caixa_texto.setText('padrão')
    return caixa_texto.text().lower()



# Caixa de texto
caixa_texto = QLineEdit()
layout.addWidget(caixa_texto, 0, 0, 1, 2)
caixa_texto.setPlaceholderText('Qual pokemon?')
caixa_texto.returnPressed.connect(lambda: pegar_imagem(textBox()))


# Botão de busca
botao = QPushButton('Buscar')
layout.addWidget(botao,  0, 2, 1, 1)
botao.setObjectName('botao')
botao.clicked.connect(lambda: pegar_imagem(textBox()))


# Imagem
imagem = QLabel()
pixmap = QPixmap('Exemplos/Pokedex/pokebola.png').scaled(415,450)
imagem.setScaledContents(True)
imagem.setPixmap(pixmap)
layout.addWidget(imagem, 1, 0, 1, 3)
layout.setRowStretch(415,384)



# Folha de estilo
with open("Exemplos/Pokedex/Pokedex.qss", "r") as arquivo:
    qss = arquivo.read()

janela.setStyleSheet(qss)
janela.setWindowTitle('Pokedex')
janela.setWindowIcon(pixmap)
janela.setFixedSize(500,550)
#janela.setFixedWidth(500)
janela.setLayout(layout)
janela.show()
app.exec()

