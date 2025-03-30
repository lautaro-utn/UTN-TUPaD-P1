## 1) Contestar las siguientes preguntas utilizando las guías y documentación proporcionada
### ¿Qué es GitHub?
GitHub es una plataforma de desarrollo colaborativo basada en la nube que utiliza Git como sistema de control de versiones. Permite a los desarrolladores alojar, compartir y colaborar en proyectos de software.

### ¿Cómo crear un repositorio en GitHub?
1. Hacer clic en el botón "+" en la esquina superior derecha y seleccionar "New repository".
2. Ingresar un nombre para el repositorio.
3. Opcionalmente, agregar una descripción y elegir si será público o privado.

### ¿Cómo crear una rama en Git?
```sh
 git branch nombre-rama
```

### ¿Cómo cambiar a una rama en Git?
```sh
 git checkout nombre-rama
```
O:
```sh
 git switch nombre-rama
```

### ¿Cómo fusionar ramas en Git?
```sh
 git checkout rama-principal
 git merge nombre-rama
```

### ¿Cómo crear un commit en Git?
```sh
 git add .
 git commit -m "Mensaje del commit"
```

### ¿Cómo enviar un commit a GitHub?
```sh
 git push origin nombre-rama
```

### ¿Qué es un repositorio remoto?
Un repositorio remoto es una versión del repositorio almacenada en la nube o en otro servidor, como GitHub.

### ¿Cómo agregar un repositorio remoto a Git?
```sh
 git remote add origin URL-del-repositorio
```

### ¿Cómo empujar cambios a un repositorio remoto?
```sh
 git push origin nombre-rama
```

### ¿Cómo tirar de cambios de un repositorio remoto?
```sh
 git pull origin nombre-rama
```

### ¿Qué es un fork de repositorio?
Un fork es una copia de un repositorio en tu cuenta de GitHub para hacer cambios sin afectar el original.

### ¿Cómo crear un fork de un repositorio?
1. Ir al repositorio en GitHub.
2. Hacer click en el botón "Fork" en la esquina superior derecha.

### ¿Cómo enviar una solicitud de extracción (pull request) a un repositorio?
1. Hacer los cambios y subir tu rama a GitHub.
2. Ir al repositorio en GitHub y hacer click en "Compare & pull request".
3. Agrega una descripción y hacer click en "Create pull request".

### ¿Cómo aceptar una solicitud de extracción?
1. Ir a la pestaña "Pull requests" en el repositorio.
2. Abrir la solicitud de extracción.
3. Revisar los cambios y hacer click en "Merge pull request".

### ¿Qué es una etiqueta en Git?
Una etiqueta (tag) es una referencia a un punto específico en el historial de commits, usualmente para marcar versiones.

### ¿Cómo crear una etiqueta en Git?
```sh
 git tag -a v1.0 -m "Versión 1.0"
```

### ¿Cómo enviar una etiqueta a GitHub?
```sh
 git push origin v1.0
```

### ¿Qué es un historial de Git?
El historial de Git es el registro de todos los commits hechos en un repositorio.

### ¿Cómo ver el historial de Git?
```sh
 git log
```

### ¿Cómo buscar en el historial de Git?
```sh
 git log --grep="palabra clave"
```

### ¿Cómo borrar el historial de Git?
El historial no se puede borrar directamente, pero se puede reiniciar el repositorio con:
```sh
 git reset --hard HEAD~n  # Revierte los últimos n commits
```

### ¿Qué es un repositorio privado en GitHub?
Es un repositorio visible solo para personas con permiso.

### ¿Cómo crear un repositorio privado en GitHub?
1. Hacer clic en el botón "+" en la esquina superior derecha y seleccionar "New repository".
2. Ingresar un nombre para el repositorio.
3. Opcionalmente, agregar una descripción y elegir "Private" en la configuración.

### ¿Cómo invitar a alguien a un repositorio privado en GitHub?
1. Ir al repositorio y hacer click en "Settings".
2. Ir a "Collaborators" y agregar el usuario.

### ¿Qué es un repositorio público en GitHub?
Un repositorio visible para cualquier usuario en GitHub.

### ¿Cómo crear un repositorio público en GitHub?
1. Hacer clic en el botón "+" en la esquina superior derecha y seleccionar "New repository".
2. Ingresar un nombre para el repositorio.
3. Opcionalmente, agregar una descripción y elegir "Public" en la configuración.

### ¿Cómo compartir un repositorio público en GitHub?
Simplemente proporcionando la URL del repositorio a quien se desee compartirlo.

## 2) 
Link al repo de resolución: https://github.com/lautaro-utn/UTN-TUPaD-P1-TP2-A2

## 3) 
Link al repo de resolución: https://github.com/lautaro-utn/UTN-TUPaD-P1-TP2-A3