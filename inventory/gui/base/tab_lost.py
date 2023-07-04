# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_lost.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QVBoxLayout, QWidget)

from inventory.gui.widgets.parts import PartsWidget

class Ui_TabLost(object):
    def setupUi(self, TabLost):
        if not TabLost.objectName():
            TabLost.setObjectName(u"TabLost")
        TabLost.resize(767, 575)
        self.verticalLayout = QVBoxLayout(TabLost)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.parts = PartsWidget(TabLost)
        self.parts.setObjectName(u"parts")

        self.verticalLayout.addWidget(self.parts)


        self.retranslateUi(TabLost)

        QMetaObject.connectSlotsByName(TabLost)
    # setupUi

    def retranslateUi(self, TabLost):
        TabLost.setWindowTitle(QCoreApplication.translate("TabLost", u"Form", None))
    # retranslateUi

