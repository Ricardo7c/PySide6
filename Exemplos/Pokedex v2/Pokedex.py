from PySide6.QtWidgets import QApplication, QWidget,\
QFrame, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit,\
QGridLayout, QGroupBox
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt
import requests
import os

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
        with open("Exemplos/Pokedex v2/imagem.png", "wb") as file:
            file.write(imagem_baixada)
        # Atualiza a imagem pela imagem baixada!
        pixmap = QPixmap('Exemplos/Pokedex v2/imagem.png')
        imagem.setPixmap(pixmap)
        pegar_info(dados_api)
    else:
        caixa_texto.clear()
        caixa_texto.setPlaceholderText('Não encontrado!')
        pixmap = QPixmap('Exemplos/Pokedex v2/pokebola.png')
        imagem.setPixmap(pixmap)
        info.setText('')

def pegar_info(dados):
    habilidades = []
    for cada in dados.json()['abilities']:
        hab = {}
        hab['nome'] = (cada['ability']['name']).capitalize()
        dados_api = requests.get(cada['ability']['url'])
        hab['descrição'] = dados_api.json()['effect_entries'][1]['short_effect']
        habilidades.append(hab)
    mostrar_info(habilidades)

def mostrar_info(dict):
    lista = []
    for cada in dict:
        lista.append(f"{cada['nome']}: {cada['descrição']}")
    info.setText('\n \n'.join(lista))

def tratar_texto(texto):
    if texto.text() == '':
        texto.setText('padrão')
    return texto.text().lower().strip()

app = QApplication()
janela = QWidget()
layout = QHBoxLayout(spacing=0)
left_Frame = QFrame(objectName='left')
right_Frame = QFrame(objectName='right')
left = QGridLayout(left_Frame)
right = QVBoxLayout(right_Frame)
grupo = QGroupBox('Informações', objectName='grupo')
info_Layout = QVBoxLayout()

# Layout principal
layout.addWidget(left_Frame)
layout.addWidget(right_Frame)
layout.setContentsMargins(0, 0, 0, 0)
left.setContentsMargins(10,5,10,10)
right.setContentsMargins(10, 10, 10, 10)

# Frames
left_Frame.setMaximumWidth(320)
right_Frame.setMaximumWidth(320)

# Elementos da esquerda ######################################################
caixa_texto = QLineEdit(objectName='caixa_texto')
left.addWidget(caixa_texto, 0, 0)
caixa_texto.setPlaceholderText('Qual pokemon?')
caixa_texto.returnPressed.connect(lambda: pegar_imagem(tratar_texto(caixa_texto)))

# Botão de busca
botao = QPushButton('Buscar', objectName='botao')
botao.clicked.connect(lambda: pegar_imagem(tratar_texto(caixa_texto)))
left.addWidget(botao, 0,1)
botao.setMinimumWidth(90)

# Imagem
imagem = QLabel()
pixmap = QPixmap('Exemplos/Pokedex v2/pokebola.png')
imagem.setPixmap(pixmap)
imagem.setScaledContents(True)
imagem.setMaximumHeight(280)
imagem.setAlignment(Qt.AlignTop)
left.addWidget(imagem, 1, 0, 2, 2)
left.setRowStretch(1, 330)

# Elementos da direita ########################################################
right.addWidget(grupo)
grupo.setLayout(info_Layout)

info = QLabel('', objectName='info')
info_Layout.addWidget(info)
info.setWordWrap(True)
info.setAlignment(Qt.AlignTop)

with open("Exemplos/Pokedex v2/Pokedex.qss", "r") as arquivo:
    qss = arquivo.read()

janela.setStyleSheet(qss)
janela.setLayout(layout)
janela.setWindowTitle('Pokedex 2.0')
icon = QIcon('Exemplos/Pokedex v2/pokebola.ico')
janela.setWindowIcon(icon)
janela.setFixedSize(640,450)
janela.show()
print(os.getcwd())
app.exec()