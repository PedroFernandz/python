# Python Scripts Collection 🐍💻

Este repositorio contiene una colección de scripts en **Python** diseñados para diversas tareas, incluyendo copias de seguridad de bases de datos, control de velocidad de ventiladores y análisis de calidad de películas.

---

## 📂 Contenido del Repositorio

| Script                      | Descripción                                                                                         |
| --------------------------- | --------------------------------------------------------------------------------------------------- |
| `backup_database.py`        | Realiza una copia de seguridad de una base de datos PostgreSQL.                                     |
| `fan_speed_control.py`      | Controla la velocidad del ventilador en sistemas compatibles.                                       |
| `movie_quality_analyzer.py` | Analiza y evalúa la calidad de archivos de video.                                                   |
| `read-fan-speed.py`         | Lee y muestra la velocidad actual del ventilador del sistema.                                       |

---

## ⚙️ Requisitos

- **Python 3.x**: Asegúrate de tener instalada la versión 3.x de Python.
- **Dependencias específicas**:
  - Para `backup_database.py`:
    - Biblioteca `psycopg2` para la conexión con bases de datos PostgreSQL.
    - Credenciales de acceso a la base de datos.
  - Para `fan_speed_control.py` y `read-fan-speed.py`:
    - Acceso a interfaces del sistema que permitan la lectura y control de la velocidad del ventilador.
    - Permisos de superusuario pueden ser necesarios.
  - Para `movie_quality_analyzer.py`:
    - Bibliotecas como `ffmpeg` o `opencv` para el análisis de video.

---

## 🚀 Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/PedroFernandz/python.git
   cd python
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 📂 Contenido del Repositorio y Ejemplos de Uso

### `backup_database.py` 🗄️

**Descripción:**
Realiza una copia de seguridad de una base de datos PostgreSQL y la almacena en un archivo comprimido.

**Ejemplo de uso:**
```bash
python backup_database.py
```
El script debe ser configurado con los detalles de la base de datos en su código.

---

### `fan_speed_control.py` 🌬️

**Descripción:**
Controla la velocidad del ventilador del sistema ajustando los parámetros según la temperatura o configuraciones predefinidas.

**Ejemplo de uso:**
```bash
sudo python fan_speed_control.py
```
Este script requiere permisos de superusuario para modificar la velocidad del ventilador.

---

### `movie_quality_analyzer.py` 🎥

**Descripción:**
Analiza archivos de video para evaluar su calidad basándose en métricas como resolución, bitrate y códecs utilizados.

**Ejemplo de uso:**
```bash
python movie_quality_analyzer.py
```
El script analiza un archivo de video especificado dentro del código.

---

### `read-fan-speed.py` 🌡️

**Descripción:**
Lee y muestra la velocidad actual del ventilador del sistema en RPM (revoluciones por minuto).

**Ejemplo de uso:**
```bash
sudo python read-fan-speed.py
```
Este script requiere permisos de superusuario para acceder a los sensores del sistema.

---

> **Nota:** Asegúrate de revisar y entender cada script antes de ejecutarlo en tu sistema. Algunos scripts pueden requerir permisos de superusuario o configuraciones específicas. Además, es recomendable probar los scripts en un entorno de desarrollo antes de implementarlos en producción.
