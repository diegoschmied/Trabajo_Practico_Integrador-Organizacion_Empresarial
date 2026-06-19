# Chatbot de Soporte Técnico Nivel 1

## Descripción

Proyecto desarrollado en Python que automatiza la atención inicial de incidencias frecuentes mediante un chatbot. El sistema consulta una base de conocimientos con soluciones predefinidas y, en caso de no resolver el problema, deriva el ticket al soporte de Nivel 2.

## Objetivo

Automatizar la atención inicial de incidencias frecuentes para reducir los tiempos de respuesta y optimizar los recursos del área de soporte técnico.

## Características

* Registro de consultas de usuarios.
* Búsqueda automática de soluciones conocidas.
* Confirmación de resolución del problema.
* Derivación al soporte técnico de Nivel 2 cuando sea necesario.
* Almacenamiento de información mediante archivos CSV.

## Tecnologías utilizadas

* Python
* Archivos CSV
* Visual Studio Code
* Git y GitHub

## Estructura del proyecto

```text
├── main.py
├── problemas.csv
├── tickets.csv
└── README.md
```

## Base de datos

### problemas.csv

Contiene los problemas frecuentes y sus respectivas soluciones.

Campos:

* problema
* solucion

### tickets.csv

Almacena el historial de incidencias registradas.

Campos:

* id
* usuario
* problema
* estado

## Funcionamiento del sistema

1. El usuario ejecuta el programa.
2. Ingresa su nombre.
3. Describe el inconveniente experimentado.
4. El sistema analiza la información ingresada.
5. Si existe una solución registrada, esta es mostrada al usuario.
6. El usuario confirma si la solución funcionó.
7. En caso de funcionar, el ticket se cierra.
8. En caso contrario, el incidente es derivado al soporte técnico de Nivel 2.

## Manual de usuario

### Requisitos

* Python 3 instalado.

### Ejecución del programa

1. Clonar el repositorio:

```bash
git clone https://github.com/diegoschmied/Trabajo_Practico_Integrador-Organizacion_Empresarial.git
```

2. Acceder al directorio del proyecto:

```bash
cd nombre-del-repositorio
```

3. Ejecutar el programa:

```bash
python main.py
```

### Uso del sistema

* Ingrese su nombre cuando sea solicitado.
* Describa el problema técnico presentado.
* Si el sistema encuentra una solución, siga las instrucciones mostradas.
* Indique si la solución resolvió el inconveniente.
* Si el problema persiste o no se encuentra registrado, el sistema derivará automáticamente el caso al soporte técnico de Nivel 2.

  
