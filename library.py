class Book:
    """
    Класс представляющий книгу
    """
    
    def __init__(self):
        """
        Инициализация книги
        
        Атрибуты объекта:
            title: Название книги
            author: Автор книги
            year: Год издания книги
            
        Все атрибуты получаем путем пользовательского ввода в консоли
        """

        self.title = input("Название: ")
        self.author = input("Автор: ")
        self.year = input("Год издания: ")


    def __str__(self):
        """Строковая версия объекта"""

        # Если книга в библиотеке, у нее есть id и статус, также их печатаем
        if hasattr(self, "id") and hasattr(self, "status"):
            return f"id: {self.id}\n" + f"Название: {self.title}\n" + f"Автор: {self.author}\n" + f"Год издания: {self.year}\n" + f"Статус: {self.status}\n"
        # Если нет, то печатаем только базовые атрибуты
        else:
            return f"Название: {self.title}\n" + f"Автор: {self.author}\n" + f"Год издания: {self.year}\n"


class Library:
    """
    Класс представляющий библиотеку книг

    Артибуты класса:
        book_id: Счетчик порядкового номера id. Текущее значение используется при добавлении книги в библиотеку.
        book_statuses: Возможные статусы книг в библиотеке.
    """

    book_id: int = 1
    book_statuses: list = ["в наличии", "выдана"]


    def __init__(self) -> None:
        """Инициализация библиотеки."""

        self.books: list[Book] = []


    def add_book(self) -> None:
        """Добавление книги в библиотеку."""

        #Создаем книгу, присваиваем ей id и статус "в наличии"
        book = Book()
        book.id = Library.book_id
        Library.book_id += 1
        book.status = "в наличии"

        #Добавляем книгу в библиотеку
        self.books.append(book)


    def change_book_status(self) -> None:
        """Изменение статуса книги."""

        # Запрашиваем у пользователя id книги, проверяем корректность ввода
        try:
            id: int = int(input("id: ")) 
        except ValueError:
            print("Неккоректный id")
            return
        
        # Запрашиваем у пользователя новый статус книги, проверяем что он валидный (в списке book_statuses)
        status:str = input("Статус: ")
        if status not in Library.book_statuses:
            print("Некорректный статус")
            return 

        # Ищем книгу с данным id
        for book in self.books:
            if book.id == id:
                # меняем статус
                book.status = status
                # Сообщаем пользоваетелю об успешном изменении статуса
                print("Статус изменен")
                return
        
        # Если не нашли книгу - сообщаем пользователю
        print("Книга не найдена")
        return
    

    def delete_book(self) -> None:
        """Удаление книги."""

        # Запрашиваем у пользователя id книги, проверяем корректность ввода
        try:
            id: int = int(input("id: ")) 
        except ValueError:
            print("Неккоректный id")
            return

        # Ищем книгу с данным id
        for book in self.books:
            if book.id == id:
                #Удаляем книгу
                self.books.remove(book)
                # Сообщаем пользоваетелю об успешном удалении книги
                print("Книга удалена")
                return
        
        # Если не нашли книгу - сообщаем пользователю
        print("Книга не найдена")
        return


    def print_all_books(self) -> None:
        """Печатание всех книг в библиотеке."""

        # Печачаем новую строку для отделения от предыдущего текста
        print()
        # Печатаем все книги в библиотеке
        for book in self.books:
            print(book)


    def search_book_by_author(self) -> None:
        """Поиск книг по автору."""

        # Запрашиваем у пользователя автора
        author: str = input("Автор: ")
        # Создаем список, куда поместим все найденные результаты
        result: list = []

        # Ищем книги, добавляем каждую в список результатов
        for book in self.books:
            if book.author == author:
                result.append(book)

        # Если не нашли книги, добавляем в результат сообщение для пользователя    
        if not result:
            result.append("Книги не найдены")
        
        # Печатаем новую строку (для отделения) и все результаты
        print()
        for item in result:
            print(item)
            
        return


    def search_book_by_title(self) -> None:
        """Поиск книг по названию."""
        # Запрашиваем у пользователя название
        title: str = input("Название: ")
        # Создаем список, куда поместим все найденные результаты
        result: list = []

        # Ищем книги, добавляем каждую в список результатов
        for book in self.books:
            if book.title == title:
                result.append(book)
        
        # Если не нашли книги, добавляем в результат сообщение для пользователя   
        if not result:
            result.append("Книги не найдены")
        
        # Печатаем новую строку (для отделения) и все результаты
        print()
        for item in result:
            print(item)

        return


    def search_book_by_year(self) -> None:
        """Поиск книг по году издания."""

        # Запрашиваем у пользователя
        year: str = input("Год: ")
        # Создаем список, куда поместим все найденные результаты
        result: list = []

        # Ищем книги, добавляем каждую в список результатов
        for book in self.books:
            if book.year == year:
                result.append(book)
        
        # Если не нашли книги, добавляем в результат сообщение для пользователя 
        if not result:
            result.append("Книги не найдены")
        
        # Печатаем новую строку (для отделения) и все результаты
        print()
        for item in result:
            print(item)

        return
    

def main():

    #Создаем библиотеку
    library = Library()

    #Уточняем сколько книг хочет добавить пользователь
    while True:
        try:
            quantity = int(input("Сколько книг Вы хотите добавить? "))
        # Проверяем корректность ввода
        except ValueError:
            print("Неккоректное количество")
        else:
            break

    # Добавляем книги
    for _ in range(0, quantity):
        library.add_book()

    #Пробуем все методы (изменение статуса, поиск, удаление)
    library.change_book_status()
    library.search_book_by_author()
    library.search_book_by_title()
    library.search_book_by_year()
    library.delete_book()


if __name__ == "__main__":
    main()