
## 1. Project Overview

This project implements a reusable UI automation framework using Python, Playwright, and Pytest.

The framework validates the Books to Scrape catalogue and the Quotes to Scrape demo login flow. It includes navigation checks, data consistency validation, hyperlink verification, image validation, pagination, automated reporting, and continuous integration.

## 2. How to run
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
### Running Tests

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

## 3. Features

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

## 4. Tech Stack

- Python 3.12
- Playwright
- Pytest
- pytest-playwright
- pytest-html
- Allure Pytest integration
- Requests
- Docker
- GitHub Actions

## 5. Environment Setup

The framework uses the following demo websites:

- Books: https://books.toscrape.com/index.html
- Quotes: https://quotes.toscrape.com/

```bash
export QUOTES_USERNAME="your_verified_test_username"
export QUOTES_PASSWORD="your_verified_test_password"
```

## 6. Test Case Coverage

| Test case | Validation |
|---|---|
| TC-01 | Homepage URL, title, headings and books |
| TC-02 | Navigation to five randomly selected books |
| TC-03 | Title and price consistency for five books |
| TC-04 | Unique homepage hyperlinks return HTTP 200 |
| TC-05 | Product image attributes, loading and pagination |
| TC-06 | Quotes demo login flow and logout link |

## 7. Report Generation

```bash
mkdir -p reports

python -m pytest \
  --html=reports/report.html \
  --self-contained-html \
  --alluredir=allure-results \
  --clean-alluredir
```

## 8. HTML Report Guide

The HTML report is generated at:

`reports/report.html`

Open it locally:

```bash
xdg-open reports/report.html
```
## 9. Allure Report Guide

Install Java and Allure CLI before generating the report.

```bash
allure generate allure-results --clean -o allure-report
```

Open the report:

```bash
allure open allure-report
```

Allure results and the generated Allure HTML report are separate outputs.

## 10. Docker Execution

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

## 11. GitHub Actions Setup

The workflow is located at:

`.github/workflows/playwright.yml`

It runs on pushes to `main` or `master`, pull requests targeting those branches, and manual workflow dispatch.

The pipeline installs dependencies, installs Chromium, executes tests, generates reports, and uploads artifacts.

To inspect a run, open the repository's Actions tab, select the workflow run, and download the generated artifacts.

## 12. CI/CD Artifacts

The GitHub Actions workflow uploads available:

- pytest HTML report
- Allure results
- Allure HTML report
- Playwright test output
- Screenshots
- Videos
- Trace files

