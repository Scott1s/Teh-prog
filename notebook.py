from collections import deque

class Notebook:
    def __init__(self):
        self.notes = deque()
    
    def add_note(self, note):
        """Додає нотатку в кінець"""
        self.notes.append(note)
    
    def add_note_front(self, note):
        """Додає нотатку на початок"""
        self.notes.appendleft(note)
    
    def remove_last(self):
        """Видаляє останню нотатку"""
        if self.notes:
            self.notes.pop()
    
    def remove_first(self):
        """Видаляє першу нотатку"""
        if self.notes:
            self.notes.popleft()
    
    def show_notes(self):
        """Показує всі нотатки"""
        return list(self.notes)


def main():
    nb = Notebook()
    print("=== Нотатник ===")
    
    while True:
        print("\n1. Додати нотатку (в кінець)")
        print("2. Додати нотатку (на початок)")
        print("3. Видалити останню нотатку")
        print("4. Видалити першу нотатку")
        print("5. Показати всі нотатки")
        print("6. Запустити тести")
        print("0. Вихід")
        
        choice = input("Оберіть дію: ")
        
        if choice == '1':
            note = input("Введіть нотатку: ")
            nb.add_note(note)
            print("Додано!")
        elif choice == '2':
            note = input("Введіть нотатку: ")
            nb.add_note_front(note)
            print("Додано на початок!")
        elif choice == '3':
            nb.remove_last()
            print("Останню нотатку видалено!")
        elif choice == '4':
            nb.remove_first()
            print("Першу нотатку видалено!")
        elif choice == '5':
            notes = nb.show_notes()
            if notes:
                print("Ваші нотатки:")
                for i, note in enumerate(notes, 1):
                    print(f"{i}. {note}")
            else:
                print("Нотаток немає")
        elif choice == '6':
            import unittest
            from test_notebook import TestNotebook
            suite = unittest.TestLoader().loadTestsFromTestCase(TestNotebook)
            unittest.TextTestRunner(verbosity=2).run(suite)
        elif choice == '0':
            print("До побачення!")
            break
        else:
            print("Невірний CHOSE!")

if __name__ == "__main__":
    main()
