# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_slots.ui'
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

class Ui_WidgetSlots(object):
    def setupUi(self, WidgetSlots):
        if not WidgetSlots.objectName():
            WidgetSlots.setObjectName(u"WidgetSlots")
        WidgetSlots.resize(838, 528)
        self.verticalLayout = QVBoxLayout(WidgetSlots)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.slots = QTableWidget(WidgetSlots)
        self.slots.setObjectName(u"slots")
        self.slots.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.EditKeyPressed)
        self.slots.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.slots.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.slots.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.slots.horizontalHeader().setDefaultSectionSize(80)
        self.slots.horizontalHeader().setStretchLastSection(True)
        self.slots.verticalHeader().setDefaultSectionSize(60)

        self.verticalLayout.addWidget(self.slots)


        self.retranslateUi(WidgetSlots)

        QMetaObject.connectSlotsByName(WidgetSlots)
    # setupUi

    def retranslateUi(self, WidgetSlots):
        WidgetSlots.setWindowTitle(QCoreApplication.translate("WidgetSlots", u"Form", None))
    # retranslateUi

