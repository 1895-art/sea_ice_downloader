# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_seaicedata.ui'
#
# Created: Tue Oct  7 21:00:43 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SeaIceData(object):
    def setupUi(self, SeaIceData):
        SeaIceData.setObjectName(_fromUtf8("SeaIceData"))
        SeaIceData.resize(406, 408)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SeaIceData.sizePolicy().hasHeightForWidth())
        SeaIceData.setSizePolicy(sizePolicy)
        self.label_5 = QtGui.QLabel(SeaIceData)
        self.label_5.setGeometry(QtCore.QRect(12, 12, 178, 19))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.widget = QtGui.QWidget(SeaIceData)
        self.widget.setGeometry(QtCore.QRect(0, 41, 405, 357))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.startDate = QtGui.QDateEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startDate.sizePolicy().hasHeightForWidth())
        self.startDate.setSizePolicy(sizePolicy)
        self.startDate.setDateTime(QtCore.QDateTime(QtCore.QDate(1980, 1, 1), QtCore.QTime(0, 0, 0)))
        self.startDate.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1980, 1, 1), QtCore.QTime(0, 0, 0)))
        self.startDate.setMaximumDate(QtCore.QDate(2013, 12, 31))
        self.startDate.setMinimumDate(QtCore.QDate(1980, 1, 1))
        self.startDate.setCalendarPopup(True)
        self.startDate.setDate(QtCore.QDate(1980, 1, 1))
        self.startDate.setObjectName(_fromUtf8("startDate"))
        self.horizontalLayout.addWidget(self.startDate)
        self.endDate = QtGui.QDateEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endDate.sizePolicy().hasHeightForWidth())
        self.endDate.setSizePolicy(sizePolicy)
        self.endDate.setCalendarPopup(True)
        self.endDate.setDate(QtCore.QDate(2013, 12, 31))
        self.endDate.setObjectName(_fromUtf8("endDate"))
        self.horizontalLayout.addWidget(self.endDate)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.txtPath = QtGui.QLineEdit(self.widget)
        self.txtPath.setText(_fromUtf8(""))
        self.txtPath.setObjectName(_fromUtf8("txtPath"))
        self.horizontalLayout_2.addWidget(self.txtPath)
        self.toolButton = QtGui.QToolButton(self.widget)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.checkBoxComposite = QtGui.QCheckBox(self.widget)
        self.checkBoxComposite.setObjectName(_fromUtf8("checkBoxComposite"))
        self.gridLayout.addWidget(self.checkBoxComposite, 2, 0, 1, 1)
        self.checkBoxCanvas = QtGui.QCheckBox(self.widget)
        self.checkBoxCanvas.setObjectName(_fromUtf8("checkBoxCanvas"))
        self.gridLayout.addWidget(self.checkBoxCanvas, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.widget)
        self.plainTextEdit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(0, 180))
        self.plainTextEdit.setBaseSize(QtCore.QSize(0, 0))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayout_2.addWidget(self.plainTextEdit, 1, 0, 1, 1)
        self.btnDownload = QtGui.QPushButton(self.widget)
        self.btnDownload.setObjectName(_fromUtf8("btnDownload"))
        self.gridLayout_2.addWidget(self.btnDownload, 2, 0, 1, 1)

        self.retranslateUi(SeaIceData)
        QtCore.QObject.connect(self.btnDownload, QtCore.SIGNAL(_fromUtf8("clicked()")), SeaIceData.accept)
        QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL(_fromUtf8("clicked()")), SeaIceData.open)
        QtCore.QObject.connect(self.checkBoxComposite, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), SeaIceData.update)
        QtCore.QObject.connect(self.checkBoxCanvas, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), SeaIceData.show)
        QtCore.QMetaObject.connectSlotsByName(SeaIceData)

    def retranslateUi(self, SeaIceData):
        SeaIceData.setWindowTitle(_translate("SeaIceData", "OceanData", None))
        self.label_5.setText(_translate("SeaIceData", "Sea Ice Concentration", None))
        self.label_2.setText(_translate("SeaIceData", "Date range:  ", None))
        self.startDate.setDisplayFormat(_translate("SeaIceData", "yyyy/MM/dd", None))
        self.endDate.setDisplayFormat(_translate("SeaIceData", "yyyy/MM/dd", None))
        self.label.setText(_translate("SeaIceData", "Download to:", None))
        self.toolButton.setText(_translate("SeaIceData", "...", None))
        self.checkBoxComposite.setText(_translate("SeaIceData", "Create composite", None))
        self.checkBoxCanvas.setText(_translate("SeaIceData", "Add data to canvas", None))
        self.btnDownload.setText(_translate("SeaIceData", "Download", None))
