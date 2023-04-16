from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # Нельзя добавить одну и ту же книгу дважды
    def test_add_new_book_add_similar_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    # Проверяем некорректные значения при добавлении книги
    @pytest.mark.parametrize("new_book", ['', 12345, None])
    def test_add_new_book_add_empty_or_incorrect_shows_error(self, new_book):
        collector = BooksCollector()

        collector.add_new_book(new_book)
        
        assert collector.get_book_rating(new_book) != 1

    # Негативная проверка установки рейтинга книги
    @pytest.mark.parametrize("invalid_rating", [-1, 0, 11, "good", None])
    def test_set_book_rating_invalid_rating(self, invalid_rating):
        collector = BooksCollector()
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)

        collector.set_book_rating(book_name, invalid_rating)
        assert collector.get_book_rating(book_name) != invalid_rating

    # Проверка, нельзя установить рейтинг на не добавленной книге
    def test_set_book_rating_str_and_none_shows_error(self):
        collector = BooksCollector()
        collector.set_book_rating("Оно", 5)

        assert collector.get_book_rating("Оно") != 5

    # Проверка возвращения рейтинга
    def test_get_book_rating(self):
        collector = BooksCollector()
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)
        assert collector.get_book_rating(book_name) == 1

    # У не добавленной книги нет рейтинга
    @pytest.mark.parametrize("nonexistent", ['', 'Война и мир'])
    def test_get_book_rating_nonexistent(self, nonexistent):
        collector = BooksCollector()
        assert collector.get_book_rating(nonexistent) != 1

    # Проверка возвращения корректных книг
    def test_get_books_with_specific_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_rating('Война и мир', 4)
        collector.add_new_book('Самый богатый человек в Вавилоне')
        collector.set_book_rating('Самый богатый человек в Вавилоне', 8)
        collector.add_new_book('Триумфальная арка')
        collector.set_book_rating('Триумфальная арка', 4)
        collector.add_new_book('1984')
        collector.set_book_rating('1984', 8)


        books = collector.get_books_with_specific_rating(4)

        assert 'Война и мир' in books
        assert 'Триумфальная арка' in books

    # Проверка возвращения пустого массива, когда передаем несуществующее значение
    def test_get_books_with_specific_rating_empty(self):
        collector = BooksCollector()
        assert collector.get_books_with_specific_rating(3) == [] 

    # Проверка возвращения пустого массива, когда передаем некорректное значение
    @pytest.mark.parametrize("invalid_rating", [5, -4])
    def test_get_books_with_specific_rating_invalid_rating(self, invalid_rating):
        collector = BooksCollector()
        collector.add_new_book('Мир наизнанку') # рейтинг у него поумолчанию 1
        assert collector.get_books_with_specific_rating(invalid_rating) == [] 

    # Проверка вовзращения рейтинга книги в виде словаря
    def test_get_books_rating(self):
        collector = BooksCollector()
        collector.add_new_book("Атлант расправил плечи")
        collector.set_book_rating("Атлант расправил плечи", 6)
        assert collector.get_books_rating() == {"Атлант расправил плечи": 6}

    # Проверка добавления книги в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Если наступит завтра")
        collector.add_book_in_favorites("Если наступит завтра")
        assert "Если наступит завтра" in collector.get_list_of_favorites_books()

    # Проверка добавления уже существующего в избранное
    def test_add_book_in_favorites_duplicate_book(self):
        collector = BooksCollector()
        collector.add_new_book("Если наступит завтра")
        collector.add_book_in_favorites("Если наступит завтра")
        collector.add_book_in_favorites("Если наступит завтра")
        assert len(collector.get_list_of_favorites_books()) == 1

    # Проверка добавления несуществующих и некорректных названий книг
    @pytest.mark.parametrize("invalid_book", ['Если наступит завтра', '', 5,])
    def test_add_book_in_favorites_invalid_book(self, invalid_book):
        collector = BooksCollector()
        collector.add_new_book('Волшебник из страны Оз')
        collector.add_book_in_favorites(invalid_book)
        assert invalid_book not in collector.get_list_of_favorites_books()

    # Проверка удаления книги из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Отцы и дети")
        collector.add_book_in_favorites("Отцы и дети")
        collector.delete_book_from_favorites("Отцы и дети")

        assert "Отцы и дети" not in collector.get_list_of_favorites_books()

    # Проверка корректного возвращения книг из избранных
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book("451 по фаренгейту")
        collector.add_book_in_favorites("451 по фаренгейту")
        collector.add_new_book("Мастер и Маргарита")
        collector.add_book_in_favorites("Мастер и Маргарита")

        assert ["451 по фаренгейту", "Мастер и Маргарита"] == collector.get_list_of_favorites_books()

        










