# Ejemplo (datos ficticios)

## Pedido del usuario

> Te paso el DNI de la dueña y la escritura. Es un depto en Córdoba Capital, lo quiere vender en 95 mil dólares, exclusiva por 90 días, honorarios 3% a cargo del vendedor. Armame la autorización.

*(Adjunta dos fotos: DNI y primera hoja de la escritura.)*

## Respuesta esperada (paso 2)

| Dato | Valor detectado | Fuente |
|---|---|---|
| Propietaria | María Laura Ejemplo | DNI |
| DNI | 30.000.000 | DNI |
| Estado civil | ⚠️ No figura | — |
| Inmueble | Av. Siempre Viva 123, 4° B, Córdoba | Escritura |
| Matrícula registral | 000000/00 | Escritura |
| Nomenclatura catastral | ⚠️ Ilegible en la foto | Escritura |
| Titularidad | 100 % | Escritura |

Para completar la autorización necesito:

1. Estado civil de la propietaria (y, si es casada, los datos del cónyuge).
2. Una foto más nítida de la nomenclatura catastral, o el número.
3. Tus datos como corredor: nombre, matrícula y domicilio.

## Respuesta esperada (paso 4)

El documento completo según `references/estructura-autorizacion.md`, con `[COMPLETAR: ...]` en lo que siga faltando, la lista de verificación y el aviso final.
