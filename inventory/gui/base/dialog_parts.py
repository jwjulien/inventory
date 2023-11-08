# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_parts.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QSizePolicy, QVBoxLayout, QWidget)

from inventory.gui.widgets.parts import PartsWidget

class Ui_PartsDialog(object):
    def setupUi(self, PartsDialog):
        if not PartsDialog.objectName():
            PartsDialog.setObjectName(u"PartsDialog")
        PartsDialog.resize(767, 382)
        self.verticalLayout = QVBoxLayout(PartsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.parts = PartsWidget(PartsDialog)
        self.parts.setObjectName(u"parts")

        self.verticalLayout.addWidget(self.parts)

        self.buttons = QDialogButtonBox(PartsDialog)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setOrientation(Qt.Horizontal)
        self.buttons.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.buttons)


        self.retranslateUi(PartsDialog)
        self.buttons.accepted.connect(PartsDialog.accept)
        self.buttons.rejected.connect(PartsDialog.reject)

        QMetaObject.connectSlotsByName(PartsDialog)
    # setupUi

    def retranslateUi(self, PartsDialog):
        PartsDialog.setWindowTitle(QCoreApplication.translate("PartsDialog", u"Parts", None))
    # retranslateUi

