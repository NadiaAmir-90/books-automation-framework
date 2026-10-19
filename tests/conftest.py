
import pytest
from playwright.sync_api import (
    Browser,
    BrowserContext,
    Page,
    Playwright,
    sync_playwright,
)
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def browser() -> Browser:
    """Launch one browser for the entire test session."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=False
        )

        yield browser

        browser.close()


@pytest.fixture
def context(browser: Browser) -> BrowserContext:
    """Create an isolated browser context for each test."""
    context = browser.new_context(
        viewport={"width": 1366, "height": 768},
        ignore_https_errors=True,
    )

    yield context

    context.close()


@pytest.fixture
def page(context: BrowserContext) -> Page:
    """Create a fresh page for each test."""
    page = context.new_page()
    page.set_default_timeout(10_000)

    yield page

    # The context fixture closes the page and its context.
