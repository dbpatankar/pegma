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
import numpy as np
import scipy.signal
import earthquakepy as ep
# PySide imports
from PySide6.QtCore import QAbstractListModel
from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox, QInputDialog

# Matplotlib
import matplotlib as mpl
import matplotlib.ticker as ticker
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT
from matplotlib.widgets import Cursor
import copy
from . import pgmfigureoptions
from matplotlib.backend_bases import MouseEvent



class TimeSeries:

    def __init__(self, tsList, source:str, xi=0.05, baseCorr="None") -> None:
        """
        Create a TimeSeries object to be used in model view by PySide.

        Parameters
        ----------
        tsList: list of earthquakepy timeseries objects [accel, vel, disp]
        source: name of the source. Can be one from ["peer", "cosmosvdc", "raw", "custom"]
        """
        self.tsList = tsList
        self.baseCorr = baseCorr
        self.xi = xi
        self.source = source
        self.uncorrTs = tsList[0]
        self.ts = copy.deepcopy(tsList[0])
        self.apply_baseline_correction(type=baseCorr)
        self.ts.Notes = ""
        self.fs = tsList[0].get_fourier_spectrum()
        self.fs.T = 1 / self.fs.frequencies[1:]
        self.ps = tsList[0].get_power_spectrum()
        self.ps.T = 1 / self.ps.frequencies[1:]
        Ts = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09]
        Ts.extend(list(np.arange(0.1, 10.01, 0.1)))
        Ts.extend(list(np.arange(20, 100.01, 10)))
        self.rs = tsList[0].get_response_spectra(T=Ts, xi=xi)
        self.freqTable = FreqChar(self.fs, self.ps)
        if source.lower() == "cosmosvdc":
            vel = tsList[1].y
            disp = tsList[2].y
        else:
            vel = tsList[0].get_numerical_int()
            __tmp = ep.timeseries.TimeSeries(tsList[0].t, vel)
            disp = __tmp.get_numerical_int()
        
        self.its = ep.timeseries.TimeSeries(self.ts.t, vel)
        self.iits = ep.timeseries.TimeSeries(self.ts.t, disp)

    def __repr__(self) -> str:
        out = ""
        for k, v in self.__dict__.items():
            out += f"{k:>10s}: {v}"
        return out

    def apply_baseline_correction(self, type="None"):
        if type in ["Constant", "Linear"]:
            self.ts.y = scipy.signal.detrend(self.uncorrTs.y, type=type.lower())
        elif type == "Quadratic":
            polyCoeffs = np.polynomial.Polynomial.fit(self.uncorrTs.t, self.uncorrTs.y, deg=2).coef
            dy = polyCoeffs[0] * self.uncorrTs.t**2 + polyCoeffs[1] * self.uncorrTs.t + polyCoeffs[2]
            self.ts.y = self.uncorrTs.y - dy
        elif type == "Cubic":
            polyCoeffs = np.polynomial.Polynomial.fit(self.uncorrTs.t, self.uncorrTs.y, deg=3).coef
            dy = polyCoeffs[0] * self.uncorrTs.t**3 + polyCoeffs[1] * self.uncorrTs.t**2 + polyCoeffs[2] * self.uncorrTs.t + polyCoeffs[3]
            self.ts.y = self.uncorrTs.y - dy
        elif type == "None":
            self.ts.y = self.uncorrTs.y

    def recompute(self, baseCorr="None"):
        self.apply_baseline_correction(type=baseCorr)
        self.fs = self.ts.get_fourier_spectrum()
        self.fs.T = 1 / self.fs.frequencies[1:]
        self.ps = self.ts.get_power_spectrum()
        self.ps.T = 1 / self.ps.frequencies[1:]
        Ts = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09]
        Ts.extend(list(np.arange(0.1, 10.01, 0.1)))
        Ts.extend(list(np.arange(20, 100.01, 10)))
        self.rs = self.ts.get_response_spectra(T=Ts, xi=self.xi)
        self.freqTable = FreqChar(self.fs, self.ps)
        if self.source.lower() == "cosmosvdc":
            vel = self.tsList[1].y
            disp = self.tsList[2].y
        else:
            vel = self.ts.get_numerical_int()
            __tmp = ep.timeseries.TimeSeries(self.ts.t, vel)
            disp = __tmp.get_numerical_int()
        
        self.its = ep.timeseries.TimeSeries(self.ts.t, vel)
        self.iits = ep.timeseries.TimeSeries(self.ts.t, disp)




class PegmaNavigationToolbar2QT(NavigationToolbar2QT):

    def __init__(self, canvas, qtWidget, configFile=None) -> None:
        super().__init__(canvas, qtWidget)
        self.configFile = configFile

    def edit_parameters(self):
        axes = self.canvas.figure.get_axes()
        if not axes:
            QMessageBox.warning(
                self.canvas.parent(), "Error", "There are no axes to edit.")
            return
        elif len(axes) == 1:
            ax, = axes
        else:
            titles = [
                ax.get_label() or
                ax.get_title() or
                ax.get_title("left") or
                ax.get_title("right") or
                " - ".join(filter(None, [ax.get_xlabel(), ax.get_ylabel()])) or
                f"<anonymous {type(ax).__name__}>"
                for ax in axes]
            duplicate_titles = [
                title for title in titles if titles.count(title) > 1]
            for i, ax in enumerate(axes):
                if titles[i] in duplicate_titles:
                    titles[i] += f" (id: {id(ax):#x})"  # Deduplicate titles.
            item, ok = QInputDialog.getItem(
                self.canvas.parent(),
                'Customize', 'Select axes:', titles, 0, False)
            if not ok:
                return
            ax = axes[titles.index(item)]
        pgmfigureoptions.figure_edit(ax, self)


class AnnotatedCursor(Cursor):
    """
    A crosshair cursor like `~matplotlib.widgets.Cursor` with a text showing \
    the current coordinates.

    For the cursor to remain responsive you must keep a reference to it.
    The data of the axis specified as *dataaxis* must be in ascending
    order. Otherwise, the `numpy.searchsorted` call might fail and the text
    disappears. You can satisfy the requirement by sorting the data you plot.
    Usually the data is already sorted (if it was created e.g. using
    `numpy.linspace`), but e.g. scatter plots might cause this problem.
    The cursor sticks to the plotted line.

    Parameters
    ----------
    line : `matplotlib.lines.Line2D`
        The plot line from which the data coordinates are displayed.

    numberformat : `python format string <https://docs.python.org/3/\
    library/string.html#formatstrings>`_, optional, default: "{0:.4g};{1:.4g}"
        The displayed text is created by calling *format()* on this string
        with the two coordinates.

    offset : (float, float) default: (5, 5)
        The offset in display (pixel) coordinates of the text position
        relative to the cross-hair.

    dataaxis : {"x", "y"}, optional, default: "x"
        If "x" is specified, the vertical cursor line sticks to the mouse
        pointer. The horizontal cursor line sticks to *line*
        at that x value. The text shows the data coordinates of *line*
        at the pointed x value. If you specify "y", it works in the opposite
        manner. But: For the "y" value, where the mouse points to, there might
        be multiple matching x values, if the plotted function is not biunique.
        Cursor and text coordinate will always refer to only one x value.
        So if you use the parameter value "y", ensure that your function is
        biunique.

    Other Parameters
    ----------------
    textprops : `matplotlib.text` properties as dictionary
        Specifies the appearance of the rendered text object.

    **cursorargs : `matplotlib.widgets.Cursor` properties
        Arguments passed to the internal `~matplotlib.widgets.Cursor` instance.
        The `matplotlib.axes.Axes` argument is mandatory! The parameter
        *useblit* can be set to *True* in order to achieve faster rendering.

    """

    def __init__(self, line, numberformat="{0:.4g};{1:.4g}", offset=(5, 5),
                 dataaxis='x', textprops=None, **cursorargs):
        if textprops is None:
            textprops = {}
        # The line object, for which the coordinates are displayed
        self.line = line
        # The format string, on which .format() is called for creating the text
        self.numberformat = numberformat
        # Text position offset
        self.offset = np.array(offset)
        # The axis in which the cursor position is looked up
        self.dataaxis = dataaxis

        # First call baseclass constructor.
        # Draws cursor and remembers background for blitting.
        # Saves ax as class attribute.
        super().__init__(**cursorargs)

        # Default value for position of text.
        self.set_position(self.line.get_xdata()[0], self.line.get_ydata()[0])
        # Create invisible animated text
        self.text = self.ax.text(
            self.ax.get_xbound()[0],
            self.ax.get_ybound()[0],
            "0, 0",
            animated=bool(self.useblit),
            visible=False, **textprops)
        # The position at which the cursor was last drawn
        self.lastdrawnplotpoint = None

    def onmove(self, event):
        """
        Overridden draw callback for cursor. Called when moving the mouse.
        """

        # Leave method under the same conditions as in overridden method
        if self.ignore(event):
            self.lastdrawnplotpoint = None
            return
        if not self.canvas.widgetlock.available(self):
            self.lastdrawnplotpoint = None
            return

        # If the mouse left drawable area, we now make the text invisible.
        # Baseclass will redraw complete canvas after, which makes both text
        # and cursor disappear.
        if event.inaxes != self.ax:
            self.lastdrawnplotpoint = None
            self.text.set_visible(False)
            super().onmove(event)
            return

        # Get the coordinates, which should be displayed as text,
        # if the event coordinates are valid.
        plotpoint = None
        if event.xdata is not None and event.ydata is not None:
            # Get plot point related to current x position.
            # These coordinates are displayed in text.
            plotpoint = self.set_position(event.xdata, event.ydata)
            # Modify event, such that the cursor is displayed on the
            # plotted line, not at the mouse pointer,
            # if the returned plot point is valid
            if plotpoint is not None:
                event.xdata = plotpoint[0]
                event.ydata = plotpoint[1]

        # If the plotpoint is given, compare to last drawn plotpoint and
        # return if they are the same.
        # Skip even the call of the base class, because this would restore the
        # background, draw the cursor lines and would leave us the job to
        # re-draw the text.
        if plotpoint is not None and plotpoint == self.lastdrawnplotpoint:
            return

        # Baseclass redraws canvas and cursor. Due to blitting,
        # the added text is removed in this call, because the
        # background is redrawn.
        super().onmove(event)

        # Check if the display of text is still necessary.
        # If not, just return.
        # This behaviour is also cloned from the base class.
        if not self.get_active() or not self.visible:
            return

        # Draw the widget, if event coordinates are valid.
        if plotpoint is not None:
            # Update position and displayed text.
            # Position: Where the event occurred.
            # Text: Determined by set_position() method earlier
            # Position is transformed to pixel coordinates,
            # an offset is added there and this is transformed back.
            temp = [event.xdata, event.ydata]
            temp = self.ax.transData.transform(temp)
            temp = temp + self.offset
            temp = self.ax.transData.inverted().transform(temp)
            self.text.set_position(temp)
            self.text.set_text(self.numberformat.format(*plotpoint))
            self.text.set_visible(self.visible)

            # Tell base class, that we have drawn something.
            # Baseclass needs to know, that it needs to restore a clean
            # background, if the cursor leaves our figure context.
            self.needclear = True

            # Remember the recently drawn cursor position, so events for the
            # same position (mouse moves slightly between two plot points)
            # can be skipped
            self.lastdrawnplotpoint = plotpoint
        # otherwise, make text invisible
        else:
            self.text.set_visible(False)

        # Draw changes. Cannot use _update method of baseclass,
        # because it would first restore the background, which
        # is done already and is not necessary.
        if self.useblit:
            self.ax.draw_artist(self.text)
            self.canvas.blit(self.ax.bbox)
        else:
            # If blitting is deactivated, the overridden _update call made
            # by the base class immediately returned.
            # We still have to draw the changes.
            self.canvas.draw_idle()

    def set_position(self, xpos, ypos):
        """
        Finds the coordinates, which have to be shown in text.

        The behaviour depends on the *dataaxis* attribute. Function looks
        up the matching plot coordinate for the given mouse position.

        Parameters
        ----------
        xpos : float
            The current x position of the cursor in data coordinates.
            Important if *dataaxis* is set to 'x'.
        ypos : float
            The current y position of the cursor in data coordinates.
            Important if *dataaxis* is set to 'y'.

        Returns
        -------
        ret : {2D array-like, None}
            The coordinates which should be displayed.
            *None* is the fallback value.
        """

        # Get plot line data
        xdata = self.line.get_xdata()
        ydata = self.line.get_ydata()

        # The dataaxis attribute decides, in which axis we look up which cursor
        # coordinate.
        if self.dataaxis == 'x':
            pos = xpos
            data = xdata
            lim = self.ax.get_xlim()
        elif self.dataaxis == 'y':
            pos = ypos
            data = ydata
            lim = self.ax.get_ylim()
        else:
            raise ValueError(f"The data axis specifier {self.dataaxis} should "
                             f"be 'x' or 'y'")

        # If position is valid and in valid plot data range.
        if pos is not None and lim[0] <= pos <= lim[-1]:
            # Find closest x value in sorted x vector.
            # This requires the plotted data to be sorted.
            index = np.searchsorted(data, pos)
            # Return none, if this index is out of range.
            if index < 0 or index >= len(data):
                return None
            # Return plot point as tuple.
            return (xdata[index], ydata[index])

        # Return none if there is no good related point for this x position.
        return None

    def clear(self, event):
        """
        Overridden clear callback for cursor, called before drawing the figure.
        """

        # The base class saves the clean background for blitting.
        # Text and cursor are invisible,
        # until the first mouse move event occurs.
        super().clear(event)
        if self.ignore(event):
            return
        self.text.set_visible(False)

    def _update(self):
        """
        Overridden method for either blitting or drawing the widget canvas.

        Passes call to base class if blitting is activated, only.
        In other cases, one draw_idle call is enough, which is placed
        explicitly in this class (see *onmove()*).
        In that case, `~matplotlib.widgets.Cursor` is not supposed to draw
        something using this method.
        """

        if self.useblit:
            super()._update()

class MatplotlibWidget(FigureCanvasQTAgg):

    def __init__(self, parent=None, **kwargs):
        super(MatplotlibWidget, self).__init__(parent)

        figure = Figure(layout="constrained")
        self.canvas = FigureCanvasQTAgg(figure)
        self.axes = figure.add_subplot()
        # self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.toolbar = PegmaNavigationToolbar2QT(self.canvas, self, configFile=kwargs["configFile"])
        self.toolbar.setMinimumWidth(450)
        self.toolbar.setMaximumHeight(30)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)

    def add_cursor(self):
        self.cursor = AnnotatedCursor(self.axes.lines[0], 
                                      ax=self.axes,
                                      dataaxis="x",
                                      numberformat="{0:.2f}; {1:.2f}",
                                      offset=(20, 0),
                                      textprops={"color": "red", 
                                                 "fontweight": "normal",
                                                 "backgroundcolor": "white",
                                                 "bbox": {"boxstyle": "square", "fc": "white"},},
                                      useblit=True,
                                      color="red",
                                      linewidth=0.4)
        t = self.axes.transData
        MouseEvent(
            "motion_notify_event", self.axes.figure.canvas, *t.transform((-2, 10))
        )._process()


class TripartitePlot:

    def __init__(self, rs:ep.timeseries.ResponseSpectra, ax:mpl.figure.Axes.axes) -> None:
        self.rs = rs
        self.psvStart, self.psvEnd = [rs.PSv[0], rs.PSv[-1]]
        self.Tstart, self.Tend = [rs.T[0], rs.T[-1]]
        self.Tmin = self.Tstart / 10
        self.Tmax = self.Tend * 10
        # self.psvMin = self.psvStart / 10
        # self.psvMax = np.max(rs.PSv) * 10
        self.psvMin = 10**np.floor(np.log10(np.min(self.rs.PSv))) / 10
        self.psvMax = np.max(self.rs.PSv) * 10

        self.sdMin = 1 / (2*np.pi) * self.Tmin * self.psvMin
        self.sdMax = 1 / (2*np.pi) * self.Tmax * self.psvMax

        self.psaMin = (2*np.pi) * self.psvMin  / self.Tmax
        self.psaMax = (2*np.pi) * self.psvMax / self.Tmin

        # self.TGridValues = self.get_grid_values(self.Tmin, self.Tmax)
        # self.PSvGridValues = self.get_grid_values(self.psvMin, self.psvMax)
        self.dispGridValues = self.get_grid_values(self.sdMin, self.sdMax)
        self.accGridValues = self.get_grid_values(self.psaMin, self.psaMax)
        
        X, Y = np.meshgrid(np.logspace(-3, 3, 100), np.logspace(-5, 5, 100))
        A = 2 * np.pi * Y / X
        D = Y * X / (2*np.pi)

        # ax.set_xlim(self.Tmin, self.Tmax)
        # ax.set_ylim(self.psvMin, self.psvMax)

        c1 = ax.contour(X, Y, A, levels=self.accGridValues, colors="red", linewidths=0.4, alpha=0.4)
        self.c2 = ax.contour(X, Y, A, levels=self.accGridValues[::9], colors="red", linewidths=0.8, alpha=1.0)
        c3 = ax.contour(X, Y, D, levels=self.dispGridValues, colors="blue", linewidths=0.4, alpha=0.4)
        self.c4 = ax.contour(X, Y, D, levels=self.dispGridValues[::9], colors="blue", linewidths=0.8, alpha=1.0)
        fmt = ticker.LogFormatterMathtext()
        fmt.create_dummy_axis()
        self.get_acc_label_locations()
        self.get_disp_label_locations()

        for val, t, v in self.dispTickPositions[1:-1]:
            ax.annotate(f"{10**(np.round(np.log10(val)))}", xy=[t, v], rotation=-45, ha="right", color="blue",
                        bbox=dict(fc="white"))
        for val, t, v in self.accTickPositions[1:-1]:
            ax.annotate(f"{10**(np.round(np.log10(val)))}", xy=[t, v], rotation=45, ha="left", color="red", 
                        bbox=dict(fc="white"))
        c5 = ax.contour(X, Y, A, levels=[self.dispAxisLineLevel], colors="blue", linewidths=1.4, alpha=1.0)
        c6 = ax.contour(X, Y, D, levels=[self.accAxisLineLevel], colors="red", linewidths=1.4, alpha=1.0)
        ax.annotate(r"S$_D\rightarrow$", xy=self.dispLabelPosition, rotation=45, color="blue", 
                    va="top", ha="right",
                    bbox=dict(fc="white"))
        ax.annotate(r"$\leftarrow$ PS$_a$", xy=self.accLabelPosition, rotation=-45, color="red", 
                    va="top", ha="left",
                    bbox=dict(fc="white"))
        ax.plot(rs.T, rs.PSv, color="k", linewidth=2)
        ax.set_xscale("log")
        ax.set_yscale("log")
        # ax.set_xlabel("Period (s)")
        # ax.set_ylabel(r"PS$_v$")
        ax.set_aspect("equal", "box")
        ax.set_xlim(self.Tmin, self.Tmax)
        ymin = 10**np.floor(np.log10(np.min(self.rs.PSv)))
        ax.set_ylim(ymin, self.psvMax)

    def get_grid_values(self, min, max):
        logMin = np.floor(np.log10(min))
        logMax = np.ceil(np.log10(max))
        majorVals = 10**np.arange(logMin, logMax+1e-3, 1)
        gvals = []
        for i, v in enumerate(majorVals[:-1]):
            tl = np.arange(v, majorVals[i+1], v)
            gvals.extend(list(tl))
        return gvals

    def clabel_formatter(self, labelVal):
        return np.format_float_scientific(labelVal, unique=False, precision=1)

    def get_disp_label_locations(self):
        locations = []
        psaStart = 2*np.pi / self.rs.T[0] * self.rs.PSv[0]
        self.dispAxisLineLevel = 10**np.ceil(np.log10(np.max(self.rs.PSa)))
        T = 2*np.pi * np.sqrt(self.dispGridValues[::9]/self.dispAxisLineLevel)
        V = self.dispAxisLineLevel * T / (2*np.pi)
        for i, v in enumerate(V):
            if T[i] > self.Tmin and T[i] < self.Tmax and v > self.psvMin and v < self.psvMax:
                locations.append([self.dispGridValues[::9][i], T[i], v])
        labelPosY = self.dispAxisLineLevel * 20 * 1e-2 / (2*np.pi)
        self.dispLabelPosition = (1e-2, labelPosY)
        self.dispTickPositions = locations

    def get_acc_label_locations(self):
        locations = []
        sdEnd = self.rs.T[-1] * self.rs.PSv[-1] / (2*np.pi)
        self.accAxisLineLevel = 10**np.ceil(np.log10(np.max(self.rs.Sd)))
        T = 2*np.pi * np.sqrt(self.accAxisLineLevel / self.accGridValues[::9])
        V = (2*np.pi) / T * self.accAxisLineLevel
        for i, v in enumerate(V):
            if T[i] > self.Tmin and T[i] < self.Tmax and v > self.psvMin and v < self.psvMax:
                locations.append([self.accGridValues[::9][i], T[i], v])
        labelPosY = 2*np.pi * self.accAxisLineLevel * 15 / 1e2 
        self.accLabelPosition = (1e2, labelPosY)
        self.accTickPositions = locations


class FreqChar:
    """Store frequency related characteristics of the timeseries."""
    def __init__(self, fs: ep.timeseries.FourierSpectrum, ps: ep.timeseries.PowerSpectrum, winLen=50, poly=2) -> None:
        """Each attribute should only be a scalar value. Arrays will be ignored by tableViewModel."""
        self.fs = fs
        self.ps = ps
        self.get_tp_bandwidth(winLen=winLen, poly=poly)

    def get_tp_bandwidth(self, winLen=50, poly=2):
        N = self.fs.N // 2
        freq = self.fs.frequencies[0:N]
        amp = self.fs.amplitude[0:N]
        yf = scipy.signal.savgol_filter(amp, window_length=winLen, polyorder=poly)
        imax = np.argmax(yf)
        ymax = yf[imax]
        self.fp = freq[imax]
        self.Tp = f"{(1 / self.fp):.4f}"
        iwidth = np.where(yf > ymax/np.sqrt(2))[0]
        self.band = f"{freq[iwidth[0]]:.2f} - {freq[iwidth[-1]]:.2f}"
        self.bandwidth = f"{(freq[iwidth[-1]] - freq[iwidth[0]]):.2f}"


class TimeseriesProps:

    def __init__(self, tts: TimeSeries, clipboard, xmin=0, xmax=None) -> None:
        self.clipb = clipboard
        if xmax is None:
            xmax = tts.ts.t[-1]
        boolArr = (tts.ts.t >= xmin) & (tts.ts.t <= xmax)
        self.ts = ep.timeseries.TimeSeries(tts.ts.t[boolArr], tts.ts.y[boolArr])
        self.its = ep.timeseries.TimeSeries(tts.its.t[boolArr], tts.its.y[boolArr])
        self.iits = ep.timeseries.TimeSeries(tts.iits.t[boolArr], tts.iits.y[boolArr])


class DesignSpectrum:
    """Store design spectrum in its own class."""
    def __init__(self, T, Y) -> None:
        """Initiate with period vec T and ordinates Y."""
        self.T = T
        self.Y = Y

    def get_y(self, Tval):
        return np.interp(Tval, self.T, self.Y)