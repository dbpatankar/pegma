################################################################################
## PEGMA
## Copyright (C) 2023  Digvijay Patankar
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <https://www.gnu.org/licenses/>.
################################################################################

import sys
import os
import shutil
from pathlib import Path
import scipy.signal
import numpy as np
import earthquakepy as ep
import copy

# PySide imports
from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox, QSizePolicy, QWidget, QHeaderView
from PySide6 import QtGui
from PySide6.QtGui import QAccessible, QAction, QIcon, QPixmap
from PySide6.QtCore import QModelIndex, QItemSelectionModel, Qt

import matplotlib as mpl
mpl.use('QtAgg', force=True)
from matplotlib import colors
import pickle

from . import AppClasses
from . import UiClasses
from . import ui
# from AppClasses import *
# from UiClasses import *
# from ui.ui_mainwindow import *
from . import HelpSystem   # import HelpBrowser
from . import plotConfig    # import plotConfigFiles, pegmaConfigDir
import configparser

# import asyncio



# My app class
class App(ui.ui_mainwindow.Ui_MainWindow):

    def __init__(self, window, dataDict) -> None:
        self.setupUi(window)
        self.clipboard = QApplication.clipboard()
        self.setup_toolbar()
        self.data = dataDict["data"]
        self.plotConfigFiles = dataDict["plotConfigFiles"]
        self.update_data()
        
        # Connect signals
        self.tsListView.clicked.connect(self.update_data)
        self.remTsBtn.clicked.connect(self.remove_timeseries_from_data)
        self.importNewMplstyleBtn.clicked.connect(self.import_new_mplstyle)

        # Import tab
        self.sourceChecked = 0
        self.tsSourcePeer.clicked.connect(self.make_peer_options_visible)
        self.tsSourceCosmosvdc.clicked.connect(
            self.make_cosmosvdc_options_visible)
        self.tsSourceRaw.clicked.connect(self.make_raw_options_visible)
        self.tsSourceCustom.clicked.connect(self.make_custom_options_visible)
        self.fileOpenBtn.clicked.connect(self.file_opener)
        self.sourcePath.editingFinished.connect(self.update_input_output_browser)
        self.sourcePath.textChanged.connect(self.update_input_output_browser)
        self.scaleFactorBox1.valueChanged.connect(self.update_output_browser)
        self.scaleFactorBox2.valueChanged.connect(self.update_output_browser)
        self.scaleFactorBox3.valueChanged.connect(self.update_output_browser)
        self.customLineStart.valueChanged.connect(self.update_output_browser)
        self.customLineEnd.valueChanged.connect(self.update_output_browser)
        self.tsDt.valueChanged.connect(self.update_output_browser)
        self.delimBox.textChanged.connect(self.update_output_browser)
        self.importBtn.clicked.connect(self.add_ts_to_data)

        # Timeseries tab
        # self.baseCorrComboBox.textActivated.connect(self.apply_baseline_correction)
        self.tsXminDspinBox.editingFinished.connect(self.update_timeseries_plots)
        self.tsXmaxDspinBox.editingFinished.connect(self.update_timeseries_plots)

        # Fourier spectra tab
        self.lowPassFiltComboBox.addItems(["Savgol"])
        self.periodFreqComboBox.currentTextChanged.connect(self.update_fs_plots)
        self.fsXmaxDSpinBox.editingFinished.connect(self.update_fs_plots)
        self.fsXminDSpinBox.editingFinished.connect(self.update_fs_plots)

        # Response spectra tab
        self.rsComboBox.currentTextChanged.connect(self.update_rs_plot)
        self.xiDoubleSpinBox.editingFinished.connect(self.update_response_spectra)

        # Scaling tab
        self.scalingImportBtn.clicked.connect(self.import_design_spectrum)
        self.scalingComputeBtn.clicked.connect(self.compute_scaled_gm)
        self.scaledGMAddToListBtn.clicked.connect(self.add_scaled_ts_to_list)

        # Stretching tab
        self.stretchingComputeBtn.clicked.connect(self.update_stretching_tab)
        self.stretchingAddToListBtn.clicked.connect(self.add_stretched_ts_to_list)
        
        self.get_availeble_mplstyles()

    def get_selected_timeseries_index(self):
        """Check for selected timeseries and store its integer and QIndex as class attributes."""
        sids = self.tsListView.selectedIndexes()
        if len(sids) > 0:
            self.Qidx = sids[0]
            self.selectedTsIndex = self.Qidx.row()
        else:
            self.selectedTsIndex = None

    def import_new_mplstyle(self):
        dialog = QFileDialog()
        dialog.setDefaultSuffix("mplstyle")
        filename = dialog.getOpenFileName(filter="Matplotlib style (*.mplstyle)")[0]
        if len(filename) > 0 :
            if not filename.endswith(".mplstyle"):
                filename += ".mplstyle"
            with open(filename, "rb") as fp:
                mplUserLibraryPath = mpl.style.core.USER_LIBRARY_PATHS[0]
                # mplUserLibraryPath = Path("matplotlib/mpl-data/stylelib/")
                filepath = Path(filename)
                shutil.copy(filepath, mplUserLibraryPath)
                # self.restart_required_message()
                self.get_availeble_mplstyles()

    def get_availeble_mplstyles(self):
        # Matplotlib stylesheets
        try:
            self.mplStylesheetCombo.currentTextChanged.disconnect()
        except:
            pass
        self.mplStylesheetCombo.clear()
        mpl.style.reload_library()
        self.mplstyles = ["default"] + sorted(
            [style for style in mpl.style.available if not (style.startswith("_") or style.startswith("seaborn"))])
        self.mplStylesheetCombo.addItems(self.mplstyles)
        self.mplStylesheetCombo.currentTextChanged.connect(self.update_for_stylesheet)

    def remove_timeseries_from_data(self):
        sids = self.tsListView.selectedIndexes()
        self.tsNameModel.removeRows(sids[0].row(), 1)

    def make_importtab_visible(self):
        self.tabWidget.setCurrentWidget(self.importTab)

    def update_for_stylesheet(self):
        idx = self.tsListView.selectedIndexes()[0]
        # self.update_data(index=idx)
        self.update_plots(self.data[idx.row()])

    def apply_baseline_correction(self, tts):
        corrType = self.baseCorrComboBox.currentText()
        tts.recompute(baseCorr=corrType)
        # self.data[self.selectedTsIndex].apply_baseline_correction(type=corrType)
        # self.tts = self.data[self.selectedTsIndex]
        # self.update_data(self.Qidx)

    ############################################################################
    ## TOOLBAR actions
    ############################################################################
    def setup_toolbar(self):
        # Save session
        self.saveSessionAction = QAction(QIcon(QPixmap(u":/icon8/icons/icons8-save-64.png")), "Save session")
        self.saveSessionAction.triggered.connect(self.save_session_to_disk)
        self.toolBar.addAction(self.saveSessionAction)

        # Load session
        self.loadSessionAction = QAction(QIcon(QPixmap(u":/icon8/icons/icons8-open-file-folder-48.png")), "Open session")
        self.loadSessionAction.triggered.connect(self.load_session_from_disk)
        self.toolBar.addAction(self.loadSessionAction)

        # Append session
        self.appendSessionAction = QAction(QIcon(QPixmap(u":/icon8/icons/icons8-architecture-64.png")), "Append session")
        self.appendSessionAction.triggered.connect(self.append_session_from_disk)
        self.toolBar.addAction(self.appendSessionAction)

        # Clear session
        self.clearSessionAction = QAction(QIcon(QPixmap(u":/icon8/icons/icons8-broom-48.png")), "Clear session")
        self.clearSessionAction.triggered.connect(self.clear_current_session)
        self.toolBar.addAction(self.clearSessionAction)
        self.toolBar.addSeparator()

        # Empty widget
        empty = QWidget()
        empty.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.toolBar.addWidget(empty)
        self.toolBar.addSeparator()

        # Help system
        self.openHelpAction = QAction(QIcon(QPixmap(u":/icon8/icons/icons8-help-48.png")), "Help")
        self.openHelpAction.triggered.connect(self.show_help_window)
        self.toolBar.addAction(self.openHelpAction)

        # About info
        # horizontalSpacer = QSpacerItem(200, 40, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.aboutAction = QAction(QIcon(QPixmap(u":/allIcons/icons/about.svg")), "About")
        self.aboutAction.triggered.connect(self.show_about_info)
        self.toolBar.addAction(self.aboutAction)

    def show_about_info(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("About PEGMA")
        msgBox.setText("""
        <p><b>PEGMA</b> is a package for exploratory analysis of ground motions, developed using <a href="https://github.com/gauthamrdy/earthquakepy">earthquakepy</a> and PySide6.<br />
        <p>It is licensed under the terms of GNU GPLv3. For more details about licensing <a href="https://www.gnu.org/licenses/gpl-3.0.en.html">click here</a>.<br />
        <p>Some of the icons used in the app are downloaded from <a href="https://icons8.com">icons8 website</a>.
        <p><b>Developer:</b>
        <ul>
        <li><a href="https://dbpatankar.github.io">Digvijay Patankar</a></li>
        </ul>
        <!--<p><b>Contributors:</b>
        <ul>
        <li>May be you?</li>
        </ul>-->
        """)
        msgBox.setIconPixmap(QPixmap(u":/logo/logo_small_150px.png"))
        msgBox.exec()

    def save_session_to_disk(self, sig):
        dialog = QFileDialog()
        dialog.setDefaultSuffix("pgm")
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        filename = dialog.getSaveFileName(None, "Filename to save session", "", "PEGMA file (*.pgm)")[0]
        if len(filename) > 0 :
            if not filename.endswith(".pgm"):
                filename += ".pgm"
            with open(filename, "wb") as fp:
                pickle.dump(self.data, fp)

    def load_session_from_disk(self, sig):
        dialog = QFileDialog()
        dialog.setDefaultSuffix("pgm")
        filename = dialog.getOpenFileName(filter="PEGMA file (*.pgm)")[0]
        if len(filename) > 0:
            with open(filename, "rb") as fp:
                _temp = pickle.load(fp)
            del(self.data[0:])
            for i in range(len(_temp)):
                self.tsNameModel.insertRows(len(self.data), 1, _temp[i])

    def append_session_from_disk(self, sig):
        dialog = QFileDialog()
        dialog.setDefaultSuffix("pgm")
        filename = dialog.getOpenFileName(filter="PEGMA file (*.pgm)")[0]
        if len(filename) > 0:
            with open(filename, "rb") as fp:
                _temp = pickle.load(fp)
            for i in range(len(_temp)):
                self.tsNameModel.insertRows(len(self.data), 1, _temp[i])

    def clear_current_session(self, sig):
        dialog = QMessageBox()
        dialog.setText("You are about to clear all the data from current session. This cannot be undone! Are you sure?")
        dialog.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        dialog.setDefaultButton(QMessageBox.No)
        #dialog.setIcon(QMessageBox.Question)
        dialog.setIconPixmap(QPixmap(u":/icon8/icons/icons8-high-priority-94.png"))
        button = dialog.exec()
        if button == QMessageBox.Yes:
            del(self.data[0:])
        else:
            pass

    def show_help_window(self, checked):
        """Show help browser."""
        self.browser = HelpSystem.HelpBrowser()
        self.browser.setWindowTitle("PEGMA Documentation")
        self.browser.webView.load(ui.ui_mainwindow.QUrl("qrc:/docs/index.html"))
        self.browser.show()

    ######################################
    ## IMPORT TAB SLOTS
    ######################################
    def add_ts_to_data(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        for fl in self.filenames:
            self.sourcePath.setText(fl)
            self.tsNameModel.insertRows(len(self.data), 1, self.tts)
            indexObject = self.tsNameModel.createIndex(len(self.data)-1, 0)
            self.tsListView.selectionModel().select(indexObject, QItemSelectionModel.Select)
        QApplication.restoreOverrideCursor()

    def file_opener(self):
        if self.sourceChecked:
            self.filenames = QFileDialog.getOpenFileNames(caption="Select one or more data sources", dir="")[0]
            if len(self.filenames) > 1:
                self.multiImport = 1
            else:
                self.multiImport = 0
            self.sourcePath.setText(self.filenames[0])
        else:
            dialog = QMessageBox()
            dialog.setText("Please select a time history source.")
            dialog.setStandardButtons(QMessageBox.Ok)
            dialog.setIcon(QMessageBox.Question)
            dialog.exec()

    def DELfile_opener(self, text):
        filename = QFileDialog.getOpenFileName()[0]
        self.sourcePath.setText(filename)

    def make_peer_options_visible(self):
        self.sourceChecked = 1
        self.sourcePath.setEnabled(True)
        self.scaleFactorBox1.setEnabled(True)
        self.scaleFactorBox2.setEnabled(False)
        self.scaleFactorBox3.setEnabled(False)
        self.customLineStart.setEnabled(False)
        self.customLineEnd.setEnabled(False)
        self.tsDt.setEnabled(False)
        self.delimBox.setEnabled(False)

    def make_cosmosvdc_options_visible(self):
        self.sourceChecked = 1
        self.sourcePath.setEnabled(True)
        self.scaleFactorBox1.setEnabled(True)
        self.scaleFactorBox2.setEnabled(True)
        self.scaleFactorBox3.setEnabled(True)
        self.customLineStart.setEnabled(False)
        self.customLineEnd.setEnabled(False)
        self.tsDt.setEnabled(False)
        self.delimBox.setEnabled(False)

    def make_raw_options_visible(self):
        self.sourceChecked = 1
        self.sourcePath.setEnabled(True)
        self.scaleFactorBox1.setEnabled(True)
        self.scaleFactorBox2.setEnabled(False)
        self.scaleFactorBox3.setEnabled(False)
        self.customLineStart.setEnabled(False)
        self.customLineEnd.setEnabled(False)
        self.tsDt.setEnabled(False)
        self.delimBox.setEnabled(True)

    def make_custom_options_visible(self):
        self.sourceChecked = 1
        self.sourcePath.setEnabled(True)
        self.scaleFactorBox1.setEnabled(True)
        self.scaleFactorBox2.setEnabled(False)
        self.scaleFactorBox3.setEnabled(False)
        self.customLineStart.setEnabled(True)
        self.customLineEnd.setEnabled(True)
        self.tsDt.setEnabled(True)
        self.delimBox.setEnabled(False)

    def update_input_browser(self):
        with open(self.sourcePath.text(), "r") as f:
            text = f.read()
        self.inputBrowser.setText(text)

    def update_output_browser(self):
        while True:
            filename = self.sourcePath.text()
            if self.tsSourcePeer.isChecked():
                ts = ep.read_peer_nga_file(
                    filename,
                    scale_factor=self.scaleFactorBox1.value())
                ts.scale_factor = f"{self.scaleFactorBox1.value():.4f}"
                source = "peernga"
                tts = AppClasses.TimeSeries([ts], source=source)
                break
            elif self.tsSourceCosmosvdc.isChecked():
                ts, its, iits = ep.read_cosmos_vdc_file(
                    filename,
                    scale_factor=[
                        self.scaleFactorBox1.value(),
                        self.scaleFactorBox2.value(),
                        self.scaleFactorBox3.value()
                    ])
                ts.scale_factor = f"{self.scaleFactorBox1.value():.4f}, {self.scaleFactorBox2.value():.4f}, {self.scaleFactorBox3.value():.4f}"
                source = "cosmosvdc"
                tts = AppClasses.TimeSeries([ts, its, iits], source=source)
                break
            elif self.tsSourceRaw.isChecked():
                ts = ep.read_raw_timeseries_file(
                    filename,
                    scale_factor=self.scaleFactorBox1.value(),
                    delimiter=self.delimBox.text())
                ts.scale_factor = f"{self.scaleFactorBox1.value():.4f}"
                source = "raw"
                tts = AppClasses.TimeSeries([ts], source=source)
                break
            elif self.tsSourceCustom.isChecked():
                if self.customLineEnd.value() < 0:
                    end = None
                else:
                    end = self.customLineEnd.value() - 1
                ts = ep.read_custom_timeseries_file(
                    filename,
                    dt=self.tsDt.value(),
                    start=self.customLineStart.value() - 1,
                    end=end,
                    scale_factor=self.scaleFactorBox1.value())
                ts.scale_factor = f"{self.scaleFactorBox1.value():.4f}"
                source = "custom"
                tts = AppClasses.TimeSeries([ts], source=source)
                break
            else:
                dialog = QMessageBox()
                dialog.setText("Please use all appropriate inputs.")
                dialog.setStandardButtons(QMessageBox.Ok)
                dialog.setIcon(QMessageBox.Question)
                dialog.exec()
        self.tts = tts
        self.outputBrowser.setText(ts.__repr__())

    def update_input_output_browser(self):
        self.update_input_browser()
        self.update_output_browser()

    def update_data(self, index=None):
        self.tsNameModel = UiClasses.TsListModel(self.data)
        self.tsListView.setModel(self.tsNameModel)

        # selectedTs = self.tsListView.selectedIndexes()
        if index is not None:
            # Select the item in the list based on index
            indexObject = self.tsNameModel.createIndex(index.row(), 0)

            self.tsListView.selectionModel().select(indexObject, QItemSelectionModel.Select)
            self.apply_baseline_correction(self.data[index.row()])

            self.tsTableModel = UiClasses.TsTableModel(self.data[index.row()].ts, self.clipboard)
            self.accTable.setModel(self.tsTableModel)

            self.itsTableModel = UiClasses.TsTableModel(self.data[index.row()].its, self.clipboard)
            self.velTable.setModel(self.itsTableModel)

            self.iitsTableModel = UiClasses.TsTableModel(self.data[index.row()].iits, self.clipboard)
            self.dispTable.setModel(self.iitsTableModel)

            self.tsProps = AppClasses.TimeseriesProps(self.data[index.row()], self.clipboard)
            self.tsPropsTableModel = UiClasses.TsPropsTableModel(self.tsProps)
            # self.tsPropsTableModel = TsPropsTableModel(self.data[index.row()], self.clipboard)
            self.tsPropsTableView.setModel(self.tsPropsTableModel)

            self.metaTableModel = UiClasses.MetadataTable(self.data[index.row()].ts)
            self.metaTableView.setModel(self.metaTableModel)
            self.metaTableView.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

            self.fsTableModel = UiClasses.FourierTableModel(self.data[index.row()], self.clipboard)
            self.fsTableView.setModel(self.fsTableModel)

            self.rsTableModel = UiClasses.ResponseSpectraTableModel(self.data[index.row()].rs, self.clipboard)
            self.rsTableView.setModel(self.rsTableModel)

            self.freqTableModel = UiClasses.FrequencyCharacteristicsTableModel(self.data[index.row()].freqTable, self.clipboard)
            self.freqCharTableView.setModel(self.freqTableModel)

            self.tsToClipboardBtn.clicked.connect(self.tsTableModel.copy_to_clipboard)
            self.itsToClipboardBtn.clicked.connect(self.itsTableModel.copy_to_clipboard)
            self.iitsToClipboardBtn.clicked.connect(self.iitsTableModel.copy_to_clipboard)
            self.tsPropCopyBtn.clicked.connect(self.tsPropsTableModel.copy_to_clipboard)
            self.fsToClipboardBtn.clicked.connect(self.fsTableModel.copy_to_clipboard)
            self.rsToClipboardBtn.clicked.connect(self.rsTableModel.copy_to_clipboard)
            self.freqCharCopyBtn.clicked.connect(self.freqTableModel.copy_to_clipboard)

            self.update_plots(self.data[index.row()])

    ######################################
    ## TIMESERIES TAB SLOTS
    ######################################

    def update_timeseries_plots(self):
        """Update only timeseries plots."""
        self.get_selected_timeseries_index()
        xmin = self.tsXminDspinBox.value()
        xmax = self.tsXmaxDspinBox.value()
        if (xmax <= 0.0) or (xmax <= xmin):
            xmax = None
        self.tsProps = AppClasses.TimeseriesProps(self.data[self.selectedTsIndex], self.clipboard, xmin=xmin, xmax=xmax)
        self.tsPropsTableModel = UiClasses.TsPropsTableModel(self.tsProps)
        self.tsPropsTableView.setModel(self.tsPropsTableModel)
        self.tsPropCopyBtn.clicked.connect(self.tsPropsTableModel.copy_to_clipboard)
        tts = self.data[self.selectedTsIndex]
        self.update_ts_plot(tts)
        self.update_its_plot(tts)
        self.update_iits_plot(tts)

    ######################################
    ## FOURIER TAB SLOTS
    ######################################
    def update_freq_data_and_plot(self):
        self.get_selected_timeseries_index()
        self.freqTableModel = UiClasses.FrequencyCharacteristicsTableModel(self.data[self.selectedTsIndex].freqTable, self.clipboard)
        self.freqCharTableView.setModel(self.freqTableModel)
        self.freqCharCopyBtn.clicked.connect(self.freqTableModel.copy_to_clipboard)
        self.update_fs_amp_plot(self.data[self.selectedTsIndex])

    def update_tp_bandwidth_data(self, tts: AppClasses.TimeSeries):
        self.get_selected_timeseries_index()
        idx = self.selectedTsIndex
        winLen = self.windowSizeSpinBox.value()
        poly = self.polyDegSpinBox.value()
        freqTable = AppClasses.FreqChar(self.data[idx].fs, self.data[idx].ps, winLen, poly)
        self.data[idx].freqTable = freqTable
        self.update_freq_data_and_plot()

    def get_tp_and_bandwidth(self):
        filt = self.lowPassFiltComboBox.currentText()
        windowSize = self.windowSizeSpinBox.value()
        poly = self.polyDegSpinBox.value()
        self.get_selected_timeseries_index()
        idx = self.selectedTsIndex
        N = self.data[idx].fs.N // 2
        if filt.lower() == "savgol":
            yf = scipy.signal.savgol_filter(self.data[idx].fs.amplitude, windowSize, poly)
        try:
            self.fsAmpWidget.axes.lines[0].remove()
        except:
        # self.fsAmpWidget.axes.set_xlabel(xaxis)
        # self.fsAmpWidget.axes.set_xlim(left=xmin, right=xmax)
        # self.fsUnwrappedPhaseWidget.axes.set_xlim(left=0.0, right=None)
            pass
        self.update_tp_bandwidth_data(self.data[idx])
        xaxis = self.periodFreqComboBox.currentText()
        if xaxis.lower() == "frequency (hz)":
            self.fsAmpWidget.axes.plot(self.data[idx].fs.frequencies[0:N], yf[0:N],
                                    label="Smoothed spectra")
        else:
            self.fsAmpWidget.axes.plot(self.data[idx].fs.T[0:N-1], yf[1:N])

    def update_fs_plots(self):
        """Update only fourier tab plots."""
        self.get_selected_timeseries_index()
        tts = self.data[self.selectedTsIndex]
        self.update_fs_amp_plot(tts)
        self.update_fs_phase_plot(tts)
        self.update_fs_unwrappedphase_plot(tts)
        self.update_ps_amp_plot(tts)


    ######################################
    ## RESPONSE SPECTRA TAB SLOTS
    ######################################
    def update_rs_trip_plot_data(self, index: QModelIndex):
        self.rsTableModel = UiClasses.ResponseSpectraTableModel(self.data[index.row()].rs, self.clipboard)
        self.rsTableView.setModel(self.rsTableModel)
        self.rsToClipboardBtn.clicked.connect(self.rsTableModel.copy_to_clipboard)
        self.update_psa_plot(self.data[index.row()])
        self.update_tripartite_plot(self.data[index.row()])

    def update_response_spectra(self):
        self.get_selected_timeseries_index()
        xi = self.xiDoubleSpinBox.value()/100.0
        Ts = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09]
        Ts.extend(list(np.arange(0.1, 10.01, 0.1)))
        Ts.extend(list(np.arange(20, 100.01, 10)))
        self.data[self.selectedTsIndex].rs = self.data[self.selectedTsIndex].ts.get_response_spectra(T=Ts, xi=xi)
        self.update_rs_trip_plot_data(self.tsListView.selectedIndexes()[0])

    def update_rs_plot(self):
        """Update only response spectrum plot."""
        self.get_selected_timeseries_index()
        tts = self.data[self.selectedTsIndex]
        self.update_psa_plot(tts)


    ######################################
    ## GM SCALING TAB SLOTS
    ######################################
    def plot_design_spectrum(self, ds: AppClasses.DesignSpectrum):
        self.dsPlotWidget = AppClasses.MatplotlibWidget(configFile=self.plotConfigFiles["designSpectrum"])
        self.scalingSpecPlotLayout.addWidget(self.dsPlotWidget)
        self.dsPlotWidget.axes.clear()
        self.dsPlotWidget.axes.plot(ds.T, ds.Y, label="Target spectrum")
        add_persistant_config(self.dsPlotWidget.axes, self.plotConfigFiles["designSpectrum"])
        self.dsPlotWidget.add_cursor()
        self.dsPlotWidget.draw()

    def import_design_spectrum(self):
        """The file must be two column delimited with a comma and readable by np.genfromtxt()."""
        dialog = QFileDialog(parent=None, caption="Select design spectrum file.")
        filename = dialog.getOpenFileName()[0]
        ds = np.genfromtxt(filename, delimiter=",")
        self.ds = AppClasses.DesignSpectrum(ds[:, 0], ds[:, 1])
        dsModel = UiClasses.DesignSpecModel(self.ds)
        self.designSpecView.setModel(dsModel)
        self.plot_design_spectrum(self.ds)

    def plot_computed_sa(self, T, Sa, scale_factor):
        # self.dsPlotWidget.axes.plot(rs.T, rs.Sa, color="red", label="Scaled")
        self.dsPlotWidget.axes.scatter(x=T, y=Sa, color="blue", label="Unscaled")
        self.dsPlotWidget.axes.scatter(x=T, y=Sa*scale_factor, color="red", label="Scaled")
        self.dsPlotWidget.axes.legend()
        # self.dsPlotWidget.add_cursor()
        # self.dsPlotWidget.draw()

    def compute_scaled_gm(self):
        method = self.scalingMethodcomboBox.currentText()
        xi = self.scalingXiDSpinBox.value()/100.0
        T = self.scalingPeriodDSpinBox.value()
        designSa = self.ds.get_y(T)
        s = ep.sdof(T=T, xi=xi)
        self.get_selected_timeseries_index()
        t, x, v, a = s.get_response_frequency_domain(self.data[self.selectedTsIndex].ts, tsType="baseExcitation")
        Sa = np.max(np.abs(np.real(a)))
        scale_factor = designSa / Sa
        scaled_y = self.data[self.selectedTsIndex].ts.y * scale_factor
        ts = ep.timeseries.TimeSeries(self.data[self.selectedTsIndex].ts.t, scaled_y)
        # rs = ts.get_response_spectra(xi=xi)
        ts.T = T
        ts.xi = xi
        ts.GMscale_factor = scale_factor
        origPath = Path(self.data[self.selectedTsIndex].ts.filepath)
        pseudoPath = f"{origPath.parent}/^{origPath.name}"
        ts.filepath = pseudoPath
        scaledTsModel = UiClasses.TsTableModel(ts, self.clipboard)
        self.scaledGMView.setModel(scaledTsModel)
        self.scaledGMCopyToClipboardBtn.clicked.connect(scaledTsModel.copy_to_clipboard)
        # Add scaled ts to the list
        self.scaledTs = AppClasses.TimeSeries([ts], "raw", xi=xi)
        self.plot_computed_sa(T, Sa, scale_factor)
        
    def add_scaled_ts_to_list(self):
        self.get_selected_timeseries_index()
        self.tsNameModel.insertRows(self.selectedTsIndex + 1, 1, self.scaledTs)
    
    ###################################################################
    ## GM STRETCHING SLOTS
    ###################################################################
    def get_stretching_inputs(self):
        self.stretchingFactor = self.stretchingFactorDSpinBox.value()

    def compute_stretched_tts(self):
        self.get_selected_timeseries_index()
        oldDt = self.data[self.selectedTsIndex].ts.dt
        newDt = oldDt * self.stretchingFactor
        newTs = copy.deepcopy(ep.timeseries.TimeSeries(newDt, self.data[self.selectedTsIndex].ts.y))
        newTs.GMstretchFactor = self.stretchingFactor
        origPath = Path(self.data[self.selectedTsIndex].ts.filepath)
        pseudoPath = f"{origPath.parent}/_{origPath.name}"
        newTs.filepath = pseudoPath
        self.stretchedTts = AppClasses.TimeSeries([newTs], source="raw", xi=0.05)
        stretchedTsModel = UiClasses.StretchedTimeseriesModel(self.stretchedTts, self.clipboard)
        self.stretchingTsView.setModel(stretchedTsModel)
        self.stretchingCopyToClipboardBtn.clicked.connect(stretchedTsModel.copy_to_clipboard)

    def plot_stretched_ts(self):
        try:
            self.stretchedTsPlotWidget.deleteLater()
        except:
            pass
        self.stretchedTsPlotWidget = AppClasses.MatplotlibWidget(configFile=self.plotConfigFiles["stretchedTs"])
        self.stretchingTsLayout.addWidget(self.stretchedTsPlotWidget)
        self.stretchedTsPlotWidget.axes.clear()
        self.stretchedTsPlotWidget.axes.plot(self.stretchedTts.ts.t, self.stretchedTts.ts.y)
        self.stretchedTsPlotWidget.axes.set_xlabel("Time (s)")
        self.stretchedTsPlotWidget.axes.set_ylabel("y")
        self.stretchedTsPlotWidget.axes.set_xlim(left=0.0, right=None)
        add_persistant_config(self.stretchedTsPlotWidget.axes, self.plotConfigFiles["stretchedTs"])
        self.stretchedTsPlotWidget.add_cursor()
        self.stretchedTsPlotWidget.draw()

    def plot_stretched_fs(self):
        N = self.stretchedTts.fs.N // 2
        try:
            self.stretchedFsPlotWidget.deleteLater()
        except:
            pass
        self.stretchedFsPlotWidget = AppClasses.MatplotlibWidget(configFile=self.plotConfigFiles["stretchedFs"])
        self.stretchingFsLayout.addWidget(self.stretchedFsPlotWidget)
        self.stretchedFsPlotWidget.axes.clear()
        self.stretchedFsPlotWidget.axes.plot(self.stretchedTts.fs.frequencies[0:N], 
                                             self.stretchedTts.fs.amplitude[0:N])
        self.stretchedFsPlotWidget.axes.set_xlabel("Frequency (Hz)")
        self.stretchedFsPlotWidget.axes.set_ylabel("FSA")
        self.stretchedFsPlotWidget.axes.set_xlim(left=0.0, right=None)
        add_persistant_config(self.stretchedFsPlotWidget.axes, self.plotConfigFiles["stretchedFs"])
        self.stretchedFsPlotWidget.add_cursor()
        self.stretchedFsPlotWidget.draw()
    
    def plot_stretched_rs(self):
        try:
            self.stretchedRsPlotWidget.deleteLater()
        except:
            pass
        self.stretchedRsPlotWidget = AppClasses.MatplotlibWidget(configFile=self.plotConfigFiles["stretchedRs"])
        self.stretchingRsLayout.addWidget(self.stretchedRsPlotWidget)
        self.stretchedRsPlotWidget.axes.clear()
        self.stretchedRsPlotWidget.axes.plot(self.stretchedTts.rs.T, self.stretchedTts.rs.PSa)
        self.stretchedRsPlotWidget.axes.set_xlabel("Period (s)")
        self.stretchedRsPlotWidget.axes.set_ylabel("PSa")
        self.stretchedRsPlotWidget.axes.set_xlim(left=0.0, right=10.0)
        add_persistant_config(self.stretchedRsPlotWidget.axes, self.plotConfigFiles["stretchedRs"])
        self.stretchedRsPlotWidget.add_cursor()
        self.stretchedRsPlotWidget.draw()

    def plot_stretched_tab_plots(self):
        self.plot_stretched_ts()
        self.plot_stretched_fs()
        self.plot_stretched_rs()

    def add_stretched_ts_to_list(self):
        self.get_selected_timeseries_index()
        self.tsNameModel.insertRows(self.selectedTsIndex+1, 1, self.stretchedTts)

    def update_stretching_tab(self):
        self.get_stretching_inputs()
        self.compute_stretched_tts()
        self.plot_stretched_tab_plots()
        

    ###################################################################
    # UPDATE PLOTS
    ###################################################################
    def update_ts_plot(self, ts: AppClasses.TimeSeries):
        try:
            self.tsWidget.deleteLater()
        except:
            pass

        xmin = self.tsXminDspinBox.value()
        xmax = self.tsXmaxDspinBox.value()
        if (xmax <= 0.0) or (xmax <= xmin):
            xmax = None

        self.tsWidget = AppClasses.MatplotlibWidget(configFile=self.plotConfigFiles["ts"])
        self.tsLayout.addWidget(self.tsWidget)
        self.tsWidget.axes.clear()
        self.tsWidget.axes.plot(ts.ts.t, ts.ts.y)
        add_persistant_config(self.tsWidget.axes, self.plotConfigFiles["ts"])
        # self.tsWidget.axes.set_ylabel("y (Timeseries)")
        # self.tsWidget.axes.set_xlabel("Time (s)")
        self.tsWidget.axes.set_xlim(left=xmin, right=xmax)
        self.tsWidget.add_cursor()
        self.tsWidget.draw()

    def update_its_plot(self, ts: AppClasses.TimeSeries):
        try:
            self.itsWidget.deleteLater()
        except:
            pass
        xmin = self.tsXminDspinBox.value()
        xmax = self.tsXmaxDspinBox.value()
        if (xmax <= 0.0) or (xmax <= xmin):
            xmax = None

        self.itsWidget = AppClasses.MatplotlibWidget(configFile=self.plotConfigFiles["its"])
        self.itsLayout.addWidget(self.itsWidget)
        self.itsWidget.axes.clear()
        # self.itsWidget.axes.set_ylabel("$\int y \mathrm{d}t$")
        # self.itsWidget.axes.set_xlabel("Time (s)")
        self.itsWidget.axes.plot(ts.its.t, ts.its.y)
        add_persistant_config(self.itsWidget.axes, self.plotConfigFiles["its"])
        self.itsWidget.axes.set_xlim(left=xmin, right=xmax)
        self.itsWidget.add_cursor()
        self.itsWidget.draw()

    def update_iits_plot(self, ts: AppClasses.TimeSeries):
        try:
            self.iitsWidget.deleteLater()
        except:
            pass
        xmin = self.tsXminDspinBox.value()
        xmax = self.tsXmaxDspinBox.value()
        if (xmax <= 0.0) or (xmax <= xmin):
            xmax = None

        self.iitsWidget = AppClasses.MatplotlibWidget(configFile=self.plotConfigFiles["iits"])
        self.iitsLayout.addWidget(self.iitsWidget)
        self.iitsWidget.axes.clear()
        # self.iitsWidget.axes.set_ylabel(
            # "$\int \int y \mathrm{d} t \mathrm{d} t$")
        # self.iitsWidget.axes.set_xlabel("Time (s)")
        self.iitsWidget.axes.plot(ts.iits.t, ts.iits.y)
        add_persistant_config(self.iitsWidget.axes, self.plotConfigFiles["iits"])
        self.iitsWidget.axes.set_xlim(left=xmin, right=xmax)
        self.iitsWidget.add_cursor()
        self.iitsWidget.draw()

    def update_fs_amp_plot(self, ts: AppClasses.TimeSeries):
        N = ts.fs.N // 2
        try:
            self.lowPassFiltComboBox.currentTextChanged.disconnect()
            self.windowSizeSpinBox.editingFinished.disconnect()
            self.polyDegSpinBox.editingFinished.disconnect()
        except:
            pass
        try:
            self.fsAmpWidget.deleteLater()
        except:
            pass
        self.fsAmpWidget = AppClasses.MatplotlibWidget(configFile=self.plotConfigFiles["fsAmp"])
        self.fsAmpLayout.addWidget(self.fsAmpWidget)
        self.fsAmpWidget.axes.clear()
        # self.fsAmpWidget.axes.set_ylabel("Fourier amplitude")
        # self.fsAmpWidget.axes.set_xlabel("Frequency (Hz)")
        xaxis = self.periodFreqComboBox.currentText()
        xmin = self.fsXminDSpinBox.value()
        xmax = self.fsXmaxDSpinBox.value()
        if xmax <= 0.0:
            xmax = None
        if xaxis.lower() == "frequency (hz)":
            self.fsAmpWidget.axes.plot(
                ts.fs.frequencies[0:N], ts.fs.amplitude[0:N])
        else:
            self.fsAmpWidget.axes.plot(ts.fs.T[0:N-1], ts.fs.amplitude[1:N])
        add_persistant_config(self.fsAmpWidget.axes, self.plotConfigFiles["fsAmp"])
        self.fsAmpWidget.axes.set_xlabel(xaxis)
        self.fsAmpWidget.axes.set_xlim(left=xmin, right=xmax)
        # self.fsAmpWidget.axes.set_xlim(left=0.0, right=None)
        self.fsAmpWidget.add_cursor()
        self.fsAmpWidget.draw()
        self.lowPassFiltComboBox.currentTextChanged.connect(self.get_tp_and_bandwidth)
        self.windowSizeSpinBox.editingFinished.connect(self.get_tp_and_bandwidth)
        self.polyDegSpinBox.editingFinished.connect(self.get_tp_and_bandwidth)

    def update_fs_phase_plot(self, ts: AppClasses.TimeSeries):
        N = ts.fs.N // 2
        try:
            self.fsPhaseWidget.deleteLater()
        except:
            pass
        self.fsPhaseWidget = AppClasses.MatplotlibWidget(configFile=self.plotConfigFiles["fsPhase"])
        self.fsPhaseLayout.addWidget(self.fsPhaseWidget)
        self.fsPhaseWidget.axes.clear()
        # self.fsPhaseWidget.axes.set_ylabel("Fourier phase")
        # self.fsPhaseWidget.axes.set_xlabel("Frequency (Hz)")
        xaxis = self.periodFreqComboBox.currentText()
        xmin = self.fsXminDSpinBox.value()
        xmax = self.fsXmaxDSpinBox.value()
        if xmax <= 0.0:
            xmax = None
        if xaxis.lower() == "frequency (hz)":
            self.fsPhaseWidget.axes.plot(ts.fs.frequencies[0:N], ts.fs.phase[0:N])
        else:
            self.fsPhaseWidget.axes.plot(ts.fs.T[0:N-1], ts.fs.phase[1:N])
        add_persistant_config(self.fsPhaseWidget.axes, self.plotConfigFiles["fsPhase"])
        self.fsPhaseWidget.axes.set_xlabel(xaxis)
        self.fsPhaseWidget.axes.set_xlim(left=xmin, right=xmax)
        self.fsPhaseWidget.add_cursor()
        # self.fsPhaseWidget.axes.set_xlim(left=0.0, right=None)
        self.fsPhaseWidget.draw()

    def update_fs_unwrappedphase_plot(self, ts: AppClasses.TimeSeries):
        N = ts.fs.N // 2
        try:
            self.fsUnwrappedPhaseWidget.deleteLater()
        except:
            pass
        self.fsUnwrappedPhaseWidget = AppClasses.MatplotlibWidget(configFile=self.plotConfigFiles["fsUnwrappedPhase"])
        self.fsUnwrappedPhaseLayout.addWidget(self.fsUnwrappedPhaseWidget)
        self.fsUnwrappedPhaseWidget.axes.clear()
        # self.fsUnwrappedPhaseWidget.axes.set_ylabel("Fourier unwrapped phase")
        # self.fsUnwrappedPhaseWidget.axes.set_xlabel("Frequency (Hz)")
        self.fsUnwrappedPhaseWidget.axes.plot(
            ts.fs.frequencies[0:N], ts.fs.unwrappedPhase[0:N])
        add_persistant_config(self.fsUnwrappedPhaseWidget.axes,
                              self.plotConfigFiles["fsUnwrappedPhase"])
        self.fsUnwrappedPhaseWidget.add_cursor()
        self.fsUnwrappedPhaseWidget.draw()

    def update_ps_amp_plot(self, ts: AppClasses.TimeSeries):
        N = ts.ps.N // 2
        try:
            self.psAmpWidget.deleteLater()
        except:
            pass
        self.psAmpWidget = AppClasses.MatplotlibWidget(configFile=self.plotConfigFiles["psAmp"])
        self.psAmpLayout.addWidget(self.psAmpWidget)
        self.psAmpWidget.axes.clear()
        # self.psAmpWidget.axes.set_ylabel("Power")
        # self.psAmpWidget.axes.set_xlabel("Frequency (Hz)")
        xaxis = self.periodFreqComboBox.currentText()
        xmin = self.fsXminDSpinBox.value()
        xmax = self.fsXmaxDSpinBox.value()
        if xmax <= 0.0:
            xmax = None
        if xaxis.lower() == "frequency (hz)":
            self.psAmpWidget.axes.plot(
                ts.ps.frequencies[0:N], ts.ps.amplitude[0:N])
        else:
            self.psAmpWidget.axes.plot(
                ts.ps.T[0:N-1], ts.ps.amplitude[1:N])
        add_persistant_config(self.psAmpWidget.axes,
                              self.plotConfigFiles["psAmp"])
        self.psAmpWidget.axes.set_xlabel(xaxis)
        self.psAmpWidget.axes.set_xlim(left=xmin, right=xmax)
        self.psAmpWidget.add_cursor()
        # self.psAmpWidget.axes.set_xlim(left=0.0, right=None)
        self.psAmpWidget.draw()

    def update_psa_plot(self, tts):
        try:
            self.psaWidget.deleteLater()
        except:
            pass
        yAxisComboText = self.rsComboBox.currentText()
        if yAxisComboText.lower() == "pseudo-spectral acceleration (psa)":
            yaxis = tts.rs.PSa
        elif yAxisComboText.lower() == "pseudo-spectral velocity (psv)":
            yaxis = tts.rs.PSv
        elif yAxisComboText.lower() == "spectral displacement (sd)":
            yaxis = tts.rs.Sd
        elif yAxisComboText.lower() == "spectral velocity (sv)":
            yaxis = tts.rs.Sv
        elif yAxisComboText.lower() == "spectral acceleration (sa)":
            yaxis = tts.rs.Sa

        self.psaWidget = AppClasses.MatplotlibWidget(configFile=self.plotConfigFiles["psa"])
        self.psaLayout.addWidget(self.psaWidget)
        self.psaWidget.axes.clear()
        # self.psaWidget.axes.set_ylabel("PS$_a$")
        # self.psaWidget.axes.set_xlabel("Period (s)")
        self.psaWidget.axes.plot(tts.rs.T, yaxis)
        add_persistant_config(self.psaWidget.axes,
                              self.plotConfigFiles["psa"])
        self.psaWidget.axes.set_ylabel(yAxisComboText)
        self.psaWidget.add_cursor()
        # self.psaWidget.axes.set_xlim(left=0.0, right=10.0)
        self.psaWidget.draw()

    def update_tripartite_plot(self, tts):
        try:
            self.tripartiteWidget.deleteLater()
        except:
            pass
        self.tripartiteWidget = AppClasses.MatplotlibWidget(figsize=(6.4, 6.4), configFile=self.plotConfigFiles["tripartite"])
        self.tripartiteLayout.addWidget(self.tripartiteWidget)
        self.tripartiteWidget.axes.clear()
        AppClasses.TripartitePlot(tts.rs, self.tripartiteWidget.axes)
        add_persistant_config(self.tripartiteWidget.axes,
                              self.plotConfigFiles["tripartite"])
        self.tripartiteWidget.draw()

    def update_plots(self, tts: AppClasses.TimeSeries):
        """
        Update all the plots.

        Currently all the plots are redrawn. This is inefficient and time consuming.
        A better approach would be to only update the data. However, this didn't work
        as the axes weren't updating according to new data.
        QChart may be a better alternative, but latex symbols for legends aren't possible currently.
        """
        QApplication.setOverrideCursor(Qt.WaitCursor)
        mpl.style.use(self.mplStylesheetCombo.currentText())
        self.update_ts_plot(tts)
        self.update_its_plot(tts)
        self.update_iits_plot(tts)
        self.update_fs_amp_plot(tts)
        self.update_fs_phase_plot(tts)
        self.update_fs_unwrappedphase_plot(tts)
        self.update_ps_amp_plot(tts)
        self.update_psa_plot(tts)
        self.update_tripartite_plot(tts)
        QApplication.restoreOverrideCursor()

def set_persistant_config(ax, confFile):
    config = configparser.ConfigParser()
    config.read(confFile)
    gen = config["general"]
    ax.set_title(gen["title"])
    ax.title.set_fontsize(gen["titlefontsize"])
    if confFile.name != "_tripartite.rc":
        ax.set_xlim(left=0, right=None)
    if confFile.name == "_psa.rc":
        ax.set_xlim(left=0, right=float(gen["xmax"]))
    ax.set_xlabel(gen["xlabel"])
    ax.set_xscale(gen["xscale"])
    # ax._axis_map["x"].label.set_size(gen["xlabelfontsize"])
    # ax.set_ylim(bottom=0.0, top=None)
    ax.set_ylabel(gen["ylabel"])
    ax.set_yscale(gen["yscale"])
    # ax._axis_map["y"].label.set_size(gen["ylabelfontsize"])

    for i, line in enumerate(ax.lines):
        c = config[f"curve{i}"]
        line.set_label(c["label"])
        line.set_linestyle(c["linestyle"])
        line.set_drawstyle(c["drawstyle"])
        line.set_linewidth(c["linewidth"])
        # line.set_color(colors.to_rgba(c["color"]))
        # line.set_alpha(c["alpha"])
        if c["markerstyle"] != 'none':
            line.set_marker(c["markerstyle"])
            line.set_markersize(c["markersize"])
            # line.set_markerfacecolor(c["markerfacecolor"])
            # line.set_markeredgecolor(c["markeredgecolor"])

def set_default_config():
    f = os.path.abspath(__file__)
    defConfigPath = Path(f).parent / "defaultConfigs"
    for file in defConfigPath.glob("*.rc"):
        shutil.copy(file, plotConfig.pegmaConfigDir)


def add_persistant_config(ax, confFile):
    if Path(confFile).exists():
        set_persistant_config(ax, confFile)
    else:
        set_default_config()
        set_persistant_config(ax, confFile)


def run_app(data={"data": [], "plotConfigFiles": plotConfig.plotConfigFiles}):
    qapp = QApplication(sys.argv)
    mw = ui.ui_mainwindow.QMainWindow()
    app = App(mw, data)
    mw.show()
    sys.exit(qapp.exec())


if __name__ == "__main__":
    # ts1 = ep.read_peer_nga_file("/home/digvijay/tmp/eqpyTests/RSN77_SFERN_PUL164.AT2", scale_factor=9.81)
    # ts2 = ep.read_peer_nga_file("/home/digvijay/tmp/eqpyTests/RSN77_SFERN_PUL164.AT2", scale_factor=1.0)
    # tts1 = AppClasses.TimeSeries([ts1], source="peer")
    # tts2 = AppClasses.TimeSeries([ts2], source="peer")
    # data = [tts1, tts2]
    data = []
    dataDict = {
        "data": data,
        "plotConfigFiles": plotConfig.plotConfigFiles
    }
    run_app(dataDict)
