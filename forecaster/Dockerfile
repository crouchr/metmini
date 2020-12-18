FROM python:3.8.6-buster
LABEL author="Richard Crouch"
LABEL description="Weather Forecast microservice"

# Prerequisites
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

# Copy application and files
RUN mkdir /app
COPY app/*.py /app/
WORKDIR /app

EXPOSE 9501

CMD ["python3", "forecaster_service.py"]
