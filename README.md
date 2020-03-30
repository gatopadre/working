# working
A lot of stuff here

# comando para correr este archivo Dockerfile
docker build --tag [descripcion]-image .

# para borrar todas las imagenes docker
docker rmi -f $(docker images -q)

# para borrar todos los contenedores de docker
docker rm -f $(docker ps -a -q)

# para crear un contenedor docker con postgres sql, con una bd llamada postgres, usuario postgres y clave Sebastian
docker run --name postgresContainer -e POSTGRES_PASSWORD=Sebastian -d postgres -it

# crear un contenedor desde una imagen de ubuntu
docker run -it --name ubuntuContainer \
  -p 5001:5001 \
  -v "/home/seba/Proyectos/Docker/Ubuntu":"/var/python" \
  custom-ubuntu /bin/bash

# para guardar estado de la imagen docker
docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]

# comando para correr desde dockerfile
docker build --tag python_container .

# comando para correr el archivo docker-compose.yml
- docker-compose up
ó
- docker-compose up -d

############################################################
COMANDO PARA CREAR EL CONTENEDOR POSTGRES STANDAR CONFIGURADO
############################################################

docker run -it --name postgresContainerHost postgres:latest \
    -e POSTGRES_HOST_AUTH_METHOD=trust \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_DB=database \
    -e POSTGRES_PASSWORD=password \
    -e PGDATA=/var/lib/postgresql/data/pgdata \
    -v ${PWD}/postgresql/data/pgdata=/var/lib/postgresql/data/pgdata \
    --network dockerNetwork \
    --ip 10.0.0.1 \
    -p 9001:5432 \
    -h postgresContainerHost \
    -l ["name=postgresContainer","version=1", "autor=Seba"] \
    /bin/bash

# para sacar un contenedor para prueba básica de una imagen
docker run -it --name infra_test infra_image:latest /bin/bash

### receta dockerfile para crear una carpeta y hacer un archivo ###
# step 1
RUN mkdir -p /home/data
# step 2
RUN cd /home/data
# step 3
RUN touch /home/data/container.txt
# step 4
ADD ./data /home/data

### creando una nueva imagen
docker run -it --name installing_postgres -p 9001:5432 -v /home/seba/Works/Proyects/working/data:/var/lib/ postgresql/data/pgdata ubuntu_base

# pal docker file
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils

# pal dockerfile de postgres hay que verificar el estado del servicio
service postgresql status
# para levantar el servicio postgres
service postgresql start
