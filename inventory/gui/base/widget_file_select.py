# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_file_select.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_FileSelectWidget(object):
    def setupUi(self, FileSelectWidget):
        if not FileSelectWidget.objectName():
            FileSelectWidget.setObjectName(u"FileSelectWidget")
        FileSelectWidget.resize(713, 134)
        self.verticalLayout = QVBoxLayout(FileSelectWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(FileSelectWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.editor = QLineEdit(FileSelectWidget)
        self.editor.setObjectName(u"editor")

        self.horizontalLayout.addWidget(self.editor)

        self.browse = QPushButton(FileSelectWidget)
        self.browse.setObjectName(u"browse")

        self.horizontalLayout.addWidget(self.browse)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.error = QLabel(FileSelectWidget)
        self.error.setObjectName(u"error")
        sizePolicy.setHeightForWidth(self.error.sizePolicy().hasHeightForWidth())
        self.error.setSizePolicy(sizePolicy)
        font = QFont()
        font.setItalic(True)
        self.error.setFont(font)
        self.error.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.error)


        self.retranslateUi(FileSelectWidget)

        QMetaObject.connectSlotsByName(FileSelectWidget)
    # setupUi

    def retranslateUi(self, FileSelectWidget):
        FileSelectWidget.setWindowTitle(QCoreApplication.translate("FileSelectWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("FileSelectWidget", u"Label", None))
        self.browse.setText(QCoreApplication.translate("FileSelectWidget", u"Browse", None))
        self.error.setText(QCoreApplication.translate("FileSelectWidget", u"Error Message", None))
    # retranslateUi

