FROM ubuntu:20.04
WORKDIR /code
COPY . .
RUN apt -y update && apt install -y python3-pip && pip3 install flask
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0
ENTRYPOINT ["flask", "run"]
