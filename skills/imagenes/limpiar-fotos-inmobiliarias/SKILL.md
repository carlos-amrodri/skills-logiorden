---
name: limpiar-fotos-inmobiliarias
description: Editar fotografías inmobiliarias de una carpeta para despejar ambientes, retirar muebles y renovar cortinas existentes, además de hacer cambios visuales pedidos por el usuario. Usar cuando el usuario pida limpiar o preparar para un aviso varias fotos de una propiedad; no para publicar avisos.
---

# Limpiar Fotos Inmobiliarias

Trabaja con las imágenes de la carpeta que indique el usuario. Si no hay una ruta explícita, identifica la carpeta por el contexto o pídesela. Enumera los archivos de imagen de esa carpeta, excluye originales ya editados (`*-editada.*`) y confirma visualmente qué fotos corresponden al ambiente solicitado. No supongas que todas las imágenes de un proyecto pertenecen al mismo ambiente.

Usa la skill `imagegen` y su herramienta de edición para cada foto. Inspecciona primero cada imagen. Formula instrucciones particulares para cada toma, basadas en lo que realmente aparece en ella, y mantén coherencia de materiales, colores y cambios entre vistas del mismo ambiente.

## Criterios de edición

- Conserva encuadre, perspectiva, iluminación creíble, dimensiones, aberturas, revestimientos, pisos, carpintería e instalaciones fijas. Mejora exposición y nitidez con moderación.
- Quita los objetos que pida el usuario y despeja superficies y piso de pertenencias, basura y objetos sueltos.
- Retira todos los muebles visibles por defecto, incluidos los muebles de guardado y los empotrados. Conserva o reemplaza únicamente aquellos que el usuario señale. Mantén electrodomésticos e instalaciones fijas, salvo indicación contraria.
- Si hay cortinas, reemplázalas por cortinas nuevas, lisas y limpias, de tonos suaves que armonicen con las paredes, la madera y la luz de esa habitación. Mantén su ubicación y no agregues cortinas donde no las había.
- Cambia colores y artefactos solo cuando el usuario lo pida. No introduzcas elementos que no aparecían en esa toma para cumplir una instrucción aplicable a otra vista.
- Reconstruye las zonas ocultas por objetos retirados con pared, zócalo y piso acordes a las superficies contiguas.
- Conserva intacto cualquier logo o marca de agua del aviso, incluida su posición y texto. Revisa legibilidad al final.

Revisa cada resultado antes de entregarlo: objetos solicitados retirados, continuidad de azulejos/pisos, correspondencia entre tomas, ausencia de artefactos inventados y logo legible. Corrige los errores visibles con una nueva edición focalizada.

Guarda una copia por foto en la misma carpeta de origen con el nombre original más `-editada.png`, sin sobrescribir originales ni ediciones existentes. Si ya existe ese nombre, crea una versión numerada. Si no puedes escribir en la carpeta, conserva las versiones en un espacio accesible y explica dónde quedaron. Al entregar, indica qué fotos se editaron y que son imágenes modificadas digitalmente; si se agregaron artefactos o se cambiaron terminaciones, evita presentarlos como el estado actual del inmueble.
