# qa python

**test_add_new_book_add_two_books** - Проверка добавление двух книг
**test_add_new_book_add_similar_book** - Проверка подставления рейтинга поумолчанию
**test_add_new_book_duplicate** - Нельзя добавить одну и ту же книгу
**test_add_new_book_add_empty_or_incorrect_shows_error**- Проверяем некорректные значения при добавлении книги

**test_set_book_rating** - Проверить, что рейтинг книги устанавливается корректно
**test_add_new_book_add_empty_or_incorrect_shows_error** - Проверить, что не устанавливается рейтинг книги, если значение равно -1, 0, 11, “good” и None
**test_set_book_rating_invalid_rating** - Негативная проверка установки рейтинга книги
**test_set_book_rating_none_shows_error** - Проверка, что нельзя установить рейтинг на не добавленной книге

**test_get_book_rating** - Проверка возвращения рейтинга
**test_get_book_rating_nonexistent** - У не добавленной книге нет рейтинга

**test_get_books_with_specific_rating** - Проверка возвращения корректных книг со специфичным рейтингом
**test_get_books_with_specific_rating_empty** - Проверка возвращения пустого массива, когда передаем несуществующее значение
**test_get_books_with_specific_rating_invalid_rating** - Проверка возвращения пустого массива, когда передаем некорректное значение


**test_get_books_rating** - Проверка вовзращения рейтинга книги в виде словаря


**test_add_book_in_favorites** - Проверить, что книга добавляется в избранное
**test_add_book_in_favorites_duplicate_book** - Проверка добавления уже существующего в избранное
**test_add_book_in_favorites_invalid_book** - Проверка добавления несуществующих и некорректных названий книг


**test_delete_book_from_favorites** - Проверка удаления книги из избранного


**test_get_list_of_favorites_books** - Проверка возвращения избранных книг

