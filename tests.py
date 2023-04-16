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
        
