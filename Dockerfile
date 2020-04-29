# Set the base image
FROM ubuntu
FROM mysql:latest
FROM python:3.7.5-slim

ENV MYSQL_DATABASE myUsers

COPY userDb.sql /docker-entrypoint-initdb.d/
 
# Work dir
WORKDIR /app

# Copy the code
COPY . /app

RUN pip3 install -r app/requirements.txt

# Expose the default port
EXPOSE 8080

# Set default container command
ENTRYPOINT ["python3"]

CMD ["app/app.py"]
CMD ["app/config.py"]
CMD ["app/main.py"]

