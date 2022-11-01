FROM python:3.10

EXPOSE 5023

RUN mkdir -p /opt/services/bot/mcs-bot
WORKDIR /opt/services/bot/mcs-bot


COPY . /opt/services/bot/mcs-bot/

RUN pip install -r requirements.txt

CMD ["python", "/opt/services/bot/mcs-bot/main.py"]