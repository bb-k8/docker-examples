# Total Image size: 956MB
FROM python:3.9.4

WORKDIR /app
# for uwsgi spooler / background tasks
RUN mkdir ./spooler

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./flask_app ./flask_app
COPY uwsgi.ini .

# not used in this app, but can be useful for configs
ENV FLASK_APP=flask_app
ENV FLASK_ENV=production
ENV FLASK_DATABASE_URI=postgres://user:pass@host:port/db
EXPOSE 5000

CMD ["uwsgi", "--ini", "uwsgi.ini"]
