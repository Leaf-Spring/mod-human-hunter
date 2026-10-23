# AzerothCore: Módulo Humano Cazador

Este módulo para **AzerothCore (WotLK 3.3.5a)** habilita la combinación de raza y clase **Humano Cazador**. Incluye los scripts automatizados necesarios para parchear los archivos del cliente y del servidor de forma legal, sin distribuir binarios protegidos por derechos de autor.

> **IMPORTANTE:** Por motivos de derechos de autor, no se proporcionan los archivos de datos originales del juego de ninguna manera. Debes extraer los archivos DBC base desde tu propio cliente.

Los archivos requeridos para que este módulo funcione son:
- `CharBaseInfo.dbc`
- `CharStartOutfit.dbc`
- `SkillLineAbility.dbc`

---

## Paso 1: Parcheo y Creación del Archivo MPQ

1. Coloca tus 3 archivos DBC originales limpios en el mismo directorio donde se encuentran los scripts de instalación.

2. Abre tu terminal y otorga permisos de ejecución al script principal:

   ```bash
   chmod +x human_hunter.sh
   ```

3. Ejecuta el script:

   ```bash
   ./human_hunter.sh
   ```

**El script automatizado se encargará de realizar todo el trabajo pesado:**
- Verificará e instalará la herramienta `mpqcli` automáticamente si no la tienes en tu sistema.
- Ejecutará el script de Python (`human_hunter.py`) para inyectar la combinación de clase/raza y los trajes de inicio en tus archivos DBC, clonando el equipamiento del Cazador Elfo de la Noche para equipar arco en lugar de rifle.
- Creará la estructura interna requerida para el juego (`DBFilesClient/`) y copiará los DBCs ahí.
- Empaquetará la carpeta dentro de un archivo MPQ personalizado llamado `patch-y.mpq`.

---

## Paso 2: Instalación en el Servidor (AzerothCore)

Para que el emulador reconozca que el Humano puede ser Cazador, necesitas instalar el módulo, compilarlo y actualizar tus tablas.

1. Descarga o clona este repositorio directamente dentro del directorio `modules/` de tu código fuente de AzerothCore.
2. **Recompila el servidor:** Vuelve a ejecutar CMake y compila tu proyecto (con `make` en Linux o Visual Studio en Windows). Esto es indispensable para que el núcleo registre el módulo y prepare la inyección de la base de datos.
3. Toma los archivos DBC ya modificados por el script (`CharBaseInfo.dbc`, `CharStartOutfit.dbc`, `SkillLineAbility.dbc`).
4. Copia estos archivos dentro de la carpeta de datos de tu servidor ya compilado:  
   `bin/Data/dbc/` (o `data/dbc/` según la estructura de tu instalación).
5. Inicia tu servidor (`worldserver`). Al arrancar, el sistema inyectará el parche SQL automáticamente y cargará los nuevos DBCs en memoria.

---

## Paso 3: Instalación en el Cliente

Para que tu cliente de World of Warcraft 3.3.5a te permita crear el personaje y ver sus objetos iniciales sin errores:

1. Toma el archivo `patch-y.mpq` generado por el script automatizado.
2. Guarda el archivo `patch-y.mpq` directamente en la carpeta `Data/` de tu cliente de World of Warcraft 3.3.5a.
3. Elimina la carpeta `Cache` ubicada en la raíz de tu cliente de WoW.
4. ¡Inicia el juego!

> **Nota:** La inyección de la base de datos (SQL) es manejada automáticamente por el gestor de módulos de AzerothCore al compilar, por lo que no requieres realizar pasos manuales en tu gestor de base de datos.

---

## Apoyo
Si este módulo te ha sido de utilidad y deseas apoyar mi trabajo, puedes invitarme un café:  
☕ [buymeacoffee.com/foliaprintempo](https://buymeacoffee.com/foliaprintempo)