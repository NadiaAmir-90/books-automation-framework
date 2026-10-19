from playwright.sync_api import Page, Locator, expect

from config.settings import BOOKS_HOME_URL


class BooksPage:
    

    def __init__(self, page: Page):

        self.page = page
        self.book_items = page.locator("article.product_pod")
        self.book_links = page.locator("article.product_pod h3 a")
        self.book_prices = page.locator("article.product_pod .price_color")
        self.book_images = page.locator("article.product_pod img.thumbnail")
        self.next_button = page.locator("li.next a")

    def open(self) -> None:
        self.page.goto(BOOKS_HOME_URL, wait_until="domcontentloaded")

    def get_book_count(self) -> int:
        return self.book_items.count()

    def get_book_title(self, index: int) -> str:
        return (self.book_links.nth(index).get_attribute("title") or "").strip()

    def get_book_price(self, index: int) -> str:
        return self.book_prices.nth(index).inner_text().strip()

    def open_book(self, index: int) -> None:
        self.book_links.nth(index).click()

    def is_next_page_available(self) -> bool:
        return self.next_button.count() > 0

    def go_to_next_page(self) -> None:
        expect(self.next_button).to_be_visible()
        self.next_button.click()