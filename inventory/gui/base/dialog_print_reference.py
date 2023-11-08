# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_print_reference.ui'
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
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

class Ui_PrintReferenceDialog(object):
    def setupUi(self, PrintReferenceDialog):
        if not PrintReferenceDialog.objectName():
            PrintReferenceDialog.setObjectName(u"PrintReferenceDialog")
        PrintReferenceDialog.resize(378, 158)
        self.verticalLayout = QVBoxLayout(PrintReferenceDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.preview = QLabel(PrintReferenceDialog)
        self.preview.setObjectName(u"preview")
        self.preview.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.preview)

        self.buttons = QDialogButtonBox(PrintReferenceDialog)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setOrientation(Qt.Horizontal)
        self.buttons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttons)


        self.retranslateUi(PrintReferenceDialog)
        self.buttons.accepted.connect(PrintReferenceDialog.accept)
        self.buttons.rejected.connect(PrintReferenceDialog.reject)

        QMetaObject.connectSlotsByName(PrintReferenceDialog)
    # setupUi

    def retranslateUi(self, PrintReferenceDialog):
        PrintReferenceDialog.setWindowTitle(QCoreApplication.translate("PrintReferenceDialog", u"Print Reference", None))
        self.preview.setText(QCoreApplication.translate("PrintReferenceDialog", u"Label Preview", None))
    # retranslateUi

