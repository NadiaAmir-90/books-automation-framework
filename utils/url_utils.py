from urllib.parse import urljoin, urldefrag, urlparse

# Resolve a link against its base URL and remove fragments.
def normalize_url(base_url: str, href: str) -> str | None:

    href = href.strip()
    if not href:
        return None
    if href.startswith(("mailto:", "tel:", "javascript:")):
        return None


    absolute_url = urljoin(base_url, href)
    absolute_url, _ = urldefrag(absolute_url)
    parsed = urlparse(absolute_url)

    if parsed.scheme not in ("http", "https"):
        return None

    return absolute_url