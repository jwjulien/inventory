# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_supplier.ui'
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
    QFormLayout, QFrame, QLabel, QLineEdit,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_SupplierDialog(object):
    def setupUi(self, SupplierDialog):
        if not SupplierDialog.objectName():
            SupplierDialog.setObjectName(u"SupplierDialog")
        SupplierDialog.resize(400, 201)
        self.formLayout = QFormLayout(SupplierDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label = QLabel(SupplierDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.name = QLineEdit(SupplierDialog)
        self.name.setObjectName(u"name")
        self.name.setMaxLength(40)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name)

        self.label_2 = QLabel(SupplierDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.website = QLineEdit(SupplierDialog)
        self.website.setObjectName(u"website")
        self.website.setMaxLength(100)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.website)

        self.label_3 = QLabel(SupplierDialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.search = QLineEdit(SupplierDialog)
        self.search.setObjectName(u"search")
        self.search.setMaxLength(200)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.search)

        self.help = QTextBrowser(SupplierDialog)
        self.help.setObjectName(u"help")
        self.help.setFrameShape(QFrame.NoFrame)
        self.help.setFrameShadow(QFrame.Plain)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.help)

        self.buttonBox = QDialogButtonBox(SupplierDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.buttonBox)


        self.retranslateUi(SupplierDialog)
        self.buttonBox.accepted.connect(SupplierDialog.accept)
        self.buttonBox.rejected.connect(SupplierDialog.reject)

        QMetaObject.connectSlotsByName(SupplierDialog)
    # setupUi

    def retranslateUi(self, SupplierDialog):
        SupplierDialog.setWindowTitle(QCoreApplication.translate("SupplierDialog", u"Edit Supplier Information", None))
        self.label.setText(QCoreApplication.translate("SupplierDialog", u"Name:", None))
        self.label_2.setText(QCoreApplication.translate("SupplierDialog", u"Website:", None))
        self.label_3.setText(QCoreApplication.translate("SupplierDialog", u"Search:", None))
        self.help.setHtml(QCoreApplication.translate("SupplierDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Search string substitutions:</p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">{number}:</span> Supplier part number</li></ul></body></html>", None))
    # retranslateUi

