# Total Image size: 956MB
FROM python:3.9.4

WORKDIR /app


COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./manage.py .
COPY ./django_app ./django_app
COPY ./myapp ./myapp
EXPOSE 8000

# bind to 0.0.0.0 to connect over http externally
# if running behind nginx, use a socket and not http
CMD ["gunicorn", "django_app.asgi:application", "-b", "0.0.0.0", "-w", "4", "-k", "uvicorn.workers.UvicornWorker"]

# If sharing a socket with nginx, create a socket
# CMD ["gunicorn", "django_app.asgi:application", "-b", "unix:/tmp/sockets/uvicorn.sock", "-w", "4", "-k", "uvicorn.workers.UvicornWorker"]