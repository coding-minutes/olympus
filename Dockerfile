FROM python:3.8-slim

RUN pip install poetry

WORKDIR /app

RUN pip install gunicorn==19.9.0
RUN poetry config virtualenvs.create false
ADD pyproject.toml poetry.lock /app/
RUN poetry install --no-root --no-interaction --no-ansi


COPY . .

ENTRYPOINT [ "gunicorn", "olympus.wsgi", "-b", "0.0.0.0:8982" ]