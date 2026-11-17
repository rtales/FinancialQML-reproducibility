FROM python:3.13.11-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    MPLCONFIGDIR=/tmp/matplotlib

WORKDIR /release
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt
COPY data ./data
COPY src ./src
RUN mkdir -p /release/outputs/reproduced

CMD ["python", "src/reproduce.py", "--out", "outputs/reproduced"]
