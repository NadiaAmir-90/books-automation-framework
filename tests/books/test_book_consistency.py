import random

from playwright.sync_api import Page, expect

from config.settings import RANDOM_BOOK_COUNT
from pages.books_page import BooksPage
from pages.book_details_page import BookDetailsPage

# Compare listing title and price with the details page.
def test_random_book_data_consistency(page: Page):

    books_page = BooksPage(page)
    books_page.open()
    book_count = books_page.get_book_count()

    assert book_count >= RANDOM_BOOK_COUNT, (
        f"Expected at least {RANDOM_BOOK_COUNT} books, "
        f"but found {book_count}."
    )
    selected_indices = random.sample(range(book_count), RANDOM_BOOK_COUNT)


    for index in selected_indices:
        listed_books_title = books_page.get_book_title(index)
        listed_books_price = books_page.get_book_price(index)

        books_page.open_book(index)

        details_page = BookDetailsPage(page)

        details_page_title = details_page.get_title()
        details_page_price = details_page.get_price()

        assert listed_books_title == details_page_title, (
            f"Title mismatch: listing={listed_books_title!r}, "
            f"details={details_page_title!r}"
        )

        assert listed_books_price == details_page_price , (
            f"Price mismatch for {listing_title!r}: "
            f"listing={listed_books_price!r}, "
            f"details={details_page_price!r}"
        )

        details_page.go_back()

