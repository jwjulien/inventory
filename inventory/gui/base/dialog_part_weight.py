# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_part_weight.ui'
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
    QDoubleSpinBox, QFormLayout, QHBoxLayout, QLCDNumber,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QWidget)

class Ui_PartWeightDialog(object):
    def setupUi(self, PartWeightDialog):
        if not PartWeightDialog.objectName():
            PartWeightDialog.setObjectName(u"PartWeightDialog")
        PartWeightDialog.resize(255, 187)
        self.formLayout = QFormLayout(PartWeightDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_count = QLabel(PartWeightDialog)
        self.lbl_count.setObjectName(u"lbl_count")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_count)

        self.count = QSpinBox(PartWeightDialog)
        self.count.setObjectName(u"count")
        self.count.setMinimum(1)
        self.count.setMaximum(9999)
        self.count.setSingleStep(10)
        self.count.setValue(10)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.count)

        self.display_widget = QWidget(PartWeightDialog)
        self.display_widget.setObjectName(u"display_widget")
        self.horizontalLayout = QHBoxLayout(self.display_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.weight = QLCDNumber(self.display_widget)
        self.weight.setObjectName(u"weight")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weight.sizePolicy().hasHeightForWidth())
        self.weight.setSizePolicy(sizePolicy)
        self.weight.setMinimumSize(QSize(135, 45))
        self.weight.setDigitCount(5)

        self.horizontalLayout.addWidget(self.weight)

        self.label_weight_units = QLabel(self.display_widget)
        self.label_weight_units.setObjectName(u"label_weight_units")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(18)
        self.label_weight_units.setFont(font)
        self.label_weight_units.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout.addWidget(self.label_weight_units)


        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.display_widget)

        self.lbl_part_weight = QLabel(PartWeightDialog)
        self.lbl_part_weight.setObjectName(u"lbl_part_weight")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_part_weight)

        self.part_weight = QDoubleSpinBox(PartWeightDialog)
        self.part_weight.setObjectName(u"part_weight")
        self.part_weight.setReadOnly(True)
        self.part_weight.setDecimals(3)
        self.part_weight.setMaximum(999999.000000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.part_weight)

        self.buttons = QDialogButtonBox(PartWeightDialog)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setOrientation(Qt.Horizontal)
        self.buttons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.buttons)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(4, QFormLayout.FieldRole, self.verticalSpacer)

        self.tare = QPushButton(PartWeightDialog)
        self.tare.setObjectName(u"tare")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.tare)


        self.retranslateUi(PartWeightDialog)
        self.buttons.accepted.connect(PartWeightDialog.accept)
        self.buttons.rejected.connect(PartWeightDialog.reject)

        QMetaObject.connectSlotsByName(PartWeightDialog)
    # setupUi

    def retranslateUi(self, PartWeightDialog):
        PartWeightDialog.setWindowTitle(QCoreApplication.translate("PartWeightDialog", u"Part Scale", None))
        self.lbl_count.setText(QCoreApplication.translate("PartWeightDialog", u"Part Count:", None))
        self.label_weight_units.setText(QCoreApplication.translate("PartWeightDialog", u"g", None))
        self.lbl_part_weight.setText(QCoreApplication.translate("PartWeightDialog", u"Part Weight:", None))
        self.part_weight.setSuffix(QCoreApplication.translate("PartWeightDialog", u"g", None))
        self.tare.setText(QCoreApplication.translate("PartWeightDialog", u"Tare", None))
    # retranslateUi

