from main import BooksCollector
import pytest

@pytest.fixture
def collector():
    collector = BooksCollector()
    collector.books_rating.clear() # Очистка словаря
    collector.favorites.clear() # Очистка списка

    return collector
