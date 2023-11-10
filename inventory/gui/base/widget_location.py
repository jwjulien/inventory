# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_location.ui'
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
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_LocationWidget(object):
    def setupUi(self, LocationWidget):
        if not LocationWidget.objectName():
            LocationWidget.setObjectName(u"LocationWidget")
        LocationWidget.resize(925, 187)
        self.horizontalLayout = QHBoxLayout(LocationWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.locations = QTableWidget(LocationWidget)
        if (self.locations.columnCount() < 3):
            self.locations.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.locations.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.locations.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.locations.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.locations.setObjectName(u"locations")
        self.locations.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.locations.setSelectionMode(QAbstractItemView.SingleSelection)
        self.locations.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.locations.horizontalHeader().setStretchLastSection(True)
        self.locations.verticalHeader().setVisible(False)

        self.horizontalLayout.addWidget(self.locations)


        self.retranslateUi(LocationWidget)

        QMetaObject.connectSlotsByName(LocationWidget)
    # setupUi

    def retranslateUi(self, LocationWidget):
        LocationWidget.setWindowTitle(QCoreApplication.translate("LocationWidget", u"Form", None))
        ___qtablewidgetitem = self.locations.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("LocationWidget", u"Quantity", None));
        ___qtablewidgetitem1 = self.locations.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("LocationWidget", u"Last Counted", None));
        ___qtablewidgetitem2 = self.locations.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("LocationWidget", u"Location", None));
    # retranslateUi

