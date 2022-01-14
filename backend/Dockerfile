FROM python:3
WORKDIR /app
ADD . /app

RUN python3 -m pip install -U pip
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3", "server.py"]
