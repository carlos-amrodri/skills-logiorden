---
name: autorizacion-de-venta
description: Genera el borrador de una autorización de venta inmobiliaria a partir de fotos o escaneos de DNI, escritura o informe de dominio y datos de la operación. Usar cuando un agente o corredor inmobiliario pide armar, redactar o completar una autorización de venta, captación o mandato de venta.
license: MIT
metadata:
  version: "0.1.0"
  estado: beta
  tematica: inmobiliaria
  tags: [inmobiliaria, documentos-legales, captacion]
  plataformas: [claude, chatgpt]
---

# Autorización de venta

Armar un borrador completo y prolijo de autorización de venta, tomando los datos de las imágenes que sube el usuario y pidiendo solo lo que falte.

## Datos que necesitás

**Del o los propietarios** (de las fotos de DNI): nombre completo, DNI, CUIT/CUIL si aparece, estado civil, domicilio. Si hay cónyuge con derecho sobre el bien, también sus datos (asentimiento conyugal).

**Del inmueble** (de la escritura o informe de dominio): dirección, localidad y provincia, matrícula o folio registral, nomenclatura catastral, superficie, porcentaje de titularidad de cada propietario.

**Del corredor:** nombre, matrícula, colegio profesional, domicilio. Si no los tenés, preguntalos una sola vez.

**De la operación:** precio y moneda, plazo de vigencia, exclusividad (sí/no), honorarios (% y quién los paga), jurisdicción.

## Pasos

1. Revisá cada imagen e identificá qué documento es.
2. Extraé los datos y armá una tabla de **datos detectados**, marcando con ⚠️ los que estén borrosos, incompletos o no coincidan entre documentos (por ejemplo, un nombre escrito distinto en el DNI y en la escritura).
3. Preguntá en un solo mensaje todo lo que falte o esté marcado con ⚠️. No sigas hasta tener los datos obligatorios.
4. Redactá la autorización usando la estructura de `references/estructura-autorizacion.md`.
5. Al final agregá la lista de verificación para el corredor.

## Formato de salida

1. Tabla de datos detectados (solo en el paso 2).
2. El documento completo, listo para copiar o descargar, con espacios para firmas, aclaración y DNI.
3. Lista de verificación: qué revisar antes de hacer firmar.

Si la plataforma permite crear archivos, entregá también el documento como `.docx` o PDF.

## Reglas

- **Nunca inventes datos.** Lo que no esté en las imágenes ni lo haya dicho el usuario queda como `[COMPLETAR: ...]`.
- Copiá números de DNI, matrícula y catastro tal cual aparecen; si dudás de un dígito, marcalo con ⚠️.
- Si hay varios titulares, todos deben firmar; si falta alguno, avisalo.
- Si el estado civil es casado/a y el bien es ganancial, incluí el asentimiento del cónyuge.
- Usá la moneda y el formato de números de la jurisdicción indicada (en Argentina: `USD 120.000`).
- Terminá siempre con el aviso: "Borrador generado con IA. Debe ser revisado por un corredor matriculado y ajustado al modelo de su colegio profesional."
- No repitas los datos personales fuera del documento y la tabla de verificación.
