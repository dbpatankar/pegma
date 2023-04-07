
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtWebEngineWidgets import QWebEngineView

class HelpBrowser(QWidget):

    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()
        self.webView = QWebEngineView()
        layout.addWidget(self.webView)
        self.setLayout(layout)
