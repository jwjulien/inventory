# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_slot_select.ui'
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
    QSizePolicy, QToolBox, QVBoxLayout, QWidget)

from inventory.gui.widgets.areas import AreasWidget
from inventory.gui.widgets.slots import SlotsWidget
from inventory.gui.widgets.units import UnitsWidget

class Ui_SlotSelectDialog(object):
    def setupUi(self, SlotSelectDialog):
        if not SlotSelectDialog.objectName():
            SlotSelectDialog.setObjectName(u"SlotSelectDialog")
        SlotSelectDialog.resize(1038, 599)
        self.verticalLayout = QVBoxLayout(SlotSelectDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolbox = QToolBox(SlotSelectDialog)
        self.toolbox.setObjectName(u"toolbox")
        self.page_area = QWidget()
        self.page_area.setObjectName(u"page_area")
        self.page_area.setGeometry(QRect(0, 0, 1020, 461))
        self.verticalLayout_4 = QVBoxLayout(self.page_area)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.areas = AreasWidget(self.page_area)
        self.areas.setObjectName(u"areas")

        self.verticalLayout_4.addWidget(self.areas)

        self.toolbox.addItem(self.page_area, u"Area")
        self.page_unit = QWidget()
        self.page_unit.setObjectName(u"page_unit")
        self.page_unit.setGeometry(QRect(0, 0, 1020, 461))
        self.verticalLayout_2 = QVBoxLayout(self.page_unit)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.units = UnitsWidget(self.page_unit)
        self.units.setObjectName(u"units")

        self.verticalLayout_2.addWidget(self.units)

        self.toolbox.addItem(self.page_unit, u"Unit")
        self.page_slot = QWidget()
        self.page_slot.setObjectName(u"page_slot")
        self.verticalLayout_3 = QVBoxLayout(self.page_slot)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.slots = SlotsWidget(self.page_slot)
        self.slots.setObjectName(u"slots")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.slots.sizePolicy().hasHeightForWidth())
        self.slots.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.slots)

        self.toolbox.addItem(self.page_slot, u"Slot")

        self.verticalLayout.addWidget(self.toolbox)

        self.buttons = QDialogButtonBox(SlotSelectDialog)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setOrientation(Qt.Horizontal)
        self.buttons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttons)


        self.retranslateUi(SlotSelectDialog)
        self.buttons.accepted.connect(SlotSelectDialog.accept)
        self.buttons.rejected.connect(SlotSelectDialog.reject)

        self.toolbox.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(SlotSelectDialog)
    # setupUi

    def retranslateUi(self, SlotSelectDialog):
        SlotSelectDialog.setWindowTitle(QCoreApplication.translate("SlotSelectDialog", u"Dialog", None))
        self.toolbox.setItemText(self.toolbox.indexOf(self.page_area), QCoreApplication.translate("SlotSelectDialog", u"Area", None))
        self.toolbox.setItemText(self.toolbox.indexOf(self.page_unit), QCoreApplication.translate("SlotSelectDialog", u"Unit", None))
        self.toolbox.setItemText(self.toolbox.indexOf(self.page_slot), QCoreApplication.translate("SlotSelectDialog", u"Slot", None))
    # retranslateUi

