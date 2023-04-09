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
import os
import numpy as np
from PySide6.QtCore import QAbstractListModel, QAbstractTableModel, QModelIndex
from PySide6.QtCore import Qt
from . import AppClasses
import earthquakepy as ep



class TsListModel(QAbstractListModel):

    def __init__(self, tsData=[], parent=None) -> None:
        super(TsListModel, self).__init__(parent)
        self._tsData = tsData

    def rowCount(self, parent) -> int:
        return len(self._tsData)
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            tsName = os.path.basename(self._tsData[index.row()].ts.filepath)
            return tsName
    
    def insertRows(self, row: int, count: int, tts:AppClasses.TimeSeries, parent=QModelIndex()) -> bool:
        self.beginInsertRows(QModelIndex(), row, row + count - 1)

        for i in range(count):
            self._tsData.insert(row, tts)
        self.endInsertRows()
        return True
    
    def removeRows(self, row: int, count: int, parent=QModelIndex()) -> bool:
        self.beginRemoveRows(QModelIndex(), row, count - 1)

        for i in range(count):
            del(self._tsData[row])  # self._tsData[row])

        self.dataChanged.emit(row, row)

        self.endRemoveRows()
        return True
        

class TsTableModel(QAbstractTableModel):

    def __init__(self, ts, clipboard, parent=None) -> None:
        super(TsTableModel, self).__init__(parent)
        self._ts = ts
        self._clipb = clipboard
        self._data = np.array([self._ts.t, self._ts.y]).T

    def rowCount(self, parent) -> int:
        return self._ts.npts
    
    def columnCount(self, parent) -> int:
        return 2
    
    def data(self, index, role):
        row = index.row()
        column = index.column()

        if role == Qt.DisplayRole:
            return f"{np.format_float_scientific(self._data[row, column], precision=4, trim='k', unique=False):>11s}"
        
    def headerData(self, section, orientation, role):
        header = ["t", "y"]
        
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return header[section]
            if orientation == Qt.Vertical:
                return str(section+1)
        
    def copy_to_clipboard(self):
        out = "t, y\n"
        for t, y in self._data:
            out += f"{t}, {y}\n"
        self._clipb.setText(out)


class DELMinmaxTableModel(QAbstractTableModel):

    def __init__(self, ts, parent=None) -> None:
        super(DELMinmaxTableModel, self).__init__(parent)
        self._ts = ts
        maxi = np.argmax(ts.y)
        mini = np.argmin(ts.y)
        ymax = ts.y[maxi]
        ymin = ts.y[mini]
        tmax = ts.t[maxi]
        tmin = ts.t[mini]
        amaxi = np.argmax(np.abs(ts.y))
        peak = np.abs(ts.y[amaxi])
        tpeak = ts.t[amaxi]
        self._data = [
            [peak, tpeak],
            [ymax, tmax],
            [ymin, tmin]
        ]

    def rowCount(self, parent) -> int:
        return len(self._data)
    
    def columnCount(self, parent) -> int:
        return len(self._data[0])
    
    def data(self, index, role):
        row = index.row()
        column = index.column()

        if role == Qt.DisplayRole:
            return np.format_float_scientific(self._data[row][column], precision=4, trim="k", unique=False)
        
    def headerData(self, section, orientation, role):
        header = ["y", "@t"]
        rows = ["|Max|", "Max", "Min"]
        
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return header[section]
            if orientation == Qt.Vertical:
                return str(rows[section])


class TsPropsTableModel(QAbstractTableModel):
    """Combine all the timeseries properties into one class."""
    def __init__(self, tsProps: AppClasses.TimeseriesProps, parent=None) -> None:

        super(TsPropsTableModel, self).__init__(parent)
        self.ts = tsProps.ts
        self.its = tsProps.its
        self.iits = tsProps.iits
        self._clipb = tsProps.clipb

        # imax = np.argmax([self.ts.y, self.its.y, self.iits.y], axis=1)
        # imin = np.argmin([self.ts.y, self.its.y, self.iits.y], axis=1)
        iabsmax = np.argmax(np.abs([self.ts.y, self.its.y, self.iits.y]), axis=1)
        # Amax, Vmax, Dmax = self.ts.y[imax[0]], self.its.y[imax[1]], self.iits.y[imax[2]]
        # tmax = self.ts.t[imax[0]], self.its.t[imax[1]], self.iits.t[imax[2]]
        # Amin, Vmin, Dmin = self.ts.y[imin[0]], self.its.y[imin[1]], self.iits.y[imin[2]]
        # tmin = self.ts.t[imin[0]], self.its.t[imin[1]], self.iits.t[imin[2]]
        Aabsmax, Vabsmax, Dabsmax = np.abs(self.ts.y[iabsmax[0]]), np.abs(self.its.y[iabsmax[1]]), np.abs(self.iits.y[iabsmax[2]])
        tabsmax = self.ts.t[iabsmax[0]], self.its.t[iabsmax[1]], self.iits.t[iabsmax[2]]
        self._data = [
            # ["Amax", Amax, tmax[0]],
            # ["Vmax", Vmax, tmax[1]],
            # ["Dmax", Dmax, tmax[2]],
            # ["Amin", Amin, tmin[0]],
            # ["Vmin", Vmin, tmin[1]],
            # ["Dmin", Dmin, tmin[2]],
            ["PGA", Aabsmax, tabsmax[0]],
            ["PGV", Vabsmax, tabsmax[1]],
            ["PGD", Dabsmax, tabsmax[2]],
            ["2*π*PGV/PGA", Vabsmax / Aabsmax * 2 * np.pi, "None"],
            ["Mean T", self.ts.get_mean_period(), "None"],
            ["Mean Fr (Hz)", self.ts.get_mean_frequency(), "None"],
            ["ε", self.ts.get_epsilon(), "None"],
            ["I_arias", self.ts.get_total_arias(), "None"],
            ["Signf. Durn.", self.ts.get_sig_duration(), "None"],
            ["Destr. Pot.", self.ts.get_destructive_potential(), "None"],
            ["Cumul. | V |", self.ts.get_cum_abs_vel(), "None"],
            ["Cumul. | D |", self.its.get_cum_abs_disp(), "None"],
            ["Sp. energy", self.its.get_specific_energy(), "None"],
            ["A_rms", self.ts.get_rms(), "None"],
            ["V_rms", self.its.get_rms(), "None"],
            ["D_rms", self.iits.get_rms(), "None"],
        ]

        self.tooltips = [
            "PGA: Peak Ground Acceleration",
            "PGV: Peak Ground Velocity",
            "PGD: Peak Ground Displacement",
            "2*π*(PGV / PGA): = T (Period of equivalent harmonic wave).",
            "Mean T: Mean period: Refer Rathje et al [1998]",
            "Mean Fr: Mean square frequency in Hz. Refer Schnabel [1973]",
            "ε: Dimensionless frequency indicator. Refer Clough and Penzien",
            "I_arias: Total arias intensity.",
            "Signf. Durn.: Significant duration of the ground motion encompassing 5 % to 95 % of the total arias intensity.",
            "Destr. Pot.: Destructive potential. Refer Araya and Sargoni [1984].",
            "Cumul. | V |: Cumulative absolute velocity.",
            "Cumul. | D |: Cumulative absolute displacement.",
            "Sp.energy: Specific energy density.",
            "A_rms: Root mean square value of acceleration time history.",
            "V_rms: Root mean square value of velocity time history.",
            "D_rms: Root mean square value of Displacement time history.",
        ]

    def rowCount(self, parent: QModelIndex) -> int:
        return len(self._data)
    
    def columnCount(self, parent: QModelIndex) -> int:
        return 2

    def data(self, index: QModelIndex, role: int):
        row = index.row()
        column = index.column()

        if role == Qt.DisplayRole:
            if type(self._data[row][column+1]) in [float, int, np.float_, np.int_]:
                v = np.format_float_scientific(self._data[row][column+1], precision=4, unique=False, trim="k")
                return f"{v:>11s}"
            else:
                return self._data[row][column+1]

        if role == Qt.ToolTipRole:
            return self.tooltips[row]

        self.dataChanged.emit(row, column)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        header = ["Value", "@t"]

        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return header[section]
            if orientation == Qt.Vertical:
                return f"{self._data[section][0]:>12s}"

    def copy_to_clipboard(self):
        out = "Param, Value, @t\n"
        for p, v, t in self._data:
            out += f"{p}, {v}, {t}\n"
        self._clipb.setText(out)
            
class DELTsPropsTableModel(QAbstractTableModel):
    """Combine all the timeseries properties into one class."""
    def __init__(self, tts: AppClasses.TimeSeries, clipboard, parent=None) -> None:
        super(TsPropsTableModel, self).__init__(parent)
        self.ts = tts.ts
        self.its = tts.its
        self.iits = tts.iits
        self._clipb = clipboard

        # imax = np.argmax([self.ts.y, self.its.y, self.iits.y], axis=1)
        # imin = np.argmin([self.ts.y, self.its.y, self.iits.y], axis=1)
        iabsmax = np.argmax(np.abs([self.ts.y, self.its.y, self.iits.y]), axis=1)
        # Amax, Vmax, Dmax = self.ts.y[imax[0]], self.its.y[imax[1]], self.iits.y[imax[2]]
        # tmax = self.ts.t[imax[0]], self.its.t[imax[1]], self.iits.t[imax[2]]
        # Amin, Vmin, Dmin = self.ts.y[imin[0]], self.its.y[imin[1]], self.iits.y[imin[2]]
        # tmin = self.ts.t[imin[0]], self.its.t[imin[1]], self.iits.t[imin[2]]
        Aabsmax, Vabsmax, Dabsmax = np.abs(self.ts.y[iabsmax[0]]), np.abs(self.its.y[iabsmax[1]]), np.abs(self.iits.y[iabsmax[2]])
        tabsmax = self.ts.t[iabsmax[0]], self.its.t[iabsmax[1]], self.iits.t[iabsmax[2]]
        self._data = [
            # ["Amax", Amax, tmax[0]],
            # ["Vmax", Vmax, tmax[1]],
            # ["Dmax", Dmax, tmax[2]],
            # ["Amin", Amin, tmin[0]],
            # ["Vmin", Vmin, tmin[1]],
            # ["Dmin", Dmin, tmin[2]],
            ["PGA", Aabsmax, tabsmax[0]],
            ["PGV", Vabsmax, tabsmax[1]],
            ["PGD", Dabsmax, tabsmax[2]],
            ["2*π*PGV/PGA", Vabsmax / Aabsmax * 2 * np.pi, "None"],
            ["Mean T", self.ts.get_mean_period(), "None"],
            ["Mean Fr (Hz)", self.ts.get_mean_frequency(), "None"],
            ["ε", self.ts.get_epsilon(), "None"],
            ["I_arias", self.ts.get_total_arias(), "None"],
            ["Signf. Durn.", self.ts.get_sig_duration(), "None"],
            ["Destr. Pot.", self.ts.get_destructive_potential(), "None"],
            ["Cumul. | V |", self.ts.get_cum_abs_vel(), "None"],
            ["Cumul. | D |", self.its.get_cum_abs_disp(), "None"],
            ["Sp. energy", self.its.get_specific_energy(), "None"],
            ["A_rms", self.ts.get_rms(), "None"],
            ["V_rms", self.its.get_rms(), "None"],
            ["D_rms", self.iits.get_rms(), "None"],
        ]

        self.tooltips = [
            "PGA: Peak Ground Acceleration",
            "PGV: Peak Ground Velocity",
            "PGD: Peak Ground Displacement",
            "2*π*(PGV / PGA): = T (Period of equivalent harmonic wave).",
            "Mean T: Mean period: Refer Rathje et al [1998]",
            "Mean Fr: Mean square frequency in Hz. Refer Schnabel [1973]",
            "ε: Dimensionless frequency indicator. Refer Clough and Penzien",
            "I_arias: Total arias intensity.",
            "Signf. Durn.: Significant duration of the ground motion encompassing 5 % to 95 % of the total arias intensity.",
            "Destr. Pot.: Destructive potential. Refer Araya and Sargoni [1984].",
            "Cumul. | V |: Cumulative absolute velocity.",
            "Cumul. | D |: Cumulative absolute displacement.",
            "Sp.energy: Specific energy density.",
            "A_rms: Root mean square value of acceleration time history.",
            "V_rms: Root mean square value of velocity time history.",
            "D_rms: Root mean square value of Displacement time history.",
        ]

    def rowCount(self, parent: QModelIndex) -> int:
        return len(self._data)
    
    def columnCount(self, parent: QModelIndex) -> int:
        return 2

    def data(self, index: QModelIndex, role: int):
        row = index.row()
        column = index.column()

        if role == Qt.DisplayRole:
            if type(self._data[row][column+1]) in [float, int, np.float_, np.int_]:
                v = np.format_float_scientific(self._data[row][column+1], precision=4, unique=False, trim="k")
                return f"{v:>11s}"
            else:
                return self._data[row][column+1]

        if role == Qt.ToolTipRole:
            return self.tooltips[row]

    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        header = ["Value", "@t"]

        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return header[section]
            if orientation == Qt.Vertical:
                return self._data[section][0]

    def copy_to_clipboard(self):
        out = "Param, Value, @t\n"
        for p, v, t in self._data:
            out += f"{p}, {v}, {t}\n"
        self._clipb.setText(out)



class MetadataTable(QAbstractTableModel):

    def __init__(self, ts, parent=None) -> None:
        """For earthquake metadata"""
        super(MetadataTable, self).__init__(parent)
        self._ts = ts
        self._data = []
        for k, v in ts.__dict__.items():
            if k not in ["t", "y"]:
                self._data.append([k, v])
        # self._data.append(["Notes", ""])
    
    def rowCount(self, parent) -> int:
        return len(self._data)
    
    def columnCount(self, parent) -> int:
        return len(self._data[0])
    
    def data(self, index, role):
        row = index.row()
        column = index.column()

        if role == Qt.DisplayRole:
            return str(self._data[row][column])

        if role == Qt.EditRole:
            return str(self._data[row][column])
    
    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        header = ["Parameter", "Value"]
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return header[section]

    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        return super().flags(index) | Qt.ItemIsEditable

    def setData(self, index: QModelIndex, value, role: int) -> bool:
        row = index.row()
        column = index.column()
        if role == Qt.EditRole:
            self._data[row][column] = value
            setattr(self._ts, str(self._data[row][0]), value)
            return True
        return False
        

class FourierTableModel(QAbstractTableModel):

    def __init__(self, tts, clipboard, parent=None) -> None:
        super(FourierTableModel, self).__init__(parent)
        self._fs = tts.fs
        self._ps = tts.ps
        N = self._fs.N //2
        self._clipb = clipboard
        self._data = np.array([self._fs.frequencies[0:N], self._fs.amplitude[0:N], self._fs.phase[0:N], self._ps.amplitude[0:N]]).T

    def rowCount(self, parent):
        return self._fs.N // 2
    
    def columnCount(self, parent):
        return 4
    
    def data(self, index, role):

        row = index.row()
        column = index.column()

        if role == Qt.DisplayRole:
            return np.format_float_scientific(self._data[row][column], precision=4, trim="k", unique=False)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):

        header = ["Frequency (Hz)", "Fourier Amplitude", "Phase", "Power Amplitude"]

        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return header[section]

            if orientation == Qt.Vertical:
                return str(section+1)

    def copy_to_clipboard(self):
        out = "Frequency_Hz, Fourier_Amplitude, Phase, Power_Amplitude\n"
        for (fr, fsA, ph, psA) in self._data:
            out += f"{fr}, {fsA}, {ph}, {psA}\n"
        self._clipb.setText(out)


class ResponseSpectraTableModel(QAbstractTableModel):

    def __init__(self, rs, clipboard, parent=None) -> None:
        super(ResponseSpectraTableModel, self).__init__(parent)
        self._rs = rs
        self._clipb = clipboard
        self._data = np.array([self._rs.T, self._rs.Sd, self._rs.Sv, self._rs.Sa, self._rs.PSv, self._rs.PSa]).T

    def rowCount(self, parent):
        return len(self._rs.T)
    
    def columnCount(self, parent):
        return 6
    
    def data(self, index, role):

        row = index.row()
        column = index.column()

        if role == Qt.DisplayRole:
            return np.format_float_scientific(self._data[row][column], precision=4, trim="k", unique=False)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):

        header = ["Period (s)", "Sd", "Sv", "Sa", "PSv", "PSa"]

        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return header[section]

            if orientation == Qt.Vertical:
                return str(section+1)

    def setData(self, index: QModelIndex, value, role, rs) -> bool:
        row = index.row()
        column = index.column()
        self.dataChanged.emit(row, column)
        return True
        # if role == Qt.DisplayRole:
        #     self._data[row, 5] = rs.PSa[row]
        #     return True            
        # return False
    
    def copy_to_clipboard(self):
        out = "Period_s, Sd, Sv, Sa, PSv, PSa\n"
        for (t, sd, sv, sa, psv, psa) in self._data:
            out += f"{t}, {sd}, {sv}, {sa}, {psv}, {psa}\n"
        self._clipb.setText(out)


class FrequencyCharacteristicsTableModel(QAbstractTableModel):

    def __init__(self, charTable:AppClasses.FreqChar, clipboard, parent=None) -> None:
        super(FrequencyCharacteristicsTableModel, self).__init__(parent)
        self._clipb = clipboard
        self._data = [
            ["Fp (Hz)", f"{charTable.fp:.4f}"],
            ["Tp (s)", charTable.Tp],
            ["Band (Hz)", charTable.band],
            ["Bandwidth (Hz)", charTable.bandwidth],
            ["0th Moment", f"{charTable.ps.get_nth_moment(n=0):.4f}"],
            ["1st Moment", f"{charTable.ps.get_nth_moment(n=1):.4f}"],
            ["2nd Moment", f"{charTable.ps.get_nth_moment(n=2):.4f}"],
            ["Central Freq (Hz)", f"{charTable.ps.centralFreq:.4f}"],
            ["Shape factor", f"{charTable.ps.shapeFactor:.4f}"],
        ]

        self.tooltips = [
            "Fp: Predominant frequency: Frequency corresponding to the peak amplitude of the smoothed Fourier amplitude spectrum.",
            "Tp: Predominant period: = 1 / Fp. Period corresponding to the Predominant frequency.",
            "Band: Frequency band: Band of frequencies between the first and last exceedence of the smoothed Fourier amplitude above 1/sqrt(2) * (peak fourier amplitude)",
            "Bandwidth: Width of the frequency band",
            "0th Moment: 0th order moment of power spectrum amplitude. n^th moment = \int (w^n |ps|) dw",
            "1st Moment: 1st order moment of power spectrum amplitude. n^th moment = \int (w^n |ps|) dw",
            "2nd Moment: 2nd order moment of power spectrum amplitude. n^th moment = \int (w^n |ps|) dw",
            "Central Freq: Refer Geotechnical Earthquake Engineering book by Steven Kramer (Page 77).",
            "Shape factor: Refer Geotechnical Earthquake Engineering book by Steven Kramer (Page 77).",
        ]

    def rowCount(self, parent: QModelIndex) -> int:
        return len(self._data)
    
    def columnCount(self, parent: QModelIndex) -> int:
        return 1

    def data(self, index: QModelIndex, role: int):
        row = index.row()
        column = index.column()

        if role == Qt.DisplayRole:
            return str(self._data[row][column+1])

        if role == Qt.ToolTipRole:
            return self.tooltips[row]
        
    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        header = ["Value"]
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return header[section]
            
            if orientation == Qt.Vertical:
                return f"{self._data[section][0]:>20s}"

    def setData(self, index: QModelIndex, value, role: int) -> bool:
        row = index.row()
        column = index.column()
        self.dataChanged.emit(row, column)
        return True

    def copy_to_clipboard(self):
        out = "Parameter, Value\n"
        for p, m in self._data:
            out += f"{p}, {m}\n"
        self._clipb.setText(out)
        

class DesignSpecModel(QAbstractTableModel):

    def __init__(self, ds: AppClasses.DesignSpectrum, parent=None) -> None:
        super(DesignSpecModel, self).__init__(parent)
        self._data = np.array([ds.T, ds.Y]).T

    def rowCount(self, parent: None) -> int:
        return len(self._data)
    
    def columnCount(self, parent: None) -> int:
        return 2

    def data(self, index: QModelIndex, role: int):
        
        row = index.row()
        column = index.column()

        if role == Qt.DisplayRole:
            return f"{self._data[row][column]:.4f}"

    def headerData(self, section: int, orientation: Qt.Orientation, role: int ):
        header = ["Period (s)", "Sa"]
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return header[section]
            if orientation == Qt.Vertical:
                return f"{section+1}"
        return super().headerData(section, orientation, role)
    

class StretchedTimeseriesModel(QAbstractTableModel):

    def __init__(self, tts:AppClasses.TimeSeries, clipboard, parent=None) -> None:
        super(StretchedTimeseriesModel, self).__init__(parent)
        self._tts = tts
        self._clipb = clipboard
        self._data = np.array([self._tts.ts.t, self._tts.ts.y]).T

    def rowCount(self, parent: QModelIndex) -> int:
        return len(self._data)
    
    def columnCount(self, parent: QModelIndex) -> int:
        return 2

    def data(self, index: QModelIndex, role: int):
        row = index.row()
        column = index.column()
        if role == Qt.DisplayRole:
            return np.format_float_scientific(self._data[row][column], trim="k", precision=4, unique=False)
    
    def copy_to_clipboard(self):
        out = "t, y\n"
        for t, y in self._data:
            out += f"{t}, {y}\n"
        self._clipb.setText(out)