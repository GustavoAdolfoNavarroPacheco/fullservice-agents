# scripts/

Herramientas mecánicas del agente. No redactan cláusulas ni deciden contenido legal — eso sigue siendo trabajo del agente en conversación con el usuario, siguiendo `CLAUDE.md`. Lo que automatizan es la parte que antes se rehacía a mano en cada contrato (montar sobre la plantilla corporativa, líneas de firma reales, verificación previa a entrega).

## build_contract.py

```
python scripts/build_contract.py build --data contratos/<cliente>/datos.json --out "contratos/<cliente>/Contrato - <Cliente> - <YYYY-MM-DD>.docx"
python scripts/build_contract.py check --file "contratos/<cliente>/Contrato - <Cliente> - <YYYY-MM-DD>.docx"
```

`build` ensambla el `.docx` sobre `recursos/Contrato - Plantilla Base.docx` (nunca sobre un documento en blanco) y, al terminar, corre automáticamente los mismos gates que `check`:

1. **Gate de placeholders** — falla si queda cualquier `[PENDIENTE ...]` sin resolver en el cuerpo, tablas, encabezado o pie de página.
2. **Gate de diseño corporativo** — falla si el `.docx` perdió la referencia a la imagen de membrete en el header, o si el bloque de firmas no tiene un párrafo con borde inferior (línea física).

Si el script termina con código de salida distinto de 0, el contrato **no** debe moverse a `contratos/<cliente>/` como versión de entrega — hay que resolver lo reportado y volver a generar.

`--skip-check` desactiva la verificación automática (solo para borradores intermedios que el usuario sabe que están incompletos).

### Esquema del JSON de datos

```jsonc
{
  "titulo": "CONTRATO DE PRESTACIÓN DE SERVICIOS ENTRE EMPRESA Y CLIENTE",
  "secciones": [
    {
      "encabezado": "OBJETO",      // nombre de la cláusula, en el orden que corresponda
      "nivel": 1,                   // 1 = Heading 1, 2 = Heading 2, etc.
      "parrafos": ["texto ya redactado, un string por párrafo"],
      "tabla": {                    // opcional — para cronogramas, formas de pago, etc.
        "encabezados": ["Fase", "Valor", "Fecha"],
        "filas": [["Fase 0", "$X", "dd/mm/aaaa"]]
      }
    }
  ],
  "firmantes": [
    {
      "rol": "EL CONTRATISTA",
      "nombre": "NOMBRE APELLIDO",
      "cargo": "Representante legal",
      "identificacion": "C.C. 000.000.000"   // opcional
    },
    {
      "rol": "EL CLIENTE",
      "nombre": "NOMBRE APELLIDO",
      "cargo": "Representante legal"
    }
  ]
}
```

El `datos.json` de cada contrato es un artefacto de trabajo — puede vivir en `contratos/<cliente>/datos.json` junto al `.docx` final, como registro de qué se generó (útil para reconstruir o revisar una versión posterior sin reabrir el `.docx`).

### Dependencias

Requiere `python-docx` (`pip install python-docx`). Ya está disponible en este entorno.
