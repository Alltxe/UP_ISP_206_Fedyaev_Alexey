# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.layoutWidget = Form
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)

        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 1, 1, 1)
        self.training_btn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.training_btn.sizePolicy().hasHeightForWidth())
        self.training_btn.setSizePolicy(sizePolicy)
        self.training_btn.setMinimumSize(QtCore.QSize(253, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.training_btn.setFont(font)
        self.training_btn.setObjectName("training_btn")
        self.gridLayout.addWidget(self.training_btn, 3, 3, 1, 1)
        self.challenge_btn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.challenge_btn.sizePolicy().hasHeightForWidth())
        self.challenge_btn.setSizePolicy(sizePolicy)
        self.challenge_btn.setMinimumSize(QtCore.QSize(253, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.challenge_btn.setFont(font)
        self.challenge_btn.setObjectName("challenge_btn")
        self.gridLayout.addWidget(self.challenge_btn, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 3)
        self.exit_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.exit_btn.setFont(font)
        self.exit_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('images\exit.png'), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.exit_btn.setIcon(icon)
        self.exit_btn.setIconSize(QtCore.QSize(50, 50))
        self.exit_btn.setObjectName("exit_btn")
        self.gridLayout.addWidget(self.exit_btn, 5, 4, 1, 1)
        self.info_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.info_btn.setFont(font)
        self.info_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/info.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.info_btn.setIcon(icon1)
        self.info_btn.setIconSize(QtCore.QSize(50, 50))
        self.info_btn.setObjectName("info_btn")
        self.gridLayout.addWidget(self.info_btn, 5, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.training_btn.setText(_translate("Form", "Тренировочный режим"))
        self.challenge_btn.setText(_translate("Form", "Режим испытания"))
        self.label.setText(_translate("Form", "Тренажер для памяти"))
