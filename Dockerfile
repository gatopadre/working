FROM postgres
MAINTAINER "SebaZuniga sebastianzunigasaavedra@gmail.com"
WORKDIR /home
RUN echo $PWD && ls -la
RUN mkdir -p /postgresql/data/
COPY . /var/lib/postgresql/data/pgdata
EXPOSE 5432

FROM python:alpine3.7
COPY . /app
WORKDIR /app
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install --upgrade pip
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
#CMD python ./index.py
# comando para correr docker build --tag python_container .
