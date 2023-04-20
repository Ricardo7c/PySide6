import sys
from PySide6.QtWidgets import QApplication, QWidget, \
QLabel, QPushButton, QLineEdit, QCheckBox
from PySide6.QtGui import QPixmap

app = QApplication(sys.argv)
janela = QWidget()

# Funções!
def muda_texto():
    texto.setText(caixa_texto.text())

def muda_titulo():
    janela.setWindowTitle(caixa_texto.text())

def esconder(janela):
    if check.isChecked():
        imagem.setVisible(False)
        check.setText('Mostrar imagem')
    else:
        imagem.setVisible(True)
        check.setText('Esconder imagem')

# Caixa de texto
caixa_texto = QLineEdit(janela)
caixa_texto.setObjectName('caixa_texto')
caixa_texto.setPlaceholderText('Digite aqui!')
caixa_texto.move(0,2)
caixa_texto.setFixedSize(350, 60)

# Botão que muda o titulo!
botao2 = QPushButton('Muda titulo!', janela)
botao2.setObjectName('botao')
botao2.clicked.connect(muda_titulo)
botao2.move(0,65)
botao2.setFixedSize(350, 55)

# Botão que muda o texto!
botao = QPushButton('Mudar texto!',janela)
botao.setObjectName('botao')
botao.clicked.connect(muda_texto)
botao.move(0,125)
botao.setFixedSize(350, 55)


# Texto
texto = QLabel('Texto de exemplo',janela)
texto.setObjectName('texto')
texto.move(55, 180)


# Imagem
imagem = QLabel(janela)
pixmap = QPixmap('pikachu.png')
imagem.setPixmap(pixmap)
imagem.move(0,230)

# Checkbox para esconder imagem
check = QCheckBox('Esconder Imagem',janela)
check.clicked.connect(esconder)
check.setObjectName('check')
check.move(10, 615)


# Importa o aquivo de estilos!
with open("Exemplos/SemGridLayout/arquivo.qss", "r") as arquivo:
    qss = arquivo.read()

janela.setStyleSheet(qss)
janela.setWindowTitle('Exemplo de Janela')
janela.setFixedSize(350,650)
janela.show()
app.exec()