FROM python:3.10

EXPOSE 5055

RUN mkdir -p /opt/services/mcsbot/mcs-bot
WORKDIR /opt/services/mcsbot/mcs-bot


COPY . /opt/services/mcsbot/mcs-bot/

RUN pip install -r requirements.txt

CMD ["python", "/opt/services/mcsbot/mcs-bot/main.py"]