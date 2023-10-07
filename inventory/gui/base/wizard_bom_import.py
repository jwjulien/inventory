# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wizard_bom_import.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

from inventory.gui.widgets.file_select import FileSelectWidget

class Ui_BomImportWizard(object):
    def setupUi(self, BomImportWizard):
        if not BomImportWizard.objectName():
            BomImportWizard.setObjectName(u"BomImportWizard")
        BomImportWizard.resize(783, 470)
        self.verticalLayout = QVBoxLayout(BomImportWizard)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stack = QStackedWidget(BomImportWizard)
        self.stack.setObjectName(u"stack")
        self.page_browse = QWidget()
        self.page_browse.setObjectName(u"page_browse")
        self.verticalLayout_2 = QVBoxLayout(self.page_browse)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.instructions_1 = QLabel(self.page_browse)
        self.instructions_1.setObjectName(u"instructions_1")
        self.instructions_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.instructions_1)

        self.file_select = FileSelectWidget(self.page_browse)
        self.file_select.setObjectName(u"file_select")

        self.verticalLayout_2.addWidget(self.file_select)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.stack.addWidget(self.page_browse)
        self.page_project = QWidget()
        self.page_project.setObjectName(u"page_project")
        self.verticalLayout_3 = QVBoxLayout(self.page_project)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.group_project = QGroupBox(self.page_project)
        self.group_project.setObjectName(u"group_project")
        self.gridLayout = QGridLayout(self.group_project)
        self.gridLayout.setObjectName(u"gridLayout")
        self.radio_project_existing = QRadioButton(self.group_project)
        self.radio_project_existing.setObjectName(u"radio_project_existing")
        self.radio_project_existing.setChecked(True)

        self.gridLayout.addWidget(self.radio_project_existing, 0, 0, 1, 1)

        self.radio_project_new = QRadioButton(self.group_project)
        self.radio_project_new.setObjectName(u"radio_project_new")

        self.gridLayout.addWidget(self.radio_project_new, 2, 0, 1, 1)

        self.project_editor = QLineEdit(self.group_project)
        self.project_editor.setObjectName(u"project_editor")
        self.project_editor.setEnabled(False)

        self.gridLayout.addWidget(self.project_editor, 2, 1, 1, 1)

        self.project_combo = QComboBox(self.group_project)
        self.project_combo.setObjectName(u"project_combo")

        self.gridLayout.addWidget(self.project_combo, 0, 1, 1, 1)

        self.project_description = QPlainTextEdit(self.group_project)
        self.project_description.setObjectName(u"project_description")
        self.project_description.setEnabled(False)

        self.gridLayout.addWidget(self.project_description, 3, 1, 1, 1)

        self.line_2 = QFrame(self.group_project)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 2)


        self.verticalLayout_3.addWidget(self.group_project)

        self.stack.addWidget(self.page_project)
        self.page_revision = QWidget()
        self.page_revision.setObjectName(u"page_revision")
        self.verticalLayout_5 = QVBoxLayout(self.page_revision)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.project_name = QLabel(self.page_revision)
        self.project_name.setObjectName(u"project_name")
        self.project_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.project_name)

        self.group_revision = QGroupBox(self.page_revision)
        self.group_revision.setObjectName(u"group_revision")
        self.gridLayout_2 = QGridLayout(self.group_revision)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radio_revision_existing = QRadioButton(self.group_revision)
        self.radio_revision_existing.setObjectName(u"radio_revision_existing")
        self.radio_revision_existing.setChecked(True)

        self.gridLayout_2.addWidget(self.radio_revision_existing, 0, 0, 1, 1)

        self.radio_revision_new = QRadioButton(self.group_revision)
        self.radio_revision_new.setObjectName(u"radio_revision_new")

        self.gridLayout_2.addWidget(self.radio_revision_new, 2, 0, 1, 1)

        self.revision_date = QDateEdit(self.group_revision)
        self.revision_date.setObjectName(u"revision_date")
        self.revision_date.setEnabled(False)

        self.gridLayout_2.addWidget(self.revision_date, 3, 1, 1, 1)

        self.revision_combo = QComboBox(self.group_revision)
        self.revision_combo.setObjectName(u"revision_combo")

        self.gridLayout_2.addWidget(self.revision_combo, 0, 1, 1, 1)

        self.revision_editor = QLineEdit(self.group_revision)
        self.revision_editor.setObjectName(u"revision_editor")
        self.revision_editor.setEnabled(False)

        self.gridLayout_2.addWidget(self.revision_editor, 2, 1, 1, 1)

        self.line = QFrame(self.group_revision)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 2)


        self.verticalLayout_5.addWidget(self.group_revision)

        self.verticalSpacer = QSpacerItem(20, 232, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.stack.addWidget(self.page_revision)
        self.page_materials = QWidget()
        self.page_materials.setObjectName(u"page_materials")
        self.verticalLayout_4 = QVBoxLayout(self.page_materials)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.bom_title = QLabel(self.page_materials)
        self.bom_title.setObjectName(u"bom_title")
        self.bom_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.bom_title)

        self.materials = QTreeWidget(self.page_materials)
        self.materials.setObjectName(u"materials")
        self.materials.setAlternatingRowColors(True)
        self.materials.setRootIsDecorated(False)
        self.materials.header().setDefaultSectionSize(200)

        self.verticalLayout_4.addWidget(self.materials)

        self.stack.addWidget(self.page_materials)

        self.verticalLayout.addWidget(self.stack)

        self.widget = QWidget(BomImportWizard)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.back = QPushButton(self.widget)
        self.back.setObjectName(u"back")

        self.horizontalLayout.addWidget(self.back)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.next = QPushButton(self.widget)
        self.next.setObjectName(u"next")

        self.horizontalLayout.addWidget(self.next)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(BomImportWizard)

        self.stack.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(BomImportWizard)
    # setupUi

    def retranslateUi(self, BomImportWizard):
        BomImportWizard.setWindowTitle(QCoreApplication.translate("BomImportWizard", u"Dialog", None))
        self.instructions_1.setText(QCoreApplication.translate("BomImportWizard", u"Select a Markdown format BOM to get started.", None))
        self.group_project.setTitle(QCoreApplication.translate("BomImportWizard", u"Project", None))
        self.radio_project_existing.setText(QCoreApplication.translate("BomImportWizard", u"Use Exiting", None))
        self.radio_project_new.setText(QCoreApplication.translate("BomImportWizard", u"Make New", None))
        self.project_editor.setPlaceholderText(QCoreApplication.translate("BomImportWizard", u"Project Title", None))
        self.project_description.setPlaceholderText(QCoreApplication.translate("BomImportWizard", u"Project description", None))
        self.project_name.setText(QCoreApplication.translate("BomImportWizard", u"Project Name", None))
        self.group_revision.setTitle(QCoreApplication.translate("BomImportWizard", u"Revision", None))
        self.radio_revision_existing.setText(QCoreApplication.translate("BomImportWizard", u"Use Exiting", None))
        self.radio_revision_new.setText(QCoreApplication.translate("BomImportWizard", u"Make New", None))
        self.revision_editor.setPlaceholderText(QCoreApplication.translate("BomImportWizard", u"Revision name", None))
        self.bom_title.setText(QCoreApplication.translate("BomImportWizard", u"BOM Title", None))
        ___qtreewidgetitem = self.materials.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("BomImportWizard", u"Part Number", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("BomImportWizard", u"Part Summary", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("BomImportWizard", u"BOM Part Number", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("BomImportWizard", u"BOM Description", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("BomImportWizard", u"Designator", None));
        self.back.setText(QCoreApplication.translate("BomImportWizard", u"Back", None))
        self.next.setText(QCoreApplication.translate("BomImportWizard", u"Next", None))
    # retranslateUi

