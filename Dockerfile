FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN pip install --upgrade pip
COPY . /app/server
RUN pip install -r /app/server/requirements.txt

ENV LISTEN_PORT 8005
ENV PYTHONPATH="/app/jacks:/app/server"
ENV FLASK_DEBUG 1
ENV UWSGI_INI /app/server/uwsgi.ini
ENV STATIC_PATH /app/server/static
ENV STATIC_URL /JACKS/static
WORKDIR /app/server

EXPOSE 8005
