FROM python:3.10

WORKDIR /home

RUN pip install behave

COPY calculator /home/calculator
COPY behave/steps /home/features/steps

COPY features/test_calculator.feature /home/features/test_calculator.feature

CMD behave
