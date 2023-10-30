# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_parts_counter.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QHBoxLayout, QLCDNumber,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_PartsCounterDialog(object):
    def setupUi(self, PartsCounterDialog):
        if not PartsCounterDialog.objectName():
            PartsCounterDialog.setObjectName(u"PartsCounterDialog")
        PartsCounterDialog.resize(370, 307)
        self.verticalLayout = QVBoxLayout(PartsCounterDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.count = QLCDNumber(PartsCounterDialog)
        self.count.setObjectName(u"count")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.count.sizePolicy().hasHeightForWidth())
        self.count.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.count)

        self.part_weight_widget = QWidget(PartsCounterDialog)
        self.part_weight_widget.setObjectName(u"part_weight_widget")
        self.horizontalLayout = QHBoxLayout(self.part_weight_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_part_weight = QLabel(self.part_weight_widget)
        self.lbl_part_weight.setObjectName(u"lbl_part_weight")

        self.horizontalLayout.addWidget(self.lbl_part_weight)

        self.part_weight = QDoubleSpinBox(self.part_weight_widget)
        self.part_weight.setObjectName(u"part_weight")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.part_weight.sizePolicy().hasHeightForWidth())
        self.part_weight.setSizePolicy(sizePolicy1)
        self.part_weight.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.part_weight.setDecimals(3)
        self.part_weight.setMinimum(0.001000000000000)
        self.part_weight.setMaximum(500.000000000000000)
        self.part_weight.setSingleStep(0.100000000000000)
        self.part_weight.setValue(0.001000000000000)

        self.horizontalLayout.addWidget(self.part_weight)


        self.verticalLayout.addWidget(self.part_weight_widget)

        self.drawer_weight_widget = QWidget(PartsCounterDialog)
        self.drawer_weight_widget.setObjectName(u"drawer_weight_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.drawer_weight_widget)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.lbl_drawer_weight = QLabel(self.drawer_weight_widget)
        self.lbl_drawer_weight.setObjectName(u"lbl_drawer_weight")

        self.horizontalLayout_2.addWidget(self.lbl_drawer_weight)

        self.drawer_weight = QDoubleSpinBox(self.drawer_weight_widget)
        self.drawer_weight.setObjectName(u"drawer_weight")
        sizePolicy1.setHeightForWidth(self.drawer_weight.sizePolicy().hasHeightForWidth())
        self.drawer_weight.setSizePolicy(sizePolicy1)
        self.drawer_weight.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.drawer_weight.setDecimals(3)
        self.drawer_weight.setMaximum(500.000000000000000)
        self.drawer_weight.setSingleStep(0.100000000000000)

        self.horizontalLayout_2.addWidget(self.drawer_weight)


        self.verticalLayout.addWidget(self.drawer_weight_widget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.weight = QLCDNumber(PartsCounterDialog)
        self.weight.setObjectName(u"weight")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.weight.sizePolicy().hasHeightForWidth())
        self.weight.setSizePolicy(sizePolicy2)
        self.weight.setMinimumSize(QSize(135, 45))
        self.weight.setDigitCount(5)

        self.horizontalLayout_3.addWidget(self.weight)

        self.lbl_weight_units = QLabel(PartsCounterDialog)
        self.lbl_weight_units.setObjectName(u"lbl_weight_units")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(18)
        self.lbl_weight_units.setFont(font)
        self.lbl_weight_units.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout_3.addWidget(self.lbl_weight_units)

        self.sub_drawer = QCheckBox(PartsCounterDialog)
        self.sub_drawer.setObjectName(u"sub_drawer")

        self.horizontalLayout_3.addWidget(self.sub_drawer)

        self.tare = QPushButton(PartsCounterDialog)
        self.tare.setObjectName(u"tare")

        self.horizontalLayout_3.addWidget(self.tare)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.buttons = QDialogButtonBox(PartsCounterDialog)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setOrientation(Qt.Horizontal)
        self.buttons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.buttons)


        self.retranslateUi(PartsCounterDialog)
        self.buttons.accepted.connect(PartsCounterDialog.accept)
        self.buttons.rejected.connect(PartsCounterDialog.reject)

        QMetaObject.connectSlotsByName(PartsCounterDialog)
    # setupUi

    def retranslateUi(self, PartsCounterDialog):
        PartsCounterDialog.setWindowTitle(QCoreApplication.translate("PartsCounterDialog", u"Parts Counter Scale", None))
        self.lbl_part_weight.setText(QCoreApplication.translate("PartsCounterDialog", u"Part Weight:", None))
        self.part_weight.setSuffix(QCoreApplication.translate("PartsCounterDialog", u"g", None))
        self.lbl_drawer_weight.setText(QCoreApplication.translate("PartsCounterDialog", u"Drawer Weight:", None))
        self.drawer_weight.setSuffix(QCoreApplication.translate("PartsCounterDialog", u"g", None))
        self.lbl_weight_units.setText(QCoreApplication.translate("PartsCounterDialog", u"g", None))
#if QT_CONFIG(tooltip)
        self.sub_drawer.setToolTip(QCoreApplication.translate("PartsCounterDialog", u"Subtract the weight of a single drawer before counting.", None))
#endif // QT_CONFIG(tooltip)
        self.sub_drawer.setText(QCoreApplication.translate("PartsCounterDialog", u"Subtract Drawer", None))
        self.tare.setText(QCoreApplication.translate("PartsCounterDialog", u"Tare", None))
    # retranslateUi

