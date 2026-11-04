# alcances/

Una subcarpeta por proyecto: `alcances/<cliente-slug>/` (minúsculas, sin espacios ni tildes; varios proyectos → `<cliente>-<proyecto>`).

```
<cliente-slug>/
├── fuentes/   # insumos del usuario (propuestas, actas, cotizaciones, notas, correos). No se editan.
├── trabajo/   # 01-inventario-fuentes · 02-matriz-informacion · 03-pendientes · 04-registro-decisiones · 05-control-calidad
└── entrega/   # Alcance Funcional - <Cliente> - v<N.M> - <YYYY-MM-DD>.docx (editable); no se sobrescriben versiones
```

Los archivos de `trabajo/` se crean a partir de `../plantillas/`. Ver `../CLAUDE.md` para el flujo completo.

> Contienen datos del cliente (NIT, cifras comerciales). Confirmar con el usuario antes de subir este repo a un remoto.
