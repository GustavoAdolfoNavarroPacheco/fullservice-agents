#!/usr/bin/env python3
"""Comprueba que la LÓGICA del Cotizador del portal sigue siendo idéntica a la del CRM (FaseCotizacion.tsx).

Uso:
    python3 herramientas/verificar_cotizador.py [ruta/al/crm-frontend]

Por omisión busca el CRM en  ~/dev/crm-campuslands/crm/crm-frontend.  Compara, línea a línea y sin contar las aserciones no nulas
de TypeScript (`!`), tres bloques de lógica: altas/bajas/edición de módulos y meses, cálculo de costos/margen/precio y estado inicial.
Además compara los módulos copiados enteros (formato, parámetros, PDF) con sus originales. Sale con código 1 si hay diferencias de lógica.
Las diferencias permitidas (la interfaz, de dónde llegan los datos, los permisos) están descritas en CLAUDE.md, sección «Cotizador».
"""
import difflib
import os
import re
import sys

CRM = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/dev/crm-campuslands/crm/crm-frontend')
PORTAL = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'presentaciones', 'web', 'src')
FASES = os.path.join(CRM, 'src', 'features', 'proyectos', 'components', 'fases')
DATOS = os.path.join(CRM, 'src', 'features', 'proyectos', 'data')

leer = lambda p: open(p, encoding='utf-8').read()


def normalizar(texto):
    texto = re.sub(r'(?<=[\]\w\)])!(?=[\s;\)\.\],+*=])', '', texto)  # aserciones no nulas de TypeScript
    texto = texto.replace(' as const', '')  # tuplas de solo lectura (solo tipos)
    return [l.strip() for l in texto.split('\n') if l.strip()]


def bloque(src, ini, fin):
    a = src.index(ini)
    return src[a:src.index(fin, a)]


def comparar(nombre, a, b, permitidas=()):
    d = [l for l in difflib.unified_diff(a, b, lineterm='', n=0) if not l.startswith(('---', '+++', '@@'))]
    d = [l for l in d if not any(p in l for p in permitidas)]
    print(f'{"OK " if not d else "DIF"} {nombre}: {len(a)} líneas vs {len(b)} → {len(d)} diferencias')
    for l in d:
        print('     ', l)
    return len(d)


crm_fase = leer(os.path.join(FASES, 'FaseCotizacion.tsx'))
portal_fase = leer(os.path.join(PORTAL, 'components', 'cotizador', 'cotizador.tsx'))

total = 0
for nombre, ini, fin, fin_portal in [
    ('altas, bajas y edición (handleAddItem … handleUpdateMonth)', 'const handleAddItem', 'const calcNodeStats', 'const calcNodeStats'),
    ('cálculo (calcNodeStats + totales)', 'const calcNodeStats', 'const handleSave', '// En el CRM: `updateProyecto'),
    ('estado inicial', 'const canEditRolesAndPhases', 'const rolesValorHora', 'const rolesValorHora'),
    ('apertura del modal de exportación', 'const openExportModal', 'const generatePDF', 'const generatePDF'),
]:
    total += comparar(nombre, normalizar(bloque(crm_fase, ini, fin)), normalizar(bloque(portal_fase, ini, fin_portal)),
                      permitidas=('//', 'const [observaciones'))  # sin setter: la sección «Observaciones» se quitó de la interfaz

# Parámetros por proyecto (2026-10-28): estas líneas de FaseCotizacion.tsx deben estar tal cual en el componente del portal.
LINEAS_PARAMETROS_PROYECTO = [
    "const parametros = useMemo(() => combinarParametrosCotizacion(",
    "const tieneParametrosPropios = useMemo(() => diferenciasParametrosCotizacion(parametrosPorDefecto, parametros) !== null",
    "const rolesCotizacion = parametros.roles;",
    "const jornada = parametros.jornada;",
]
portal_norm = "|".join(normalizar(portal_fase))
for linea in LINEAS_PARAMETROS_PROYECTO:
    esta_crm = linea in "|".join(normalizar(crm_fase))
    esta_portal = linea in portal_norm
    print(f'{"OK " if esta_crm and esta_portal else "DIF"} parámetros por proyecto: {linea[:70]}')
    total += 0 if (esta_crm and esta_portal) else 1

# Módulos copiados enteros: solo cambian rutas de importación, el logo del PDF y la tipografía de tuplas (`as const`).
PERMITIDAS = ("from '@/types'", "from './tipos'", "cotizacionFormato", "./formato", "logo.png", "logo-cotizacion", ' as const')
for nombre, original, copia in [
    ('formato (HOUR_FACTOR, formatCurrency, aplanarFilas)', os.path.join(FASES, 'cotizacionFormato.ts'), 'formato.ts'),
    ('parámetros por defecto, valorHoraRol y combinar', os.path.join(DATOS, 'parametrosCotizacionData.ts'), 'parametros.ts'),
    ('generador del PDF', os.path.join(FASES, 'cotizacionPdf.ts'), 'pdf.ts'),
]:
    total += comparar(nombre, normalizar(leer(original)), normalizar(leer(os.path.join(PORTAL, 'lib', 'cotizador', copia))), PERMITIDAS)

print('\nRESULTADO:', 'la lógica es idéntica a la del CRM.' if total == 0 else f'{total} diferencias: revisar.')
sys.exit(1 if total else 0)
