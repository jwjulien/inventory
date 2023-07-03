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
    QLineEdit, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)

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

        self.parts = QTableView(TabParts)
        self.parts.setObjectName(u"parts")
        self.parts.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.parts.setAlternatingRowColors(True)
        self.parts.setSelectionMode(QAbstractItemView.SingleSelection)
        self.parts.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.parts.setSortingEnabled(True)
        self.parts.horizontalHeader().setCascadingSectionResizes(True)
        self.parts.horizontalHeader().setProperty("showSortIndicator", True)
        self.parts.horizontalHeader().setStretchLastSection(True)
        self.parts.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.parts)


        self.retranslateUi(TabParts)

        QMetaObject.connectSlotsByName(TabParts)
    # setupUi

    def retranslateUi(self, TabParts):
        TabParts.setWindowTitle(QCoreApplication.translate("TabParts", u"Form", None))
        self.add.setText(QCoreApplication.translate("TabParts", u"Add Part", None))
    # retranslateUi

