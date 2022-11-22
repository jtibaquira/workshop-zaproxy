# WorkShop ZAProxy

## Requerimientos

### Targets

Estos son algunos de los targets que se van a usar para las pruebas con la API

#### JUICE SHOP

docker pull bkimminich/juice-shop

docker run --rm -p 3000:3000 bkimminich/juice-shop

#### BODGEIT

docker pull psiinon/bodgeit

docker run --rm -p 8090:8080 -i -t psiinon/bodgeit

#### DVWA

docker pull vulnerables/web-dvwa

docker run --rm -it -p 3000:80 vulnerables/web-dvwa

#### DVGA

docker pull dolevf/dvga

docker run -t -p 5013:5013 -e WEB_HOST=0.0.0.0 dolevf/dvga

En el navegador http://localhost:5013

#### vAPI

git clone https://github.com/roottusk/vapi.git

cd vapi/

docker-compose build

docker-compose up -d

#### Petstore3

docker pull swaggerapi/petstore3:unstable

docker run  --name swaggerapi-petstore3 -d -p 8080:8080 swaggerapi/petstore3:unstable

### GraphQL Example

git clone https://github.com/marmelab/GraphQL-example.git

cd GraphQL-example/

make

make run-server

### KALI LINUX

- vagrant init kalilinux/rolling
- vagrant up
- vagrant ssh
- sudo apt install zaproxy

#### Instalar python Virtual Env

- python3 -m pip install --upgrade pip
- pip3 install virtualenv
- pip3 install --upgrade setuptools
- which python3
- which virtualenv
- cd directorio/projecto/
- virtualenv -p /usr/bin/python3 venv-zap
- source venv-zap/bin/activate
- pip3 install -r requirements.txt

### OWASP ZAP DAEMON MODE

Para todas las demos de este taller es necesario ejecutar el demonio de zaproxy, ejecutando el siguiente comando

<ZAP_HOME>./zap.sh -daemon -config api.key=zap-api-1337

Donde <ZAP_HOME> es la ubicacion de la instalacion del paquete de zaproxy.