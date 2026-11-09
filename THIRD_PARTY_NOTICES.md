# Avisos de terceros

Este repositorio es propiedad de Campuslands S.A.S. BIC (ver [`LICENSE`](LICENSE)), pero incluye componentes de terceros que conservan **sus propias licencias**.
Aquí se listan los que se distribuyen dentro del repositorio.

## Código y componentes de interfaz

| Componente | Dónde está | Autor | Licencia |
|---|---|---|---|
| [Lenis](https://github.com/darkroomengineering/lenis) 1.3.27 (scroll suave) | `guides/assets/lenis.min.js` | darkroom.engineering | MIT — texto en [`guides/assets/LENIS-LICENSE.txt`](guides/assets/LENIS-LICENSE.txt) |
| AnimateIcons (`@animateicons/react` 0.13.0) (animación del icono «FileDown») | `guides/_src/build.py` (icono embebido) | Avijit Dey | MIT — texto en [`guides/assets/ICONS-LICENSE.txt`](guides/assets/ICONS-LICENSE.txt) |
| [Lucide](https://github.com/lucide-icons/lucide) (forma de los iconos de interfaz) | `guides/_src/` | Lucide Contributors | ISC — texto en [`guides/assets/ICONS-LICENSE.txt`](guides/assets/ICONS-LICENSE.txt); parte de sus iconos deriva de [Feather](https://github.com/feathericons/feather) (MIT) |

Los componentes de [21st.dev](https://21st.dev) que inspiran algunos efectos de la web (Letter Swap, Wave Text, Card Stack, Coverflow, Animated Link) se **reescribieron**
en JavaScript puro para este proyecto; no se distribuye su código original.

## Tipografías

| Familia | Dónde se usa | Licencia |
|---|---|---|
| [Inter](https://rsms.me/inter/) | Web de guías (`guides/assets/fonts/`) | SIL Open Font License 1.1 |
| [Source Serif 4](https://github.com/adobe-fonts/source-serif) | Web de guías (`guides/assets/fonts/`) | SIL Open Font License 1.1 |
| [Poppins](https://github.com/itfoundry/poppins) | Presentaciones y documentos de los agentes | SIL Open Font License 1.1 |
| [Montserrat](https://github.com/JulietaUla/Montserrat) | Presentaciones | SIL Open Font License 1.1 |
| [DM Serif Display](https://github.com/googlefonts/dm-fonts) | Presentaciones | SIL Open Font License 1.1 |
| [Playfair Display](https://github.com/clauseggers/Playfair) | Presentaciones | SIL Open Font License 1.1 |
| [Roboto Mono](https://github.com/googlefonts/RobotoMono) | Presentaciones | Apache License 2.0 |

Las tipografías de la web reemplazan a las de Anthropic, que son propietarias y no se pueden redistribuir. La SIL Open Font License 1.1 permite usar, estudiar,
copiar y redistribuir las fuentes (incluso con un producto) siempre que no se vendan por sí solas y se conserve su aviso; el texto completo está en
<https://openfontlicense.org>.

## Marcas y logotipos

Los logotipos de Claude (Anthropic), Perplexity, Campuslands y de las empresas cliente (`resources/companies-logos/`) son marcas de sus titulares. Se incluyen solo para
identificar las plataformas y los proyectos, y no implican vínculo, aval ni patrocinio.

## Herramientas de desarrollo (no se distribuyen)

La web y los PDF se generan con Python (biblioteca estándar) y se verifican con [Playwright](https://playwright.dev) (Apache-2.0) sobre Chrome. Los agentes de Claude Code
usan, según el caso, `python-docx`, `PyMuPDF`, `Pillow`, `faster-whisper`, `sherpa-onnx`, LibreOffice y `ffmpeg`; se instalan por separado y cada uno tiene su propia licencia.

---

*¿Falta algún componente o hay un error en un aviso? Abre un [issue](../../issues/new/choose) o envía un pull request.*
