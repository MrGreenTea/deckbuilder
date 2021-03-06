FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
  && apk add curl \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi

RUN addgroup -S django \
    && adduser -S -G django django

RUN set -o pipefail && curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
RUN poetry config settings.virtualenvs.create false

# Requirements are installed here to ensure they will be cached.
ARG EXTRAS=none
COPY pyproject.* ./
RUN poetry install --no-dev --extras deploy --extras $EXTRAS
RUN rm pyproject.*

COPY ./compose/production/django/entrypoint /entrypoint
RUN chmod +x /entrypoint
RUN chown django /entrypoint

COPY ./compose/production/django/start /start
RUN chmod +x /start
RUN chown django /start

COPY . /app

RUN chown -R django /app

USER django

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
