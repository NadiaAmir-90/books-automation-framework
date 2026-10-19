import random

from playwright.sync_api import Page, expect

from config.settings import RANDOM_BOOK_COUNT
from pages.books_page import BooksPage
from pages.book_details_page import BookDetailsPage

# Open five randomly selected books and verify their details.

def test_random_book_navigation(page: Page):

    books_page = BooksPage(page)
    books_page.open()
    book_count = books_page.get_book_count()


    assert book_count >= RANDOM_BOOK_COUNT, (
        f"Expected at least {RANDOM_BOOK_COUNT} books, "
        f"but found {book_count}."
    )

    selected_indices = random.sample(range(book_count), RANDOM_BOOK_COUNT)

    for index in selected_indices:
        expected_title = books_page.get_book_title(index)

        assert expected_title, (f"Book at index {index} has no title.")

        books_page.open_book(index)

        details_page = BookDetailsPage(page)

        expect(details_page.title).to_be_visible()
        assert details_page.get_title() == expected_title

        expect(details_page.price).to_be_visible()
        assert details_page.has_product_information(), (f"Product information missing for {expected_title}")

        details_page.go_back()
        expect(books_page.book_items.first).to_be_visible()


