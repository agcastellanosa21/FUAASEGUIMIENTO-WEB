FROM python:3.9.1
ADD . /seguimiento-gps
WORKDIR /seguimiento-gps
RUN pip install -r requirements.txt