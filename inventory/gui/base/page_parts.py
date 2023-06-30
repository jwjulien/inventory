# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_parts.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_PageParts(object):
    def setupUi(self, PageParts):
        if not PageParts.objectName():
            PageParts.setObjectName(u"PageParts")
        PageParts.resize(871, 671)
        self.verticalLayout = QVBoxLayout(PageParts)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.parts = QTableWidget(PageParts)
        if (self.parts.columnCount() < 5):
            self.parts.setColumnCount(5)
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
        self.parts.setObjectName(u"parts")
        self.parts.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.parts.setAlternatingRowColors(True)
        self.parts.setSelectionMode(QAbstractItemView.SingleSelection)
        self.parts.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.parts.setSortingEnabled(True)
        self.parts.horizontalHeader().setStretchLastSection(True)
        self.parts.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.parts)


        self.retranslateUi(PageParts)

        QMetaObject.connectSlotsByName(PageParts)
    # setupUi

    def retranslateUi(self, PageParts):
        PageParts.setWindowTitle(QCoreApplication.translate("PageParts", u"Form", None))
        ___qtablewidgetitem = self.parts.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PageParts", u"Category", None));
        ___qtablewidgetitem1 = self.parts.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PageParts", u"Value", None));
        ___qtablewidgetitem2 = self.parts.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PageParts", u"Package", None));
        ___qtablewidgetitem3 = self.parts.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PageParts", u"Quantity", None));
        ___qtablewidgetitem4 = self.parts.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PageParts", u"Price", None));
    # retranslateUi

