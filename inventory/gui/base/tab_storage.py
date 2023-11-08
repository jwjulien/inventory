# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_storage.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

from inventory.gui.widgets.areas import AreasWidget
from inventory.gui.widgets.slots import SlotsWidget
from inventory.gui.widgets.units import UnitsWidget

class Ui_TabStorage(object):
    def setupUi(self, TabStorage):
        if not TabStorage.objectName():
            TabStorage.setObjectName(u"TabStorage")
        TabStorage.resize(966, 697)
        self.horizontalLayout_2 = QHBoxLayout(TabStorage)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stack = QStackedWidget(TabStorage)
        self.stack.setObjectName(u"stack")
        self.page_areas = QWidget()
        self.page_areas.setObjectName(u"page_areas")
        self.horizontalLayout = QHBoxLayout(self.page_areas)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.group_areas = QGroupBox(self.page_areas)
        self.group_areas.setObjectName(u"group_areas")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_areas.sizePolicy().hasHeightForWidth())
        self.group_areas.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.group_areas)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.areas = AreasWidget(self.group_areas)
        self.areas.setObjectName(u"areas")

        self.verticalLayout_2.addWidget(self.areas)


        self.horizontalLayout.addWidget(self.group_areas)

        self.group_units = QGroupBox(self.page_areas)
        self.group_units.setObjectName(u"group_units")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.group_units.sizePolicy().hasHeightForWidth())
        self.group_units.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.group_units)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.units = UnitsWidget(self.group_units)
        self.units.setObjectName(u"units")

        self.verticalLayout_3.addWidget(self.units)


        self.horizontalLayout.addWidget(self.group_units)

        self.stack.addWidget(self.page_areas)
        self.page_slots = QWidget()
        self.page_slots.setObjectName(u"page_slots")
        self.verticalLayout = QVBoxLayout(self.page_slots)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.back = QPushButton(self.page_slots)
        self.back.setObjectName(u"back")

        self.horizontalLayout_3.addWidget(self.back)

        self.title = QLabel(self.page_slots)
        self.title.setObjectName(u"title")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy2)
        self.title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.title)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.slots = SlotsWidget(self.page_slots)
        self.slots.setObjectName(u"slots")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.slots.sizePolicy().hasHeightForWidth())
        self.slots.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.slots)

        self.stack.addWidget(self.page_slots)

        self.horizontalLayout_2.addWidget(self.stack)


        self.retranslateUi(TabStorage)

        self.stack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TabStorage)
    # setupUi

    def retranslateUi(self, TabStorage):
        TabStorage.setWindowTitle(QCoreApplication.translate("TabStorage", u"Form", None))
        self.group_areas.setTitle(QCoreApplication.translate("TabStorage", u"Areas:", None))
        self.group_units.setTitle(QCoreApplication.translate("TabStorage", u"Units:", None))
        self.back.setText(QCoreApplication.translate("TabStorage", u"Back", None))
        self.title.setText(QCoreApplication.translate("TabStorage", u"Slot Title", None))
    # retranslateUi

