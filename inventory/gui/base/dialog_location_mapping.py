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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_DialogLocationMapping(object):
    def setupUi(self, DialogLocationMapping):
        if not DialogLocationMapping.objectName():
            DialogLocationMapping.setObjectName(u"DialogLocationMapping")
        DialogLocationMapping.resize(648, 378)
        self.formLayout = QFormLayout(DialogLocationMapping)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_slot = QLabel(DialogLocationMapping)
        self.lbl_slot.setObjectName(u"lbl_slot")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_slot)

        self.slot = QTreeWidget(DialogLocationMapping)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.slot.setHeaderItem(__qtreewidgetitem)
        self.slot.setObjectName(u"slot")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.slot.sizePolicy().hasHeightForWidth())
        self.slot.setSizePolicy(sizePolicy)
        self.slot.header().setVisible(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.slot)

        self.lbl_quantity = QLabel(DialogLocationMapping)
        self.lbl_quantity.setObjectName(u"lbl_quantity")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_quantity)

        self.quantity_widget = QWidget(DialogLocationMapping)
        self.quantity_widget.setObjectName(u"quantity_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.quantity_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.quantity = QSpinBox(self.quantity_widget)
        self.quantity.setObjectName(u"quantity")
        self.quantity.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.quantity.setMaximum(99999999)

        self.horizontalLayout_2.addWidget(self.quantity)

        self.count = QPushButton(self.quantity_widget)
        self.count.setObjectName(u"count")
        self.count.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.count)


        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.quantity_widget)

        self.lbl_last_counted = QLabel(DialogLocationMapping)
        self.lbl_last_counted.setObjectName(u"lbl_last_counted")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_last_counted)

        self.frame = QFrame(DialogLocationMapping)
        self.frame.setObjectName(u"frame")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.reset = QPushButton(self.frame)
        self.reset.setObjectName(u"reset")

        self.horizontalLayout.addWidget(self.reset)

        self.last_counted = QLabel(self.frame)
        self.last_counted.setObjectName(u"last_counted")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.last_counted.sizePolicy().hasHeightForWidth())
        self.last_counted.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.last_counted)

        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.frame)


        self.retranslateUi(DialogLocationMapping)
        self.buttonBox.accepted.connect(DialogLocationMapping.accept)
        self.buttonBox.rejected.connect(DialogLocationMapping.reject)

        QMetaObject.connectSlotsByName(DialogLocationMapping)
    # setupUi

    def retranslateUi(self, DialogLocationMapping):
        DialogLocationMapping.setWindowTitle(QCoreApplication.translate("DialogLocationMapping", u"Configure Part Storage Location", None))
        self.lbl_slot.setText(QCoreApplication.translate("DialogLocationMapping", u"Location:", None))
        self.lbl_quantity.setText(QCoreApplication.translate("DialogLocationMapping", u"Quantity:", None))
        self.count.setText(QCoreApplication.translate("DialogLocationMapping", u"Count...", None))
        self.lbl_last_counted.setText(QCoreApplication.translate("DialogLocationMapping", u"Last Counted:", None))
        self.reset.setText(QCoreApplication.translate("DialogLocationMapping", u"Reset", None))
        self.last_counted.setText(QCoreApplication.translate("DialogLocationMapping", u"Never", None))
    # retranslateUi

