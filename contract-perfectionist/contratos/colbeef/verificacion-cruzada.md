# Verificación cruzada — Contrato Colbeef (2026-07-09)

**Nota:** esta verificación se hizo de forma **retroactiva** (2026-07-30), no antes de la entrega. El contrato de Colbeef se generó el 2026-07-09 con scripts ad hoc anteriores a `scripts/build_contract.py` y a la plantilla actual de verificación cruzada (ver `CHANGELOG.md`), por lo que no quedó este artefacto en su momento. El `.docx` entregado **no se modifica** como resultado de esta verificación — es un registro de auditoría posterior, no un gate previo a entrega.

Fuentes usadas: `recursos/alcances/colbeef/Referencia - Contrato previo Colbeef (alcance y datos de partes).pdf` (contrato de referencia, usado solo como insumo de datos de partes y condiciones, no como plantilla de cláusulas — regla 3 de `CLAUDE.md`) y `recursos/cotizaciones/colbeef/Cotizacion - Colbeef SAS.xlsx` (hoja "🔴Colbeef agente IA").

| Dato | Valor en fuente (Alcances/Cotización) | Valor en el contrato entregado | ✓ / ✗ |
|---|---|---|---|
| Razón social del cliente | COLBEEF S.A.S. | COLBEEF S.A.S. | ✓ |
| NIT del cliente | 900.087.044-2 | 900.087.044-2 | ✓ |
| Representante legal del cliente | Diego Sigifredo Ardila Jiménez, C.C. 79.249.780, expedida en Bogotá D.C. | Diego Sigifredo Ardila Jiménez, C.C. 79.249.780, expedida en Bogotá D.C. | ✓ |
| Objeto / alcance funcional (módulos incluidos) | Automatización de faena: recepción de info. de proveedores, planillaje, cava, facturación inteligente, reportes/analítica IA (detalle remitido a "Anexo 1 – Propuesta Comercial", no transcrito en la referencia) | 11 módulos explícitos en Cláusula Tercera (Agente IA, Gestión de Casos, Tipificación, Asignación/Escalamiento, Departamentos, Clientes, Encuestas, Dashboard, Usuarios/Roles, Integraciones, Configuración General) | ✓ — el desglose de módulos del contrato coincide con la estructura de la cotización interna (XLSX), que usa exactamente los mismos 11 bloques |
| Exclusiones del alcance | No lista exclusiones nominales; delega a Anexo 1 | Parágrafo Primero, Cláusula Tercera: cualquier funcionalidad no prevista expresamente es "mejora evolutiva", cotizable aparte | ✓ — mismo tratamiento genérico |
| Valor total | $80.000.000 COP + IVA | $80.000.000 COP + IVA | ✓ |
| Forma de pago (hitos y %) | 40M / 20M / 20M — 15 / 15 / 10 días calendario tras factura | Idéntico: 40M / 20M / 20M — 15 / 15 / 10 días calendario tras factura | ✓ |
| Cronograma / fases y plazos | 5 meses calendario; fases remitidas a Anexo 1 (no enumeradas en el cuerpo) | 5 meses calendario + Fase 0/1/2/3 explícitas en Cláusula Cuarta | ✓ — el contrato final detalla lo que la referencia remitía al anexo |
| Condiciones de mantenimiento y soporte | Parágrafo Tercero, Cláusula Quinta: mantenimiento mensual **opcional** ($1.800.000/mes), a contratarse **aparte, mediante un nuevo contrato**, posterior a la entrega — no es alcance de este contrato | No se menciona ningún servicio de mantenimiento pospago, ni siquiera como opción futura | ✓ — coherente en sustancia (la propia referencia ya excluía el mantenimiento de este contrato), pero el contrato final no dejó ni la mención de la opción futura que sí tenía la referencia |
| Garantía (duración y alcance) | No fija una garantía por días; en su lugar exige 4 pólizas (cumplimiento 20%, buen manejo de anticipo 100%, calidad de servicio 20%, RC extracontractual 20%) — Cláusula Décima Tercera | Garantía de 90 días calendario tras entrega/aceptación, limitada a corrección de fallas imputables al desarrollo, con 6 exclusiones listadas — Cláusula Octava. **No se exigen pólizas.** | ✗ — diferencia sustantiva: el contrato entregado reemplazó el esquema de 4 pólizas de garantía de la referencia por una garantía de 90 días sin pólizas |

## Notas adicionales (fuera de las filas del checklist estándar, relevantes para esta revisión)

- **Cláusula penal**: la referencia fijaba 20% del valor del contrato; el contrato entregado fija 10%.
- **Cláusula de no competencia**: presente en la referencia (24 meses tras terminación, territorio Colombia); **ausente** en el contrato entregado.
- **Pólizas de garantía**: ver fila de Garantía arriba — ausentes en el contrato entregado.

Estas tres diferencias, junto con la de garantía, muestran que el contrato final es **más simple y con menos protecciones contractuales para Campuslands** que el documento de referencia (que en todo caso era un contrato distinto y anterior, usado solo como fuente de datos de partes, no como plantilla vinculante — regla 3 de `CLAUDE.md`). No se puede determinar desde los archivos disponibles si esta simplificación fue una decisión deliberada de negociación con el cliente o una omisión. Como el contrato ya está entregado y en `wiki/clientes/colbeef.md` se anota "Pendiente al cierre: fecha de firma y revisión legal externa", se recomienda confirmar con el usuario si esta reducción de cláusulas de protección (pólizas, no competencia, cláusula penal más baja) fue intencional antes de la firma definitiva.

## Integridad de datos entre archivos

| Verificación | Resultado |
|---|---|
| Los datos de partes (razón social, NIT, representante legal) del `.docx` coinciden con `wiki/clientes/colbeef.md` | ✓ |
| El `.docx` no fue modificado por esta verificación retroactiva | ✓ |
| `contratos/colbeef/datos.json` es una reconstrucción fiel del contenido del `.docx` para fines de registro (no fue el insumo real de generación — ver nota al inicio) | ✓ |

Verificación cruzada realizada retroactivamente el 2026-07-30, a solicitud del usuario, como parte de la auditoría general de los agentes del monorepo.
