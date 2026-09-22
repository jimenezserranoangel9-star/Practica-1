ARG PYTHON_VERSION=3.11

FROM python:${PYTHON_VERSION}-slim

ARG PYTHON_VERSION

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

WORKDIR /app

RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "--version"] 