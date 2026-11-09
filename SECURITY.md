# Política de seguridad

La seguridad de este repositorio importa por dos razones: es **público**, y los agentes que contiene trabajan con información comercial de Campuslands y de sus clientes.
Gracias por ayudar a mantenerlo seguro.

## Qué cubre esta política

| Dentro del alcance | Fuera del alcance |
|---|---|
| El contenido de este repositorio (instrucciones de los agentes, scripts, plantillas, recursos). | Vulnerabilidades de Claude, Perplexity, GitHub, Vercel u otras plataformas: repórtalas a sus responsables. |
| La web de guías publicada en <https://fullservice-agents.vercel.app>. | Ataques de denegación de servicio, ingeniería social o pruebas físicas. |
| Secretos, credenciales o **datos personales y de clientes** que hayan quedado expuestos en el código o en el historial. | El repositorio privado `Presentaciones` (si hay un problema ahí, repórtalo igual por el canal de abajo). |
| Instrucciones de un agente que puedan llevarlo a **actuar sin autorización** (ver «Riesgos propios de los agentes»). | Hallazgos teóricos sin una vía de explotación demostrable. |

## Versiones con soporte

Solo la rama **`main`** recibe correcciones de seguridad. No hay versiones etiquetadas.

## Cómo reportar una vulnerabilidad

**No abras un issue público ni publiques el detalle.** Usa el reporte privado de GitHub:

1. Ve a la pestaña **[Security → Report a vulnerability](https://github.com/GustavoAdolfoNavarroPacheco/fullservice-agents/security/advisories/new)**.
2. Describe el problema e incluye, si puedes: dónde está (archivo o URL), cómo reproducirlo, qué impacto tiene y, si la tienes, una propuesta de solución.
3. Si GitHub no te lo permite, contacta al mantenedor por mensaje privado en su [perfil de GitHub](https://github.com/GustavoAdolfoNavarroPacheco) o en su
   [LinkedIn](https://www.linkedin.com/in/gustavo-adolfo-navarro-pacheco-876b06356/) **sin incluir el detalle técnico** en el primer mensaje.

### Qué puedes esperar

- Un acuse de recibo en **5 días hábiles**.
- Una primera valoración (si aplica, severidad y plan) en **10 días hábiles**.
- Aviso cuando se corrija. Si lo deseas, se te menciona en el reconocimiento; si prefieres el anonimato, también.
- Divulgación coordinada: te pedimos no publicar el detalle hasta que haya una corrección o hayan pasado **90 días**, lo que ocurra primero.

## Riesgos propios de los agentes

Este repositorio contiene instrucciones que se ejecutan con modelos de IA, así que además de los fallos habituales hay riesgos específicos. Reporta, por ejemplo:

- Una instrucción o un archivo de entrada que permita una **inyección de instrucciones** (*prompt injection*) con consecuencias reales: que un agente publique, envíe, borre o exfiltre algo sin que el usuario lo haya pedido.
- Una regla que haga que un agente **pida o maneje contraseñas, tokens o datos de pago**. Por diseño, los agentes no los piden: si hay que iniciar sesión, la persona lo hace en su navegador.
- Una instrucción que haga que un agente **actúe fuera de la carpeta de su agente** o ejecute comandos destructivos sin confirmación.

`intelligence-commercial` es el agente con más autonomía (envía invitaciones de LinkedIn sin pedir aprobación mensaje por mensaje, por decisión del equipo); sus salvaguardas
se describen en su guía de desarrollador.

## Qué no debe subirse a este repositorio

Para que el repositorio siga siendo seguro, **nunca** se sube:

- Credenciales, tokens, claves de API, archivos `.env` ni certificados.
- Datos personales o confidenciales de clientes (documentos de identidad, cuentas, firmas, contratos firmados, información financiera) que no estén ya anonimizados y autorizados para publicarse.
- Modelos o archivos pesados que deban vivir fuera de git (por ejemplo, los modelos de voz del agente multifuncional).

Si subiste algo así por error: **no basta con borrarlo en un commit nuevo**, porque queda en el historial. Avisa por el canal de arriba, **revoca o rota** la credencial de inmediato y se
limpiará el historial.

## Controles activos en el repositorio

- Alertas de seguridad de dependencias y actualizaciones automáticas (Dependabot).
- Escaneo de secretos y protección de *push* de GitHub.
- Reporte privado de vulnerabilidades.
- Cabeceras de seguridad en la web publicada (`vercel.json`) y comprobación automática de que la web generada está al día (CI).
- Propietarios de código (`CODEOWNERS`): los cambios pasan por revisión del mantenedor.

Gracias por reportar de forma responsable.
