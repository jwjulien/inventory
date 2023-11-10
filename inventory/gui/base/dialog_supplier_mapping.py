# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_supplier_mapping.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_DialogSupplierMapping(object):
    def setupUi(self, DialogSupplierMapping):
        if not DialogSupplierMapping.objectName():
            DialogSupplierMapping.setObjectName(u"DialogSupplierMapping")
        DialogSupplierMapping.resize(449, 160)
        self.formLayout = QFormLayout(DialogSupplierMapping)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_slot = QLabel(DialogSupplierMapping)
        self.lbl_slot.setObjectName(u"lbl_slot")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_slot)

        self.supplier = QComboBox(DialogSupplierMapping)
        self.supplier.setObjectName(u"supplier")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.supplier)

        self.lbl_quantity = QLabel(DialogSupplierMapping)
        self.lbl_quantity.setObjectName(u"lbl_quantity")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_quantity)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(2, QFormLayout.FieldRole, self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(DialogSupplierMapping)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.buttonBox)

        self.number = QLineEdit(DialogSupplierMapping)
        self.number.setObjectName(u"number")
        self.number.setMaxLength(80)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.number)

        QWidget.setTabOrder(self.supplier, self.number)

        self.retranslateUi(DialogSupplierMapping)
        self.buttonBox.accepted.connect(DialogSupplierMapping.accept)
        self.buttonBox.rejected.connect(DialogSupplierMapping.reject)

        QMetaObject.connectSlotsByName(DialogSupplierMapping)
    # setupUi

    def retranslateUi(self, DialogSupplierMapping):
        DialogSupplierMapping.setWindowTitle(QCoreApplication.translate("DialogSupplierMapping", u"Configure Part Storage Location", None))
        self.lbl_slot.setText(QCoreApplication.translate("DialogSupplierMapping", u"Supplier:", None))
        self.lbl_quantity.setText(QCoreApplication.translate("DialogSupplierMapping", u"Part Number:", None))
    # retranslateUi

