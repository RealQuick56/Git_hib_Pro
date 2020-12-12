import sys
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QCoreApplication, QSize, QFileInfo
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import csv


count_of_ans = 0


class Widget_Info(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 400)
        self.setWindowTitle('Информация о вводе данных')
        self.label = QLabel('Привет, земляне', self)
        self.label.setGeometry(QRect(10, 10, 390, 390))
        self.label.wordWrap()


class Start(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 110)
        self.setWindowTitle('Количество ответов')

        self.label = QLabel(self)
        self.label.setGeometry(QRect(20, 20, 150, 25))
        self.label.setText('Количество вопросов:')

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(QRect(190, 20, 100, 25))

        self.btn = QPushButton(self)
        self.btn.setGeometry(QRect(160, 80, 65, 25))
        self.btn.setText('Создать')

        self.btn_exit = QPushButton(self)
        self.btn_exit.setGeometry(QRect(230, 80, 65, 25))
        self.btn_exit.setText('Выйти')

        self.btn_info = QPushButton('Инфо', self)
        self.btn_info.setGeometry(QRect(90, 80, 65, 25))

        self.btn_exit.clicked.connect(self.exit)
        self.btn.clicked.connect(self.create_lines)
        self.btn_info.clicked.connect(self.info)

    def exit(self):
        self.close()

    def create_lines(self):
        count_of_ans = self.lineEdit.text()
        self.main = MainWindow(count_of_ans)
        self.main.show()
        self.close()

    def info(self):
        self.widget_info = Widget_Info()
        self.widget_info.show()


class End(QWidget):
    def __init__(self, ending):
        super().__init__()
        self.ending = ending
        self.resize(400, 400)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(10, 10, 380, 380)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['Ф.И.О', 'Правильность в %'])
        self.tableWidget.setRowCount(len(self.ending))
        for i in range(len(self.ending)):
            surname, proc = self.ending[i].split(',')
            self.tableWidget.setItem(i, 0, QTableWidgetItem(surname))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(f'{proc}%'))


class MainWindow(QMainWindow):
    def __init__(self, count_of_ans):
        super().__init__()
        self.resize(800, 600)
        self.count_of_ans = int(count_of_ans)
        self.right_answers = []
        self.count_of_classmates = []
        self.surnames_and_marks = []
        if self.count_of_ans < 14:
            count_of_ques = 1
            for i in range(1, self.count_of_ans + 1):
                line = QLineEdit(self)
                line.setGeometry(QRect(40, 20 * i * 2, 150, 20))
                line.setObjectName(f'lineEdit{i}')
                label = QLabel(self)
                label.setGeometry(QRect(6, 20 * i * 2, 30, 20))
                label.setText(f'№{count_of_ques}')
                count_of_ques += 1
        elif self.count_of_ans >= 14 and self.count_of_ans <= 28:
            if self.count_of_ans % 2 == 0:
                count_of_ques = 1                            # Здесь создаются строки для ввода ответов (четные)
                for i in range(1, self.count_of_ans // 2 + 1):         #Только два ряда
                    for j in range(1, 3):
                        if j == 1:
                            line = QLineEdit(self)
                            line.setGeometry(QRect(40 * j, 20 * i * 2, 150, 20))
                            line.setObjectName(f'lineEdit{i}{j}')
                            label = QLabel(self)
                            label.setGeometry(QRect(3 * j * 2, 20 * i * 2, 30, 20))
                            label.setText(f'№{count_of_ques}')
                            count_of_ques += 1
                        else:
                            line = QLineEdit(self)
                            line.setGeometry(QRect(40 * j * 3, 20 * i * 2, 150, 20))
                            line.setObjectName(f'lineEdit{i}{j}')
                            label = QLabel(self)
                            label.setGeometry(QRect(3 * j * 34, 20 * i * 2, 30, 20))
                            label.setText(f'№{count_of_ques}')
                            count_of_ques += 1

            elif self.count_of_ans % 2 != 0:                        #Здесь создаются строки для ввода (нечетные)
                x_coord = 0
                count_of_ques = 1
                for i in range(1, self.count_of_ans // 2 + 1):
                    for j in range(1, 3):
                        if j == 1:
                            line = QLineEdit(self)
                            line.setGeometry(QRect(40 * j, 20 * i * 2, 150, 20))
                            line.setObjectName(f'lineEdit{i}{j}')
                            label = QLabel(self)
                            label.setGeometry(QRect(3 * j * 2, 20 * i * 2, 30, 20))
                            label.setText(f'№{count_of_ques}')
                            count_of_ques += 1
                        else:
                            line = QLineEdit(self)
                            line.setGeometry(QRect(40 * j * 3, 20 * i * 2, 150, 20))
                            line.setObjectName(f'lineEdit{i}{j}')
                            label = QLabel(self)
                            label.setGeometry(QRect(3 * j * 34, 20 * i * 2, 30, 20))
                            label.setText(f'№{count_of_ques}')
                            count_of_ques += 1
                    x_coord = i

                line = QLineEdit(self)
                line.setGeometry(QRect(40, 20 * (int(x_coord) + 1) * 2, 150, 20))
                line.setObjectName(f'lineEdit{x_coord + 1}{1}')
                label = QLabel(self)
                label.setGeometry(QRect(6, 20 * (int(x_coord) + 1) * 2, 30, 20))
                label.setText(f'№{count_of_ques}')

        self.btn = QPushButton('Проверка', self)
        self.btn.setGeometry(QRect(700, 20, 90, 30))
        self.btn.clicked.connect(self.checkout)

        self.btn_2 = QPushButton('Итог', self)
        self.btn_2.setGeometry(QRect(700, 60, 90, 30))
        self.btn_2.clicked.connect(self.ending)

        self.btn_restart = QPushButton('Рестарт', self)
        self.btn_restart.setGeometry(QRect(700, 100, 90, 30))
        self.btn_restart.clicked.connect(self.restart)

        self.btn_exit = QPushButton('Выход', self)
        self.btn_exit.setGeometry(QRect(700, 140, 90, 30))
        self.btn_exit.clicked.connect(self.exit_app)


    def checkout(self):
        for i in range(1, self.count_of_ans + 1):
            child = self.findChild(QLineEdit, f'lineEdit{i}')
            self.right_answers.append(child.text())
        valid = QMessageBox.question(self, 'Проверка', 'Вы уверены, что все ответы введены?',
                                     QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            fname = QFileDialog.getOpenFileName(self, 'Выбрать файл', '')[0]
            with open(fname, encoding='utf8') as filecsv:
                reader = csv.reader(filecsv, delimiter=';', quotechar='"')
                for words in reader:
                    self.count_of_classmates.append(words)

            for pupil in self.count_of_classmates:
                for j in range(1, len(pupil) - 1):
                    if int(pupil[j]) == int(self.right_answers[j - 1]):
                        pupil[j] = 1
                    else:
                        pupil[j] = 0

            for i in self.count_of_classmates:
                mark = (i.count(1) * 100) / self.count_of_ans
                self.surnames_and_marks.append(f'{i[0]}, {round(mark)}')

            print(self.surnames_and_marks)
        else:
            self.close()

    def ending(self):
        if len(self.surnames_and_marks) == 0:
            QMessageBox.warning(self, 'Ошибка', 'Вы не проверели ответы', QMessageBox.Ok)
        else:
            self.widget_of_end = End(self.surnames_and_marks)
            self.widget_of_end.show()

    def exit_app(self):
        valid = QMessageBox.question(self, 'Выход', 'Вы точно хотите выйти?', QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            self.close()
        else:
            pass

    def restart(self):
        pass
                                                          # Нужно сделать: Проверку, если какие - то ответы отсутсвуют
                                                        # А также доделать функцию рестарт
if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Start()
    gui.show()
    sys.exit(app.exec_())