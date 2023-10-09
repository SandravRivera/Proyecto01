# Proyecto01_WebService
Proyecto01, Modelado y Programación.

## Integrantes
  * Morales Flores Luis Enrique (modelo, diccionarios, caché)
  * Sánchez Estrada Alejandro (vista, json)
  * Acevedo Romero Miroslava (pruebas unitarias, presentación)
  * Rivera Lara Sandra Valeria (controlador, Levenshtein)
## Requerimientos
El programa funciona con Python 3 y tiene los siguientes requerimientos:

### Frameworks
* Flask 2.3.3

### Bibliotecas y paquetes
* blinker  1.6.2
* certifi  2023.7.22
* charset-normalizer  3.3.0
* click  8.1.7
* colorama  0.4.6
* Flask  2.3.3
* idna  3.4
* itsdangerous  2.1.2
* Jinja2  3.1.2
* MarkupSafe  2.1.3
* numpy  1.26.0
* requests  2.31.0
* Unidecode  1.3.7
* urllib3  2.0.6
* Werkzeug  2.3.7


## Instrucciones de Ejecución
Es recomendable crear primero un entorno virtual dentro de la carpeta Proyecto01. Para hacerlo y activarlo, se deben de seguir las siguientes instrucciones: https://python.land/virtual-environments/virtualenv

### Instalación de paquetes
Dentro de la carpeta Proyecto01 escribir:

pip install -r requirements.txt

Para confirmar que se instaló todo de "Bibliotecas y paquetes" correctamente, revisar que estén en la lista obtenida con el siguiente comando:

pip list

De no haberse instalado algún paquete, escribir el comando:

pip install <nombre paquete>

### Pruebas unitarias

Abrir una terminal en la carpeta Proyecto01/src y ejecutar el comando:

python -m unittest

para correr todas las pruebas unitarias del modelo.

### Ejecución

Escribir en la carpeta Proyecto01 el siguiente comando:

python src\app.py

Puede tardar unos minutos en cargar, pero luego se debe dar click en el link que se muestra en la consola. Ahora la app se debe de abrir en el navegador y después de que cargue ya está lista para usarse.


