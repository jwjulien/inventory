# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_location_mapping.ui'
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
    QDialogButtonBox, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QWidget)

class Ui_DialogLocationMapping(object):
    def setupUi(self, DialogLocationMapping):
        if not DialogLocationMapping.objectName():
            DialogLocationMapping.setObjectName(u"DialogLocationMapping")
        DialogLocationMapping.resize(449, 160)
        self.formLayout = QFormLayout(DialogLocationMapping)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_slot = QLabel(DialogLocationMapping)
        self.lbl_slot.setObjectName(u"lbl_slot")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_slot)

        self.slot = QComboBox(DialogLocationMapping)
        self.slot.setObjectName(u"slot")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.slot)

        self.lbl_quantity = QLabel(DialogLocationMapping)
        self.lbl_quantity.setObjectName(u"lbl_quantity")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_quantity)

        self.frame = QFrame(DialogLocationMapping)
        self.frame.setObjectName(u"frame")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.last_counted = QLabel(self.frame)
        self.last_counted.setObjectName(u"last_counted")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.last_counted.sizePolicy().hasHeightForWidth())
        self.last_counted.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.last_counted)

        self.reset = QPushButton(self.frame)
        self.reset.setObjectName(u"reset")

        self.horizontalLayout.addWidget(self.reset)


        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.frame)

        self.buttonBox = QDialogButtonBox(DialogLocationMapping)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.buttonBox)

        self.lbl_last_counted = QLabel(DialogLocationMapping)
        self.lbl_last_counted.setObjectName(u"lbl_last_counted")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_last_counted)

        self.quantity = QSpinBox(DialogLocationMapping)
        self.quantity.setObjectName(u"quantity")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.quantity)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(3, QFormLayout.FieldRole, self.verticalSpacer)


        self.retranslateUi(DialogLocationMapping)
        self.buttonBox.accepted.connect(DialogLocationMapping.accept)
        self.buttonBox.rejected.connect(DialogLocationMapping.reject)

        QMetaObject.connectSlotsByName(DialogLocationMapping)
    # setupUi

    def retranslateUi(self, DialogLocationMapping):
        DialogLocationMapping.setWindowTitle(QCoreApplication.translate("DialogLocationMapping", u"Configure Part Storage Location", None))
        self.lbl_slot.setText(QCoreApplication.translate("DialogLocationMapping", u"Slot:", None))
        self.lbl_quantity.setText(QCoreApplication.translate("DialogLocationMapping", u"Quantity:", None))
        self.last_counted.setText(QCoreApplication.translate("DialogLocationMapping", u"Never", None))
        self.reset.setText(QCoreApplication.translate("DialogLocationMapping", u"Reset", None))
        self.lbl_last_counted.setText(QCoreApplication.translate("DialogLocationMapping", u"Last Counted:", None))
    # retranslateUi

