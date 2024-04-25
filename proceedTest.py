from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel


class CounterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set up the layout
        layout = QVBoxLayout()

        # Create a label to display the count
        self.label = QLabel('0/3', self)
        layout.addWidget(self.label)

        # Create a button to update the count
        self.button = QPushButton('Increment', self)
        self.button.clicked.connect(self.increment_count)
        layout.addWidget(self.button)

        # Create a "Yay!" button that is initially hidden
        self.yay_button = QPushButton('Yay!', self)
        self.yay_button.hide()  # Start hidden
        layout.addWidget(self.yay_button)

        # Set the layout on the application's window
        self.setLayout(layout)

        # Initialize counter
        self.counter = 0

    def increment_count(self):
        # Increment and update the label if counter is less than 3
        if self.counter < 3:
            self.counter += 1
            self.label.setText(f'{self.counter}/3')

        # Check if the counter is 3 and show the "Yay!" button if true
        if self.counter == 3:
            self.yay_button.show()


def main():
    app = QApplication([])
    ex = CounterApp()
    ex.show()
    app.exec()


if __name__ == '__main__':
    main()
