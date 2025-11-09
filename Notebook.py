from collections import deque

class Notebook:
    def __init__(self):
        # створюємо порожній дек для зберігання нотаток
        self.notes = deque()

    def add_note(self, note):
        """Додає нову нотатку в кінець списку"""
        self.notes.append(note)
        print(" Нотатку додано!")

    def add_note_front(self, note):
        """Додає нову нотатку на початок списку"""
        self.notes.appendleft(note)
        print(" Нотатку додано на початок!")

    def remove_last(self):
        """Видаляє останню нотатку"""
        if self.notes:
            removed = self.notes.pop()
            print(f" Видалено останню нотатку: {removed}")
        else:
            print(" Немає нотаток для видалення!")

    def remove_first(self):
        """Видаляє першу нотатку"""
        if self.notes:
            removed = self.notes.popleft()
            print(f" Видалено першу нотатку: {removed}")
        else:
            print(" Немає нотаток для видалення!")

    def show_notes(self):
        """Виводить усі нотатки"""
        if self.notes:
            print("\n Усі нотатки:")
            for i, note in enumerate(self.notes, 1):
                print(f"{i}. {note}")
        else:
            print(" Записник порожній!")

    def search(self, keyword):
        """Пошук нотатки за ключовим словом"""
        results = [note for note in self.notes if keyword.lower() in note.lower()]
        if results:
            print(f"\n Знайдено нотатки за ключовим словом '{keyword}':")
            for note in results:
                print(f"- {note}")
        else:
            print(f" Нічого не знайдено за ключовим словом '{keyword}'.")


def main():
    notebook = Notebook()

    while True:
        print("\n--- МЕНЮ ЗАПИСНИКА ---")
        print("1. Додати нотатку (в кінець)")
        print("2. Додати нотатку (на початок)")
        print("3. Видалити першу нотатку")
        print("4. Видалити останню нотатку")
        print("5. Показати всі нотатки")
        print("0. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            note = input("Введіть текст нотатки: ")
            notebook.add_note(note)
        elif choice == "2":
            note = input("Введіть текст нотатки: ")
            notebook.add_note_front(note)
        elif choice == "3":
            notebook.remove_first()
        elif choice == "4":
            notebook.remove_last()
        elif choice == "5":
            notebook.show_notes()
        elif choice == "0":
            print("Вихід із програми...")
            break
        else:
            print(" Невірний вибір! Спробуйте ще раз.")


if __name__ == "__main__":
    main()
