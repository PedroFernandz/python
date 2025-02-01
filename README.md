# Useful Scripts Collection 📜💻

Este repositorio contiene una colección de scripts útiles para diversas tareas de administración del sistema, desde la gestión de alias y rotación de logs hasta la realización de copias de seguridad y monitoreo de temperatura en una Raspberry Pi.

---

## 📂 Contenido del Repositorio

| Script                         | Descripción                                                                                         |
| ------------------------------ | --------------------------------------------------------------------------------------------------- |
| `add_alias.sh`                 | Añade un alias al archivo `.bashrc` del usuario actual.                                             |
| `add_logrotate.sh`             | Configura la rotación de logs para un archivo o directorio específico.                              |
| `backup_database.sh`           | Realiza una copia de seguridad de una base de datos PostgreSQL.                                    |
| `backup_mysql.sh`              | Realiza una copia de seguridad de una base de datos MySQL.                                         |
| `change-uuid.sh`               | Cambia el UUID de un sistema de archivos ext4.                                                      |
| `change_storage_engine.sql`    | Cambia el motor de almacenamiento de todas las tablas en una base de datos MySQL.                   |
| `clean-folder-files.sh`        | Elimina archivos en un directorio que tienen más de un número específico de días.                   |
| `temperature-raspberry.sh`     | Muestra la temperatura actual de la CPU en una Raspberry Pi.                                       |

---

## ⚙️ Requisitos

- **Sistemas Unix/Linux**: Estos scripts están diseñados para entornos Unix o Linux.
- **Permisos de ejecución**: Asegúrate de que los scripts tengan permisos de ejecución. Puedes otorgarlos con:
  ```bash
  chmod +x script_name.sh
  ```
- **Dependencias específicas**:
  - Para `backup_database.sh`: Se requiere tener instalado `pg_dump`.
  - Para `backup_mysql.sh`: Se requiere tener instalado `mysqldump`.
  - Para `temperature-raspberry.sh`: Se necesita una Raspberry Pi con los comandos adecuados disponibles.

---

## 🚀 Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/PedroFernandz/useful-scripts.git
   cd useful-scripts
   ```

---

## 📂 Contenido del Repositorio y Ejemplos de Uso

### `add_alias.sh` 🔗

**Descripción:**
Añade un alias al archivo `.bashrc` del usuario actual.

**Ejemplo de uso:**
```bash
./add_alias.sh gs "git status"
```
Esto añadirá el alias `gs` que ejecuta `git status`.

---

### `add_logrotate.sh` 🔄

**Descripción:**
Configura la rotación de logs para un archivo o directorio específico.

**Ejemplo de uso:**
```bash
./add_logrotate.sh /var/log/myapp.log
```
Esto configurará la rotación de logs para `/var/log/myapp.log`.

---

### `backup_database.sh` 🗄️

**Descripción:**
Realiza una copia de seguridad de una base de datos PostgreSQL.

**Ejemplo de uso:**
```bash
./backup_database.sh mydatabase
```
Esto creará una copia de seguridad de `mydatabase`.

---

### `backup_mysql.sh` 🗄️

**Descripción:**
Realiza una copia de seguridad de una base de datos MySQL.

**Ejemplo de uso:**
```bash
./backup_mysql.sh mydatabase
```
Esto creará una copia de seguridad de `mydatabase`.

---

### `change-uuid.sh` 🆔

**Descripción:**
Cambia el UUID de un sistema de archivos ext4.

**Ejemplo de uso:**
```bash
./change-uuid.sh /dev/sdX1
```
Esto cambiará el UUID de la partición `/dev/sdX1`.

---

### `change_storage_engine.sql` 🔧

**Descripción:**
Cambia el motor de almacenamiento de todas las tablas en una base de datos MySQL.

**Ejemplo de uso:**
```sql
source change_storage_engine.sql
```
Esto cambiará el motor de almacenamiento de todas las tablas a InnoDB.

---

### `clean-folder-files.sh` 🧹

**Descripción:**
Elimina archivos en un directorio que tienen más de un número específico de días.

**Ejemplo de uso:**
```bash
./clean-folder-files.sh /path/to/directory 30
```
Esto eliminará archivos en `/path/to/directory` que tienen más de 30 días.

---

### `temperature-raspberry.sh` 🌡️

**Descripción:**
Muestra la temperatura actual de la CPU en una Raspberry Pi.

**Ejemplo de uso:**
```bash
./temperature-raspberry.sh
```
Esto mostrará la temperatura actual de la CPU.

---

> **Nota:** Asegúrate de revisar y entender cada script antes de ejecutarlo en tu sistema. Algunos scripts pueden requerir permisos de superusuario o configuraciones específicas.
