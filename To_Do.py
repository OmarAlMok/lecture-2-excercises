import json
from PyQt6.QtCore import QAbstractListModel, Qt
from PyQt6.QtGui import QImage


class TodoModel(QAbstractListModel):
    """Backend model that stores todos and persists them to a JSON file.

    This module is backend-only: it exposes a Qt-compatible list model that
    any frontend (such as `too.py`) can import and use.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.todos = self._load()
        self.tick = QImage("tick.png")

    def _load(self):
        try:
            with open("data.db", mode="r", encoding="utf-8") as todo_db:
                return json.load(todo_db)
        except FileNotFoundError:
            return []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            _, text = self.todos[index.row()]
            return text

        if role == Qt.ItemDataRole.DecorationRole:
            status, _ = self.todos[index.row()]
            if status:
                return self.tick

    def rowCount(self, index):
        return len(self.todos)

    def add(self, todo_text):
        self.todos.append((False, todo_text))
        self._save()

    def _save(self):
        with open("data.db", mode="w", encoding="utf-8") as todo_db:
            json.dump(self.todos, todo_db)
        # Notify any attached views that the data/layout changed.
        self.layoutChanged.emit()

    def delete(self, index):
        try:
            del self.todos[index]
        except IndexError:
            return
        self._save()

    def complete(self, index):
        try:
            self.todos[index] = (True, self.todos[index][1])
        except IndexError:
            return
        self._save()