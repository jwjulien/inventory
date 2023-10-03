# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_part_select.ui'
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

class Ui_PartSelectDialog(object):
    def setupUi(self, PartSelectDialog):
        if not PartSelectDialog.objectName():
            PartSelectDialog.setObjectName(u"PartSelectDialog")
        PartSelectDialog.resize(899, 309)
        self.verticalLayout = QVBoxLayout(PartSelectDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.parts = PartsWidget(PartSelectDialog)
        self.parts.setObjectName(u"parts")

        self.verticalLayout.addWidget(self.parts)

        self.buttonBox = QDialogButtonBox(PartSelectDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(PartSelectDialog)
        self.buttonBox.accepted.connect(PartSelectDialog.accept)
        self.buttonBox.rejected.connect(PartSelectDialog.reject)

        QMetaObject.connectSlotsByName(PartSelectDialog)
    # setupUi

    def retranslateUi(self, PartSelectDialog):
        PartSelectDialog.setWindowTitle(QCoreApplication.translate("PartSelectDialog", u"Part Select", None))
    # retranslateUi

