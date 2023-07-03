# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_parts.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_TabParts(object):
    def setupUi(self, TabParts):
        if not TabParts.objectName():
            TabParts.setObjectName(u"TabParts")
        TabParts.resize(871, 671)
        self.verticalLayout = QVBoxLayout(TabParts)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filter = QLineEdit(TabParts)
        self.filter.setObjectName(u"filter")

        self.horizontalLayout.addWidget(self.filter)

        self.add = QPushButton(TabParts)
        self.add.setObjectName(u"add")

        self.horizontalLayout.addWidget(self.add)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.parts = QTableWidget(TabParts)
        if (self.parts.columnCount() < 7):
            self.parts.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.parts.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.parts.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.parts.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.parts.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.parts.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.parts.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.parts.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.parts.setObjectName(u"parts")
        self.parts.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.parts.setAlternatingRowColors(True)
        self.parts.setSelectionMode(QAbstractItemView.SingleSelection)
        self.parts.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.parts.setSortingEnabled(True)
        self.parts.horizontalHeader().setStretchLastSection(True)
        self.parts.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.parts)


        self.retranslateUi(TabParts)

        QMetaObject.connectSlotsByName(TabParts)
    # setupUi

    def retranslateUi(self, TabParts):
        TabParts.setWindowTitle(QCoreApplication.translate("TabParts", u"Form", None))
        self.add.setText(QCoreApplication.translate("TabParts", u"Add Part", None))
        ___qtablewidgetitem = self.parts.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TabParts", u"Category", None));
        ___qtablewidgetitem1 = self.parts.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TabParts", u"Value", None));
        ___qtablewidgetitem2 = self.parts.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TabParts", u"Number", None));
        ___qtablewidgetitem3 = self.parts.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TabParts", u"Package", None));
        ___qtablewidgetitem4 = self.parts.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("TabParts", u"Quantity", None));
        ___qtablewidgetitem5 = self.parts.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("TabParts", u"Price", None));
        ___qtablewidgetitem6 = self.parts.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("TabParts", u"Liability", None));
    # retranslateUi

