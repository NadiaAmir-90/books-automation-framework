import requests

from playwright.sync_api import Page

from config.settings import BOOKS_HOME_URL
from utils.url_utils import normalize_url

# Check that unique HTTP hyperlinks return status 200.
def test_homepage_links_return_http_200(page: Page):

    page.goto(BOOKS_HOME_URL, wait_until="domcontentloaded")

    hrefs = page.locator("a[href]").evaluate_all("(links) => links.map(link => link.href)")

    unique_urls = sorted({
        normalized
        for href in hrefs
        if (normalized := normalize_url(BOOKS_HOME_URL, href))
    })

    assert unique_urls, "No HTTP hyperlinks were found."

    failures = []

    with requests.Session() as session:
        for url in unique_urls:
            try:
                response = session.get(
                    url,
                    timeout=15,
                    allow_redirects=True,
                )

                if response.status_code != 200:
                    failures.append(f"{url} returned {response.status_code}")

            except requests.RequestException as error:
                failures.append(f"{url}: {error}")

    assert not failures, ("Broken or unsuccessful links found:\n"+ "\n".join(failures))