# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_areas.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QListWidget, QListWidgetItem,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_WidgetAreas(object):
    def setupUi(self, WidgetAreas):
        if not WidgetAreas.objectName():
            WidgetAreas.setObjectName(u"WidgetAreas")
        WidgetAreas.resize(379, 541)
        self.verticalLayout = QVBoxLayout(WidgetAreas)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.areas = QListWidget(WidgetAreas)
        self.areas.setObjectName(u"areas")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.areas.sizePolicy().hasHeightForWidth())
        self.areas.setSizePolicy(sizePolicy)
        self.areas.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.areas.setAlternatingRowColors(True)

        self.verticalLayout.addWidget(self.areas)


        self.retranslateUi(WidgetAreas)

        QMetaObject.connectSlotsByName(WidgetAreas)
    # setupUi

    def retranslateUi(self, WidgetAreas):
        WidgetAreas.setWindowTitle(QCoreApplication.translate("WidgetAreas", u"Form", None))
    # retranslateUi

