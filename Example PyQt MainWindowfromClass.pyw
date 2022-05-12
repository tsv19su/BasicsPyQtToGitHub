#  Interpreter 3.7

# Изучение Qt (GPL и коммерческий)
# https://itproger.com/course/python-pyqt5/2
# Qt/QML в целом лучше, чем GTK2+, GTK3+ (еще не полностью портированы в Windows)

from PyQt5.QtWidgets import QApplication
import sys

# Импорт пользовательской библиотеки (файла *.py в этой же папке)
import Classes


def myApplication():
    # Одно прикладное приложение
    app = QApplication(sys.argv)
    # Делаем экземпляры
    myWindow = Classes.Window_000()  # первое окно (окон может быть несклько)
    myWindowPasted_001 = Classes.Ui_MainWindow_001()  # второе окно
    myWindowPasted_001.setupUi(MainWindow_000=myWindowPasted_001)
    myWindowPasted_002 = Classes.Ui_MainWindow_002()  # третье окно
    myWindowPasted_002.setupUi(MainWindow_000=myWindowPasted_002)
    myWindow.setWindowTitle("PyQt5 Example (Part 1)")
    myWindow.PushButtonString = "PyQt5 Example (Part 1) Button is pushed"
    myWindowPasted_001.setWindowTitle("PyQt Example (Part 2)")
    myWindowPasted_001.comboBox.addItem("First Item")
    myWindowPasted_001.comboBox.addItem("Second Item")
    myWindowPasted_001.lineEdit.setText("DSN")
    myWindowPasted_001.textEdit.setText("String 001")
    myWindowPasted_001.plainTextEdit.appendPlainText("Plain Text")
    myWindowPasted_002.setWindowTitle("PyQt Example (Part 3)")
    # Отрисовка окон
    myWindow.show()
    myWindowPasted_001.show()
    myWindowPasted_002.show()
    # if myWindowPasted_001.onTheRun:
    #     myWindowPasted_001.pushButton.setEnabled(False)
    #     myWindowPasted_001.pushButton_2.setEnabled(True)
    #     myWindowPasted_001.pushButton_3.setEnabled(True)
    # else:
    #     myWindowPasted_001.pushButton.setEnabled(True)
    #     myWindowPasted_001.pushButton_2.setEnabled(False)
    #     myWindowPasted_001.pushButton_3.setEnabled(False)
    # Правильное закрытие окна
    sys.exit(app.exec_())


# если этот файл не импортированный
if __name__ == "__main__":
    myApplication()
