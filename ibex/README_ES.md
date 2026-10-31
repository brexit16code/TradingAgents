# IBEX 35 diario para TradingAgents

Adaptación de TauricResearch/TradingAgents v0.7.1, base
`c4544913a14ed3df5f1ed7b9e8483270ce20682a`. Investigación sin operaciones reales.
No incorpora credenciales de bróker, cuentas personales ni funciones de compra/venta.

## Estado de esta instalación — 31/10/2026

- Fork creado: https://github.com/brexit16code/TradingAgents
- Informe web publicado: https://brexit16code.github.io/TradingAgents/
- Análisis de datos de 35 valores y publicación diaria activos a las 19:47.
- Dos ejecuciones en la nube completadas; la segunda aplica el filtro de nombres
  para excluir titulares sobre otras empresas. Buscador y filtros web comprobados.
- Comprobaciones del proyecto completas en Python 3.11, 3.12, 3.13 y 3.14.
- Alta de Google AI Studio completada por el titular. Comprobado en la cuenta:
  «No hay una cuenta de facturación» y nivel gratuito. Gemini 3.1 Flash Lite
  muestra 15 solicitudes/minuto, 250.000 tokens/minuto y 500 solicitudes/día.
  Gemini 3.5 Flash Lite muestra los mismos límites y también tiene tarifa gratuita.
  Clave conectada como secreto cifrado de GitHub el 01/11/2026, con autorización
  del titular. IA habilitada; primera ejecución completa en comprobación.
  No se han contratado servicios de pago.

## Qué se ha preparado

- Universo de 35 empresas con símbolos de Madrid, contrastado con el histórico de BME
  de septiembre de 2026. Redeia utiliza `RED.MC`.
- Ejecución diaria a las **19:47, Europe/Madrid**, también sábados y domingos.
  Puede haber retrasos de GitHub; no es una hora de entrega garantizada.
- Precios de hasta dos años; último cierre terminado, RSI 14, medias 20/50/200,
  MACD, rentabilidad, volatilidad y fuerza relativa frente a `^IBEX`.
- Ratios, resumen de estados financieros y comparación de PER estimado con los
  valores del mismo sector y tipo cuando hay al menos tres comparables.
- Titulares fechados y enlazados de los últimos siete días y contexto macro de
  España/eurozona. Los titulares de empresa deben mencionar su nombre o un alias;
  no basta con que el nombre aparezca como editor del artículo. Son muestras de
  búsqueda; se debe comprobar la relevancia.
- Informe HTML independiente, JSON e informe Markdown legible desde GitHub en
  Android, con justificación de señales, riesgos, fuentes y datos faltantes.
- Integración optativa con el **grafo real de TradingAgents**, sus analistas
  técnico/fundamental/noticias, debates, gestores y memoria, en castellano.

## Estado y límite de la versión gratuita

El filtro de reglas funciona sin clave de IA. **No es una ejecución de
TradingAgents ni interpreta semánticamente las noticias**: ambas cosas se
distinguen en el informe. Sus etiquetas son Vigilar favorable, Neutral,
Precaución y Datos insuficientes, no órdenes de negociación.

La integración completa está desactivada hasta verificar un proyecto de Gemini
en el nivel gratuito y sin facturación. No basta con que una clave funcione:
hay que comprobar el estado de facturación de ese proyecto. No se contrata ni
se activa ningún servicio de pago automáticamente.

Se han verificado `gemini-3.1-flash-lite` y `gemini-3.5-flash-lite` en la cuenta.
Los valores se reparten de forma alterna entre ambos modelos; cada empresa
ejecuta el grafo completo con un solo modelo, identificado en el JSON. Se mantienen
los tres analistas, los debates y los gestores; se permiten dos rondas de
herramientas por analista, apoyadas en los datos ya descargados.
La adaptación
espacia las solicitudes al menos 5,1 segundos, comparte el control entre los
analistas paralelos y limita las estimaciones conservadoras de entrada/salida
a 200.000 por ventana de 61 segundos y modelo. El tope es de 450 solicitudes por
modelo y ejecución, con margen respecto a las 500 diarias observadas por modelo.
Los informes completos se conservan para reanudar sin nuevas llamadas si siguen
siendo del mismo día y no han cambiado precios, fundamentales ni noticias.
Otras aplicaciones o ejecuciones
el mismo día comparten la cuota: los topes locales no la reservan.
La cuota gratuita no garantiza 35 ejecuciones
completas del grafo cada día. Si se agota, se detiene la IA y el informe conserva
los datos de los 35 valores; los análisis incompletos se marcan como tales.
Los topes locales de llamadas/caracteres son preventivos, no un límite de
facturación certificado. Nunca activar facturación para resolver un error de cuota
sin autorización expresa del titular.

## Aplicación a la cuenta de GitHub

Estos pasos están preparados para que el asistente los realice al disponer de
acceso autenticado; no indican que el fork o la programación estén ya activos.

1. Crear un fork real de `TauricResearch/TradingAgents` en la cuenta del usuario.
   Reutilizar un fork previo si existe; no crear copias duplicadas.
2. Incorporar `ibex/`, `.github/workflows/ibex-daily.yml`,
   `tests/test_ibex.py` y las dos exclusiones añadidas a `.gitignore`.
3. Activar Actions y el workflow del fork. GitHub desactiva inicialmente los
   workflows programados en forks; subir archivos por sí solo no los activa.
4. Lanzar manualmente **IBEX 35 diario**, esperar a que termine y comprobar
   cobertura de 35 valores, fechas, enlaces e informe móvil.
5. Si se quiere activar la IA gratuita, verificar el proyecto de Gemini,
   introducir `GOOGLE_API_KEY` como **Repository secret** y establecer la
   variable **Repository variable** `IBEX_FREE_TIER_VERIFIED=true`.
   Una clave de API nunca debe pegarse en un chat, código o informe.
6. Probar un día de uso, medir cuántos grafos caben en la cuota y mantener
   desactivada cualquier opción de pago. Si la cuota no alcanza, explicar las
   alternativas antes de cambiar el alcance o contratar un servicio.

El workflow solo se ejecuta en forks **públicos**, usando un runner Linux
estándar. Su rama `ibex-reports` contendrá informes genéricos con datos públicos.
No incluir cartera real, datos personales, secretos ni cuentas en estos informes.
Si se desea privacidad de los informes, revisar primero otra configuración y su
cuota, sin hacer público ningún dato privado.

## Consulta desde Android

Una vez desplegado, guardar en Chrome el enlace real que devuelva el asistente:
`https://github.com/USUARIO/TradingAgents/blob/ibex-reports/latest/Informe.md`.
La ruta puede variar si el fork tiene otro nombre. No es necesario abrir Codespaces,
tener un ordenador encendido ni ejecutar Python en el teléfono.

También se pueden ver los resultados en **Actions → IBEX 35 diario → última
ejecución** y descargar el paquete de informes durante siete días. `index.html`
incluye buscador, filtros y gráficos sin servicios externos de gráficos.
Los informes completos de agentes quedan enlazados cuando se han podido generar.

El workflow **Publicar informe IBEX** publica el HTML en GitHub Pages cuando
termina correctamente el análisis diario. Pages usa únicamente la carpeta de
informes ya pública de la rama `ibex-reports`; no publica credenciales ni cartera.

## Reglas y límites de datos

- Tendencia alcista ordenada: +2; bajista: −2.
- Fuerza relativa en 63 sesiones mayor que +3 puntos: +1; menor que −3: −1.
  Se usan las mismas fechas para ambas series. El IBEX de referencia es un
  índice de precio; esta comparación con acciones ajustadas no es alfa de
  rentabilidad total y no incorpora una cartera equiponderada.
- Crecimiento de ingresos positivo: +1; inferior a −5%: −1.
- PER estimado menor que 0,8 veces la mediana: +1; mayor que 1,2: −1.
  Los grupos pequeños y las diferencias entre negocios limitan su validez.
- Deuda neta/EBITDA mayor que 4: −1 solo para corporaciones; no para bancos,
  aseguradoras ni socimis.
- Puntuación ≥3: Vigilar favorable; ≤−2: Precaución; resto: Neutral.
- Precios ausentes/atrasados, menos de 200 sesiones, moneda incorrecta o
  composición sin verificar: Datos insuficientes.
- El consenso se presenta como consenso, no como valor intrínseco. No se inventa
  un DCF ni un objetivo universal para bancos, socimis y negocios industriales.
- Los estados llevan fecha de período, que no es necesariamente la fecha de
  publicación. Este complemento es para el día actual, **no para backtesting**.
- Si BME registra una nueva revisión sin cambios, se admite. Si hay altas/bajas,
  se bloquean las señales hasta revisar la lista; no se analiza una lista antigua
  como si siguiera siendo el IBEX actual.
- Titulares, nombres y texto de proveedores son datos no confiables; el informe
  escapa HTML y los agentes reciben instrucciones de no obedecer ese contenido.

El filtro no está validado como estrategia rentable. Una evaluación real de
resultados exigiría precios posteriores a cada decisión, costes y dividendos,
datos disponibles en cada fecha y comparación con un índice de rentabilidad total.

## Mantenimiento

Los workflows programados de repositorios públicos pueden desactivarse tras
60 días sin actividad en el repositorio. Comprobar su estado cuando deje de
actualizarse; no dar una automatización por permanente. Revisar también
cambios de API, cuota y composición. El horario distingue invierno y verano.

Para ejecutar el filtro en un entorno de desarrollo:

```sh
python -m pip install -r ibex/requirements.txt
python -m ibex.run
```

La orden con `--with-agents` exige la verificación del nivel gratuito y la clave.
No hay cambio automático a otro proveedor ni a una tarifa de pago.

Fuentes oficiales revisadas el 31/10/2026:

- https://github.com/TauricResearch/TradingAgents
- https://www.bolsasymercados.es/dam/descargas/indices/composicion-ibex-35-es-en.pdf
- https://docs.github.com/en/actions/concepts/billing-and-usage
- https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
- https://ai.google.dev/gemini-api/docs/pricing
- https://ai.google.dev/gemini-api/docs/rate-limits
