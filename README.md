# HidraVP_escritorio
La siguiente aplicación se desarrollo para el trabajo de grado titulado *Desarrollo de una herramienta computacional para el diseño de dos estructuras hidráulicas: Vertedero de  cresta larga y Partidor proporcional* para obtener el titulo de ingeniero agrícola de la Universidad del Valle


## Instalación
### **Windows**

En windows no es necesario instalar un programa previo basta con descargar este repositorio en una carpeta comprimida en formato zip, descomprima la carpeta y siga la siguiente ruta: 

'HidraVP_escritorio -> ejecutable -> aplicacion' 

Esta ultima carpeta contiene el archivo aplicacion.exe al dar doble clic sobre el, inmediatamente dara inicio a la herramienta.

### **Mac y Linux**

Para su ejecución es necesario contar con Python, en una versión igual o mayor a 3.3 

Puede reaizar su instalación por medio de este enlace: [Python Download](https://www.python.org/downloads/) 

Posteriormente se realiza la descarga de este repositorio en una carpeta comprimida en formato zip. A continuación, desde una terminal omitiendo el signo *$* ingrese lo siguiente:

*Instalación de requerimientos*
```shell
$ cd HidraVP_escritorio/
$ pip install -r requirements.txt
```

*Ejecución*
```shell
$ cd src/
$ python aplicacion.py
```