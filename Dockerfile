FROM python:3.12-alpine
RUN apk add --update python3 py3-pip
RUN python3 -m venv /opt/venv
RUN pip install Flask


WORKDIR /app 
COPY . .
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]