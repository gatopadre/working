# working
A lot of stuff here

# para borrar todas las imagenes docker
docker rmi -f $(docker images -q)

# para crear un contenedor docker con postgres sql, con una bd llamada postgres, usuario postgres y clave Sebastian
docker run --name postgresContainer -e POSTGRES_PASSWORD=Sebastian -d postgres -it

# crear un contenedor desde una imagen de ubuntu
docker run -it --name ubuntuContainer \
  -p 5001:5001 \
  -v "/home/seba/Proyectos/Docker/Ubuntu":"/var/python" \
  custom-ubuntu /bin/bash

# para guardar estado de la imagen docker
docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]

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
