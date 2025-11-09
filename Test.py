import unittest
from collections import deque
from Notebook import Notebook  


class TestNotebook(unittest.TestCase):

    def setUp(self):
        """Створюємо новий записник перед кожним тестом"""
        self.nb = Notebook()

    # --- Тести для add_note ---
    def test_add_note_adds_to_end(self):
        self.nb.add_note("Перша нотатка")
        self.assertEqual(self.nb.notes[-1], "Перша нотатка")

    def test_add_note_multiple(self):
        self.nb.add_note("А")
        self.nb.add_note("Б")
        self.assertEqual(list(self.nb.notes), ["А", "Б"])

    def test_add_note_type(self):
        self.nb.add_note("Тест")
        self.assertIsInstance(self.nb.notes, deque)

    # --- Тести для add_note_front ---
    def test_add_note_front_adds_to_start(self):
        self.nb.add_note("Стара")
        self.nb.add_note_front("Нова")
        self.assertEqual(self.nb.notes[0], "Нова")

    def test_add_note_front_multiple(self):
        self.nb.add_note_front("1")
        self.nb.add_note_front("2")
        self.assertEqual(list(self.nb.notes), ["2", "1"])

    def test_add_note_front_type(self):
        self.nb.add_note_front("Тест")
        self.assertIsInstance(self.nb.notes, deque)

    # --- Тести для remove_last ---
    def test_remove_last_removes_item(self):
        self.nb.add_note("Одна")
        self.nb.remove_last()
        self.assertEqual(len(self.nb.notes), 0)

    def test_remove_last_from_empty(self):
        self.nb.remove_last()
        self.assertEqual(len(self.nb.notes), 0)

    def test_remove_last_keeps_others(self):
        self.nb.add_note("A")
        self.nb.add_note("B")
        self.nb.remove_last()
        self.assertEqual(list(self.nb.notes), ["A"])

    # --- Тести для remove_first ---
    def test_remove_first_removes_item(self):
        self.nb.add_note("Одна")
        self.nb.remove_first()
        self.assertEqual(len(self.nb.notes), 0)

    def test_remove_first_from_empty(self):
        self.nb.remove_first()
        self.assertEqual(len(self.nb.notes), 0)

    def test_remove_first_keeps_others(self):
        self.nb.add_note("A")
        self.nb.add_note("B")
        self.nb.remove_first()
        self.assertEqual(list(self.nb.notes), ["B"])

    # --- Тести для show_notes ---
    def test_show_notes_empty(self):
        # якщо список порожній
        self.assertEqual(len(self.nb.notes), 0)

    def test_show_notes_not_empty(self):
        self.nb.add_note("Тест")
        self.assertIn("Тест", self.nb.notes)

    @unittest.expectedFailure
    def test_show_notes_multiple(self):
        self.nb.add_note("A")
        self.nb.add_note("B")
        self.assertEqual(len(self.nb.notes), 1)
        






if __name__ == "__main__":
    unittest.main()
