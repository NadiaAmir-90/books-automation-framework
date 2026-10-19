from playwright.sync_api import Page, expect
from config.settings import BOOKS_HOME_URL, MAX_IMAGE_PAGES


# Validate book images across up to five catalogue pages.
def test_product_images_and_pagination(page: Page):
    page.goto(BOOKS_HOME_URL, wait_until="domcontentloaded")


    for page_number in range(1, MAX_IMAGE_PAGES + 1):

        images = page.locator("article.product_pod img.thumbnail")

        expect(images.first).to_be_visible()
        assert images.count() > 0, (f"No product images on page {page_number}")


        for index in range(images.count()):
            image = images.nth(index)
            expect(image).to_be_visible()

            src = image.get_attribute("src")
            alt = image.get_attribute("alt")
            classes = image.get_attribute("class") or ""

            assert src and src.strip(), (f"Image {index} on page {page_number} " "has no src.")
            assert alt and alt.strip(), (f"Image {index} on page {page_number} " "has no alt text.")
            assert "thumbnail" in classes.split(), (f"Image {index} lacks the thumbnail class.")

            loaded = image.evaluate("""async (el) => {
                   try {
                    await el.decode();          
                    return el.naturalWidth > 0;
                   }catch (e) {
                    return false;               
                   }
                }"""
            )
            assert loaded, (f"Image failed to load on page {page_number}: "f"{src}")

        next_button = page.locator("li.next a")

        if page_number == MAX_IMAGE_PAGES:
            break

        if next_button.count() == 0:
            break

        expect(next_button).to_be_visible()
        next_button.click()

        expect(page.locator("article.product_pod").first).to_be_visible()