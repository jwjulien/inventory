# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_category.ui'
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
    QFormLayout, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_DialogCategory(object):
    def setupUi(self, DialogCategory):
        if not DialogCategory.objectName():
            DialogCategory.setObjectName(u"DialogCategory")
        DialogCategory.resize(400, 98)
        self.formLayout = QFormLayout(DialogCategory)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_title = QLabel(DialogCategory)
        self.lbl_title.setObjectName(u"lbl_title")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_title)

        self.title = QLineEdit(DialogCategory)
        self.title.setObjectName(u"title")
        self.title.setMaxLength(50)
        self.title.setFrame(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.title)

        self.lbl_designator = QLabel(DialogCategory)
        self.lbl_designator.setObjectName(u"lbl_designator")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_designator)

        self.designator = QLineEdit(DialogCategory)
        self.designator.setObjectName(u"designator")
        self.designator.setMaxLength(10)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.designator)

        self.buttonBox = QDialogButtonBox(DialogCategory)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.buttonBox)


        self.retranslateUi(DialogCategory)
        self.buttonBox.accepted.connect(DialogCategory.accept)
        self.buttonBox.rejected.connect(DialogCategory.reject)

        QMetaObject.connectSlotsByName(DialogCategory)
    # setupUi

    def retranslateUi(self, DialogCategory):
        DialogCategory.setWindowTitle(QCoreApplication.translate("DialogCategory", u"Dialog", None))
        self.lbl_title.setText(QCoreApplication.translate("DialogCategory", u"Title:", None))
        self.lbl_designator.setText(QCoreApplication.translate("DialogCategory", u"Designator:", None))
    # retranslateUi

