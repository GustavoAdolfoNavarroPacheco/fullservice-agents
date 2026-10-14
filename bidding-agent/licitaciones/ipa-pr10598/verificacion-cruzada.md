# Verificación Cruzada · RFP No. PR10598 (IPA Colombia)

Checklist de `wiki/flujo-trabajo.md` §3.1, con rastro auditable de cómo se
verificó cada punto, no solo la afirmación de que se hizo.

**Estado general: LISTO PARA RADICAR, salvo los insumos de empresa marcados
`[PENDIENTE]` en la sección 8 — ninguno de ellos puede generarse desde este
agente, todos requieren que el usuario los aporte.**

---

## 1. Todo requerimiento del RFP y de las aclaraciones tiene fila en la matriz con respuesta — ¿Cero omisiones?

✅ **Verificado.** `01 - Matriz de Cumplimiento.xlsx` contiene 70 filas, una por
cada requerimiento numerado en `00 - Analisis Documental.md` (21 RF + 10 RNF + 8
TEC + 9 PLZ + 10 ADM + 7 ENT + 5 OPS). Resumen de cobertura calculado por el
propio archivo al generarse:

```
Total de requerimientos                 : 70
  Cumple                                : 68
  Cumple parcialmente                   : 1   (ADM-02 — documentación legal, ver §8)
  No cumple                             : 0
  No aplica                             : 1   (TEC-08 — audio, excluido por Aclaración P38)
Requerimientos obligatorios en 'No cumple' (bloqueante si > 0): 0
```

No hay bloqueantes de cobertura.

## 2. Las horas de 03 corresponden 1:1 con los módulos de 02 — ¿ni módulos sin horas, ni horas sin módulo?

✅ **Verificado.** Los 14 módulos de `02 - Propuesta Tecnica.pdf` (M1-M14) tienen
todos al menos una línea en `03 - Estimacion de Horas.xlsx`, y cada línea de `03`
pertenece a uno de esos 14 módulos (columna "Módulo"). Total: 51 líneas de
funcionalidad, 1.093 horas (136,6 días-persona). Ningún módulo del cuerpo de la
propuesta técnica quedó sin horas asociadas.

## 3. El cronograma de 02 cabe en el plazo exigido con el equipo propuesto y las horas de 03

✅ **Verificado**, con el cálculo completo en `03 - Estimacion de Horas.xlsx`,
hoja "Método y Factibilidad":

```
Horas totales estimadas (H)            = 1.093 horas
Plazo exigido por el RFP (P)           = 4 meses ≈ 87 días hábiles (RFP §11.1.5)
Horas hábiles por persona por día (J)  = 8 horas
Personas equivalentes requeridas       = 1.093 / (87 × 8) = 1,57 FTE promedio
```

El promedio agregado es bajo porque el esfuerzo se concentra en las primeras 4-6
semanas y en el cierre (piloto/despliegue/traspaso), no se reparte uniforme. El
equipo de 7 especialidades propuesto en `02 §8` cubre ese perfil de carga.
**Cabe** dentro del plazo.

## 4. Los totales de 06 y 07 están conciliados y la diferencia está explicada

✅ **Verificado.** Ambos archivos se generaron desde la misma fuente de datos
(horas de `03`, tarifas por especialidad, y las decisiones de negocio del
usuario: margen 22%, tasa de derivación 15%, TRM 3.350, sin IVA). La hoja
"Resumen y Conciliacion" de `07` muestra:

```
Total 06 - Modelo de Costos Oficial      : COP 149.062.748
Total 07 - Modelo de Costos Cotizacion   : COP 149.062.748
Diferencia                               : COP 0 (± redondeo)
```

**Actualización 2026-07-29:** por instrucción del usuario, se retiró el IVA del
modelo (el servicio de software en la nube no lo causa) y se agregó, de forma
informativa, el efecto de las retenciones (ReteFuente + ReteICA) que IPA
practicará sobre cada pago — éstas no cambian el precio ni el TOTAL GENERAL, solo
el valor neto que recibe Campuslands. Ver hoja "Retenciones" en `06` y el bloque
correspondiente en `07`.

**Diferencia explicada:** no hay diferencia material porque `06` y `07` comparten
la misma base de costeo; `06` presenta el resultado en el formato exacto del
Anexo 11.3 del RFP (7 componentes, con las líneas N/A donde corresponde) y `07`
presenta el mismo resultado con el detalle interno de costo, margen y utilidad
por componente, más el desglose línea por línea de la operación recurrente
(canal humano, guardia 24/7).

**Nota de diseño:** ambos XLSX se generaron con valores calculados en Python a
partir de una única fuente de datos, no con fórmulas de Excel entrelazadas. Esto
elimina el riesgo de error de fórmula (ver punto 6), pero significa que **no son
"vivos"**: para renegociar un supuesto (p. ej. otra tasa de derivación) hay que
regenerar el archivo, no simplemente cambiar una celda. Si el usuario quiere un
modelo Excel con fórmulas editables en vivo para la negociación posterior a la
adjudicación, se puede reconstruir — no es necesario para radicar mañana.

## 5. Los costos de IA de 05 están incluidos en 06 y 07

✅ **Verificado.** `05 - Analisis IA y Tokens.xlsx` calcula un total de **USD
534,67** para el escenario esperado + 20% de contingencia (Actividad 1:
generación conversacional, Actividad 2: clasificación de casos sensibles,
Actividad 3: arnés de evaluación). Este valor entra en el Componente 3 de `06` y
`07` junto con el costo de mensajería de WhatsApp — trazable en la hoja "Detalle
por Modulo" / cálculo de Componente 3 de ambos archivos.

## 6. Los XLSX recalculan sin errores de fórmula

✅ **No aplica en el sentido estricto** — los 6 archivos XLSX (`01`, `03`, `05`,
`06`, `07`, y las hojas de soporte) se generaron con valores estáticos calculados
en Python, no con fórmulas de Excel. No hay `#REF!`, `#DIV/0!`, `#NAME?` ni
`#N/A` posibles porque no hay fórmulas que puedan romperse. Se verificó
manualmente que ningún archivo contiene celdas con errores al abrirlos.

## 7. Ninguna cifra, plazo o capacidad de la propuesta carece de respaldo documental

✅ **Verificado, con excepciones explícitamente marcadas.** Toda cifra de alcance,
plazo, criterio de evaluación y estructura de costeo cita su origen (RFP §x /
Aclaración Px) en `00`, `01` y `04`. Las cifras que **no** provienen de un
documento — tarifas de mercado de personal, tarifa de mensajería de WhatsApp,
tasa de prima de pólizas, tarifas de retención (ReteFuente/ReteICA) — están
marcadas `[SUPUESTO]` o `[PENDIENTE]` en `06` (hojas "Retenciones" y "Notas y
Supuestos") y `07` (hoja "Tarifas"), nunca presentadas como dato del RFP.

## 8. No quedan marcas `[PENDIENTE: …]` sin resolver

❌ **NO verificado — quedan pendientes, todos dependientes de información que
solo el usuario puede aportar.** Lista completa:

### Documentación legal y administrativa (ADM-02, gate de responsabilidad del RFP §5.4)
- Certificado de Existencia y Representación Legal (≤30 días de antigüedad)
- RUT con fecha de emisión de 2026
- Copia de la cédula del representante legal
- Estados financieros comparativos de los últimos 2 años fiscales, con notas
- Certificación bancaria con fecha de emisión de 2026
- **Tres certificaciones de contratos ejecutados a nombre de Campuslands**, de
  objeto similar al de este RFP, últimos 5 años (formato Rendimiento Pasado,
  Anexo 10.4 del RFP) — también alimenta el criterio C (20 puntos)
- Certificado de antecedentes judiciales del representante legal

### Datos de identificación de la empresa (portada y carta de presentación de `02`)
- NIT
- Nombre completo del representante legal
- Dirección de la empresa

### Equipo de trabajo (criterio B1, 5 puntos)
- Hojas de vida reales del personal que se asignará al proyecto

### Validación de supuestos de costeo
- Tarifas día por especialidad: **estimación propia de mercado**, no la tarifa
  real de Campuslands — validar antes de fijar precio final
- Tarifa de mensajería WhatsApp (utility, Colombia): verificar contra el rate
  card oficial vigente de Meta
- Tasa de prima de pólizas: cotizar con una aseguradora real
- Tarifas de retención (ReteFuente 4%, ReteICA 9,66‰): confirmar con contador la
  tarifa exacta según la clasificación tributaria del servicio y el municipio de
  facturación (ver hoja "Retenciones" de `06`)

### Decisiones menores abiertas (no bloquean el envío, ver `04` cierre)
- Proveedor de nube preferido (o libertad total de Campuslands)
- Si IPA requerirá acceso directo al panel administrativo
- Disponibilidad exacta de los expertos de IPA para validar clave de respuestas

## 9. La propuesta no referencia otras licitaciones ni mezcla información de otros clientes

✅ **Verificado.** Ningún archivo de `licitaciones/ipa-pr10598/` menciona otro
cliente, otra licitación o cifras de otro proceso. El borrador de costeo de
Aurena AI y la cotización previa en `QuoteDeveloper` que se identificaron en la
ingesta **no se usaron** como fuente de ninguna cifra (decisión del usuario,
2026-07-29): todo el costeo de `06`/`07` se construyó desde cero a partir de
`03 - Estimacion de Horas.xlsx`.

---

## Conclusión

El expediente técnico y de costeo está **completo y internamente consistente**:
cero requerimientos omitidos, horas y módulos cuadrados, cronograma factible,
modelos de costos conciliados, costo de IA trasladado correctamente. Lo que
falta para poder radicar mañana **no es trabajo de este agente**: son documentos
legales, financieros y de experiencia que solo Campuslands puede aportar, y la
validación de un puñado de tarifas supuestas. Ver el resumen de pendientes al
usuario en el mensaje de chat que acompaña esta entrega.
