FROM python:3.11

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD [ "fastapi", "run", "main.py", "--port", "80" ]