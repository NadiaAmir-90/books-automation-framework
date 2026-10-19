# Enterprise UI Automation Framework – Books to Scrape

## 1. Project Overview

This project implements a reusable UI automation framework using Python, Playwright, and Pytest.

The framework validates the Books to Scrape catalogue and the Quotes to Scrape demo login flow. It includes navigation checks, data consistency validation, hyperlink verification, image validation, pagination, automated reporting, and continuous integration.

## 2. Features

- Homepage URL and title validation
- Visible heading validation
- Random selection and navigation of five books
- Book title and price consistency checks
- Unique hyperlink response validation
- Product image attribute and loading validation
- Pagination testing for up to five pages
- Demo login and logout link validation
- Reusable Page Object Model classes
- Pytest fixtures and modular tests
- HTML reports using pytest-html
- Allure test results and HTML reports
- Failure screenshots, videos, and traces
- Docker-based execution
- GitHub Actions CI/CD integration

## 3. Tech Stack

- Python 3.12
- Playwright
- Pytest
- pytest-playwright
- pytest-html
- Allure Pytest integration
- Requests
- Docker
- GitHub Actions

## 4. Project Structure

```text
enterprise-books-automation/
├── .github/
│   └── workflows/
│       └── playwright.yml
├── config/
│   └── settings.py
├── pages/
│   ├── books_page.py
│   ├── book_details_page.py
│   └── quotes_login_page.py
├── tests/
│   ├── books/
│   │   ├── test_homepage.py
│   │   ├── test_book_navigation.py
│   │   ├── test_book_consistency.py
│   │   ├── test_broken_links.py
│   │   └── test_product_images.py
│   └── quotes/
│       └── test_login_logout.py
├── utils/
│   └── url_utils.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## 5. Installation Guide

Requirements:

- Python 3.12
- Git
- Docker (optional for containerized execution)
- Java and Allure CLI for generating Allure HTML reports

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd enterprise-books-automation
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies and Chromium:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## 6. Environment Setup

The framework uses the following demo websites:

- Books: https://books.toscrape.com/index.html
- Quotes: https://quotes.toscrape.com/

Optional login configuration can be supplied using environment variables:

```bash
export QUOTES_USERNAME="your_verified_test_username"
export QUOTES_PASSWORD="your_verified_test_password"
```

Use only verified demo credentials. Never commit private credentials to Git.

## 7. Running Tests

Run the complete test suite:

```bash
python -m pytest
```

Run a specific test:

```bash
python -m pytest tests/books/test_homepage.py -v
```

Run tests with a visible browser:

```bash
python -m pytest tests/books/test_homepage.py --headed
```

## 8. Test Case Coverage

| Test case | Validation |
|---|---|
| TC-01 | Homepage URL, title, headings and books |
| TC-02 | Navigation to five randomly selected books |
| TC-03 | Title and price consistency for five books |
| TC-04 | Unique homepage hyperlinks return HTTP 200 |
| TC-05 | Product image attributes, loading and pagination |
| TC-06 | Quotes demo login flow and logout link |

## 9. Report Generation

Generate HTML and Allure results:

```bash
mkdir -p reports

python -m pytest \
  --html=reports/report.html \
  --self-contained-html \
  --alluredir=allure-results \
  --clean-alluredir
```

## 10. HTML Report Guide

The HTML report is generated at:

`reports/report.html`

Open it locally:

```bash
xdg-open reports/report.html
```

The report contains test outcomes and failure details.

## 11. Allure Report Guide

Install Java and Allure CLI before generating the report.

```bash
allure generate allure-results --clean -o allure-report
```

Open the report:

```bash
allure open allure-report
```

Allure results and the generated Allure HTML report are separate outputs.

## 12. Docker Execution

Build the image:

```bash
docker build -t books-automation .
```

Run the tests:

```bash
docker run --rm \
  -v "$PWD/reports:/app/reports" \
  -v "$PWD/allure-results:/app/allure-results" \
  books-automation
```

## 13. GitHub Actions Setup

The workflow is located at:

`.github/workflows/playwright.yml`

It runs on pushes to `main` or `master`, pull requests targeting those branches, and manual workflow dispatch.

The pipeline installs dependencies, installs Chromium, executes tests, generates reports, and uploads artifacts.

To inspect a run, open the repository's Actions tab, select the workflow run, and download the generated artifacts.

## 14. Design Decisions

### Page Object Model

Page classes encapsulate locators and browser actions. Tests focus on expected behavior and assertions.

### Fixtures

Pytest fixtures provide isolated browser pages and reusable test setup.

### DRY and SOLID

Shared logic is implemented once and reused. Each page object has a focused responsibility, while configuration, utilities, tests, and reporting remain separated.

### Synchronization

Playwright's auto-waiting and web-first assertions are preferred over fixed sleeps.

### Randomized testing

Five distinct book indices are selected per navigation and consistency test. Failures should record enough information to identify the selected book.

## 15. Known Limitations

- The target websites are external dependencies and may occasionally be unavailable.
- External hyperlinks can fail because of rate limits, network restrictions, or server policies.
- Randomized selection can make failures harder to reproduce unless a seed is recorded.
- Demo login behavior must be verified against the current website.
- A successful HTTP response does not guarantee that a page is functionally correct.
- Allure HTML generation requires the Allure command-line tool.

## 16. CI/CD Artifacts

The GitHub Actions workflow uploads available:

- pytest HTML report
- Allure results
- Allure HTML report
- Playwright test output
- Screenshots
- Videos
- Trace files

## 17. Maintenance

1. Keep dependencies under version control.
2. Update page-object locators when the website structure changes.
3. Run relevant tests locally before pushing changes.
4. Review CI artifacts after failures.
5. Keep secrets and generated files out of Git.
