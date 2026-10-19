import os

from playwright.sync_api import Page, expect

from pages.quotes_login_page import QuotesLoginPage

# Validate the demo login flow and aut
def test_quotes_login_and_logout_link(page: Page):
    quotes_page = QuotesLoginPage(page)

    username = os.getenv("QUOTES_USERNAME", "demo-user")
    password = os.getenv("QUOTES_PASSWORD", "demo-password")

    quotes_page.open_homepage()

    expect(page).to_have_url("https://quotes.toscrape.com/")

    expect(quotes_page.login_link).to_be_visible()
    expect(quotes_page.login_link).to_be_enabled()

    quotes_page.open_login_page()

    expect(quotes_page.username).to_be_visible()
    expect(quotes_page.password).to_be_visible()

    quotes_page.login(username, password)

    expect(quotes_page.logout_link).to_be_visible()
    expect(quotes_page.logout_link).to_be_enabled()

    assert quotes_page.is_logout_available(), ("Logout is not available after login.")