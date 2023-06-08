FROM python:3.10

WORKDIR /home

RUN pip install radish-bdd

COPY calculator /home/calculator
COPY radish/radish /home/radish/radis

COPY features/test_calculator.feature /home/features/test_calculator.feature

CMD PYTHONPATH=. radish features/
