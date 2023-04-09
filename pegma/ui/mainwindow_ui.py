# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QComboBox, QDockWidget, QDoubleSpinBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListView, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTabWidget, QTableView,
    QTextBrowser, QToolBar, QVBoxLayout, QWidget)
import Main_icons_rc
import docs_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1149, 878)
        MainWindow.setFocusPolicy(Qt.StrongFocus)
        icon = QIcon()
        icon.addFile(u":/logo/logo_favicon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 0px solid #C2C7CB;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 2px solid #C4C4C3;\n"
"    /*border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 15ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"\n"
""
                        "QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"\n"
"/* make use of negative margins for overlapping tabs */\n"
"QTabBar::tab:selected {\n"
"    /* expand/overlap to the left and right by 4px */\n"
"    margin-left: -4px;\n"
"    margin-right: -4px;\n"
"}\n"
"\n"
"QTabBar::tab:first:selected {\n"
"    margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
"}\n"
"\n"
"QTabBar::tab:last:selected {\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"}\n"
"\n"
"QTabBar::tab:only-one {\n"
"\n"
"    margin: 0; /* if there is only one tab, we don't want overlapping margins */\n"
"}\n"
"\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.mplStylesheetCombo = QComboBox(self.frame_4)
        self.mplStylesheetCombo.setObjectName(u"mplStylesheetCombo")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplStylesheetCombo.sizePolicy().hasHeightForWidth())
        self.mplStylesheetCombo.setSizePolicy(sizePolicy)
        self.mplStylesheetCombo.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.mplStylesheetCombo)

        self.importNewMplstyleBtn = QPushButton(self.frame_4)
        self.importNewMplstyleBtn.setObjectName(u"importNewMplstyleBtn")
        icon1 = QIcon()
        icon1.addFile(u":/allIcons/icons/import.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.importNewMplstyleBtn.setIcon(icon1)
        self.importNewMplstyleBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.importNewMplstyleBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tabWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.importTab = QWidget()
        self.importTab.setObjectName(u"importTab")
        self.verticalLayout_7 = QVBoxLayout(self.importTab)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_8 = QFrame(self.importTab)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_11)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.frame_11)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.tsSourcePeer = QRadioButton(self.groupBox)
        self.tsSourcePeer.setObjectName(u"tsSourcePeer")

        self.verticalLayout_10.addWidget(self.tsSourcePeer)

        self.tsSourceCosmosvdc = QRadioButton(self.groupBox)
        self.tsSourceCosmosvdc.setObjectName(u"tsSourceCosmosvdc")

        self.verticalLayout_10.addWidget(self.tsSourceCosmosvdc)

        self.tsSourceRaw = QRadioButton(self.groupBox)
        self.tsSourceRaw.setObjectName(u"tsSourceRaw")

        self.verticalLayout_10.addWidget(self.tsSourceRaw)

        self.tsSourceCustom = QRadioButton(self.groupBox)
        self.tsSourceCustom.setObjectName(u"tsSourceCustom")

        self.verticalLayout_10.addWidget(self.tsSourceCustom)


        self.verticalLayout_9.addWidget(self.groupBox)


        self.horizontalLayout_2.addWidget(self.frame_11)

        self.frame_15 = QFrame(self.frame_8)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_15)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_12 = QFrame(self.frame_15)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.fileOpenBtn = QPushButton(self.frame_12)
        self.fileOpenBtn.setObjectName(u"fileOpenBtn")
        self.fileOpenBtn.setMinimumSize(QSize(80, 0))
        icon2 = QIcon()
        icon2.addFile(u":/allIcons/icons/opened_folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fileOpenBtn.setIcon(icon2)
        self.fileOpenBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.fileOpenBtn)

        self.sourcePath = QLineEdit(self.frame_12)
        self.sourcePath.setObjectName(u"sourcePath")
        self.sourcePath.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.sourcePath)


        self.verticalLayout_11.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_15)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_13)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 4, 1, 1)

        self.scaleFactorBox2 = QDoubleSpinBox(self.frame_13)
        self.scaleFactorBox2.setObjectName(u"scaleFactorBox2")
        self.scaleFactorBox2.setEnabled(False)
        sizePolicy.setHeightForWidth(self.scaleFactorBox2.sizePolicy().hasHeightForWidth())
        self.scaleFactorBox2.setSizePolicy(sizePolicy)
        self.scaleFactorBox2.setMinimumSize(QSize(80, 0))
        self.scaleFactorBox2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.scaleFactorBox2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.scaleFactorBox2.setDecimals(4)
        self.scaleFactorBox2.setMinimum(-99999999.000000000000000)
        self.scaleFactorBox2.setMaximum(99999999.000000000000000)
        self.scaleFactorBox2.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.scaleFactorBox2, 1, 2, 1, 1)

        self.scaleFactorBox3 = QDoubleSpinBox(self.frame_13)
        self.scaleFactorBox3.setObjectName(u"scaleFactorBox3")
        self.scaleFactorBox3.setEnabled(False)
        sizePolicy.setHeightForWidth(self.scaleFactorBox3.sizePolicy().hasHeightForWidth())
        self.scaleFactorBox3.setSizePolicy(sizePolicy)
        self.scaleFactorBox3.setMinimumSize(QSize(80, 0))
        self.scaleFactorBox3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.scaleFactorBox3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.scaleFactorBox3.setDecimals(4)
        self.scaleFactorBox3.setMinimum(-99999999.000000000000000)
        self.scaleFactorBox3.setMaximum(99999999.000000000000000)
        self.scaleFactorBox3.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.scaleFactorBox3, 1, 3, 1, 1)

        self.label_4 = QLabel(self.frame_13)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)

        self.scaleFactorBox1 = QDoubleSpinBox(self.frame_13)
        self.scaleFactorBox1.setObjectName(u"scaleFactorBox1")
        self.scaleFactorBox1.setEnabled(False)
        sizePolicy.setHeightForWidth(self.scaleFactorBox1.sizePolicy().hasHeightForWidth())
        self.scaleFactorBox1.setSizePolicy(sizePolicy)
        self.scaleFactorBox1.setMinimumSize(QSize(80, 0))
        self.scaleFactorBox1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.scaleFactorBox1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.scaleFactorBox1.setDecimals(4)
        self.scaleFactorBox1.setMinimum(-99999999.000000000000000)
        self.scaleFactorBox1.setMaximum(99999999.000000000000000)
        self.scaleFactorBox1.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.scaleFactorBox1, 1, 1, 1, 1)

        self.label_5 = QLabel(self.frame_13)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)

        self.label_3 = QLabel(self.frame_13)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_6 = QLabel(self.frame_13)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 3, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_13)

        self.frame_32 = QFrame(self.frame_15)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.frame_32)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 50))
        self.frame_33.setFrameShape(QFrame.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_33)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_10 = QLabel(self.frame_33)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_10, 1, 2, 1, 1)

        self.label_9 = QLabel(self.frame_33)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_9, 0, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 0, 6, 1, 1)

        self.label_8 = QLabel(self.frame_33)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 1)

        self.customLineStart = QSpinBox(self.frame_33)
        self.customLineStart.setObjectName(u"customLineStart")
        self.customLineStart.setEnabled(False)
        self.customLineStart.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.customLineStart.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.customLineStart.setMaximum(99999999)
        self.customLineStart.setValue(10)

        self.gridLayout_4.addWidget(self.customLineStart, 0, 1, 1, 1)

        self.label_7 = QLabel(self.frame_33)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)

        self.customLineEnd = QSpinBox(self.frame_33)
        self.customLineEnd.setObjectName(u"customLineEnd")
        self.customLineEnd.setEnabled(False)
        self.customLineEnd.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.customLineEnd.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.customLineEnd.setMinimum(-99999999)
        self.customLineEnd.setMaximum(99999999)
        self.customLineEnd.setValue(20)

        self.gridLayout_4.addWidget(self.customLineEnd, 1, 1, 1, 1)

        self.delimBox = QLineEdit(self.frame_33)
        self.delimBox.setObjectName(u"delimBox")
        self.delimBox.setEnabled(False)
        sizePolicy.setHeightForWidth(self.delimBox.sizePolicy().hasHeightForWidth())
        self.delimBox.setSizePolicy(sizePolicy)
        self.delimBox.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_4.addWidget(self.delimBox, 1, 3, 1, 1)

        self.tsDt = QDoubleSpinBox(self.frame_33)
        self.tsDt.setObjectName(u"tsDt")
        self.tsDt.setEnabled(False)
        sizePolicy.setHeightForWidth(self.tsDt.sizePolicy().hasHeightForWidth())
        self.tsDt.setSizePolicy(sizePolicy)
        self.tsDt.setMaximumSize(QSize(100, 16777215))
        self.tsDt.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tsDt.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.tsDt.setDecimals(4)
        self.tsDt.setMaximum(999999.000000000000000)
        self.tsDt.setValue(0.010000000000000)

        self.gridLayout_4.addWidget(self.tsDt, 0, 3, 1, 1)

        self.importBtn = QPushButton(self.frame_33)
        self.importBtn.setObjectName(u"importBtn")
        sizePolicy.setHeightForWidth(self.importBtn.sizePolicy().hasHeightForWidth())
        self.importBtn.setSizePolicy(sizePolicy)
        self.importBtn.setMinimumSize(QSize(120, 50))
        icon3 = QIcon()
        icon3.addFile(u":/allIcons/icons/ok.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.importBtn.setIcon(icon3)
        self.importBtn.setIconSize(QSize(32, 32))

        self.gridLayout_4.addWidget(self.importBtn, 0, 5, 2, 1)

        self.frame_6 = QFrame(self.frame_33)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(50, 0))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_6, 0, 4, 2, 1)


        self.horizontalLayout_15.addWidget(self.frame_33)


        self.verticalLayout_11.addWidget(self.frame_32)


        self.horizontalLayout_2.addWidget(self.frame_15)


        self.verticalLayout_7.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.importTab)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_9)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_11 = QLabel(self.frame_17)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_4.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_17)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_4.addWidget(self.label_12)


        self.verticalLayout_12.addWidget(self.frame_17)

        self.frame_16 = QFrame(self.frame_9)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.inputBrowser = QTextBrowser(self.frame_16)
        self.inputBrowser.setObjectName(u"inputBrowser")
        font = QFont()
        font.setFamilies([u"Monospace"])
        self.inputBrowser.setFont(font)

        self.horizontalLayout_5.addWidget(self.inputBrowser)

        self.frame_10 = QFrame(self.frame_16)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_5.addWidget(self.frame_10)

        self.outputBrowser = QTextBrowser(self.frame_16)
        self.outputBrowser.setObjectName(u"outputBrowser")
        self.outputBrowser.setFont(font)

        self.horizontalLayout_5.addWidget(self.outputBrowser)


        self.verticalLayout_12.addWidget(self.frame_16)


        self.verticalLayout_7.addWidget(self.frame_9)

        self.tabWidget.addTab(self.importTab, "")
        self.tsTab = QWidget()
        self.tsTab.setObjectName(u"tsTab")
        self.horizontalLayout_6 = QHBoxLayout(self.tsTab)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tWidget = QWidget(self.tsTab)
        self.tWidget.setObjectName(u"tWidget")

        self.horizontalLayout_6.addWidget(self.tWidget)

        self.frame = QFrame(self.tsTab)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 0))
        self.frame_19.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 6, -1, 0)
        self.label_23 = QLabel(self.frame_19)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.label_23)

        self.tsXminDspinBox = QDoubleSpinBox(self.frame_19)
        self.tsXminDspinBox.setObjectName(u"tsXminDspinBox")
        sizePolicy.setHeightForWidth(self.tsXminDspinBox.sizePolicy().hasHeightForWidth())
        self.tsXminDspinBox.setSizePolicy(sizePolicy)
        self.tsXminDspinBox.setMinimumSize(QSize(70, 0))
        self.tsXminDspinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tsXminDspinBox.setMaximum(9999999999.000000000000000)

        self.horizontalLayout_24.addWidget(self.tsXminDspinBox)

        self.label_24 = QLabel(self.frame_19)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.label_24)

        self.tsXmaxDspinBox = QDoubleSpinBox(self.frame_19)
        self.tsXmaxDspinBox.setObjectName(u"tsXmaxDspinBox")
        sizePolicy.setHeightForWidth(self.tsXmaxDspinBox.sizePolicy().hasHeightForWidth())
        self.tsXmaxDspinBox.setSizePolicy(sizePolicy)
        self.tsXmaxDspinBox.setMinimumSize(QSize(70, 0))
        self.tsXmaxDspinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tsXmaxDspinBox.setMinimum(-999999999.000000000000000)
        self.tsXmaxDspinBox.setMaximum(9999999999.000000000000000)
        self.tsXmaxDspinBox.setValue(-1.000000000000000)

        self.horizontalLayout_24.addWidget(self.tsXmaxDspinBox)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_10)

        self.horizontalLayout_24.setStretch(0, 1)
        self.horizontalLayout_24.setStretch(1, 1)
        self.horizontalLayout_24.setStretch(2, 1)
        self.horizontalLayout_24.setStretch(3, 1)
        self.horizontalLayout_24.setStretch(4, 5)

        self.verticalLayout_3.addWidget(self.frame_19)

        self.tsLayouts = QVBoxLayout()
        self.tsLayouts.setSpacing(0)
        self.tsLayouts.setObjectName(u"tsLayouts")
        self.frame_24 = QFrame(self.frame)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.tsLayout = QHBoxLayout()
        self.tsLayout.setSpacing(0)
        self.tsLayout.setObjectName(u"tsLayout")

        self.horizontalLayout_9.addLayout(self.tsLayout)


        self.tsLayouts.addWidget(self.frame_24)

        self.frame_26 = QFrame(self.frame)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.itsLayout = QHBoxLayout()
        self.itsLayout.setSpacing(0)
        self.itsLayout.setObjectName(u"itsLayout")

        self.horizontalLayout_10.addLayout(self.itsLayout)


        self.tsLayouts.addWidget(self.frame_26)

        self.frame_25 = QFrame(self.frame)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.iitsLayout = QHBoxLayout()
        self.iitsLayout.setSpacing(0)
        self.iitsLayout.setObjectName(u"iitsLayout")

        self.horizontalLayout_11.addLayout(self.iitsLayout)


        self.tsLayouts.addWidget(self.frame_25)

        self.tsLayouts.setStretch(0, 1)
        self.tsLayouts.setStretch(1, 1)
        self.tsLayouts.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.tsLayouts)


        self.horizontalLayout_6.addWidget(self.frame)

        self.frame_45 = QFrame(self.tsTab)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.NoFrame)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_45)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.tsPropsTableView = QTableView(self.frame_45)
        self.tsPropsTableView.setObjectName(u"tsPropsTableView")
        self.tsPropsTableView.setFont(font)
        self.tsPropsTableView.setAlternatingRowColors(True)

        self.verticalLayout_28.addWidget(self.tsPropsTableView)

        self.tsPropCopyBtn = QPushButton(self.frame_45)
        self.tsPropCopyBtn.setObjectName(u"tsPropCopyBtn")
        icon4 = QIcon()
        icon4.addFile(u":/allIcons/icons/data_sheet.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tsPropCopyBtn.setIcon(icon4)
        self.tsPropCopyBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_28.addWidget(self.tsPropCopyBtn)


        self.horizontalLayout_6.addWidget(self.frame_45)

        self.frame_2 = QFrame(self.tsTab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 100))
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_14)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.accTable = QTableView(self.frame_14)
        self.accTable.setObjectName(u"accTable")
        self.accTable.setFont(font)
        self.accTable.setWordWrap(False)

        self.verticalLayout_18.addWidget(self.accTable)

        self.tsToClipboardBtn = QPushButton(self.frame_14)
        self.tsToClipboardBtn.setObjectName(u"tsToClipboardBtn")
        self.tsToClipboardBtn.setMaximumSize(QSize(16777215, 16777215))
        self.tsToClipboardBtn.setIcon(icon4)
        self.tsToClipboardBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_18.addWidget(self.tsToClipboardBtn)


        self.verticalLayout_6.addWidget(self.frame_14)

        self.frame_34 = QFrame(self.frame_2)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(0, 100))
        self.frame_34.setFrameShape(QFrame.NoFrame)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_34)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.velTable = QTableView(self.frame_34)
        self.velTable.setObjectName(u"velTable")
        self.velTable.setFont(font)
        self.velTable.setWordWrap(False)

        self.verticalLayout_19.addWidget(self.velTable)

        self.itsToClipboardBtn = QPushButton(self.frame_34)
        self.itsToClipboardBtn.setObjectName(u"itsToClipboardBtn")
        self.itsToClipboardBtn.setMaximumSize(QSize(16777215, 16777215))
        self.itsToClipboardBtn.setIcon(icon4)
        self.itsToClipboardBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_19.addWidget(self.itsToClipboardBtn)


        self.verticalLayout_6.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.frame_2)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(0, 100))
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_35)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.dispTable = QTableView(self.frame_35)
        self.dispTable.setObjectName(u"dispTable")
        self.dispTable.setFont(font)
        self.dispTable.setWordWrap(False)

        self.verticalLayout_20.addWidget(self.dispTable)

        self.iitsToClipboardBtn = QPushButton(self.frame_35)
        self.iitsToClipboardBtn.setObjectName(u"iitsToClipboardBtn")
        self.iitsToClipboardBtn.setMaximumSize(QSize(16777215, 16777215))
        self.iitsToClipboardBtn.setIcon(icon4)
        self.iitsToClipboardBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_20.addWidget(self.iitsToClipboardBtn)


        self.verticalLayout_6.addWidget(self.frame_35)


        self.horizontalLayout_6.addWidget(self.frame_2)

        self.horizontalLayout_6.setStretch(1, 80)
        self.horizontalLayout_6.setStretch(2, 20)
        self.horizontalLayout_6.setStretch(3, 22)
        self.tabWidget.addTab(self.tsTab, "")
        self.rsTab = QWidget()
        self.rsTab.setObjectName(u"rsTab")
        self.verticalLayout_21 = QVBoxLayout(self.rsTab)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 6)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_36 = QFrame(self.rsTab)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_36)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.frame_36)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.NoFrame)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 6, 0, 0)
        self.rsLayout = QVBoxLayout()
        self.rsLayout.setObjectName(u"rsLayout")
        self.frame_18 = QFrame(self.frame_41)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy2)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.frame_18.setPalette(palette)
        self.frame_18.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_23.setSpacing(6)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(9, 6, 0, 0)
        self.label_22 = QLabel(self.frame_18)
        self.label_22.setObjectName(u"label_22")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy3)
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.label_22)

        self.rsComboBox = QComboBox(self.frame_18)
        self.rsComboBox.addItem("")
        self.rsComboBox.addItem("")
        self.rsComboBox.addItem("")
        self.rsComboBox.addItem("")
        self.rsComboBox.addItem("")
        self.rsComboBox.setObjectName(u"rsComboBox")
        sizePolicy.setHeightForWidth(self.rsComboBox.sizePolicy().hasHeightForWidth())
        self.rsComboBox.setSizePolicy(sizePolicy)
        self.rsComboBox.setMinimumSize(QSize(250, 0))
        self.rsComboBox.setStyleSheet(u"selection-background-color: rgb(0, 85, 255);")

        self.horizontalLayout_23.addWidget(self.rsComboBox)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_9)


        self.rsLayout.addWidget(self.frame_18)

        self.psaPlotLayout = QFrame(self.frame_41)
        self.psaPlotLayout.setObjectName(u"psaPlotLayout")
        self.psaPlotLayout.setFrameShape(QFrame.NoFrame)
        self.psaPlotLayout.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.psaPlotLayout)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.psaLayout = QVBoxLayout()
        self.psaLayout.setObjectName(u"psaLayout")

        self.verticalLayout_13.addLayout(self.psaLayout)


        self.rsLayout.addWidget(self.psaPlotLayout)


        self.horizontalLayout_18.addLayout(self.rsLayout)

        self.tripartiteLayout = QVBoxLayout()
        self.tripartiteLayout.setObjectName(u"tripartiteLayout")

        self.horizontalLayout_18.addLayout(self.tripartiteLayout)

        self.horizontalLayout_18.setStretch(0, 1)
        self.horizontalLayout_18.setStretch(1, 1)

        self.verticalLayout_26.addWidget(self.frame_41)


        self.horizontalLayout_14.addWidget(self.frame_36)


        self.verticalLayout_21.addLayout(self.horizontalLayout_14)

        self.frame_40 = QFrame(self.rsTab)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy2.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy2)
        self.frame_40.setFrameShape(QFrame.NoFrame)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(295, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_6)

        self.label_14 = QLabel(self.frame_40)
        self.label_14.setObjectName(u"label_14")
        font1 = QFont()
        font1.setBold(True)
        self.label_14.setFont(font1)

        self.horizontalLayout_21.addWidget(self.label_14)

        self.xiDoubleSpinBox = QDoubleSpinBox(self.frame_40)
        self.xiDoubleSpinBox.setObjectName(u"xiDoubleSpinBox")
        self.xiDoubleSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.xiDoubleSpinBox.setMinimum(0.010000000000000)
        self.xiDoubleSpinBox.setMaximum(100.000000000000000)
        self.xiDoubleSpinBox.setValue(5.000000000000000)

        self.horizontalLayout_21.addWidget(self.xiDoubleSpinBox)

        self.horizontalSpacer_7 = QSpacerItem(294, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_7)


        self.verticalLayout_21.addWidget(self.frame_40)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.rsTableView = QTableView(self.rsTab)
        self.rsTableView.setObjectName(u"rsTableView")
        self.rsTableView.setFont(font)

        self.horizontalLayout_16.addWidget(self.rsTableView)

        self.tableView = QTableView(self.rsTab)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setFont(font)

        self.horizontalLayout_16.addWidget(self.tableView)


        self.verticalLayout_21.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.frame_37 = QFrame(self.rsTab)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(0, 0))
        self.frame_37.setFrameShape(QFrame.NoFrame)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_19.setSpacing(6)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_39 = QFrame(self.frame_37)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.NoFrame)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_5)

        self.rsToClipboardBtn = QPushButton(self.frame_39)
        self.rsToClipboardBtn.setObjectName(u"rsToClipboardBtn")
        self.rsToClipboardBtn.setMaximumSize(QSize(16777215, 16777215))
        self.rsToClipboardBtn.setIcon(icon4)
        self.rsToClipboardBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_20.addWidget(self.rsToClipboardBtn)


        self.horizontalLayout_19.addWidget(self.frame_39)

        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.NoFrame)
        self.frame_38.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_19.addWidget(self.frame_38)

        self.horizontalLayout_19.setStretch(0, 1)
        self.horizontalLayout_19.setStretch(1, 1)

        self.horizontalLayout_17.addWidget(self.frame_37)


        self.verticalLayout_21.addLayout(self.horizontalLayout_17)

        self.verticalLayout_21.setStretch(0, 3)
        self.verticalLayout_21.setStretch(2, 1)
        self.tabWidget.addTab(self.rsTab, "")
        self.fsTab = QWidget()
        self.fsTab.setObjectName(u"fsTab")
        self.horizontalLayout_7 = QHBoxLayout(self.fsTab)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.frame_7 = QFrame(self.fsTab)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_7)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_42 = QFrame(self.frame_7)
        self.frame_42.setObjectName(u"frame_42")
        sizePolicy2.setHeightForWidth(self.frame_42.sizePolicy().hasHeightForWidth())
        self.frame_42.setSizePolicy(sizePolicy2)
        self.frame_42.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamilies([u"Sans Serif"])
        self.frame_42.setFont(font2)
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_42)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 6, -1, 3)
        self.windowSizeSpinBox = QSpinBox(self.frame_42)
        self.windowSizeSpinBox.setObjectName(u"windowSizeSpinBox")
        self.windowSizeSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.windowSizeSpinBox.setMaximum(99999999)
        self.windowSizeSpinBox.setValue(50)

        self.gridLayout_3.addWidget(self.windowSizeSpinBox, 1, 3, 1, 1)

        self.label_17 = QLabel(self.frame_42)
        self.label_17.setObjectName(u"label_17")
        sizePolicy2.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.label_17, 0, 4, 1, 1)

        self.label_15 = QLabel(self.frame_42)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.label_15, 0, 2, 1, 1)

        self.polyDegSpinBox = QSpinBox(self.frame_42)
        self.polyDegSpinBox.setObjectName(u"polyDegSpinBox")
        self.polyDegSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.polyDegSpinBox.setMaximum(10)
        self.polyDegSpinBox.setValue(2)

        self.gridLayout_3.addWidget(self.polyDegSpinBox, 1, 4, 1, 1)

        self.lowPassFiltComboBox = QComboBox(self.frame_42)
        self.lowPassFiltComboBox.setObjectName(u"lowPassFiltComboBox")

        self.gridLayout_3.addWidget(self.lowPassFiltComboBox, 1, 2, 1, 1)

        self.frame_3 = QFrame(self.frame_42)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_19 = QLabel(self.frame_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_19, 0, 0, 1, 1)

        self.periodFreqComboBox = QComboBox(self.frame_3)
        self.periodFreqComboBox.addItem("")
        self.periodFreqComboBox.addItem("")
        self.periodFreqComboBox.setObjectName(u"periodFreqComboBox")
        sizePolicy.setHeightForWidth(self.periodFreqComboBox.sizePolicy().hasHeightForWidth())
        self.periodFreqComboBox.setSizePolicy(sizePolicy)
        self.periodFreqComboBox.setMinimumSize(QSize(150, 0))

        self.gridLayout_5.addWidget(self.periodFreqComboBox, 0, 1, 1, 3)

        self.label_21 = QLabel(self.frame_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_21, 1, 0, 1, 1)

        self.fsXminDSpinBox = QDoubleSpinBox(self.frame_3)
        self.fsXminDSpinBox.setObjectName(u"fsXminDSpinBox")
        sizePolicy.setHeightForWidth(self.fsXminDSpinBox.sizePolicy().hasHeightForWidth())
        self.fsXminDSpinBox.setSizePolicy(sizePolicy)
        self.fsXminDSpinBox.setMinimumSize(QSize(50, 0))
        self.fsXminDSpinBox.setMaximumSize(QSize(80, 16777215))
        self.fsXminDSpinBox.setMaximum(1000.000000000000000)

        self.gridLayout_5.addWidget(self.fsXminDSpinBox, 1, 1, 1, 1)

        self.fsXmaxDSpinBox = QDoubleSpinBox(self.frame_3)
        self.fsXmaxDSpinBox.setObjectName(u"fsXmaxDSpinBox")
        sizePolicy.setHeightForWidth(self.fsXmaxDSpinBox.sizePolicy().hasHeightForWidth())
        self.fsXmaxDSpinBox.setSizePolicy(sizePolicy)
        self.fsXmaxDSpinBox.setMinimumSize(QSize(50, 0))
        self.fsXmaxDSpinBox.setMaximumSize(QSize(80, 16777215))
        self.fsXmaxDSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.fsXmaxDSpinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.fsXmaxDSpinBox.setMinimum(-9999999999.000000000000000)
        self.fsXmaxDSpinBox.setMaximum(1000.000000000000000)
        self.fsXmaxDSpinBox.setValue(-1.000000000000000)

        self.gridLayout_5.addWidget(self.fsXmaxDSpinBox, 1, 3, 1, 1)

        self.label_20 = QLabel(self.frame_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_20, 1, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_8, 0, 4, 2, 1)


        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 2, 1)

        self.label_16 = QLabel(self.frame_42)
        self.label_16.setObjectName(u"label_16")
        sizePolicy2.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.label_16, 0, 3, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 3)

        self.verticalLayout_17.addWidget(self.frame_42)

        self.frame_22 = QFrame(self.frame_7)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.frame_22)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_27)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.fsAmpLayout = QVBoxLayout()
        self.fsAmpLayout.setSpacing(0)
        self.fsAmpLayout.setObjectName(u"fsAmpLayout")

        self.verticalLayout_22.addLayout(self.fsAmpLayout)


        self.horizontalLayout_8.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_22)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_28)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.psAmpLayout = QVBoxLayout()
        self.psAmpLayout.setSpacing(0)
        self.psAmpLayout.setObjectName(u"psAmpLayout")

        self.verticalLayout_23.addLayout(self.psAmpLayout)


        self.horizontalLayout_8.addWidget(self.frame_28)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)

        self.verticalLayout_17.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.frame_7)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.frame_23)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_29)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.fsPhaseLayout = QVBoxLayout()
        self.fsPhaseLayout.setSpacing(0)
        self.fsPhaseLayout.setObjectName(u"fsPhaseLayout")

        self.verticalLayout_24.addLayout(self.fsPhaseLayout)


        self.horizontalLayout_13.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_23)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_30)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.fsUnwrappedPhaseLayout = QVBoxLayout()
        self.fsUnwrappedPhaseLayout.setSpacing(0)
        self.fsUnwrappedPhaseLayout.setObjectName(u"fsUnwrappedPhaseLayout")

        self.verticalLayout_25.addLayout(self.fsUnwrappedPhaseLayout)


        self.horizontalLayout_13.addWidget(self.frame_30)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 1)

        self.verticalLayout_17.addWidget(self.frame_23)

        self.verticalLayout_17.setStretch(1, 1)
        self.verticalLayout_17.setStretch(2, 1)

        self.horizontalLayout_7.addWidget(self.frame_7)

        self.frame_21 = QFrame(self.fsTab)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_21)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_43 = QFrame(self.frame_21)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(0, 100))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_43)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 6)
        self.freqCharTableView = QTableView(self.frame_43)
        self.freqCharTableView.setObjectName(u"freqCharTableView")
        font3 = QFont()
        font3.setFamilies([u"Monospace"])
        font3.setUnderline(False)
        self.freqCharTableView.setFont(font3)

        self.verticalLayout_27.addWidget(self.freqCharTableView)

        self.freqCharCopyBtn = QPushButton(self.frame_43)
        self.freqCharCopyBtn.setObjectName(u"freqCharCopyBtn")
        self.freqCharCopyBtn.setIcon(icon4)
        self.freqCharCopyBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_27.addWidget(self.freqCharCopyBtn)


        self.verticalLayout_16.addWidget(self.frame_43)

        self.fsTableView = QTableView(self.frame_21)
        self.fsTableView.setObjectName(u"fsTableView")
        self.fsTableView.setFont(font)

        self.verticalLayout_16.addWidget(self.fsTableView)

        self.fsToClipboardBtn = QPushButton(self.frame_21)
        self.fsToClipboardBtn.setObjectName(u"fsToClipboardBtn")
        self.fsToClipboardBtn.setMaximumSize(QSize(16777215, 16777215))
        self.fsToClipboardBtn.setIcon(icon4)
        self.fsToClipboardBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_16.addWidget(self.fsToClipboardBtn)


        self.horizontalLayout_7.addWidget(self.frame_21)

        self.horizontalLayout_7.setStretch(0, 4)
        self.horizontalLayout_7.setStretch(1, 1)
        self.tabWidget.addTab(self.fsTab, "")
        self.gmScaling = QWidget()
        self.gmScaling.setObjectName(u"gmScaling")
        self.verticalLayout_5 = QVBoxLayout(self.gmScaling)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 6, 0, 0)
        self.frame_20 = QFrame(self.gmScaling)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_50 = QFrame(self.frame_20)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.NoFrame)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_50)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_26 = QLabel(self.frame_50)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_29.addWidget(self.label_26)

        self.designSpecView = QTableView(self.frame_50)
        self.designSpecView.setObjectName(u"designSpecView")

        self.verticalLayout_29.addWidget(self.designSpecView)

        self.scalingImportBtn = QPushButton(self.frame_50)
        self.scalingImportBtn.setObjectName(u"scalingImportBtn")
        self.scalingImportBtn.setMinimumSize(QSize(0, 50))
        icon5 = QIcon()
        icon5.addFile(u":/allIcons/icons/rules.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.scalingImportBtn.setIcon(icon5)
        self.scalingImportBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_29.addWidget(self.scalingImportBtn)


        self.horizontalLayout_25.addWidget(self.frame_50)

        self.frame_46 = QFrame(self.frame_20)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.NoFrame)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_46)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.frame_46)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.NoFrame)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.scalingSpecPlotLayout = QVBoxLayout()
        self.scalingSpecPlotLayout.setObjectName(u"scalingSpecPlotLayout")

        self.horizontalLayout_27.addLayout(self.scalingSpecPlotLayout)


        self.verticalLayout_14.addWidget(self.frame_47)

        self.frame_48 = QFrame(self.frame_46)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.NoFrame)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_48)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.scalingXiDSpinBox = QDoubleSpinBox(self.frame_48)
        self.scalingXiDSpinBox.setObjectName(u"scalingXiDSpinBox")
        self.scalingXiDSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.scalingXiDSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.scalingXiDSpinBox.setMinimum(0.100000000000000)
        self.scalingXiDSpinBox.setMaximum(100.000000000000000)
        self.scalingXiDSpinBox.setValue(5.000000000000000)

        self.gridLayout_6.addWidget(self.scalingXiDSpinBox, 1, 1, 1, 1)

        self.label_29 = QLabel(self.frame_48)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_29, 2, 0, 1, 1)

        self.scalingComputeBtn = QPushButton(self.frame_48)
        self.scalingComputeBtn.setObjectName(u"scalingComputeBtn")
        icon6 = QIcon()
        icon6.addFile(u":/allIcons/icons/calculator.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.scalingComputeBtn.setIcon(icon6)
        self.scalingComputeBtn.setIconSize(QSize(32, 32))

        self.gridLayout_6.addWidget(self.scalingComputeBtn, 3, 1, 1, 1)

        self.scalingMethodcomboBox = QComboBox(self.frame_48)
        self.scalingMethodcomboBox.addItem("")
        self.scalingMethodcomboBox.setObjectName(u"scalingMethodcomboBox")

        self.gridLayout_6.addWidget(self.scalingMethodcomboBox, 0, 1, 1, 1)

        self.scalingPeriodDSpinBox = QDoubleSpinBox(self.frame_48)
        self.scalingPeriodDSpinBox.setObjectName(u"scalingPeriodDSpinBox")
        self.scalingPeriodDSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.scalingPeriodDSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.scalingPeriodDSpinBox.setDecimals(4)
        self.scalingPeriodDSpinBox.setMinimum(0.001000000000000)
        self.scalingPeriodDSpinBox.setValue(1.000000000000000)

        self.gridLayout_6.addWidget(self.scalingPeriodDSpinBox, 2, 1, 1, 1)

        self.label_28 = QLabel(self.frame_48)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_28, 1, 0, 1, 1)

        self.label_27 = QLabel(self.frame_48)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFrameShape(QFrame.NoFrame)
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_27, 0, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_11, 0, 2, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_48)


        self.horizontalLayout_25.addWidget(self.frame_46)

        self.frame_49 = QFrame(self.frame_20)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.NoFrame)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_49)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_30 = QLabel(self.frame_49)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_15.addWidget(self.label_30)

        self.scaledGMView = QTableView(self.frame_49)
        self.scaledGMView.setObjectName(u"scaledGMView")

        self.verticalLayout_15.addWidget(self.scaledGMView)

        self.scaledGMCopyToClipboardBtn = QPushButton(self.frame_49)
        self.scaledGMCopyToClipboardBtn.setObjectName(u"scaledGMCopyToClipboardBtn")
        self.scaledGMCopyToClipboardBtn.setIcon(icon4)
        self.scaledGMCopyToClipboardBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_15.addWidget(self.scaledGMCopyToClipboardBtn)

        self.scaledGMAddToListBtn = QPushButton(self.frame_49)
        self.scaledGMAddToListBtn.setObjectName(u"scaledGMAddToListBtn")
        icon7 = QIcon()
        icon7.addFile(u":/allIcons/icons/add_database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.scaledGMAddToListBtn.setIcon(icon7)
        self.scaledGMAddToListBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_15.addWidget(self.scaledGMAddToListBtn)


        self.horizontalLayout_25.addWidget(self.frame_49)

        self.horizontalLayout_25.setStretch(0, 1)
        self.horizontalLayout_25.setStretch(1, 3)
        self.horizontalLayout_25.setStretch(2, 1)

        self.verticalLayout_5.addWidget(self.frame_20)

        self.tabWidget.addTab(self.gmScaling, "")
        self.gmStretching = QWidget()
        self.gmStretching.setObjectName(u"gmStretching")
        self.verticalLayout_30 = QVBoxLayout(self.gmStretching)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_52 = QFrame(self.gmStretching)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.NoFrame)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_54 = QFrame(self.frame_52)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.NoFrame)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_54)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_58 = QFrame(self.frame_54)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.NoFrame)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.stretchingTsLayout = QVBoxLayout()
        self.stretchingTsLayout.setObjectName(u"stretchingTsLayout")

        self.horizontalLayout_32.addLayout(self.stretchingTsLayout)


        self.verticalLayout_31.addWidget(self.frame_58)

        self.frame_59 = QFrame(self.frame_54)
        self.frame_59.setObjectName(u"frame_59")
        sizePolicy2.setHeightForWidth(self.frame_59.sizePolicy().hasHeightForWidth())
        self.frame_59.setSizePolicy(sizePolicy2)
        self.frame_59.setFrameShape(QFrame.NoFrame)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_12)

        self.label_31 = QLabel(self.frame_59)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_33.addWidget(self.label_31)

        self.stretchingFactorDSpinBox = QDoubleSpinBox(self.frame_59)
        self.stretchingFactorDSpinBox.setObjectName(u"stretchingFactorDSpinBox")
        self.stretchingFactorDSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.stretchingFactorDSpinBox.setMaximum(99999999.000000000000000)
        self.stretchingFactorDSpinBox.setValue(2.000000000000000)

        self.horizontalLayout_33.addWidget(self.stretchingFactorDSpinBox)

        self.stretchingComputeBtn = QPushButton(self.frame_59)
        self.stretchingComputeBtn.setObjectName(u"stretchingComputeBtn")
        self.stretchingComputeBtn.setIcon(icon6)
        self.stretchingComputeBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_33.addWidget(self.stretchingComputeBtn)


        self.verticalLayout_31.addWidget(self.frame_59)

        self.verticalLayout_31.setStretch(0, 3)
        self.verticalLayout_31.setStretch(1, 1)

        self.horizontalLayout_28.addWidget(self.frame_54)

        self.frame_55 = QFrame(self.frame_52)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.NoFrame)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_55)
        self.verticalLayout_32.setSpacing(3)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.stretchingTsView = QTableView(self.frame_55)
        self.stretchingTsView.setObjectName(u"stretchingTsView")

        self.verticalLayout_32.addWidget(self.stretchingTsView)

        self.stretchingCopyToClipboardBtn = QPushButton(self.frame_55)
        self.stretchingCopyToClipboardBtn.setObjectName(u"stretchingCopyToClipboardBtn")
        self.stretchingCopyToClipboardBtn.setIcon(icon4)
        self.stretchingCopyToClipboardBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_32.addWidget(self.stretchingCopyToClipboardBtn)

        self.stretchingAddToListBtn = QPushButton(self.frame_55)
        self.stretchingAddToListBtn.setObjectName(u"stretchingAddToListBtn")
        self.stretchingAddToListBtn.setIcon(icon7)
        self.stretchingAddToListBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_32.addWidget(self.stretchingAddToListBtn)


        self.horizontalLayout_28.addWidget(self.frame_55)

        self.horizontalLayout_28.setStretch(0, 2)
        self.horizontalLayout_28.setStretch(1, 1)

        self.verticalLayout_30.addWidget(self.frame_52)

        self.frame_53 = QFrame(self.gmStretching)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.NoFrame)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_56 = QFrame(self.frame_53)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.NoFrame)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.stretchingRsLayout = QVBoxLayout()
        self.stretchingRsLayout.setObjectName(u"stretchingRsLayout")

        self.horizontalLayout_30.addLayout(self.stretchingRsLayout)


        self.horizontalLayout_29.addWidget(self.frame_56)

        self.frame_57 = QFrame(self.frame_53)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.NoFrame)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.stretchingFsLayout = QVBoxLayout()
        self.stretchingFsLayout.setObjectName(u"stretchingFsLayout")

        self.horizontalLayout_31.addLayout(self.stretchingFsLayout)


        self.horizontalLayout_29.addWidget(self.frame_57)


        self.verticalLayout_30.addWidget(self.frame_53)

        self.verticalLayout_30.setStretch(0, 1)
        self.verticalLayout_30.setStretch(1, 1)
        self.tabWidget.addTab(self.gmStretching, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(Qt.BottomDockWidgetArea|Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.frame_5 = QFrame(self.dockWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_44 = QFrame(self.frame_5)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.NoFrame)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_18 = QLabel(self.frame_44)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(105, 65))
        self.label_18.setMaximumSize(QSize(105, 65))
        self.label_18.setPixmap(QPixmap(u":/logo/logo.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_18)


        self.verticalLayout_2.addWidget(self.frame_44)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_2)

        self.frame_51 = QFrame(self.frame_5)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(0, 0))
        self.frame_51.setFrameShape(QFrame.NoFrame)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.frame_51)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_26.addWidget(self.label_25)

        self.baseCorrComboBox = QComboBox(self.frame_51)
        self.baseCorrComboBox.addItem("")
        self.baseCorrComboBox.addItem("")
        self.baseCorrComboBox.addItem("")
        self.baseCorrComboBox.addItem("")
        self.baseCorrComboBox.addItem("")
        self.baseCorrComboBox.setObjectName(u"baseCorrComboBox")
        sizePolicy.setHeightForWidth(self.baseCorrComboBox.sizePolicy().hasHeightForWidth())
        self.baseCorrComboBox.setSizePolicy(sizePolicy)
        self.baseCorrComboBox.setMinimumSize(QSize(150, 0))
        self.baseCorrComboBox.setStyleSheet(u"selection-background-color: rgb(0, 85, 255);")

        self.horizontalLayout_26.addWidget(self.baseCorrComboBox)


        self.verticalLayout_2.addWidget(self.frame_51)

        self.tsListView = QListView(self.frame_5)
        self.tsListView.setObjectName(u"tsListView")
        self.tsListView.setStyleSheet(u"")
        self.tsListView.setFrameShadow(QFrame.Sunken)
        self.tsListView.setLineWidth(1)
        self.tsListView.setEditTriggers(QAbstractItemView.CurrentChanged|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.tsListView.setAlternatingRowColors(True)
        self.tsListView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tsListView.setSpacing(1)
        self.tsListView.setViewMode(QListView.ListMode)

        self.verticalLayout_2.addWidget(self.tsListView)

        self.frame_31 = QFrame(self.frame_5)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)

        self.remTsBtn = QPushButton(self.frame_31)
        self.remTsBtn.setObjectName(u"remTsBtn")
        sizePolicy2.setHeightForWidth(self.remTsBtn.sizePolicy().hasHeightForWidth())
        self.remTsBtn.setSizePolicy(sizePolicy2)
        self.remTsBtn.setMaximumSize(QSize(150, 16777215))
        icon8 = QIcon()
        icon8.addFile(u":/allIcons/icons/delete_database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.remTsBtn.setIcon(icon8)
        self.remTsBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_12.addWidget(self.remTsBtn)


        self.verticalLayout_2.addWidget(self.frame_31)

        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_13)

        self.metaTableView = QTableView(self.frame_5)
        self.metaTableView.setObjectName(u"metaTableView")
        self.metaTableView.setFrameShape(QFrame.StyledPanel)
        self.metaTableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.metaTableView.setAlternatingRowColors(True)
        self.metaTableView.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.metaTableView)


        self.verticalLayout.addWidget(self.frame_5)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        QWidget.setTabOrder(self.mplStylesheetCombo, self.importNewMplstyleBtn)
        QWidget.setTabOrder(self.importNewMplstyleBtn, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.tsSourcePeer)
        QWidget.setTabOrder(self.tsSourcePeer, self.tsSourceCosmosvdc)
        QWidget.setTabOrder(self.tsSourceCosmosvdc, self.tsSourceRaw)
        QWidget.setTabOrder(self.tsSourceRaw, self.tsSourceCustom)
        QWidget.setTabOrder(self.tsSourceCustom, self.fileOpenBtn)
        QWidget.setTabOrder(self.fileOpenBtn, self.sourcePath)
        QWidget.setTabOrder(self.sourcePath, self.scaleFactorBox1)
        QWidget.setTabOrder(self.scaleFactorBox1, self.scaleFactorBox2)
        QWidget.setTabOrder(self.scaleFactorBox2, self.scaleFactorBox3)
        QWidget.setTabOrder(self.scaleFactorBox3, self.customLineStart)
        QWidget.setTabOrder(self.customLineStart, self.customLineEnd)
        QWidget.setTabOrder(self.customLineEnd, self.tsDt)
        QWidget.setTabOrder(self.tsDt, self.delimBox)
        QWidget.setTabOrder(self.delimBox, self.importBtn)
        QWidget.setTabOrder(self.importBtn, self.tsListView)
        QWidget.setTabOrder(self.tsListView, self.metaTableView)
        QWidget.setTabOrder(self.metaTableView, self.remTsBtn)
        QWidget.setTabOrder(self.remTsBtn, self.tsXminDspinBox)
        QWidget.setTabOrder(self.tsXminDspinBox, self.tsXmaxDspinBox)
        QWidget.setTabOrder(self.tsXmaxDspinBox, self.tsPropCopyBtn)
        QWidget.setTabOrder(self.tsPropCopyBtn, self.tsToClipboardBtn)
        QWidget.setTabOrder(self.tsToClipboardBtn, self.itsToClipboardBtn)
        QWidget.setTabOrder(self.itsToClipboardBtn, self.iitsToClipboardBtn)
        QWidget.setTabOrder(self.iitsToClipboardBtn, self.rsComboBox)
        QWidget.setTabOrder(self.rsComboBox, self.xiDoubleSpinBox)
        QWidget.setTabOrder(self.xiDoubleSpinBox, self.rsToClipboardBtn)
        QWidget.setTabOrder(self.rsToClipboardBtn, self.periodFreqComboBox)
        QWidget.setTabOrder(self.periodFreqComboBox, self.fsXminDSpinBox)
        QWidget.setTabOrder(self.fsXminDSpinBox, self.fsXmaxDSpinBox)
        QWidget.setTabOrder(self.fsXmaxDSpinBox, self.lowPassFiltComboBox)
        QWidget.setTabOrder(self.lowPassFiltComboBox, self.windowSizeSpinBox)
        QWidget.setTabOrder(self.windowSizeSpinBox, self.polyDegSpinBox)
        QWidget.setTabOrder(self.polyDegSpinBox, self.freqCharCopyBtn)
        QWidget.setTabOrder(self.freqCharCopyBtn, self.fsToClipboardBtn)
        QWidget.setTabOrder(self.fsToClipboardBtn, self.scalingImportBtn)
        QWidget.setTabOrder(self.scalingImportBtn, self.scalingMethodcomboBox)
        QWidget.setTabOrder(self.scalingMethodcomboBox, self.scalingXiDSpinBox)
        QWidget.setTabOrder(self.scalingXiDSpinBox, self.scalingPeriodDSpinBox)
        QWidget.setTabOrder(self.scalingPeriodDSpinBox, self.scalingComputeBtn)
        QWidget.setTabOrder(self.scalingComputeBtn, self.scaledGMCopyToClipboardBtn)
        QWidget.setTabOrder(self.scaledGMCopyToClipboardBtn, self.scaledGMAddToListBtn)
        QWidget.setTabOrder(self.scaledGMAddToListBtn, self.designSpecView)
        QWidget.setTabOrder(self.designSpecView, self.accTable)
        QWidget.setTabOrder(self.accTable, self.dispTable)
        QWidget.setTabOrder(self.dispTable, self.rsTableView)
        QWidget.setTabOrder(self.rsTableView, self.freqCharTableView)
        QWidget.setTabOrder(self.freqCharTableView, self.velTable)
        QWidget.setTabOrder(self.velTable, self.scaledGMView)
        QWidget.setTabOrder(self.scaledGMView, self.fsTableView)
        QWidget.setTabOrder(self.fsTableView, self.tableView)
        QWidget.setTabOrder(self.tableView, self.inputBrowser)
        QWidget.setTabOrder(self.inputBrowser, self.outputBrowser)
        QWidget.setTabOrder(self.outputBrowser, self.tsPropsTableView)

        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PEGMA: Package for Exploratory Ground Motion Analysis", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Plot styles", None))
#if QT_CONFIG(tooltip)
        self.importNewMplstyleBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Import new matplotlib style file from disk.", None))
#endif // QT_CONFIG(tooltip)
        self.importNewMplstyleBtn.setText(QCoreApplication.translate("MainWindow", u"Import new\n"
"plot style", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Source", None))
        self.tsSourcePeer.setText(QCoreApplication.translate("MainWindow", u"PeerNGA", None))
        self.tsSourceCosmosvdc.setText(QCoreApplication.translate("MainWindow", u"CosmosVDC", None))
        self.tsSourceRaw.setText(QCoreApplication.translate("MainWindow", u"Raw (Two columns)", None))
        self.tsSourceCustom.setText(QCoreApplication.translate("MainWindow", u"Custom", None))
        self.fileOpenBtn.setText("")
        self.sourcePath.setInputMask("")
        self.sourcePath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Path to the source file(s)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Acceleration", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Velocity", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Scale factors:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Displacement", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Delimiter: ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"dt (s): ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"End:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Start:", None))
        self.delimBox.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.importBtn.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.importTab), QCoreApplication.translate("MainWindow", u"Import", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Xmin", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Xmax", None))
        self.tsPropCopyBtn.setText(QCoreApplication.translate("MainWindow", u"Copy to clipboard", None))
        self.tsToClipboardBtn.setText(QCoreApplication.translate("MainWindow", u"Copy to clipboard", None))
        self.itsToClipboardBtn.setText(QCoreApplication.translate("MainWindow", u"Copy to clipboard", None))
        self.iitsToClipboardBtn.setText(QCoreApplication.translate("MainWindow", u"Copy to clipboard", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tsTab), QCoreApplication.translate("MainWindow", u"Time history", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Y-axis:", None))
        self.rsComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Pseudo-spectral acceleration (PSa)", None))
        self.rsComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Pseudo-spectral velocity (PSv)", None))
        self.rsComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Spectral displacement (Sd)", None))
        self.rsComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Spectral velocity (Sv)", None))
        self.rsComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Spectral acceleration (Sa)", None))

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Damping coefficient \u03be (in %): ", None))
        self.rsToClipboardBtn.setText(QCoreApplication.translate("MainWindow", u"Copy to clipboard", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rsTab), QCoreApplication.translate("MainWindow", u"Response Spectra", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Polynomial\n"
"degree", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Spectral\n"
"smoothing", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"X-axis", None))
        self.periodFreqComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Frequency (Hz)", None))
        self.periodFreqComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Period (s)", None))

        self.label_21.setText(QCoreApplication.translate("MainWindow", u"X-min", None))
#if QT_CONFIG(tooltip)
        self.fsXmaxDSpinBox.setToolTip(QCoreApplication.translate("MainWindow", u"Negative value sets the limit based on data.", None))
#endif // QT_CONFIG(tooltip)
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"X-max", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Window size", None))
        self.freqCharCopyBtn.setText(QCoreApplication.translate("MainWindow", u"Copy to clipboard", None))
        self.fsToClipboardBtn.setText(QCoreApplication.translate("MainWindow", u"Copy to clipboard", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fsTab), QCoreApplication.translate("MainWindow", u"Fourier Spectra", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Design spectrum", None))
#if QT_CONFIG(tooltip)
        self.scalingImportBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Requires comma separated values in two columns", None))
#endif // QT_CONFIG(tooltip)
        self.scalingImportBtn.setText(QCoreApplication.translate("MainWindow", u"Import\n"
"(two columns)", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"At period (s)", None))
        self.scalingComputeBtn.setText(QCoreApplication.translate("MainWindow", u"Compute >>", None))
        self.scalingMethodcomboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Sa(T1)", None))

        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Damping coefficient \u03be (in %): ", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Scaling method", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Scaled ground motion", None))
        self.scaledGMCopyToClipboardBtn.setText(QCoreApplication.translate("MainWindow", u"Copy to clipboard", None))
        self.scaledGMAddToListBtn.setText(QCoreApplication.translate("MainWindow", u"Add to list", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gmScaling), QCoreApplication.translate("MainWindow", u"GM Scaling", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Stretch factor", None))
        self.stretchingComputeBtn.setText(QCoreApplication.translate("MainWindow", u"Compute >>", None))
        self.stretchingCopyToClipboardBtn.setText(QCoreApplication.translate("MainWindow", u"Copy to clipboard", None))
        self.stretchingAddToListBtn.setText(QCoreApplication.translate("MainWindow", u"Add to list", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gmStretching), QCoreApplication.translate("MainWindow", u"GM Stretching", None))
        self.dockWidget.setWindowTitle("")
        self.label_18.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Time-histories", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Baseline correction", None))
        self.baseCorrComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.baseCorrComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Constant", None))
        self.baseCorrComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Linear", None))
        self.baseCorrComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Quadratic", None))
        self.baseCorrComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Cubic", None))

        self.remTsBtn.setText(QCoreApplication.translate("MainWindow", u"Remove\n"
"Time history", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Time history metadata", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

