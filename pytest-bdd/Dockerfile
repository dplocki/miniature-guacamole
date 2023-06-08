FROM python:3.10

WORKDIR /home

RUN pip install pytest-bdd

COPY calculator /home/calculator
COPY pytest-bdd/test_calculator.py /home/test_calculator.py

COPY features/test_calculator.feature /home/test_calculator.feature

CMD pytest
