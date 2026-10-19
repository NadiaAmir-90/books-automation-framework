FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt

RUN python -m playwright install --with-deps chromium

COPY . .

RUN mkdir -p reports allure-results test-results \
    screenshots videos traces

CMD ["python", "-m", "pytest", \
     "--html=reports/report.html", \
     "--self-contained-html", \
     "--alluredir=allure-results", \
     "--output=test-results", \
     "--screenshot=only-on-failure", \
     "--video=retain-on-failure", \
     "--tracing=retain-on-failure"]