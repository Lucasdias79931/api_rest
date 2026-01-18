FROM python:3.12-slim


WORKDIR /app


RUN sudo apt --no-cache update -y \
    && sudo apt upgrade \
    sudo apt install libpq-dev


