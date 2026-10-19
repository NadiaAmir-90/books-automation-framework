from playwright.sync_api import Page, Locator


class BookDetailsPage:
    """Page object for an individual book details page."""

    def __init__(self, page: Page):
        self.page = page

        self.title=page.locator("div.product_main h1")
        self.price=page.locator("div.product_main .price_color")
        self.product_information= page.locator( "table.table.table-striped")
        self.description= page.locator("#product_description + p")

    def get_title(self) -> str:
        return self.title.inner_text().strip()

    def get_price(self) -> str:
        return self.price.inner_text().strip()

    def has_product_information(self) -> bool:
        return (
            self.product_information.count() > 0
            and self.product_information.is_visible()
        )

    def go_back(self) -> None:
        self.page.go_back(wait_until="domcontentloaded")