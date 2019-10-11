FROM python:3.7-slim

WORKDIR .

COPY test_requirements.txt test_requirements.txt

RUN pip3 install -r test_requirements.txt

COPY . .
