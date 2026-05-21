#  Organizador Inteligente de Archivos

Proyecto desarrollado en Python que permite organizar automáticamente archivos dentro de una carpeta según su tipo de extensión.

---

# Funcionalidades

* Organiza imágenes automáticamente
* Organiza archivos PDF
* Organiza documentos de texto
* Organiza música
* Organiza videos
* Organiza archivos comprimidos
* Crea carpetas automáticamente si no existen

---

# Tecnologías utilizadas

* Python 3
* Librerías estándar:

  * os
  * shutil

---

# Estructura del proyecto

```plaintext
organizador-archivos-python/
│
├── main.py
├── README.md
│
└── carpeta_prueba/
```

---

# Cómo ejecutar el proyecto

## 1. Clonar el repositorio

```bash
git clone https://github.com/daniluescobar-hue/organizador-archivos-python.git
```

---

## 2. Entrar a la carpeta del proyecto

```bash
cd organizador-archivos-python
```

---

## 3. Ejecutar el programa

```bash
python main.py
```

---

# ¿Cómo funciona?

El programa solicita la ruta de una carpeta y automáticamente:

* detecta los archivos,
* identifica su extensión,
* crea carpetas organizadas,
* y mueve cada archivo a su ubicación correspondiente.

---

# Ejemplo de funcionamiento

## Antes

```plaintext
carpeta_prueba/
foto.jpg
tarea.pdf
musica.mp3
video.mp4
```

---

## Después

```plaintext
carpeta_prueba/
│
├── Imagenes/
│   └── foto.jpg
│
├── PDFs/
│   └── tarea.pdf
│
├── Musica/
│   └── musica.mp3
│
└── Videos/
    └── video.mp4
```

---

## Objetivo del proyecto

Este proyecto fue desarrollado como práctica de automatización y manejo de archivos en Python, fortaleciendo habilidades de:

* lógica de programación,
* automatización,
* manipulación de archivos,
* y organización de código.

---

# Autora

Evelyn Daniela Escobar

Estudiante de Desarrollo de Software en UNAD Colombia.
