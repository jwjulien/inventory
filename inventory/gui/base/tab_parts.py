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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QVBoxLayout, QWidget)

from inventory.gui.widgets.parts import PartsWidget

class Ui_TabParts(object):
    def setupUi(self, TabParts):
        if not TabParts.objectName():
            TabParts.setObjectName(u"TabParts")
        TabParts.resize(871, 671)
        self.verticalLayout = QVBoxLayout(TabParts)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.parts = PartsWidget(TabParts)
        self.parts.setObjectName(u"parts")

        self.verticalLayout.addWidget(self.parts)


        self.retranslateUi(TabParts)

        QMetaObject.connectSlotsByName(TabParts)
    # setupUi

    def retranslateUi(self, TabParts):
        TabParts.setWindowTitle(QCoreApplication.translate("TabParts", u"Form", None))
    # retranslateUi

