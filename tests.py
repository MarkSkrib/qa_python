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

    # Проверка, подставляется ли книге рейтинг 1 по умолчанию 
    def test_add_new_book_add_similar_book(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        result = collector.get_book_rating('Гордость и предубеждение и зомби')

        assert result == 1, f"Ожидалось {1}, но получено {result}."

        # Проверка, что метод не добавляет дубликаты книг 
    def test_add_new_book_duplicate(self, collector):
        book_name = "Гордость и предубеждение и зомби"
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        result = len(collector.get_books_rating())
        assert result == 1, f"Ожидалось {1}, но получено {result}."

     # Проверяем некорректные значения при добавлении книги
    @pytest.mark.parametrize("new_book", ['', 12345, None])
    def test_add_new_book_add_empty_or_incorrect_shows_error(self, new_book):
        collector = BooksCollector()

        collector.add_new_book(new_book)
        book_keys = collector.get_books_rating().keys()
        
        assert new_book not in book_keys, f"Ожидание: {new_book} не находится в book_rating, фактически: book_rating.keys() возвращает {book_keys}." # Нашел такой вариант решения
 
     # Проверка, корректной установки рейтинга книги
    def test_set_book_rating(self, collector):
        book_name = 'Гордость и предубеждение и зомби'

        collector.add_new_book(book_name)

        collector.set_book_rating(book_name, 5)
        assert collector.get_book_rating(book_name) == 5

     # Негативная проверка установки рейтинга книги
    @pytest.mark.parametrize("invalid_rating", [-1, 0, 11, "good", None])
    def test_set_book_rating_invalid_rating(self, collector, invalid_rating):
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, invalid_rating)
        book_rating = collector.get_book_rating(book_name)

        assert book_rating != invalid_rating, f"Ожидание: рейтинг {book_name} = {1}, но получено {book_rating}."


     # Проверка, нельзя установить рейтинг на не добавленной книге
    def test_set_book_rating_none_shows_error(self, collector):
        collector.set_book_rating("Оно", None) # установил значение к None
        book_rating = collector.get_book_rating("Оно")

        assert book_rating is None, f"Ожидалось {None}, но получено {book_rating}."

     # Проверка возвращения рейтинга
    def test_get_book_rating(self, collector):
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)
        book_rating = collector.get_book_rating(book_name) 
        assert book_rating == 1, f"Ожидалось {1}, но получено {book_rating}."

     # У не добавленной книги нет рейтинга
    @pytest.mark.parametrize("nonexistent", ['', 'Война и мир'])
    def test_get_book_rating_nonexistent(self, collector, nonexistent):
        book_rating = collector.get_book_rating(nonexistent)
        assert book_rating is None, f"Ожидалось {None}, но получено {book_rating}." # подставил None


     # Проверка возвращения корректных книг
    def test_get_books_with_specific_rating(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_rating('Война и мир', 4)
        collector.add_new_book('1984')
        collector.set_book_rating('1984', 8)
        books = collector.get_books_with_specific_rating(4)

        assert 'Война и мир' in books, f"Ожидание: Война и мир, но в списке: {books}."# Уменьшили код


     # Проверка возвращения пустого массива, когда передаем несуществующее значение
    def test_get_books_with_specific_rating_empty(self, collector):
        assert collector.get_books_with_specific_rating(3) == [] 

     # Проверка возвращения пустого массива, когда передаем некорректное значение
    @pytest.mark.parametrize("invalid_rating", [5, -4])
    def test_get_books_with_specific_rating_invalid_rating(self, collector, invalid_rating):
        collector.add_new_book('Мир наизнанку') # рейтинг у него поумолчанию 1
        books = collector.get_books_with_specific_rating(invalid_rating)
        assert books == [], f"Ожидалось пустой массив [], но получено {books}."


     # Проверка вовзращения рейтинга книги в виде словаря
    def test_get_books_rating(self, collector):
        book_name = "Атлант расправил плечи" # Подготовили данные
        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, 6)
        result = collector.get_books_rating()

        assert result == {book_name: 6}, "Ожидался словарь " + {book_name: 6} + ", но получено " + {result} + "."

     # Проверка добавления книги в избранное
    def test_add_book_in_favorites(self, collector):
        book_name = "Если наступит завтра"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        result = collector.get_list_of_favorites_books()

        assert book_name in result, f"Ожидалось добавление {book_name} в избранное, но в избранных находится: {result}."


     # Проверка добавления уже существующего в избранное
    def test_add_book_in_favorites_duplicate_book(self, collector):
        book_name = "Если наступит завтра"

        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name)
        length_favorites = len(collector.get_list_of_favorites_books())
        assert length_favorites == 1, f"Ожидание: длина списка равно {1}, фактически длина списка: {length_favorites}."


     # Проверка добавления несуществующих и некорректных названий книг
    @pytest.mark.parametrize("invalid_book", ['Если наступит завтра', '', 5,])
    def test_add_book_in_favorites_invalid_book(self, collector, invalid_book):
        collector.add_book_in_favorites(invalid_book)
        result = collector.get_list_of_favorites_books()
        assert invalid_book not in result, f"Ожидание: {invalid_book} не добавится в избранное, фактически список избранных книг: {result}."

     # Проверка удаления книги из избранного
    def test_delete_book_from_favorites(self, collector):
        book_name = "Отцы и дети"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        result = collector.get_list_of_favorites_books()

        assert book_name not in result, f"Ожидание: {book_name} нет в избранных, фактически в спике избранных: {result}."


     # Проверка корректного возвращения книг из избранных
    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book("451 по фаренгейту")
        collector.add_book_in_favorites("451 по фаренгейту")
        collector.add_new_book("Мастер и Маргарита")
        collector.add_book_in_favorites("Мастер и Маргарита")
        favorite_books = collector.get_list_of_favorites_books()

        assert ["451 по фаренгейту", "Мастер и Маргарита"] == favorite_books, f"Ожидание: [\"451 по фаренгейту\", \"Мастер и Маргарита\"] равняется списку избранных, фактически {favorite_books} != [\"451 по фаренгейту\", \"Мастер и Маргарита\"]."
        










