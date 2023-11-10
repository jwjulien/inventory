# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_units.ui'
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

class Ui_WidgetUnits(object):
    def setupUi(self, WidgetUnits):
        if not WidgetUnits.objectName():
            WidgetUnits.setObjectName(u"WidgetUnits")
        WidgetUnits.resize(336, 535)
        self.verticalLayout = QVBoxLayout(WidgetUnits)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.units = QTableWidget(WidgetUnits)
        if (self.units.columnCount() < 3):
            self.units.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.units.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.units.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.units.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.units.setObjectName(u"units")
        self.units.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.EditKeyPressed)
        self.units.setAlternatingRowColors(True)
        self.units.setSelectionMode(QAbstractItemView.SingleSelection)
        self.units.horizontalHeader().setStretchLastSection(True)
        self.units.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.units)


        self.retranslateUi(WidgetUnits)

        QMetaObject.connectSlotsByName(WidgetUnits)
    # setupUi

    def retranslateUi(self, WidgetUnits):
        WidgetUnits.setWindowTitle(QCoreApplication.translate("WidgetUnits", u"Form", None))
        ___qtablewidgetitem = self.units.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("WidgetUnits", u"Name", None));
        ___qtablewidgetitem1 = self.units.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("WidgetUnits", u"Rows", None));
        ___qtablewidgetitem2 = self.units.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("WidgetUnits", u"Columns", None));
    # retranslateUi

