# Cómo crear o modificar una skill

## 1. Elegí la temática

Las skills se agrupan por **área de trabajo** (`inmobiliaria`, `imagenes`, `documentos`, `marketing`). Si ninguna encaja, creá una temática nueva copiando `templates/categoria/README.md`.

## 2. Copiá la plantilla

```bash
cp -r templates/skill skills/<tematica>/<nombre-de-la-skill>
```

## 3. Convenciones obligatorias

- **Nombre:** minúsculas, números y guiones, sin tildes ni ñ (`autorizacion-de-venta`). Máximo 64 caracteres.
- **El `name` del frontmatter es igual al nombre de la carpeta** y es único en todo el repo.
- **`description`:** qué hace y cuándo usarla, en una o dos oraciones (máx. 1024 caracteres). Es lo que la IA lee para decidir si activa la skill.
- **Datos extra** (versión, tags, plataformas) van dentro de `metadata:` para respetar el estándar.
- **`SKILL.md` es para la IA, `README.md` es para personas.** No dupliques contenido.
- **Portabilidad:** no menciones herramientas propias de una sola plataforma en las instrucciones principales. Si algo depende de la plataforma, ponelo en una sección "Según la plataforma".
- **Sin datos reales:** ejemplos siempre ficticios (nombres, DNI, domicilios, fotos).
- `SKILL.md` idealmente de menos de 500 líneas; el detalle va en `references/`.

## 4. Validá antes de subir

```bash
python scripts/validate.py
```

## 5. Actualizá el README de la temática

Agregá la skill a la tabla con su estado (`beta` o `estable`) y anotá el cambio en `CHANGELOG.md`.
