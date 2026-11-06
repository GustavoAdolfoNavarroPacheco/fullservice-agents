---
titulo: Instalación: instala el repositorio y usa los agentes
resumen: Procedimientos para instalar fullservice-agents, clonar el repositorio aparte de las presentaciones, solicitar permiso para publicar y montar un agente como Proyecto en Claude o Perplexity.
---

## Instalación

La instalación puede hacerse por dos rutas, que dejan exactamente el mismo resultado.

::: switch instalacion
::: tab usuario | Instalación para usuario | user
### Instalación mediante la IA

No requiere escribir comandos. Se entrega **un mensaje** a una IA que pueda trabajar en el computador (Claude Code, la pestaña *Code* de Claude Desktop u otra similar), que clona el repositorio en el lugar correcto, lo verifica e informa qué falta.

```flow
Abrir la IA | Una que pueda ejecutar comandos en el computador.
Copiar el mensaje | Con el botón «Copiar» de abajo.
Pegarlo y responder | La IA pregunta en qué carpeta guardar el proyecto y qué agentes se usarán.
Iniciar sesión si se solicita | GitHub abre el navegador: se usa la cuenta propia.
Revisar el resumen | Debe indicar dónde quedó todo y cómo abrir cada agente.
```

```prompt
Necesito instalar el repositorio «fullservice-agents» de Campuslands (los agentes del flujo comercial) en este computador. Hazlo tú, paso a paso, y NO subas nada a GitHub.

Reglas:
- Nunca me pidas contraseñas ni tokens. Si GitHub necesita que inicie sesión, dime que lo haga yo en el navegador y espera.
- Si no puedes ejecutar comandos en mi computador, dame los pasos uno a uno y espera mi confirmación en cada uno.

Pasos:
1. Comprueba que tengo Git instalado (git --version). Si no, dime cómo instalarlo y espera.
2. Si uso Windows, ejecuta: git config --global core.longpaths true (evita errores por nombres de ruta largos).
3. Pregúntame en qué carpeta quiero guardar el proyecto. Propón una corta, como «dev» dentro de mi carpeta personal, y créala si no existe.
4. En esa carpeta clona el repositorio de los agentes:
   git clone https://github.com/GustavoAdolfoNavarroPacheco/fullservice-agents
5. Pregúntame si voy a usar el agente «presentations-designer» (Estudio de Presentaciones). Si NO, salta el paso 6.
6. Las presentaciones viven en un repositorio aparte y privado. La carpeta «presentaciones» llega vacía al clonar el primero: no la crees en otro lugar ni copies archivos a mano. Clónalo DENTRO de la carpeta del agente, con este nombre exacto:
   cd fullservice-agents/agents/claude-agents/presentations-designer
   git clone https://github.com/GustavoAdolfoNavarroPacheco/Presentaciones presentaciones
   Si dice «Repository not found», es que aún no tengo acceso: detente y recuérdame que debo pedírselo a Gustavo Navarro.
7. Verifica y muéstrame el resultado: que existan las carpetas agents/claude-agents y agents/perplexity-agents y, si hiciste el paso 6, que presentaciones/decks y presentaciones/web existan y que «git -C presentaciones remote -v» apunte a GustavoAdolfoNavarroPacheco/Presentaciones.
8. Termina con un resumen en lenguaje sencillo: dónde quedó instalado y cómo abrir cada agente (mi IA debe abrirse dentro de la carpeta del agente, por ejemplo agents/claude-agents/functional-scope). Aclárame que los dos agentes de Perplexity no se abren desde el repositorio: se montan como Space.
9. Si instalé presentations-designer, recuérdame tres cosas:
   a) Para publicar presentaciones (git push) necesito permiso de Gustavo en el repositorio Presentaciones; no hagas push hasta que yo confirme que ya lo tengo.
   b) Después del push, la presentación tarda aproximadamente 2 minutos en verse en la web.
   c) Las presentaciones públicas se ven en https://fullservicepresentations.vercel.app/<nombre>, y el catálogo en la raíz exige una cuenta.
```

::: tab dev | Instalación para desarrollador | terminal
### Comandos por pasos

Se requiere **Git** y, para los agentes de Claude Code, **Claude Code** instalado. Cada agente indica en su guía de desarrollador las herramientas que usa (Python, Chrome, Node…). En Windows, antes se activan las rutas largas y se elige una carpeta corta:

```powershell
git config --global core.longpaths true
mkdir C:\dev; cd C:\dev
```

#### 1. Clonar el repositorio de los agentes

```bash
git clone https://github.com/GustavoAdolfoNavarroPacheco/fullservice-agents
cd fullservice-agents
```

#### 2. Solo si usarás el Estudio de Presentaciones: clona `Presentaciones` dentro de su carpeta

El repositorio de las presentaciones es **privado** y se clona **aparte**. La carpeta `presentaciones/` ya existe, vacía; `git clone` funciona sobre una carpeta vacía y falla si tiene archivos. Antes, [pide acceso](#repositorio-aparte-las-presentaciones).

```bash
cd agents/claude-agents/presentations-designer
git clone https://github.com/GustavoAdolfoNavarroPacheco/Presentaciones presentaciones
```

#### 3. Verifica que cada repositorio apunta a su remoto

```bash
git rev-parse --show-toplevel                    # el repositorio de los agentes
git remote -v                                    # origin ... fullservice-agents
git -C presentaciones rev-parse --show-toplevel  # debe terminar en .../presentations-designer/presentaciones
git -C presentaciones remote -v                  # origin ... Presentaciones
git -C presentaciones status -sb                 # ## main...origin/main
```

> [!importante] Mira siempre en qué repositorio estás
> Un `git add .` en la carpeta equivocada arrastra cambios de otros agentes. Dentro de `presentaciones/` se usa `git add .`; en el repositorio de los agentes, solo archivos puntuales.

#### 4. Abre el agente

Abre Claude Code **dentro de la carpeta del agente**, para que lea su `CLAUDE.md`:

```bash
cd agents/claude-agents/functional-scope     # o el agente que vayas a usar
claude
```

Los dos agentes de Perplexity (`prospection-agent` e `intelligence-commercial`) no se abren desde el repositorio: se montan como Space ([ver más abajo](#usarlo-como-proyecto-en-claude-o-perplexity)).

#### Para actualizar más adelante

Son **dos** repositorios si instalaste las presentaciones: el `git pull` de uno no actualiza el otro.

```bash
git pull                        # los agentes
git -C agents/claude-agents/presentations-designer/presentaciones pull      # las presentaciones
```
:::

## Repositorio aparte: las presentaciones

El **Estudio de Presentaciones** (`presentations-designer`) es el único agente que entrega su trabajo en **otro repositorio**: `Presentaciones`, el que publica Vercel. Guardan cosas distintas y se publican por caminos distintos:

| | Repositorio 1 | Repositorio 2 |
|---|---|---|
| Nombre | `fullservice-agents` | `Presentaciones` |
| Qué guarda | Los ocho agentes, la wiki, las herramientas y estas guías | Las presentaciones (`decks/`) y el portal web (`web/`) |
| Quién lo publica | Vercel publica solo `guides/` (esta web) | Vercel publica el portal y todas las presentaciones |
| Visibilidad | Público | **Privado**: hace falta acceso |

La carpeta `presentaciones/` **vive dentro** del agente, pero Git **no la trae** al clonar el repositorio 1: llega **vacía**. Por eso se clona aparte, en esa carpeta exacta.

```repos
fullservice-agents | Repositorio 1 | Las instrucciones, la wiki y las herramientas del agente, junto con los demás agentes.
Presentaciones | Repositorio 2 · aparte | Las presentaciones ya hechas y el portal web. Es lo que publica Vercel. | decks/, web/
agents/claude-agents/presentations-designer | presentaciones/
git clone https://github.com/GustavoAdolfoNavarroPacheco/Presentaciones presentaciones
```

### 1. Clónalo en la carpeta exacta

`presentaciones/` debe quedar **dentro** de `presentations-designer/`, con ese nombre y en minúsculas. Si lo clonas al lado, en el escritorio o con otro nombre, el agente no encontrará `decks/_plantilla-campuslands/` y los comandos de publicación irán al repositorio equivocado. Tampoco copies carpetas de presentaciones a mano: se clona.

### 2. Pide acceso a Gustavo antes de clonar y de publicar

Sin acceso, el clon falla con «Repository not found» y no podrías hacer `git push`. Pide el permiso **antes** de empezar:

1. Escríbele a **Gustavo Navarro** con tu **usuario de GitHub** ([GitHub](https://github.com/GustavoAdolfoNavarroPacheco) · [LinkedIn](https://www.linkedin.com/in/gustavo-adolfo-navarro-pacheco-876b06356/)). Si no tienes cuenta, créala gratis en github.com.
2. Gustavo te agrega como **colaborador** del repositorio `Presentaciones`, con permiso de escritura.
3. **Acepta la invitación** que llega a tu correo o en github.com/notifications.
4. Al clonar o subir, GitHub abrirá el navegador para que **inicies sesión tú**, con la cuenta que recibió el permiso.

> [!cuidado] Tus credenciales son tuyas
> Nunca le des a la IA tu contraseña ni un token de GitHub, ni los pegues en el chat. Si el agente recibe un error de permisos (403 o *Permission denied*), **se detiene y te lo explica**: no intenta rodeos con otra cuenta, un *fork* ni otro remoto.

### 3. Después del push, la presentación tarda unos 2 minutos

El agente publica con `git push` dentro de `presentaciones/`. A partir de ahí no hace nada más: **Vercel** detecta el cambio, construye el portal, copia las presentaciones y las pone en línea. Ese proceso tarda **aproximadamente 2 minutos**.

```publicar
Haces el push | Los archivos suben a GitHub.
Vercel lo detecta | Empieza un build nuevo.
Construye la web | Compila el portal y copia las presentaciones.
En línea | El link ya muestra la versión nueva.
≈ 2 min
```

Mientras tanto, el link puede dar **404** o mostrar la versión anterior; no significa que algo falló. **Espera dos minutos** y recarga con `Ctrl + F5` (en Mac, `Cmd + Mayús + R`). Si pasan **más de cinco**, avísale al agente o a Gustavo. El agente comparte el link al terminar y te avisa del tiempo; no afirma que está publicado hasta confirmarlo.

Cómo funciona la web de presentaciones (el catálogo privado, los links públicos y el registro de cada presentación) está explicado en la [guía de usuario](presentations-designer/guia-usuario#como-funciona-la-web-de-presentaciones) y en la [guía de desarrollador](presentations-designer/guia-dev#el-repositorio-aparte-y-su-publicacion) del Estudio de Presentaciones.

## Usarlo como Proyecto en Claude o Perplexity

Cualquiera de los ocho agentes puede montarse como **Proyecto de Claude** (claude.ai) o como **Space de Perplexity**: subes sus archivos, pegas unas instrucciones y trabajas en un chat. Los dos agentes de Perplexity están pensados para esto; los de Claude Code también funcionan así, con un límite que conviene conocer.

> [!importante] Un Proyecto es un chat con memoria, no un agente con tu carpeta
> No tiene acceso a tu computador ni a Git. Puede planear, redactar y analizar con las reglas del agente, pero **no puede** ejecutar sus scripts o herramientas (verificadores, constructores de Word, `git push`). Cuando una regla lo pida, te dará el comando para que lo ejecutes tú. Para el ciclo completo, instala el repositorio y usa Claude Code.

| | En un Proyecto o Space | Con el repositorio instalado |
|---|---|---|
| Seguir las reglas y la wiki del agente | Sí, desde los archivos que subes | Sí |
| Planear, redactar y analizar | Sí | Sí |
| Ver tus carpetas de clientes y resultados | No (solo lo que subas en cada chat) | Sí |
| Ejecutar scripts y herramientas del agente | No: te da el comando para que lo ejecutes tú | Sí |
| Guardar los resultados en el repositorio y publicar | No | Sí |

### Qué reglas siguen todos los agentes

El conocimiento de un Proyecto es una **lista plana de archivos**, sin carpetas. Por eso:

- **El archivo de instrucciones** (`CLAUDE.md` o `Perplexity.md`) se sube **como archivo**, y en el campo de instrucciones se pega un texto corto que le dice al agente que lo lea. Así no depende del límite del campo.
- **La wiki** (`wiki/`) se sube página por página, **sin `log.md`** (la bitácora histórica, que pesa mucho y no cambia lo que el agente hace).
- **Las habilidades** (`habilidades/<nombre>/SKILL.md`) se suben con el nombre de su carpeta, porque todas se llaman igual.
- **Plantillas y manuales** que el agente usa como base se suben; **fuentes, logos y carpetas de resultados**, no.
- **Los scripts** (`scripts/`, `herramientas/`) no se suben: un Proyecto no los ejecuta.
- **Los datos de un cliente** (alcances, cotizaciones, documentos de una licitación) se suben **en cada chat**, solo los del cliente en el que trabajas.

### Crea el Proyecto o el Space

::: switch proyecto
::: tab claude | Claude (Proyecto) | claude
1. En claude.ai abre **Projects** y crea uno nuevo; ponle el nombre del agente (por ejemplo **«Alcances Funcionales»**).
2. En las **instrucciones del proyecto**, pega el texto que te da el selector de abajo para ese agente.
3. En el **conocimiento del proyecto**, sube los archivos marcados como *Archivos* en la tabla, con los nombres indicados.
4. Abre un chat **dentro del proyecto** y empieza a trabajar.

::: tab perplexity | Perplexity (Space) | pplx
1. En Perplexity abre **Spaces** y crea uno nuevo; ponle el nombre del agente (por ejemplo **«Radar de Campus»**).
2. En las **instrucciones** (*Custom instructions*), pega el texto que te da el selector de abajo para ese agente.
3. En **Archivos**, sube los archivos marcados como *Archivos* en la tabla, con los nombres indicados.
4. Haz tus preguntas **dentro del Space**.

> [!nota] Los nombres de los botones pueden variar
> Claude y Perplexity cambian sus menús con frecuencia: busca las opciones equivalentes (instrucciones del proyecto y archivos o conocimiento).
:::

### Elige el agente: qué archivo va a dónde

```proyectos
```

Lo que el Proyecto genera es solo texto. Para el Estudio de Presentaciones, por ejemplo, guarda cada presentación en `presentaciones/decks/<nombre>/` dentro del repositorio `Presentaciones` y ejecuta el verificador que el agente te indique. Para publicarla, usa Claude Code con el repositorio instalado.

## Si algo falla

| Qué ves | Por qué pasa | Qué hacer |
|---|---|---|
| `Repository not found` al clonar `Presentaciones` | El repositorio es privado y tu cuenta no tiene acceso, o iniciaste sesión con otra cuenta | Pide acceso a Gustavo con tu usuario de GitHub y acepta la invitación; luego vuelve a clonar |
| `destination path 'presentaciones' already exists and is not an empty directory` | La carpeta tiene archivos | Muévela a otro lugar, deja la carpeta vacía y clona de nuevo |
| `presentaciones/` está vacía | Solo se clonó el repositorio 1 | Ejecuta el segundo clon, dentro de `presentations-designer/` |
| `Filename too long` al clonar en Windows | Rutas demasiado largas | `git config --global core.longpaths true` y clona en una carpeta corta como `C:\dev` |
| `Permission denied` o `403` al hacer push | Tienes acceso de lectura, pero no de escritura | Pide a Gustavo permiso de escritura. El agente se detiene; no busques rodeos |
| El link da 404 justo después del push | Vercel todavía está construyendo | Espera unos 2 minutos y recarga con `Ctrl + F5` |
| Pasan más de 5 minutos y sigue sin aparecer | Puede haber fallado el build en Vercel | Avisa al agente o a Gustavo para revisar el despliegue |
| Hiciste `git add .` y se agregaron archivos de otros agentes | Estabas en la carpeta del repositorio 1 | Antes de confirmar, `git status`; en ese repositorio se agregan solo archivos puntuales |
| Mi IA dice que no puede ejecutar comandos | Es un chat sin acceso a tu computador | Usa Claude Code (o la pestaña *Code* de Claude Desktop), o sigue los comandos de «Instalación para desarrollador» a mano |
