
# Anotacion --> este archivo sirve para generar una imagen con la receta que se
# declara aqui, las configuraciones y caracteristicas necesarias.
# Anotacion --> tienen que existir los directorios en el host previamente
# Anotacion --> comando para correr este archivo: docker build --tag [descripcion]_image .

# FROM postgres AS database
# MAINTAINER "SebaZuniga sebastianzunigasaavedra@gmail.com"
# COPY ./postgresql/data/pgdata /var/lib/postgresql/data/pgdata
# VOLUME ./postgresql/data/pgdata
# EXPOSE 5432

FROM python:alpine3.7 AS backend
COPY . /app
WORKDIR /app
RUN apt install libpq-dev
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 172.0.0.24
ENV FLASK_ENV development
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# RUN pip install psycopg2
EXPOSE 5000
CMD ["flask", "run"]

#CMD python ./index.py
