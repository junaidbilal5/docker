#pull the latest MySQL image
FROM mysql:8.0
# Set the root password for MySQL/set environment variable
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=mydatabase


#ENV MYSQL_USER=myuser
#ENV MYSQL_PASSWORD=mypassword


#if you want to create the table
COPY ./init.sql /docker-entrypoint-initdb.d/



# Expose the MySQL port

EXPOSE  3307
