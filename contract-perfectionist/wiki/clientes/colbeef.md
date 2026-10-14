# Ficha de cliente — Colbeef S.A.S.

Datos legales ya confirmados. Objetivo: no volver a preguntar estos datos en un contrato futuro para el mismo cliente (otrosí, renovación, nuevo proyecto), salvo que el usuario indique que cambiaron.

## Identificación legal

| Campo | Valor | Fuente |
|---|---|---|
| Razón social | COLBEEF S.A.S. | `recursos/alcances/colbeef/Referencia - Contrato previo Colbeef (alcance y datos de partes).pdf` |
| Domicilio | Bucaramanga, Santander | ídem |
| NIT | 900.087.044-2 | ídem |
| Representante legal | Diego Sigifredo Ardila Jiménez | ídem |
| Identificación del representante | C.C. 79.249.780, expedida en Bogotá D.C. | ídem |
| Rol contractual | CONTRATANTE | ídem |

Estos datos provienen de un contrato de referencia previo entre Colbeef y Campuslands (usado únicamente como insumo de datos de partes, no como plantilla de cláusulas — ver regla 3 de `CLAUDE.md`). Antes de reutilizarlos en un contrato nuevo, confirmar con el usuario que siguen vigentes (representante legal, domicilio).

## ⚠️ Alerta: el contrato realmente firmado NO es el borrador de 2026-07-09

El 2026-09-02 se recibió el PDF firmado (`Contrato Firmado.pdf`, ZapSign bb67660d-2a4d-4cf7-acdb-61f3525aa887, firmado 2026-01-14/15 en Floridablanca) para redactar el `Documento de Aceptación y Entrega de Desarrollo`. Su contenido **no coincide** con `Contrato - Colbeef - 2026-07-09.docx` ni con `datos.json` de esa fecha:

| Punto | Borrador 2026-07-09 (`datos.json`) | Contrato realmente firmado (`Contrato Firmado.pdf`) |
|---|---|---|
| Alcance funcional | Gestión de casos, agente de voz/WhatsApp, CRM de PQRS | Sistema de automatización de faena: recepción, planillaje, gestión de cava, facturación inteligente, IA |
| Garantía | 90 días, sin pólizas | 1 año de soporte correctivo + 4 pólizas (cumplimiento 20%, buen manejo de anticipo 100%, calidad 20%, RC extracontractual 20%) |
| Cláusula penal | 10% del valor del contrato | 20% del valor del contrato |
| No competencia | Ausente | Presente (Cláusula Séptima, 24 meses tras terminación) |
| Valor / forma de pago / plazo | $80.000.000 COP + IVA, 40/20/20, 5 meses | Igual ($80.000.000 COP + IVA, 40/20/20, 5 meses) |

Esto resuelve el pendiente que dejó `wiki/log.md` (2026-07-30): el borrador de julio se redactó con un alcance funcional equivocado (aparentemente de otro proyecto tipo CRM/PQRS) y sin las pólizas/cláusula penal/no-competencia de la referencia previa. El contrato que Colbeef y Campuslands firmaron realmente sí incluye esas protecciones y el alcance de automatización de faena. **A partir de ahora, `Contrato Firmado.pdf` es la fuente de verdad para este cliente** — el `.docx` y `datos.json` de 2026-07-09 quedan como borrador histórico obsoleto, no como el contrato vigente.

## Identificación legal (confirmada en el contrato firmado)

| Campo | Valor |
|---|---|
| Razón social | COLBEEF S.A.S. |
| Domicilio | Bucaramanga, Santander |
| NIT | 900.087.044-2 |
| Representante legal | Diego Sigifredo Ardila Jiménez |
| Identificación del representante | C.C. 79.249.780, expedida en Bogotá D.C. |
| Rol contractual | CONTRATANTE |

Campuslands (CONTRATISTA): NIT 901.628.406-1, domicilio Floridablanca, Santander, representada por Yesenia Merchán Pinzón, C.C. 1.065.866.676 expedida en Aguachica, Cesar.

## Condiciones particulares acordadas (contrato firmado)

- Objeto: sistema integral de automatización operativa de faena (recepción multicanal, OCR, planillaje, gestión de cava, facturación inteligente, reportes y analítica con IA), en 6 fases, incluyendo Fase 0 de levantamiento.
- Valor: $80.000.000 COP + IVA. Forma de pago 40/20/20 (inicio / mitad de proyecto / entrega final mediante acta de aceptación).
- Plazo: 5 meses calendario desde la firma (14 de enero de 2026).
- Propiedad intelectual: cesión total, exclusiva e irrevocable del código fuente y derechos patrimoniales a favor de Colbeef (Cláusula Sexta).
- Soporte: 1 año de soporte técnico correctivo desde el acta de entrega y aceptación (gratuito); mantenimiento evolutivo mensual opcional de $1.800.000 COP mediante contrato aparte.
- Garantías: pólizas de cumplimiento (20%), buen manejo de anticipo (100%), calidad (20% + 1 año) y RC extracontractual (20%).
- Cláusula penal: 20% del valor del contrato. No competencia: 24 meses tras terminación, limitada al sector cárnico bovino en Colombia.

## Historial de documentos

Ver `wiki/index.md` para el listado completo con enlaces. Resumen:

- **2026-01-14** — Contrato de prestación de servicios firmado entre Colbeef y Campuslands (ver tabla de alerta arriba). Firmado vía ZapSign por ambos representantes legales.
- **2026-09-02** — Documento de Aceptación y Entrega de Desarrollo, certificando la entrega y aceptación de las 6 fases del sistema conforme al documento "Alcances y Requerimientos Técnicos" del proyecto. Habilita el tercer pago ($20.000.000 COP + IVA) y da inicio al año de soporte técnico correctivo.
- **2026-07-09** — Borrador de contrato con alcance funcional equivocado (ver alerta arriba). No es el contrato vigente; se conserva solo como registro histórico.
