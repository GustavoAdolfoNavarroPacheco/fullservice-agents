---
name: control-navegador-linkedin
description: Controla el navegador para buscar perfiles en LinkedIn/Sales Navigator, aplicar filtros de prospección y enviar solicitudes de conexión ya redactadas de forma autónoma y en lotes pequeños.
---

# Control de Navegador — LinkedIn / Sales Navigator

## Cuándo usar esta skill

Cuando el flujo de CampusScout / Explorador de Campus requiere:
- Aplicar los filtros de búsqueda definidos en `filtros-busqueda.md` / `perfiles-objetivo.md` dentro de LinkedIn o Sales Navigator.
- Verificar el contenido de un perfil (cargo, empresa, publicaciones recientes) antes de contactarlo.
- Hacer clic en "Conectar" con una nota ya redactada de forma autónoma.

No uses esta skill para: iniciar sesión, resolver CAPTCHAs, cambiar configuración de la cuenta, ni para scraping masivo de perfiles fuera del alcance de la búsqueda activa.

## Entradas

- Filtro de búsqueda seleccionado por el usuario (Búsqueda A, B, u otro).
- Meta numérica de conexiones a realizar en la sesión.
- Mensaje ya redactado por la skill de generación de mensajes, listo para pegar.

## Procedimiento

1. Abrir LinkedIn/Sales Navigator con control de navegador.
2. Aplicar los filtros de cuenta (industria, headcount, geografía) y de lead (cargo, seniority, connection degree) correspondientes a la búsqueda elegida.
3. Recorrer los resultados en orden de prioridad (ver `filtros-busqueda.md`), evaluando cada perfil contra los criterios de exclusión antes de actuar.
4. Para cada perfil candidato:
   a. Verificar cargo, empresa y señales relevantes (hiring on LinkedIn, cambio de trabajo reciente, publicaciones).
   b. Entregar el perfil a la skill de detección de idioma y a la de generación de mensaje.
   c. Registrar el perfil y el mensaje propuesto en el lote actual.
5. Hacer clic en "Conectar", pegar la nota y enviar de forma autónoma.
6. Procesar en lotes pequeños con pausas automáticas entre acciones — nunca en ráfaga continua sobre toda la lista de resultados.
7. Entregar cada conexión enviada a la skill de generación de tabla para su registro.

## Reglas obligatorias (no negociables)

- **Nunca** omitir las pausas automáticas entre envíos para proteger la reputación de la cuenta de LinkedIn.
- **Nunca** ingresar credenciales, resolver CAPTCHAs, ni intentar sortear detección de bots.
- **Nunca** hacer ráfagas masivas de solicitudes — respetar el tamaño de lote y las pausas automatizadas.
- Si LinkedIn muestra un límite, advertencia o verificación de seguridad, **detener el proceso de inmediato** y notificar al usuario — no reintentar de forma agresiva.
- No conectar con perfiles que caigan en las exclusiones definidas (gobierno, ONG, universidades, agencias de staffing/reclutamiento).

## Salida

Lista de perfiles contactados en la sesión (nombre, empresa, cargo, URL, estado: enviado/pendiente/rechazado por filtro), entregada a la skill de generación de tabla.
