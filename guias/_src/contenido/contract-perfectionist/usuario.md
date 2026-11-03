---
titulo: Contract Perfectionist: cómo obtener el contrato de un proyecto
resumen: Qué documentos entregarle, qué datos revisar, qué recibes y cómo revisar el contrato antes de firmarlo.
---

## En resumen

**Contract Perfectionist** redacta el contrato de un proyecto a partir de tres cosas: los **alcances** (qué se va a construir), la **cotización** (cuánto cuesta, cómo se paga y cuándo se entrega) y el **contrato madre** (el esquema de cláusulas estándar de la empresa). El resultado es un documento de Word con el membrete de Campuslands y líneas para firmar.

Su objetivo es que **ambas partes, al terminar de leer, sepan exactamente** qué se entrega, cuándo, por cuánto, bajo qué condiciones y qué pasa si algo falla.

```stats
3 | cosas que necesita: alcances, cotización y los datos de las partes
0 | datos inventados: lo que falta queda marcado y te lo pregunta
1 | documento Word con membrete y líneas de firma
```

> [!tip] Si solo tienes un minuto
> Deja los alcances y la cotización del cliente en sus carpetas y pídele el contrato. Todo lo que no encuentre en ellos, te lo preguntará.

## Para qué sirve

Úsalo cuando un proyecto ya tiene **alcance definido y cotización aprobada** y llegó el momento de formalizar el acuerdo. También sirve cuando el contrato ya está firmado y hace falta una modificación: en ese caso se prepara un **otrosí**, sin tocar el contrato original.

### Qué no es

No reemplaza la revisión legal. El agente verifica que el contrato sea fiel a tus documentos y que cumpla las reglas de formato de la empresa, pero la **validación jurídica** sigue siendo tuya.

## Antes de empezar

Reúne en las carpetas del cliente:

- **Los alcances del proyecto:** el documento que describe qué se va a construir, los módulos, las integraciones y lo que queda excluido.
- **La cotización aprobada:** con el valor, la forma de pago, el cronograma y las condiciones de mantenimiento.
- **Los datos del cliente:** razón social, NIT y representante legal. Si ya hubo un contrato anterior con el mismo cliente, el agente reutiliza esos datos.

> [!importante] Sin alcances y cotización, no hay contrato
> El agente nunca redacta un contrato sin al menos un documento de alcance y uno de cotización de ese cliente. El contrato madre ya lo tiene incorporado.

### Dónde dejar los archivos

```tree
recursos/
  alcances/
    <nombre-del-cliente>/       # documentos de alcance
  cotizaciones/
    <nombre-del-cliente>/       # cotización aprobada
```

## Paso a paso

```lanes
Tú | Deja los alcances y la cotización en las carpetas del cliente
Tú | Pídele el contrato
Agente | Revisa los documentos y te pregunta lo que falte
Tú | Responde y confirma los datos de las partes
Agente | Redacta el contrato, lo compara con las fuentes y lo verifica
Tú | Revisa el documento y lo envía a revisión legal
```

### 1. Deja los documentos

Copia los alcances y la cotización a las carpetas del cliente.

### 2. Pide el contrato

Dile el nombre del cliente. Si ya existe un contrato anterior con ese cliente, el agente lo tiene en cuenta para no repetirte preguntas.

### 3. Responde lo que falte

El agente arma una lista con los datos necesarios: razón social, NIT, representante legal, objeto, alcance, cronograma, valor, forma de pago, mantenimiento y garantías. Si falta algo, o si un documento se puede leer de dos maneras, **se detiene y te pregunta** antes de escribir esa parte.

### 4. Revisa el borrador

Recibes el contrato en Word y un archivo de verificación que muestra, dato por dato, que lo escrito coincide con tus documentos.

### 5. Revisión legal y firma

El agente deja el contrato listo para firma, pero antes debe pasar tu validación legal. El estado del contrato (borrador, pendiente de revisión legal, pendiente de firma o firmado) queda registrado en el índice.

## Ejemplos de conversación

### Empezar

```chat
Tú: Redacta el contrato de Colbeef con los alcances y la cotización que dejé en recursos.
Agente: Revisé los documentos. Para redactar con precisión necesito confirmar dos datos: el representante legal que firmará por el cliente y la forma de entrega de la última fase. El resto lo tomo de la cotización y los alcances.
```

### Completar un dato

```chat
Tú: El NIT del cliente es 900.000.000-0 y firma su gerente general.
Agente: Gracias. Reemplacé el dato pendiente del NIT y registré al gerente general como firmante por el cliente.
```

### Ajustar una condición

```chat
Tú: Para este proyecto el soporte dura 6 meses, no 12. Actualiza el contrato.
Agente: Actualicé la cláusula de mantenimiento y soporte, y la de vigencia, que dependía de ese plazo. Volví a verificar el contrato contra la cotización.
```

### Un cambio tras la firma

```chat
Tú: El cliente pidió un módulo nuevo. Prepara el otrosí.
Agente: Preparo el Otrosí 1 con el alcance y el valor adicionales. El contrato original firmado no se modifica.
```

## Qué recibes

```cards
El contrato en Word | Con el membrete de Campuslands, todas las cláusulas y líneas de firma sobre el nombre de cada representante.
La verificación cruzada | Una tabla que compara cada dato (valor, plazos, alcance…) entre tus documentos y el contrato.
La ficha del cliente | Los datos legales y condiciones confirmadas, que se reutilizan en próximos contratos.
```

### Cómo está organizado el contrato

El contrato sigue siempre el mismo orden, que viene del contrato madre:

1. **Partes y consideraciones:** quiénes firman y por qué.
2. **Objeto:** qué se compromete a entregar el contratista.
3. **Naturaleza jurídica:** el tipo de obligación asumida.
4. **Alcance, cronograma, valor y forma de pago:** lo que sale de tus documentos.
5. **Mantenimiento, soporte y garantías:** qué ocurre después de la entrega.
6. **Obligaciones de cada parte y aceptación de entregables.**
7. **Propiedad intelectual, datos personales, reserva de información y servicios de terceros.**
8. **Suspensión, terminación, fuerza mayor y cláusula penal.**
9. **Vigencia, ley aplicable y firmas.**

> [!nota] Qué sale de tus documentos y qué es estándar
> Las cláusulas sobre alcance, cronograma, valor y pago se escriben con **tus** documentos. Las de protección (propiedad intelectual, reserva de información, terceros, fuerza mayor, terminación, cláusula penal y ley aplicable) vienen del contrato madre y se mantienen igual salvo que tú indiques lo contrario para ese proyecto.

## Los datos pendientes

Cuando el agente no encuentra un dato en tus documentos, **no lo inventa**: deja una marca como esta en el texto.

> [!cuidado] Cómo se ve un dato pendiente
> `[PENDIENTE: NIT del cliente]`

El agente te lo avisa y te lo pregunta. **Un contrato con marcas pendientes no puede entregarse como final**: el control automático lo detecta y lo bloquea.

## Cómo revisar el contrato

- **Las partes:** razón social, NIT y representante legal de ambas empresas, bien escritos.
- **El objeto:** que describa el proyecto que acordaron, no otro.
- **Los valores y los pagos:** que coincidan al peso con la cotización, incluidos los hitos y los porcentajes.
- **El cronograma:** fases y plazos iguales a la cotización.
- **El soporte y la garantía:** duración y alcance correctos.
- **Las exclusiones:** que lo que no está incluido quede dicho con claridad.
- **Ninguna marca pendiente:** busca la palabra «PENDIENTE» en el documento.
- **Las firmas:** una línea sobre el nombre de cada representante, con espacio para firmar.
- **La verificación cruzada:** que no tenga filas marcadas con ✗.

> [!importante] Mira el alcance con especial atención
> Un contrato con un alcance equivocado es un riesgo serio. En una ocasión, un borrador salió con un alcance que no correspondía al proyecto real; se detectó y quedó marcado como no vigente. Compara siempre los módulos del contrato con los de tus alcances.

## Estados de un contrato

| Estado | Qué significa |
|---|---|
| Borrador | Todavía en redacción o sin pasar los controles |
| Pendiente revisión legal | Pasó los controles automáticos; falta la revisión legal externa |
| Pendiente firma | Revisado; falta solo la fecha y la firma de las partes |
| Firmado | Contrato ejecutado; es la versión final |

## Cambios y modificaciones

| Situación | Qué hace el agente |
|---|---|
| Quieres cambiar algo en un contrato sin firmar | Genera una nueva versión (`v2`, `v3`…) y conserva la anterior hasta que la nueva sea definitiva |
| El contrato ya está firmado y hay cambios | Prepara un **otrosí** numerado (`Otrosi 1`, `Otrosi 2`…); nunca modifica el original firmado |
| Quieres cambiar una cláusula estándar solo para este proyecto | Lo hace si tú lo indicas, y puede dejarlo registrado como ajuste reutilizable si lo validas |

## Lo que el agente no hace

| Si le pides… | Qué pasa | Qué hacer |
|---|---|---|
| Que complete un dato «con lo más probable» | No lo hace: lo marca como pendiente y pregunta | Aporta el dato o el documento donde aparece |
| Que copie el contrato de otro cliente | No lo hace: cada proyecto es reservado | Aporta los alcances y la cotización del cliente actual |
| Que omita una cláusula de protección | Solo si tú lo indicas para ese proyecto | Dilo expresamente; quedará registrado |
| Que entregue el contrato aunque tenga marcas pendientes | No lo hace: el control lo bloquea | Resuelve primero los datos faltantes |
| Que reemplace la validación legal | No lo hace | Envía el contrato a revisión jurídica |
| Que modifique un contrato ya firmado | No lo hace | Pide un otrosí |

## Preguntas frecuentes

**¿Qué significa «[PENDIENTE: …]»?**
Que ese dato no estaba en tus documentos. El agente te lo pedirá y lo reemplazará.

**¿Puedo editar el Word directamente?**
Es mejor pedirle el cambio al agente: así se conserva el membrete, pasa los controles y la verificación se actualiza. Si editas a mano, avísale para que lo revise.

**¿El agente conoce los datos de Campuslands?**
Sí: están registrados en la wiki. Aun así, **antes de usarlos** te confirmará que el representante legal y el domicilio siguen vigentes.

**¿Qué pasa si el cliente ya tuvo un contrato conmigo?**
El agente consulta la ficha de ese cliente y reutiliza los datos legales confirmados, para no repetirte preguntas.

**¿Qué otros documentos puede preparar?**
Además de contratos, se han preparado con este agente documentos como acuerdos de aceptación de inicio de desarrollo y documentos de aceptación y entrega. Pídelo con claridad y dale los insumos.

**¿Dónde queda el contrato?**
En la carpeta del cliente dentro de `contratos`, con el nombre `Contrato - <Cliente> - <fecha>.docx`.

## Glosario

| Término | Qué significa |
|---|---|
| Contrato madre | La plantilla de cláusulas estándar de la empresa |
| Contratista | Quien presta el servicio (Campuslands) |
| Objeto | Lo que se compromete a entregar el contratista |
| Cláusula penal | La consecuencia económica de un incumplimiento grave |
| Otrosí | Una modificación formal a un contrato ya firmado |
| NIT | Número de identificación tributaria de una empresa |
| Verificación cruzada | La comparación dato por dato entre el contrato y tus documentos |
| Gate | El control automático que bloquea un contrato incompleto |

## Si algo no funciona

Si el agente no encuentra tus documentos, revisa que estén en las carpetas del cliente. Si el control automático rechaza el contrato, el agente te explicará qué falta (casi siempre un dato pendiente). Si algo se repite o parece una falla, avisa a quien mantiene el agente; su guía técnica explica los controles y el montaje.
