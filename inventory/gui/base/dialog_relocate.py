# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_relocate.ui'
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
    QDialogButtonBox, QFormLayout, QLabel, QSizePolicy,
    QSpacerItem, QSpinBox, QWidget)

class Ui_DialogRelocate(object):
    def setupUi(self, DialogRelocate):
        if not DialogRelocate.objectName():
            DialogRelocate.setObjectName(u"DialogRelocate")
        DialogRelocate.resize(386, 162)
        self.formLayout = QFormLayout(DialogRelocate)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_move = QLabel(DialogRelocate)
        self.lbl_move.setObjectName(u"lbl_move")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_move)

        self.quantity = QSpinBox(DialogRelocate)
        self.quantity.setObjectName(u"quantity")
        self.quantity.setMaximum(1000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.quantity)

        self.lbl_of = QLabel(DialogRelocate)
        self.lbl_of.setObjectName(u"lbl_of")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_of)

        self.part = QLabel(DialogRelocate)
        self.part.setObjectName(u"part")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.part)

        self.lbl_from = QLabel(DialogRelocate)
        self.lbl_from.setObjectName(u"lbl_from")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_from)

        self.existing = QLabel(DialogRelocate)
        self.existing.setObjectName(u"existing")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.existing)

        self.lbl_to = QLabel(DialogRelocate)
        self.lbl_to.setObjectName(u"lbl_to")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_to)

        self.destination = QComboBox(DialogRelocate)
        self.destination.setObjectName(u"destination")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.destination)

        self.buttonBox = QDialogButtonBox(DialogRelocate)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.buttonBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(4, QFormLayout.FieldRole, self.verticalSpacer)


        self.retranslateUi(DialogRelocate)
        self.buttonBox.accepted.connect(DialogRelocate.accept)
        self.buttonBox.rejected.connect(DialogRelocate.reject)

        QMetaObject.connectSlotsByName(DialogRelocate)
    # setupUi

    def retranslateUi(self, DialogRelocate):
        DialogRelocate.setWindowTitle(QCoreApplication.translate("DialogRelocate", u"Relocate Stored Parts", None))
        self.lbl_move.setText(QCoreApplication.translate("DialogRelocate", u"Move:", None))
        self.lbl_of.setText(QCoreApplication.translate("DialogRelocate", u"Of:", None))
        self.part.setText(QCoreApplication.translate("DialogRelocate", u"<part name>", None))
        self.lbl_from.setText(QCoreApplication.translate("DialogRelocate", u"From:", None))
        self.existing.setText(QCoreApplication.translate("DialogRelocate", u"<existing slot name>", None))
        self.lbl_to.setText(QCoreApplication.translate("DialogRelocate", u"To:", None))
    # retranslateUi

