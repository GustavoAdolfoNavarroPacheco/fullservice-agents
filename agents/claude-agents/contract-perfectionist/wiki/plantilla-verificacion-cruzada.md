# Plantilla — Verificación cruzada previa a entrega

Copiar esta tabla a `contratos/<cliente>/verificacion-cruzada.md` al terminar el borrador de cada contrato (paso 4 del flujo en `CLAUDE.md`, "cero discrepancias"). Llenarla dato por dato contrastando el borrador contra las fuentes — no de memoria.

| Dato | Valor en fuente (Alcances/Cotización) | Valor en el borrador del contrato | ✓ / ✗ |
|---|---|---|---|
| Razón social del cliente | | | |
| NIT del cliente | | | |
| Representante legal del cliente | | | |
| Objeto / alcance funcional (módulos incluidos) | | | |
| Exclusiones del alcance | | | |
| Valor total | | | |
| Forma de pago (hitos y %) | | | |
| Cronograma / fases y plazos | | | |
| Condiciones de mantenimiento y soporte | | | |
| Garantía (duración y alcance) | | | |

Cualquier fila con ✗ debe resolverse (corrigiendo el borrador o preguntando al usuario) antes de correr `scripts/build_contract.py check` y mover el contrato a `contratos/<cliente>/` como entrega.

Después de completarla, agregar una línea en `wiki/log.md` confirmando que la verificación cruzada se hizo, no solo qué fuentes se usaron.
