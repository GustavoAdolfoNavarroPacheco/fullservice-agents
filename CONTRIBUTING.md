# Guía de contribución

Gracias por querer mejorar **fullservice-agents**. Este repositorio es el conjunto de agentes de IA del flujo comercial de Campuslands y la web de guías que los documenta.
Antes de empezar, lee el [`README`](README.md), la [licencia](LICENSE) (el repositorio es público pero **no es de código abierto**) y el [código de conducta](CODE_OF_CONDUCT.md).

> Si lo que encontraste es un problema de **seguridad**, no abras un issue: sigue la [política de seguridad](SECURITY.md).

## Qué tipo de aportes caben

- Correcciones de errores en un agente, en sus scripts o en la web de guías.
- Mejoras de las instrucciones de un agente (`CLAUDE.md` / `Perplexity.md`) y de su `wiki/`.
- Mejoras de las guías de usuario y de desarrollador (`guides/_src/contenido/`).
- Erratas, enlaces rotos y aclaraciones en la documentación.

Si vas a hacer un cambio grande (un agente nuevo, un rediseño), **abre antes un issue** para acordar el enfoque.

## Reglas de oro

1. **Todo en español**: instrucciones de los agentes, guías, commits y PR.
2. **Nada de secretos ni datos de clientes.** Nunca subas credenciales, `.env`, documentos de identidad, firmas, contratos firmados ni información financiera de clientes. Ante la duda, no lo subas.
3. **Veracidad.** Los agentes no inventan datos; lo que falta se marca `[PENDIENTE]`. Mantén ese principio al editar sus instrucciones.
4. **No se edita a mano lo generado.** Ver «Archivos generados».
5. **Presentaciones.** `agents/claude-agents/presentations-designer/presentaciones/` es un **repositorio aparte y privado**; sus cambios se confirman dentro de esa carpeta, no aquí.

## Flujo de trabajo

1. Crea una rama desde `main` con un prefijo según el tipo de cambio: `feat/…`, `fix/…`, `docs/…`, `style/…`, `refactor/…` o `chore/…`.
2. Haz commits pequeños con el formato `tipo(ámbito): resumen en presente`, por ejemplo `feat(guides): carrusel solo con el diseño vigente` o `fix(agents): corrige el orden de los recibos`.
   Ámbitos habituales: `guides`, `agents`, `resources`, `repo`.
3. Verifica (ver abajo), abre un *pull request* hacia `main` con la plantilla y espera la revisión de quien mantiene el repositorio (`CODEOWNERS`).
4. Se integra con un *merge commit*; la rama se borra al terminar.

## Cómo verificar tus cambios

### Web de guías (`guides/`)

```bash
python -X utf8 guides/_src/servir.py        # servidor local con recarga en vivo (puerto 4173)
python -X utf8 guides/_src/build.py --sin-pdf   # regenera el HTML (sin tocar los PDF)
python -X utf8 guides/_src/build.py             # regenera también los PDF (requiere Chrome y Playwright)
python -X utf8 guides/_src/probar_web.py        # batería de pruebas en un navegador real (con el servidor en marcha)
```

Cómo se escribe cada guía, qué componentes hay y cómo se mantiene la escala tipográfica y el estándar de contenedores: [`guides/README.md`](guides/README.md).
El CI vuelve a generar la web y **falla si lo generado no coincide con lo que subiste**.

### Comandos «!» de los agentes

La fuente única es `resources/comandos/comandos.py`. Si cambias un comando, corre `python -X utf8 resources/comandos/comandos.py` (y `--verificar` para comprobar que nada quedó desfasado).

### Un agente

Cada agente lleva una `wiki/` con su bitácora (`log.md`) y su índice (`index.md`). Cuando cambies su comportamiento, anota la decisión en la bitácora con el formato `## [AAAA-MM-DD] tipo | Título`.

## Archivos generados

| No se edita a mano | Se cambia en | Y se regenera con |
|---|---|---|
| `guides/**/*.html`, `guides/**/*.pdf`, `guides/assets/estilo.css`, `guides/assets/*.js` | `guides/_src/` (contenido en `contenido/*.md`, estilos en `estilo.css`, componentes en `efectos.js` y `md.py`) | `python -X utf8 guides/_src/build.py` |
| Secciones «Comandos (`!`)» de los `CLAUDE.md`/`Perplexity.md`, `resources/comandos/catalogo.md` | `resources/comandos/comandos.py` | `python -X utf8 resources/comandos/comandos.py` |
| `.github/assets/banner*.svg` | `guides/_src/readme_banner.py` | `python -X utf8 guides/_src/readme_banner.py` |

## Antes de abrir el pull request

- [ ] La rama parte de `main` actualizada y el cambio hace una sola cosa.
- [ ] No hay secretos, datos de clientes ni archivos pesados que no deban estar en git.
- [ ] Probé el cambio (servidor local, `probar_web.py`, o el agente en una sesión real).
- [ ] Regeneré lo que sea generado y lo subí en el mismo commit.
- [ ] Actualicé la guía o la bitácora que corresponda.

## Licencia de tus aportes

Al enviar un aporte aceptas que Campuslands S.A.S. BIC pueda usarlo, modificarlo y distribuirlo como parte del repositorio bajo los términos de [`LICENSE`](LICENSE).
