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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QSizePolicy, QSplitter, QWidget)

from inventory.gui.widgets.areas import AreasWidget
from inventory.gui.widgets.parts import PartsWidget
from inventory.gui.widgets.slots import SlotsWidget
from inventory.gui.widgets.units import UnitsWidget

class Ui_TabStorage(object):
    def setupUi(self, TabStorage):
        if not TabStorage.objectName():
            TabStorage.setObjectName(u"TabStorage")
        TabStorage.resize(966, 697)
        self.gridLayout = QGridLayout(TabStorage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(TabStorage)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.areas = AreasWidget(self.frame)
        self.areas.setObjectName(u"areas")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(3)
        sizePolicy1.setHeightForWidth(self.areas.sizePolicy().hasHeightForWidth())
        self.areas.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.areas)

        self.units = UnitsWidget(self.frame)
        self.units.setObjectName(u"units")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(3)
        sizePolicy2.setVerticalStretch(3)
        sizePolicy2.setHeightForWidth(self.units.sizePolicy().hasHeightForWidth())
        self.units.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.units)

        self.slots = SlotsWidget(self.frame)
        self.slots.setObjectName(u"slots")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(6)
        sizePolicy3.setVerticalStretch(3)
        sizePolicy3.setHeightForWidth(self.slots.sizePolicy().hasHeightForWidth())
        self.slots.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.slots)

        self.splitter.addWidget(self.frame)
        self.parts = PartsWidget(self.splitter)
        self.parts.setObjectName(u"parts")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.parts.sizePolicy().hasHeightForWidth())
        self.parts.setSizePolicy(sizePolicy4)
        self.splitter.addWidget(self.parts)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)


        self.retranslateUi(TabStorage)

        QMetaObject.connectSlotsByName(TabStorage)
    # setupUi

    def retranslateUi(self, TabStorage):
        TabStorage.setWindowTitle(QCoreApplication.translate("TabStorage", u"Form", None))
    # retranslateUi

