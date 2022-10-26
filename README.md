# 101 OWASP ZAP API

## Requerimientos 

### Targets

Estos son algunos de los targets que se van a usar para las pruebas con la API

#### JUICE SHOP
docker run --rm -p 3000:3000 bkimminich/juice-shop

#### BODGEIT
docker run --rm -p 8090:8080 -i -t psiinon/bodgeit

#### DVWA
docker run --rm -it -p 3000:80 vulnerables/web-dvwa


### KALI LINUX

vagrant init kalilinux/rolling
vagrant up

#### Instalar owasp pip lib

pip install python-owasp-zap-v2.4


### OWASP ZAP DAEMON MODE

Para todas las demos de este taller es necesario ejecutar el demonio de zaproxy, ejecutando el siguiente comando

<ZAP_HOME>./zap.sh -daemon -config api.key=zap-api-1337

Donde <ZAP_HOME> es la ubicacion de la instalacion del paquete de zaproxy.