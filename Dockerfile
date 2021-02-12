FROM python:3.6.12-slim-buster

WORKDIR /usr/src/app

ARG WH_PORT=8443
ARG DEPLOY_MODE=DEV

ENV PORT=${WH_PORT}
ENV MODE=${DEPLOY_MODE}

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv && \
  apt-get update && \
  apt-get install -y --no-install-recommends gcc python3-dev libssl-dev && \
  pipenv install --deploy --system && \
  apt-get remove -y gcc python3-dev libssl-dev && \
  apt-get autoremove -y && \
  pip uninstall pipenv -y

COPY . .

CMD python main.py