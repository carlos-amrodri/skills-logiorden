# Autorización de venta

> Estado: **beta** · Versión: 0.1.0

## Qué resuelve

Armar una autorización de venta a mano lleva tiempo y es fácil equivocarse al copiar un DNI o una matrícula. Esta skill lee las fotos de los documentos, extrae los datos, te avisa lo que falta o no coincide y redacta el borrador completo.

## Ejemplos de uso

- "Armame la autorización de venta con estas fotos del DNI y la escritura."
- "Tengo una captación nueva, exclusiva por 60 días al 3 %. Te paso los documentos."
- "Completá la autorización con los datos de este informe de dominio."

## Qué necesita

- Fotos o escaneos del DNI de cada propietario.
- Escritura o informe de dominio del inmueble.
- Precio, plazo, exclusividad y honorarios.
- Tus datos como corredor (te los pide si no se los diste).

## Qué entrega

1. Una tabla con los datos detectados y las dudas marcadas.
2. El borrador de la autorización, listo para revisar y firmar.
3. Una lista de verificación antes de la firma.

## Compatibilidad

| Plataforma | Estado | Notas |
|---|---|---|
| Claude | ✅ | Puede entregar además el documento en `.docx` o PDF. |
| ChatGPT | ✅ | Puede entregar además el documento en `.docx` o PDF. |

## Limitaciones

- La calidad de la extracción depende de la nitidez de las fotos.
- La estructura es genérica (basada en la práctica argentina). Si tu colegio profesional tiene un modelo oficial, pasáselo a la IA y lo va a respetar.
- **Es un borrador:** siempre lo tiene que revisar un corredor matriculado.

## Privacidad

Las fotos de DNI contienen datos personales. Usá la skill en cuentas donde tengas configurada la privacidad que necesitás y no compartas los documentos generados fuera de la operación.

## Archivos

- `SKILL.md`: instrucciones para la IA.
- `references/estructura-autorizacion.md`: secciones del documento y lista de verificación.
- `examples/ejemplo-ficticio.md`: un caso de uso con datos inventados.
