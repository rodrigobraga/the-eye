FROM python:3.10.2 as builder

WORKDIR /app

ENV DEBIAN_FRONTEND noninteractive

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONHASHSEED random
ENV PYTHONBREAKPOINT ipdb.set_trace

ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on
ENV PIP_DEFAULT_TIMEOUT 100

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

COPY ./requirements.txt .

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt


FROM python:3.10.2-slim

LABEL maintainer="webmaster@ca.com"
LABEL vendor="ca"

ENV DJANGO_SETTINGS_MODULE api.settings
ENV TZ America/Sao_Paulo
ENV DJANGO_COLORS dark

WORKDIR /app

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

RUN pip install --no-cache /wheels/*

COPY ./docker/runserver.sh /runserver.sh
RUN chmod +x "/runserver.sh"

COPY ./src /app

RUN python manage.py collectstatic --noinput

CMD ["/runserver.sh"]
