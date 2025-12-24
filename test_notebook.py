import unittest
from collections import deque
from notebook import Notebook

class TestNotebook(unittest.TestCase):
    
    def setUp(self):
        self.nb = Notebook()

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

    def test_remove_last_removes_item(self):
        self.nb.add_note("Один")
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

    def test_remove_first_removes_item(self):
        self.nb.add_note("Один")
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

    def test_show_notes_empty(self):
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