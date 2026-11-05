---
titulo: Inicio: qué es fullservice-agents y cómo está organizado
resumen: Contenido del repositorio fullservice-agents, descripción de sus siete agentes y modos de uso.
---

## Empieza aquí

`fullservice-agents` es **un solo repositorio con los siete agentes** del flujo comercial de Campuslands, de la prospección al contrato. Hay dos modos de uso, ambos descritos en la pestaña [Instalación](#instalacion):

- **Instalar el repositorio** en el computador y abrir la IA (por ejemplo Claude Code) dentro de la carpeta del agente. Es el modo completo: el agente lee los archivos del equipo, ejecuta sus herramientas y guarda los resultados.
- **Montarlo como Proyecto** en Claude o como Space en Perplexity. Es el modo ligero: los archivos del agente se cargan en la plataforma y el trabajo se realiza en un chat, sin instalar nada.

```stats
7 | agentes en un solo repositorio
2 | modos de uso: instalar el repositorio o crear un Proyecto
2 | repositorios, cuando se usa el Estudio de Presentaciones
```

> [!nota] Instalación sin conocimientos técnicos
> La pestaña [Instalación](#instalacion) incluye el modo **«Instalación para usuario»**: se copia un mensaje, se entrega a la IA y ella realiza la instalación. Para no instalar nada, véase [Usarlo como Proyecto](#usarlo-como-proyecto-en-claude-o-perplexity).

## Cómo está organizado el repositorio

El repositorio agrupa a los agentes por la plataforma donde corren. Cada agente es una carpeta con su archivo de instrucciones, su wiki y lo que necesita para trabajar.

```tree
fullservice-agents/
  agents/
    claude-agents/                  # los 5 agentes de Claude Code (CLAUDE.md)
      presentations-designer/
      functional-scope/
      quote-developer/
      bidding-agent/
      contract-perfectionist/
    perplexity-agents/              # los 2 agentes de Perplexity (Perplexity.md)
      prospection-agent/
      intelligence-commercial/
  resources/                        # marca y logos de Campuslands
  guides/                           # esta web
```

| Agente | Carpeta | Corre en | Archivo de instrucciones |
|---|---|---|---|
| Radar de Campus | `prospection-agent` | Perplexity | `Perplexity.md` |
| Explorador de Campus | `intelligence-commercial` | Perplexity | `Perplexity.md` |
| Estudio de Presentaciones | `presentations-designer` | Claude Code | `CLAUDE.md` |
| Alcances Funcionales | `functional-scope` | Claude Code | `CLAUDE.md` |
| Desarrollador de Cotizaciones | `quote-developer` | Claude Code | `CLAUDE.md` |
| Agente Licitatorio | `bidding-agent` | Claude Code | `CLAUDE.md` |
| Perfeccionador de Contratos | `contract-perfectionist` | Claude Code | `CLAUDE.md` |

El archivo de instrucciones es el que le da al agente su identidad y sus reglas: es lo primero que lee en cada sesión.

> [!importante] Hay una excepción: el Estudio de Presentaciones usa un segundo repositorio
> Las presentaciones que construye viven en otro repositorio, `Presentaciones`, que se clona **dentro** de la carpeta del agente. Está explicado en [Repositorio aparte](#repositorio-aparte-las-presentaciones), y la instalación ya lo incluye.

## Documentación relacionada

```cards
Instalación | Procedimiento para instalar el repositorio, clonar el repositorio aparte de las presentaciones y montar un agente como Proyecto de Claude o Perplexity. [Abrir la pestaña](#instalacion)
Guía de usuario | Uso de cada agente en el trabajo diario: entradas, flujo, resultados y revisión. [Ver las guías de usuario](/inicio/usuario)
Guía de desarrollador | Construcción y mantenimiento de cada agente: habilidades, reglas, formatos y controles. [Ver las guías de desarrollador](/inicio/desarrollador)
```
