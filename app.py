import sys

from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QApplication,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Number Toggle")
        self.setMinimumWidth(300)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        self.numer = QSpinBox()
        self.numer.setObjectName("numer")
        self.numer.setRange(0, 10000)
        self.numer.setReadOnly(True)
        self.numer.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.numer.setStyleSheet("QSpinBox { background-color: lightgray; }")
        layout.addWidget(self.numer)

        self.start_button = QPushButton("Start")
        self.start_button.setObjectName("start_button")
        self.start_button.setCheckable(True)
        self.start_button.toggled.connect(self.start_button_method)
        layout.addWidget(self.start_button)

        self.setCentralWidget(central_widget)

    def start_button_method(self, is_checked: bool) -> None:
        self.start_button.setText("Stop" if is_checked else "Start")


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
