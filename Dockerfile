FROM python:2-alpine

RUN pip install --no-cache-dir beautifulsoup4 requests

WORKDIR /usr/src/rltn-team-updater

COPY updater.py .

CMD [ "python", "./updater.py" ]