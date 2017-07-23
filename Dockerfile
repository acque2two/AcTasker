FROM python:3

WORKDIR /usr/src/app
CMD ["python3", "main.py"]

COPY AcTasker /usr/src/app/AcTasker
COPY static /usr/src/app/static
COPY main.py /usr/src/app
COPY config.py /usr/src/app
COPY requirements.txt /usr/src/app

RUN sh -c 'pip install -r requirements.txt; python -m compileall `find | grep \.py`'