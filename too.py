import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QListView,
    QLineEdit,
)

from To_Do import TodoModel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Todo")

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        # List view (Qt model provided by backend)
        self.list_view = QListView()
        self.model = TodoModel()
        self.list_view.setModel(self.model)

        # Input and buttons
        controls = QHBoxLayout()
        self.todo_edit = QLineEdit()
        self.todo_edit.setPlaceholderText("Enter a todo item...")
        self.add_btn = QPushButton("Add")
        self.delete_btn = QPushButton("Delete")
        self.complete_btn = QPushButton("Complete")

        controls.addWidget(self.todo_edit)
        controls.addWidget(self.add_btn)
        controls.addWidget(self.delete_btn)
        controls.addWidget(self.complete_btn)

        layout.addWidget(self.list_view)
        layout.addLayout(controls)

        # Connect signals
        self.add_btn.pressed.connect(self.add)
        self.delete_btn.pressed.connect(self.delete)
        self.complete_btn.pressed.connect(self.complete)

    def add(self):
        text = self.todo_edit.text().strip()
        if text:
            self.model.add(text)
            self.todo_edit.clear()

    def delete(self):
        indexes = self.list_view.selectedIndexes()
        if indexes:
            self.model.delete(indexes[0].row())
            self.list_view.clearSelection()

    def complete(self):
        indexes = self.list_view.selectedIndexes()
        if indexes:
            self.model.complete(indexes[0].row())
            self.list_view.clearSelection()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())