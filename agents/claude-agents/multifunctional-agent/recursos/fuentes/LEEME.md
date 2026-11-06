# Fuentes

**Poppins** (Regular, Bold, Italic, BoldItalic): la tipografía oficial de Campuslands. Licencia SIL Open Font License 1.1 (Indian Type Foundry), que permite usarla e incrustarla en documentos.

Se usan para que el Word y el PDF de las facturas se vean igual en cualquier equipo:
- el **PDF** se genera con LibreOffice, que carga estas fuentes de aquí (`scripts/comun.py → docx_a_pdf`);
- el **Word** las lleva **incrustadas** (`scripts/comun.py → incrustar_fuente`), así que se ven en Word aunque Poppins no esté instalada.
