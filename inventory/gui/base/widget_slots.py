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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHeaderView, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_WidgetSlots(object):
    def setupUi(self, WidgetSlots):
        if not WidgetSlots.objectName():
            WidgetSlots.setObjectName(u"WidgetSlots")
        WidgetSlots.resize(437, 573)
        self.verticalLayout_2 = QVBoxLayout(WidgetSlots)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(WidgetSlots)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.slots = QTableWidget(self.groupBox)
        self.slots.setObjectName(u"slots")
        self.slots.setAlternatingRowColors(True)
        self.slots.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.slots)

        self.remove = QPushButton(self.groupBox)
        self.remove.setObjectName(u"remove")
        self.remove.setEnabled(False)

        self.verticalLayout.addWidget(self.remove)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(WidgetSlots)

        QMetaObject.connectSlotsByName(WidgetSlots)
    # setupUi

    def retranslateUi(self, WidgetSlots):
        WidgetSlots.setWindowTitle(QCoreApplication.translate("WidgetSlots", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("WidgetSlots", u"Slots:", None))
        self.remove.setText(QCoreApplication.translate("WidgetSlots", u"Remove", None))
    # retranslateUi

