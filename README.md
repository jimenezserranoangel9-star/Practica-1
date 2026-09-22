Práctica 1: Entorno Multicontenedor y Control de Versiones

Descripción General

Este repositorio contiene la configuración del entorno de desarrollo multicontenedor utilizando Docker y Docker Compose, enfocado en el despliegue de aplicaciones desarrolladas en Python.

Justificación de la Elección de Versiones de Python

Para la arquitectura del entorno Docker se seleccionaron tres versiones específicas del lenguaje Python:

Python 3.11: Garantiza compatibilidad retroactiva y estabilidad con librerías legacy e infraestructuras de producción previas.

Python 3.12: Se establece como la versión base estandarizada para el desarrollo del proyecto por su equilibrio entre rendimiento y madurez en el ecosistema.

Python 3.13: Utilizada para pruebas de vanguardia, validando características recientes y evaluando el rendimiento en versiones modernas del intérprete.

Estructura del Proyecto

practica1-tc/
├── README.md
├── .gitignore
├── requirements.txt
├── pytest.ini
├── docs/
│   ├── 01-entorno.md
│   ├── 02-investigacion.md
│   ├── 03-estado-del-arte.md
│   ├── 04-jflap.md
│   ├── 05-aplicacion.md
│   ├── conclusiones.md
│   └── bibliografia.md
├── entorno/
│   ├── Dockerfile
│   ├── compose.yml
│   └── requirements.txt
├── automatas/
├── src/
│   ├── lenguajes.py
│   └── app.py
├── tests/
│   └── test_lenguajes.py
└── evidencias/
    ├── git/
    ├── docker/
    ├── jflap/
    └── app/


Uso del Entorno

Para levantar los servicios y verificar las versiones en cada contenedor, ejecuta los siguientes comandos dentro del directorio entorno/:

# Verificación de versiones de Python
docker compose run --rm py311 python --version
docker compose run --rm py312 python --version
docker compose run --rm py313 python --version

# Levantar servidor web Flet en puerto 8550
docker compose up
