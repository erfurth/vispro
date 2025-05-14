FROM python:3.11

WORKDIR /bridge-microservice 

COPY ./requirements.txt /bridge-microservice/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /bridge-microservice/requirements.txt

COPY ./app /bridge-microservice/app

#COPY .env .

CMD [ "fastapi", "run", "app/bridge.py", "--port", "80" ]