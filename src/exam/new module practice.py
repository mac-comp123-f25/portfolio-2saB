import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout


class SimpleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Demo App")
        self.setGeometry(100, 100, 300, 150)

        # Widgets
        self.label = QLabel("Hello! Click the button.", self)
        self.button = QPushButton("Click Me")

        # Connect button to method
        self.button.clicked.connect(self.update_text)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def update_text(self):
        self.label.setText("Button clicked!")

# Main program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleWindow()
    window.show()
    sys.exit(app.exec_())
