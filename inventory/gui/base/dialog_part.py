# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_part.ui'
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
    QDialogButtonBox, QDoubleSpinBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpinBox, QTabWidget, QVBoxLayout,
    QWidget)

from inventory.gui.widgets.attributes import AttributesWidget
from inventory.gui.widgets.document_list import DocumentListWidget
from inventory.gui.widgets.droppable_label import DroppableLabel
from inventory.gui.widgets.location import LocationWidget
from inventory.gui.widgets.materials import MaterialsWidget
from inventory.gui.widgets.suppliers import SuppliersWidget

class Ui_DialogPart(object):
    def setupUi(self, DialogPart):
        if not DialogPart.objectName():
            DialogPart.setObjectName(u"DialogPart")
        DialogPart.resize(1071, 650)
        self.horizontalLayout_7 = QHBoxLayout(DialogPart)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.left = QWidget(DialogPart)
        self.left.setObjectName(u"left")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left.sizePolicy().hasHeightForWidth())
        self.left.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.left)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.top = QWidget(self.left)
        self.top.setObjectName(u"top")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(2)
        sizePolicy1.setHeightForWidth(self.top.sizePolicy().hasHeightForWidth())
        self.top.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.top)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.properties_widget = QWidget(self.top)
        self.properties_widget.setObjectName(u"properties_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(5)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.properties_widget.sizePolicy().hasHeightForWidth())
        self.properties_widget.setSizePolicy(sizePolicy2)
        self.formLayout = QFormLayout(self.properties_widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, -1, 0)
        self.lbl_category = QLabel(self.properties_widget)
        self.lbl_category.setObjectName(u"lbl_category")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_category)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.category = QComboBox(self.properties_widget)
        self.category.setObjectName(u"category")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.category.sizePolicy().hasHeightForWidth())
        self.category.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.category)

        self.new_category = QPushButton(self.properties_widget)
        self.new_category.setObjectName(u"new_category")

        self.horizontalLayout.addWidget(self.new_category)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout)

        self.lbl_value = QLabel(self.properties_widget)
        self.lbl_value.setObjectName(u"lbl_value")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_value)

        self.lbl_number = QLabel(self.properties_widget)
        self.lbl_number.setObjectName(u"lbl_number")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_number)

        self.lbl_package = QLabel(self.properties_widget)
        self.lbl_package.setObjectName(u"lbl_package")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_package)

        self.lbl_price = QLabel(self.properties_widget)
        self.lbl_price.setObjectName(u"lbl_price")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lbl_price)

        self.lbl_weight = QLabel(self.properties_widget)
        self.lbl_weight.setObjectName(u"lbl_weight")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lbl_weight)

        self.value = QLineEdit(self.properties_widget)
        self.value.setObjectName(u"value")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.value)

        self.part_number = QLineEdit(self.properties_widget)
        self.part_number.setObjectName(u"part_number")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.part_number)

        self.footprint = QLineEdit(self.properties_widget)
        self.footprint.setObjectName(u"footprint")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.footprint)

        self.price = QDoubleSpinBox(self.properties_widget)
        self.price.setObjectName(u"price")
        self.price.setProperty("showGroupSeparator", True)
        self.price.setDecimals(3)
        self.price.setMaximum(10000.000000000000000)
        self.price.setSingleStep(0.010000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.price)

        self.lbl_reorder = QLabel(self.properties_widget)
        self.lbl_reorder.setObjectName(u"lbl_reorder")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lbl_reorder)

        self.threshold = QSpinBox(self.properties_widget)
        self.threshold.setObjectName(u"threshold")
        self.threshold.setMaximum(100000)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.threshold)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.weight = QDoubleSpinBox(self.properties_widget)
        self.weight.setObjectName(u"weight")
        self.weight.setDecimals(3)
        self.weight.setMaximum(1000000.000000000000000)

        self.horizontalLayout_5.addWidget(self.weight)

        self.calibrate = QPushButton(self.properties_widget)
        self.calibrate.setObjectName(u"calibrate")

        self.horizontalLayout_5.addWidget(self.calibrate)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.notes = QPlainTextEdit(self.properties_widget)
        self.notes.setObjectName(u"notes")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.notes)

        self.lbl_notes = QLabel(self.properties_widget)
        self.lbl_notes.setObjectName(u"lbl_notes")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.lbl_notes)


        self.horizontalLayout_2.addWidget(self.properties_widget)

        self.attributes = AttributesWidget(self.top)
        self.attributes.setObjectName(u"attributes")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(2)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.attributes.sizePolicy().hasHeightForWidth())
        self.attributes.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.attributes)


        self.verticalLayout_5.addWidget(self.top)

        self.tabs = QTabWidget(self.left)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setEnabled(False)
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(2)
        sizePolicy5.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy5)
        self.tabs.setTabPosition(QTabWidget.West)
        self.tab_locations = QWidget()
        self.tab_locations.setObjectName(u"tab_locations")
        self.verticalLayout_2 = QVBoxLayout(self.tab_locations)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.locations = LocationWidget(self.tab_locations)
        self.locations.setObjectName(u"locations")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.locations.sizePolicy().hasHeightForWidth())
        self.locations.setSizePolicy(sizePolicy6)

        self.verticalLayout_2.addWidget(self.locations)

        self.tabs.addTab(self.tab_locations, "")
        self.tab_projects = QWidget()
        self.tab_projects.setObjectName(u"tab_projects")
        self.verticalLayout_7 = QVBoxLayout(self.tab_projects)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.materials = MaterialsWidget(self.tab_projects)
        self.materials.setObjectName(u"materials")

        self.verticalLayout_7.addWidget(self.materials)

        self.tabs.addTab(self.tab_projects, "")
        self.tab_suppliers = QWidget()
        self.tab_suppliers.setObjectName(u"tab_suppliers")
        self.verticalLayout_6 = QVBoxLayout(self.tab_suppliers)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.suppliers = SuppliersWidget(self.tab_suppliers)
        self.suppliers.setObjectName(u"suppliers")
        sizePolicy6.setHeightForWidth(self.suppliers.sizePolicy().hasHeightForWidth())
        self.suppliers.setSizePolicy(sizePolicy6)

        self.verticalLayout_6.addWidget(self.suppliers)

        self.tabs.addTab(self.tab_suppliers, "")

        self.verticalLayout_5.addWidget(self.tabs)


        self.horizontalLayout_7.addWidget(self.left)

        self.right = QWidget(DialogPart)
        self.right.setObjectName(u"right")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.right.sizePolicy().hasHeightForWidth())
        self.right.setSizePolicy(sizePolicy7)
        self.verticalLayout_4 = QVBoxLayout(self.right)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.image_widget = QWidget(self.right)
        self.image_widget.setObjectName(u"image_widget")
        sizePolicy6.setHeightForWidth(self.image_widget.sizePolicy().hasHeightForWidth())
        self.image_widget.setSizePolicy(sizePolicy6)
        self.verticalLayout_3 = QVBoxLayout(self.image_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.image = DroppableLabel(self.image_widget)
        self.image.setObjectName(u"image")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(1)
        sizePolicy8.setVerticalStretch(1)
        sizePolicy8.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy8)
        self.image.setAcceptDrops(True)
        self.image.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.image)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.set_image = QPushButton(self.image_widget)
        self.set_image.setObjectName(u"set_image")

        self.horizontalLayout_3.addWidget(self.set_image)

        self.remove_image = QPushButton(self.image_widget)
        self.remove_image.setObjectName(u"remove_image")
        self.remove_image.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.remove_image)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_4.addWidget(self.image_widget)

        self.documents = DocumentListWidget(self.right)
        self.documents.setObjectName(u"documents")
        sizePolicy6.setHeightForWidth(self.documents.sizePolicy().hasHeightForWidth())
        self.documents.setSizePolicy(sizePolicy6)

        self.verticalLayout_4.addWidget(self.documents)

        self.buttons = QDialogButtonBox(self.right)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setOrientation(Qt.Horizontal)
        self.buttons.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Discard|QDialogButtonBox.Save)

        self.verticalLayout_4.addWidget(self.buttons)


        self.horizontalLayout_7.addWidget(self.right)


        self.retranslateUi(DialogPart)
        self.buttons.accepted.connect(DialogPart.accept)
        self.buttons.rejected.connect(DialogPart.reject)

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DialogPart)
    # setupUi

    def retranslateUi(self, DialogPart):
        DialogPart.setWindowTitle(QCoreApplication.translate("DialogPart", u"Dialog", None))
        self.lbl_category.setText(QCoreApplication.translate("DialogPart", u"Category:", None))
        self.new_category.setText(QCoreApplication.translate("DialogPart", u"New Category", None))
        self.lbl_value.setText(QCoreApplication.translate("DialogPart", u"Value:", None))
        self.lbl_number.setText(QCoreApplication.translate("DialogPart", u"Part Number:", None))
        self.lbl_package.setText(QCoreApplication.translate("DialogPart", u"Package:", None))
        self.lbl_price.setText(QCoreApplication.translate("DialogPart", u"Price:", None))
        self.lbl_weight.setText(QCoreApplication.translate("DialogPart", u"Weight:", None))
        self.price.setPrefix(QCoreApplication.translate("DialogPart", u"$", None))
        self.lbl_reorder.setText(QCoreApplication.translate("DialogPart", u"Reorder Threshold:", None))
#if QT_CONFIG(tooltip)
        self.threshold.setToolTip(QCoreApplication.translate("DialogPart", u"Part will appear in the reorder report when total quantity is LESS THAN this threshold.\n"
"\n"
"Set to zero to disable reorder (i.e. non-stocked) or set to one to reorder when completely gone.", None))
#endif // QT_CONFIG(tooltip)
        self.weight.setSuffix(QCoreApplication.translate("DialogPart", u"g", None))
        self.calibrate.setText(QCoreApplication.translate("DialogPart", u"Calibrate", None))
        self.lbl_notes.setText(QCoreApplication.translate("DialogPart", u"Notes:", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_locations), QCoreApplication.translate("DialogPart", u"Locations", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_projects), QCoreApplication.translate("DialogPart", u"Projects", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_suppliers), QCoreApplication.translate("DialogPart", u"Suppliers", None))
        self.set_image.setText(QCoreApplication.translate("DialogPart", u"Set Image", None))
        self.remove_image.setText(QCoreApplication.translate("DialogPart", u"Remove Image", None))
    # retranslateUi

