# skills-logiorden

Colección pública de **skills de IA en español**, organizadas por temática y pensadas para funcionar en **Claude** y **ChatGPT** (y en cualquier herramienta compatible con el estándar abierto [Agent Skills](https://agentskills.io)).

Una *skill* es una carpeta con un archivo `SKILL.md` que le enseña a la IA a hacer una tarea concreta de forma consistente: qué datos pedir, qué pasos seguir y qué entregar.

## Temáticas

| Temática | Qué contiene |
|---|---|
| [inmobiliaria](skills/inmobiliaria/) | Documentos y procesos propios del corretaje inmobiliario. |
| [imagenes](skills/imagenes/) | Edición y preparación de imágenes para publicar. |
| [documentos](skills/documentos/) | Lectura y análisis de documentación técnica. |
| [marketing](skills/marketing/) | Buyer personas, contenido y publicaciones para redes. |

Cada temática tiene su propio README con la lista de skills y su estado.

## Cómo instalar una skill

1. Andá a [Releases](../../releases) y descargá el `.zip` de la skill que quieras.
2. Subilo a tu plataforma:
   - **Claude** (web o escritorio): *Configuración → Capacidades → Skills → Subir skill*.
   - **ChatGPT**: sección *Skills* → *Subir skill* (la disponibilidad depende de tu plan).
   - **Claude Code / Codex / otras CLIs**: descomprimí la carpeta dentro de `.claude/skills/` o `.agents/skills/`.
3. Pedile a la IA la tarea; la skill se activa sola según su descripción.

> Para generar los `.zip` localmente: `python scripts/package.py` (quedan en `dist/`).

## Estructura del repo

```
skills/<tematica>/README.md            ← explicación de la temática
skills/<tematica>/<skill>/SKILL.md     ← instrucciones para la IA
skills/<tematica>/<skill>/README.md    ← explicación para personas
templates/                             ← plantillas para crear skills nuevas
scripts/                               ← validación y empaquetado
```

## Compatibilidad

Cada skill indica en su README en qué plataformas fue probada. Algunas dependen de capacidades que no todas las IAs tienen (por ejemplo, editar imágenes), y eso se aclara en la tabla de compatibilidad de la skill.

## Aviso

Las skills que generan documentos legales o comerciales producen **borradores**. Siempre deben ser revisados por un profesional matriculado antes de firmarse o publicarse. Ningún ejemplo del repo contiene datos reales.

## Contribuir

Ver [CONTRIBUTING.md](CONTRIBUTING.md).

## Licencia

[MIT](LICENSE)
