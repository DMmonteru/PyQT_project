import sys
import pymorphy2
import sqlite3
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


# UI:

class UIwindow0(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(242, 136)
        MainWindow.setStyleSheet("QPushButton:hover {\n"
                                 "    background-color: white\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 221, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 242, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Морфолог"))
        self.pushButton.setText(_translate("MainWindow", "Переводчик"))


class UIwindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 154)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QPushButton:hover {\n""    "
                                 "background-color: silver;\n"
                                 "}\n" "r")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 403, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" "
                                                      "font-size:10pt;\">Введите слово:</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Выполнить"))
        self.label.setText(_translate("MainWindow",
                                      "ИЛИ------------------------------------------------------"
                                      "-----------------------------------------"))
        self.label_3.setText(_translate("MainWindow", "Введите название файла:"))
        self.pushButton_2.setText(_translate("MainWindow", "Выполнить"))
        self.label_4.setText(_translate("MainWindow",
                                        "   !(слова должны быть записаны в .txt файл в столбик и без разделителей)"))


class UIwindow2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(323, 240)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 301, 181))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))


class UIwindow3(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(303, 240)
        Form.setStyleSheet("QPushButton:hover {\n"
                           "background-color: green;\n"
                           "}")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(220, 10, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 10, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.listWidget_2 = QtWidgets.QListWidget(Form)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 40, 281, 181))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setObjectName("listWidget_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Выберите номер слова(не более):"))
        self.pushButton.setText(_translate("Form", "✔"))


class UIwindow1_1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(321, 312)
        Form.setStyleSheet("QPushButton:hover {\n"
                           "    background-color: silver;\n"
                           "}\n"
                           "")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 60, 101, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 90, 301, 181))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 280, 82, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(110, 10, 101, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 268, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_en = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_en.setObjectName("checkBox_en")
        self.horizontalLayout.addWidget(self.checkBox_en)
        self.checkBox_fr = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_fr.setObjectName("checkBox_fr")
        self.horizontalLayout.addWidget(self.checkBox_fr)
        self.checkBox_uk = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_uk.setObjectName("checkBox_uk")
        self.horizontalLayout.addWidget(self.checkBox_uk)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Вставьте текст:"))
        self.pushButton.setText(_translate("Form", "Перевести"))
        self.label_4.setText(_translate("Form", "Выберите языки:"))
        self.checkBox_en.setText(_translate("Form", "Английский"))
        self.checkBox_fr.setText(_translate("Form", "Французский"))
        self.checkBox_uk.setText(_translate("Form", "Украинский"))


class UIwindow2_1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(320, 240)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 10, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 41, 301, 181))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Перевод:"))


# code:

def translate(mytext, lang):
    api_key = "trnsl.1.1.20191105T215741Z.86a8003ac493a4f9.1fd1313103133be1535bbbd0a486b6210a0b33ef"
    params = {"key": api_key, "text": mytext, "lang": f'ru-{lang}'}
    response = requests.get(url="https://translate.yandex.net/api/v1.5/tr.json/translate",
                            params=params)
    return response.json()
# Переведено сервисом «Яндекс.Переводчик»


def get_morph_inf(obj):
    arr = []
    morph = pymorphy2.MorphAnalyzer()
    inf = morph.parse(obj)[0]

    con = sqlite3.connect('morph.sqlite3')
    cur = con.cursor()
    result = cur.execute(f"SELECT name FROM pos WHERE id = '{inf.tag.POS}'").fetchone()
    pos = result[0]
    arr.append(pos)
    
    if 'anim' in inf.tag:
        arr.append('одушевлённое')
    elif 'inan' in inf.tag:
        arr.append('не одушевлённое')

    if 'perf' in inf.tag:
        arr.append('совершенный вид')
    elif 'impf' in inf.tag:
        arr.append('несовершенный вид')

    if 'nomn' in inf.tag:
        arr.append('именительный падеж')
    elif 'gent' in inf.tag:
        arr.append('родительный падеж')
    elif 'datv' in inf.tag:
        arr.append('дательный падеж')
    elif 'accs' in inf.tag:
        arr.append('винительный падеж')
    elif 'ablt' in inf.tag:
        arr.append('творительный падеж')
    elif 'loct' in inf.tag:
        arr.append('предложный падеж')

    if 'masc' in inf.tag:
        arr.append('мужской род')
    elif 'femn' in inf.tag:
        arr.append('женский род')
    elif 'neut' in inf.tag:
        arr.append('средний род')

    if 'indc' in inf.tag:
        arr.append('изъявительное наклонение')
    elif 'impr' in inf.tag:
        arr.append('повелительное наклонение')

    if 'sing' in inf.tag:
        arr.append('единственное число')
    elif 'plur' in inf.tag:
        arr.append('множественное число')

    if '1per' in inf.tag:
        arr.append('1 лицо')
    elif '2per' in inf.tag:
        arr.append('2 лицо')
    elif '3per' in inf.tag:
        arr.append('3 лицо')

    if 'pres' in inf.tag:
        arr.append('настоящее время')
    elif 'past' in inf.tag:
        arr.append('прошедшее время')
    elif 'futr' in inf.tag:
        arr.append('будущее время')

    if 'tran' in inf.tag:
        arr.append('переходное')
    elif 'intr' in inf.tag:
        arr.append('непереходное')

    if 'pssv' in inf.tag:
        arr.append('страдательный залог')
    elif 'actv' in inf.tag:
        arr.append('действительный залог')

    return arr


class Window0(QMainWindow, UIwindow0):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.open_Window1_1)
        self.pushButton_2.clicked.connect(self.open_Window1)

    def open_Window1(self):
        self.first = Window1()
        self.first.show()

    def open_Window1_1(self):
        self.first_form = Window1_1()
        self.first_form.show()


class Window1_1(QWidget, UIwindow1_1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.open_Window2_1)

    def open_Window2_1(self):
        self.all_tr_text = []
        if self.checkBox_en.isChecked():
            json = translate(self.plainTextEdit.toPlainText(), 'en')
            self.all_tr_text.append('\n\tАнлийский язык:' + '\n' + ''.join(json["text"]))
        if self.checkBox_fr.isChecked():
            json = translate(self.plainTextEdit.toPlainText(), 'fr')
            self.all_tr_text.append('\n\tФранцузский язык:' + '\n' + ''.join(json["text"]))
        if self.checkBox_uk.isChecked():
            json = translate(self.plainTextEdit.toPlainText(), 'uk')
            self.all_tr_text.append('\n\tУкраинский язык:' + '\n' + ''.join(json["text"]))

        self.second_form = Window2_1(''.join(self.all_tr_text))
        self.second_form.show()


class Window2_1(QWidget, UIwindow2_1):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)

        self.translated_text = args[-1] + '\n\nПереведено сервисом «Яндекс.Переводчик».'
        self.textBrowser.setText(self.translated_text)


class Window1(QMainWindow, UIwindow1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.open_Window2)
        self.pushButton_2.clicked.connect(self.open_Window3)

    def open_Window2(self):
        self.second = Window2(self, self.lineEdit.text())
        self.second.show()

    def open_Window3(self):
        self.third = Window3(self, self.lineEdit_2.text())
        self.third.show()


class Window2(QWidget, UIwindow2):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.sl = args[-1]

        self.label.setText(args[-1])
        self.label.adjustSize()

        main_arr = get_morph_inf(self.sl)
        main_arr[0] = 'Часть речи: ' + main_arr[0]
        
        # all info:
        self.listWidget.addItems(main_arr)


class Window3(QWidget, UIwindow3):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.file = args[-1]

        self.words_arr = []
        with open(self.file) as f:
            for word in f:
                self.words_arr.append(word.strip())
        self.label_2.setText(f'Выберите номер слова(не более {len(self.words_arr)}):')
        for i, line in enumerate(self.words_arr):
            self.listWidget_2.addItem(str(i + 1) + ') ' + line)

        self.pushButton.clicked.connect(self.open_Window2)

    def open_Window2(self):
        self.word = self.words_arr[self.spinBox.value() - 1]
        self.second = Window2(self, self.word)
        self.second.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Window0()
    form.show()
    sys.exit(app.exec())
