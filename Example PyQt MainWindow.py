#  InterPreter 3.7.1
#  UTF8

from PyQt5 import QtWidgets  # Убрали с комплектного зеркала, замена неизвестна, можно установить
# скопированный ранее пакет с файлового сервера
# Руководство по установке см. https://packaging.python.org/tutorials/installing-packages/
#from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def PushButton():
    print("Button is pushed")


def application():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()  # пока только одно окно, окон может быть несклько

    window.setWindowTitle("PyQt5 Example")
    window.setGeometry(200, 100, 200, 150)  # отступы: слева, сверху, ширина, высота

    # Внутри окна

    # Надпись
    Main_Label = QtWidgets.QLabel(window)
    Main_Label.setText("Main Label")
    Main_Label.move(50, 20)  # отступы: слева, сверху

    # Кнопка
    Button = QtWidgets.QPushButton(window)
    Button.setText("Push this Button")
    Button.move(50, 50)
    Button.clicked.connect(PushButton)  # Вызов обработчика нажатия кнопки

    window.show()  # отрисовка окна

    sys.exit(app.exec_())  # правильное закрытие окна


# если этот файл не импортированный
if __name__ == "__main__":
    application()

