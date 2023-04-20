import sys
from PySide6.QtWidgets import QApplication, QWidget, \
QGridLayout, QLabel, QPushButton, QLineEdit, QCheckBox
from PySide6.QtGui import QPixmap

app = QApplication(sys.argv)
janela = QWidget()
layout = QGridLayout()

# Funções!
def muda_texto():
    texto.setText(caixa_texto.text())
    caixa_texto.setText('')

def muda_titulo():
    janela.setWindowTitle(caixa_texto.text())
    caixa_texto.setText('')

def esconder(janela):
    if check.isChecked():
        imagem.setVisible(False)
        check.setText('Mostrar imagem')
    else:
        imagem.setVisible(True)
        check.setText('Esconder imagem')

# Caixa de texto
caixa_texto = QLineEdit()
layout.addWidget(caixa_texto)
caixa_texto.setObjectName('caixa_texto')
caixa_texto.setPlaceholderText('Digite aqui!')


# Botão que muda o titulo!
botao2 = QPushButton('Muda titulo!')
layout.addWidget(botao2)
botao2.setObjectName('botao_laranja')
botao2.clicked.connect(muda_titulo)


# Botão que muda o texto!
botao = QPushButton('Mudar texto!')
layout.addWidget(botao)
botao.setObjectName('botao_azul')
botao.clicked.connect(muda_texto)


# Texto
texto = QLabel('Texto de exemplo')
layout.addWidget(texto)
texto.setObjectName('texto')


# Imagem
imagem = QLabel()
pixmap = QPixmap('Logo.png')
imagem.setScaledContents(True)
imagem.setPixmap(pixmap)
layout.addWidget(imagem)

janela.setWindowIcon(pixmap)

# Checkbox para esconder imagem
check = QCheckBox('Esconder Imagem')
check.clicked.connect(esconder)
layout.addWidget(check)
check.setObjectName('check')


layout.setRowMinimumHeight(4,400)

# Importa o aquivo de estilos!
with open("Exemplos/QSS/arquivo.qss", "r") as arquivo:
    qss = arquivo.read()

janela.setStyleSheet(qss)
janela.setWindowTitle('Exemplo de Janela')
janela.setFixedSize(350,650)
janela.setLayout(layout)
janela.show()
app.exec()