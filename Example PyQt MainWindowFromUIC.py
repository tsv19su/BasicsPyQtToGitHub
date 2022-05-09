#  InterPreter 3.7
#  UTF8

# Загружаем ресурсный файл из Qt Designer через парсинг XML на выполнение
# ссылка на статью
# https://python-scripts.com/pyqt5#load-ui-pyqt5-designer

from PyQt5 import QtWidgets, uic
import sys

myAppliction = QtWidgets.QApplication([])
# Просто показываем ресурсные файлы
myWindow_001 = uic.loadUi("Example_QtDesigner_001.ui")
myWindow_002 = uic.loadUi("Example_QtDesigner_002.ui")

# Отрисовка окон
myWindow_001.show()
myWindow_002.show()

sys.exit(myAppliction.exec_())  # правильно выдаем код статуса

