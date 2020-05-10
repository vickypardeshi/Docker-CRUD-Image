# Set the base image
FROM ubuntu
FROM mysql:latest
FROM python:3.7.5-slim

ENV MYSQL_DATABASE myUsers
ENV MYSQL_DATABASE_USER vicky
ENV MYSQL_DATABASE_PASSWORD vicky@7767

COPY userDb.sql /docker-entrypoint-initdb.d/

# Copy the code
COPY . /app
 
# Work dir
WORKDIR /app

RUN pip3 install -r app/requirements.txt

# Expose the default port
EXPOSE 3306

# Set default container command
ENTRYPOINT ["python3"]

CMD ["app/app.py"]
CMD ["app/config.py"]
CMD ["app/main.py"]
