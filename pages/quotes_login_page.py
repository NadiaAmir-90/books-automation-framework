from playwright.sync_api import Page, Locator, expect

from config.settings import QUOTES_BASE_URL, QUOTES_LOGIN_URL


class QuotesLoginPage:

    def __init__(self, page: Page):
        
        self.page = page

        self.login_link=page.get_by_role("link", name="Login")
        self.username= page.locator("#username")
        self.password= page.locator("#password")

        self.submit_button= page.get_by_role("button", name="Login")
        self.logout_link= page.get_by_role("link", name="Logout")

    def open_homepage(self) -> None:
        self.page.goto(QUOTES_BASE_URL, wait_until="domcontentloaded")

    def open_login_page(self) -> None:
        expect(self.login_link).to_be_visible()
        self.login_link.click()
        expect(self.page).to_have_url(QUOTES_LOGIN_URL)

    def login(self, username: str, password: str) -> None:
        self.username.fill(username)
        self.password.fill(password)
        self.submit_button.click()

    def is_logout_available(self) -> bool:
        return (
            self.logout_link.is_visible()
            and self.logout_link.is_enabled()
        )