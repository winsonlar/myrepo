FROM python:3.11-slim-bullseye

LABEL name=myapp

ARG APP_DIR=/app

WORKDIR ${APP_DIR}

ENV INSTANCE_NAME=""
ENV INSTANCE_HASH=""


ADD main.py .
ADD requirements.txt .
ADD public public
ADD templates templates
ADD run.sh .
ADD utils.py .

RUN pip install -r requirements.txt

ENV APP_PORT=3000

EXPOSE ${APP_PORT}

# RUN chmod +x run.sh

ENTRYPOINT python main.py
CMD []
# ENTRYPOINT ["python", "main.py"]

# docker container run -d -p 5000:5000 --name winliaolar winliaolar/dov-bear:v1.0.0 -e INSTANCE_NAME="dov-bear" -e APP_PORT=5000