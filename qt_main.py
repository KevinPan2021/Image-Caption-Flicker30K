# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Application(object):
    def setupUi(self, Application):
        Application.setObjectName("Application")
        Application.resize(950, 650)
        Application.setMinimumSize(QtCore.QSize(950, 650))
        Application.setMaximumSize(QtCore.QSize(950, 650))
        Application.setMouseTracking(True)
        Application.setStyleSheet("background-color:rgb(32, 38, 52);")
        Application.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(Application)
        self.centralwidget.setMinimumSize(QtCore.QSize(950, 650))
        self.centralwidget.setMaximumSize(QtCore.QSize(950, 650))
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setStyleSheet("background-color:rgb(32, 38, 52);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolButton_import = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_import.setMinimumSize(QtCore.QSize(100, 38))
        self.toolButton_import.setMaximumSize(QtCore.QSize(100, 38))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.toolButton_import.setFont(font)
        self.toolButton_import.setStyleSheet("QToolButton {\n"
"    color:white; \n"
"    background:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0,         stop:0 rgba(32, 38, 52, 255), \n"
"        stop:1 rgba(91, 99, 120, 255));\n"
"    border: 2px solid black;\n"
"    border-radius: 8px;\n"
"}")
        self.toolButton_import.setObjectName("toolButton_import")
        self.horizontalLayout.addWidget(self.toolButton_import)
        self.lineEdit_import = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_import.setEnabled(False)
        self.lineEdit_import.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_import.setStyleSheet("QLineEdit {\n"
"    border-radius: 4px;\n"
"    background-color:rgb(83, 89, 110);\n"
"    color:white;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    border-radius: 4px;\n"
"    background-color:rgb(83, 89, 110);\n"
"    color:rgb(200, 200, 200);\n"
"    border: 0px solid black;\n"
"}")
        self.lineEdit_import.setObjectName("lineEdit_import")
        self.horizontalLayout.addWidget(self.lineEdit_import)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setMinimumSize(QtCore.QSize(450, 450))
        self.label_image.setMaximumSize(QtCore.QSize(450, 450))
        self.label_image.setAutoFillBackground(False)
        self.label_image.setStyleSheet("background-color: rgb(56, 64, 85);")
        self.label_image.setText("")
        self.label_image.setScaledContents(True)
        self.label_image.setObjectName("label_image")
        self.verticalLayout.addWidget(self.label_image)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.textEdit_caption = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_caption.setMinimumSize(QtCore.QSize(450, 450))
        self.textEdit_caption.setMaximumSize(QtCore.QSize(450, 450))
        self.textEdit_caption.setStyleSheet("background-color: rgb(56, 64, 85);")
        self.textEdit_caption.setObjectName("textEdit_caption")
        self.verticalLayout_2.addWidget(self.textEdit_caption)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.comboBox_model = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_model.setMinimumSize(QtCore.QSize(140, 25))
        self.comboBox_model.setMaximumSize(QtCore.QSize(140, 25))
        self.comboBox_model.setStyleSheet("QComboBox {\n"
"    border-radius: 4px;\n"
"    background-color:rgb(83, 89, 110);\n"
"    color:white;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView { color: white; }\n"
"\n"
"QComboBox:disabled {\n"
"    border-radius: 4px;\n"
"    background-color:rgb(83, 89, 110);\n"
"    color:rgb(200, 200, 200);\n"
"    border: 0px solid black;\n"
"}")
        self.comboBox_model.setObjectName("comboBox_model")
        self.comboBox_model.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_model)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.toolButton_process = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_process.setMinimumSize(QtCore.QSize(100, 38))
        self.toolButton_process.setMaximumSize(QtCore.QSize(100, 38))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.toolButton_process.setFont(font)
        self.toolButton_process.setStyleSheet("QToolButton {\n"
"    color:white; \n"
"    background:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0,         stop:0 rgba(32, 38, 52, 255), \n"
"        stop:1 rgba(91, 99, 120, 255));\n"
"    border: 2px solid black;\n"
"    border-radius: 8px;\n"
"}")
        self.toolButton_process.setObjectName("toolButton_process")
        self.horizontalLayout_4.addWidget(self.toolButton_process)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        Application.setCentralWidget(self.centralwidget)

        self.retranslateUi(Application)
        QtCore.QMetaObject.connectSlotsByName(Application)

    def retranslateUi(self, Application):
        _translate = QtCore.QCoreApplication.translate
        Application.setWindowTitle(_translate("Application", "MainWindow"))
        self.toolButton_import.setText(_translate("Application", "Import"))
        self.label_3.setText(_translate("Application", "Image"))
        self.label_4.setText(_translate("Application", "Caption"))
        self.label_6.setText(_translate("Application", "Model"))
        self.comboBox_model.setItemText(0, _translate("Application", "AttentionCNN"))
        self.toolButton_process.setText(_translate("Application", "Process"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Application = QtWidgets.QMainWindow()
    ui = Ui_Application()
    ui.setupUi(Application)
    Application.show()
    sys.exit(app.exec_())
