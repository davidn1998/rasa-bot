FROM python:3.6

RUN pip3 install --no-cache rasa==1.10.2
ADD . /app/
RUN chmod +x /app/start_services.sh
CMD /app/start_services.sh