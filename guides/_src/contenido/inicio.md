---
titulo: Inicio: qué es fullservice-agents y cómo está organizado
resumen: Qué reúne el repositorio fullservice-agents, cuáles son sus siete agentes y por dónde empezar.
---

## Empieza aquí

`fullservice-agents` es **un solo repositorio con los siete agentes** del flujo comercial de Campuslands, de la prospección al contrato. Hay dos maneras de usarlos, y las dos están explicadas en la pestaña [Instalación](#instalacion):

- **Instalar el repositorio** en tu computador y abrir tu IA (por ejemplo Claude Code) dentro de la carpeta del agente. Es la forma completa: el agente lee tus archivos, ejecuta sus herramientas y guarda los resultados.
- **Montarlo como Proyecto** en Claude o como Space en Perplexity. Es la forma rápida: sube sus archivos a la plataforma y trabaja en un chat, sin instalar nada.

```stats
7 | agentes en un solo repositorio
2 | formas de usarlos: instalar el repositorio o crear un Proyecto
2 | repositorios, si vas a usar el Estudio de Presentaciones
```

> [!tip] ¿No programas?
> Abre la pestaña [Instalación](#instalacion) y elige **«Instalación para usuario»**: copias un mensaje, se lo das a tu IA y ella instala todo. Si prefieres no instalar nada, ve directo a [Usarlo como Proyecto](#usarlo-como-proyecto-en-claude-o-perplexity).

## Cómo está organizado el repositorio

El repositorio agrupa a los agentes por la plataforma donde corren. Cada agente es una carpeta con su archivo de instrucciones, su wiki y lo que necesita para trabajar.

```tree
fullservice-agents/
  agents/
    claude-agents/                  # los cinco agentes de Claude Code (cada uno con su CLAUDE.md)
      presentations-designer/
      functional-scope/
      quote-developer/
      bidding-agent/
      contract-perfectionist/
    perplexity-agents/              # los dos agentes de Perplexity (cada uno con su Perplexity.md)
      prospection-agent/
      intelligence-commercial/
  resources/                        # marca y logos de Campuslands, compartidos por todos
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

## Siguientes pasos

```cards
Instalación | Instala el repositorio en tu computador, clona bien el repositorio aparte de las presentaciones y monta un agente como Proyecto de Claude o Perplexity. [Abrir la pestaña](#instalacion)
Guía de usuario | Cómo trabajar con cada agente día a día, sin tecnicismos. [Ver las guías de usuario](/inicio/usuario)
Guía de desarrollador | Cómo está construido cada agente y cómo se mantiene. [Ver las guías de desarrollador](/inicio/desarrollador)
```
