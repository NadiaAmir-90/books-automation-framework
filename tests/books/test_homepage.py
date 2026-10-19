from playwright.sync_api import Page, expect

from config.settings import BOOKS_HOME_URL
from pages.books_page import BooksPage

# Validate homepage URL, title, headings and book listing."
def test_homepage_validation(page: Page):

    books_page = BooksPage(page)
    books_page.open()

    expect(page).to_have_url(BOOKS_HOME_URL)
    expect(page).to_have_title("All products | Books to Scrape - Sandbox")

    headings = page.locator("h1, h2, h3, h4, h5, h6")
    heading_count = headings.count()

    assert heading_count > 0, "No headings were found."

    for index in range(heading_count):
        heading = headings.nth(index)

        if heading.is_visible():
            expect(heading).to_be_visible()
            assert heading.inner_text().strip(),(f"Heading at index {index} has empty text.")

    expect(books_page.book_items.first).to_be_visible()
    assert books_page.get_book_count() > 0, ("The homepage contains no books.")