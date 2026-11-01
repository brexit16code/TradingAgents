# IBEX 35 diario para TradingAgents

Adaptación de TauricResearch/TradingAgents v0.7.1, base
`c4544913a14ed3df5f1ed7b9e8483270ce20682a`. Investigación sin operaciones reales.
No incorpora credenciales de bróker, cuentas personales ni funciones de compra/venta reales.

## Estado de esta instalación — 01/11/2026

- Fork creado: https://github.com/brexit16code/TradingAgents
- Informe web publicado: https://brexit16code.github.io/TradingAgents/
- Inicio automático diario a las 19:47, Europe/Madrid. La web se actualiza cuando
  termina el análisis; GitHub puede retrasar el inicio.
- Ejecución de comprobación del 01/11/2026: **35/35 informes completos de
  TradingAgents**, con precios del último cierre disponible (30/10/2026).
  Verificación: https://github.com/brexit16code/TradingAgents/actions/runs/41279251665
- La ejecución usó 400 llamadas: 112 con Gemini 3.1 Flash Lite y 288 con
  Gemini 3.5 Flash Lite, por debajo del tope preventivo de 450 por modelo.
- Hay titulares recientes para 33 empresas. Cellnex e Inmobiliaria Colonial
  indican la falta de titulares propios verificados; no se presenta ese vacío
  como ausencia de acontecimientos.
- Buscador, filtros y enlaces a informes completos disponibles desde Android.
- Comprobaciones del proyecto completas en Python 3.11, 3.12, 3.13 y 3.14.
- Alta de Google AI Studio completada por el titular. Comprobado en la cuenta:
  «No hay una cuenta de facturación» y nivel gratuito. Gemini 3.1 Flash Lite
  muestra 15 solicitudes/minuto, 250.000 tokens/minuto y 500 solicitudes/día.
  Gemini 3.5 Flash Lite muestra los mismos límites y también tiene tarifa gratuita.
  Clave conectada como secreto cifrado de GitHub el 01/11/2026, con autorización
  del titular. IA habilitada con los dos modelos Lite gratuitos verificados.
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

La integración completa está activada en esta instalación, con un proyecto de
Gemini cuyo nivel gratuito y ausencia de facturación se han comprobado. En una
instalación nueva debe verificarse ese estado antes de habilitarla: una clave
que funcione no acredita por sí sola el nivel gratuito. No se contrata ni activa
ningún servicio de pago automáticamente.

Se han verificado `gemini-3.1-flash-lite` y `gemini-3.5-flash-lite` en la cuenta.
Los valores se reparten de forma alterna entre ambos modelos; cada empresa
ejecuta el grafo con un solo modelo, identificado en el JSON. Se mantienen
los tres analistas, los debates y los gestores. Los precios, indicadores,
ratios, estados financieros y titulares se descargan y verifican antes del
grafo. Cada analista los interpreta en una llamada sin repetir esas consultas.
La evidencia determina también la identidad del punto de reanudación: un cambio
de datos comienza un análisis nuevo, en lugar de continuar con un contexto viejo.
La adaptación
espacia las solicitudes al menos 5,1 segundos, comparte el control entre los
analistas paralelos y limita las estimaciones conservadoras de entrada/salida
a 200.000 por ventana de 61 segundos y modelo. El tope es de 450 solicitudes por
modelo y ejecución, con margen respecto a las 500 diarias observadas por modelo.
Los informes completos se conservan para reanudar sin nuevas llamadas si siguen
siendo del mismo día y no han cambiado precios, fundamentales ni noticias.
Un cambio de orden de los mismos titulares no invalida el informe; un cambio
en los estados financieros sí lo invalida. Los estados anuales descargados
también se incluyen entre las evidencias facilitadas a los agentes.
Los errores de servidor de Google HTTP 500/502/503/504 se reintentan como máximo
dos veces, tras 20 y 40 segundos, retomando el punto guardado del grafo. No se
reintentan automáticamente errores de cuota, autenticación o permisos.
Si un modelo sigue devolviendo errores de servidor, se puede usar el otro
modelo Lite gratuito de la lista ya verificada. Un error de cuota o credenciales
no activa ese cambio. No se incorpora ningún modelo de pago.
La ejecución queda marcada como incompleta si falta algún informe de IA,
aunque se conservan y publican los datos y los informes que sí estén disponibles.
Otras aplicaciones o ejecuciones
el mismo día comparten la cuota: los topes locales no la reservan.
La cuota gratuita no garantiza 35 ejecuciones
completas del grafo cada día. Si se agota, se detiene la IA y el informe conserva
los datos de los 35 valores; los análisis incompletos se marcan como tales.
Los topes locales de llamadas/caracteres son preventivos, no un límite de
facturación certificado. Nunca activar facturación para resolver un error de cuota
sin autorización expresa del titular.

## Configuración activa en GitHub

El fork público `brexit16code/TradingAgents` tiene Actions y Pages configurados:

- **IBEX 35 diario**: datos y análisis de los 35 valores; también permite iniciar
  una ejecución manual desde Actions.
- **Publicar informe IBEX**: publica los informes disponibles cuando termina
  la ejecución diaria, incluso si alguno ha fallado. La cobertura se muestra
  explícitamente; una ejecución incompleta no se presenta como completa.
- **Comprobar Gemini gratuito**: diagnóstico manual de los dos modelos permitidos,
  con una petición breve por modelo y sin mostrar la clave.
- `GOOGLE_API_KEY`: secreto cifrado del repositorio.
- `IBEX_FREE_TIER_VERIFIED=true`: variable que habilita la IA tras la verificación
  del proyecto gratuito. No modificarla para saltarse una comprobación pendiente.

El workflow solo se ejecuta en forks **públicos**, usando un runner Linux
estándar. La rama `ibex-reports` contiene informes genéricos con datos públicos.
No incluir cartera real, datos personales, secretos ni cuentas en estos informes.
Para reutilizar la adaptación en otra cuenta hay que crear su propio fork,
activar sus workflows y verificar su propio proveedor y cuotas antes de añadir
una clave. Nunca pegar una clave de API en un chat, código o informe.

## Consulta desde Android

Abrir https://brexit16code.github.io/TradingAgents/ en Chrome y guardar el enlace
como marcador. Buscar una empresa y abrir su informe de TradingAgents desde la
tarjeta correspondiente. No hace falta tener un ordenador encendido ni ejecutar
Python en el teléfono.

La versión de texto está en:
https://github.com/brexit16code/TradingAgents/blob/ibex-reports/latest/Informe.md

También se pueden ver los resultados en **Actions → IBEX 35 diario → última
ejecución** y descargar el paquete de informes durante siete días. `index.html`
incluye buscador, filtros y gráficos sin servicios externos de gráficos.
Los informes completos de agentes quedan enlazados cuando se han podido generar.

GitHub Pages publica únicamente la carpeta `latest/` de la rama de informes;
no publica credenciales ni cartera.

## Cartera virtual y seguimiento de resultados

Abrir https://brexit16code.github.io/TradingAgents/cartera.html desde Android.
La página principal también enlaza la cartera. El experimento es público y usa
solo dinero ficticio; no contiene una cartera personal ni ejecuta órdenes reales.

- Capital inicial fijo: **10.000 €**; presupuesto por entrada: **1.000 € con costes**;
  máximo diez posiciones. Compras de acciones enteras y ventas solo de posiciones
  existentes; sin crédito ni ventas en corto.
- Usa la **calificación final de TradingAgents**, con una correspondencia fija:
  Buy/Strong Buy/Overweight abren una posición si no existe; Hold la conserva sin
  abrir ni ampliar; Sell/Strong Sell/Underweight la cierra. La reducción completa
  ante Underweight es una regla simplificada del experimento. Una calificación
  desconocida o incompleta no se sustituye por el filtro «Vigilar favorable».
- Se guardan la decisión, su justificación, modelo, fecha, cierre de referencia y
  huella de las evidencias en `paper-history/`. Ese registro permanece aunque la
  recomendación del día siguiente sea diferente. No se inventan aciertos anteriores.
- Se simula la ejecución en la primera **apertura de una sesión posterior al día
  de registro**, nunca en un precio anterior a la señal. Para poder usar datos
  diarios completos, la liquidación se actualiza después del cierre. Tampoco se
  liquidan barras intradía sin terminar.
- Costes ficticios: **2 € por compra y 2 € por venta**, más **0,1 % de ajuste
  desfavorable** sobre la apertura en cada sentido. No son comisiones cobradas
  al usuario ni una estimación de las condiciones de un bróker concreto.
- Primero se liquidan ventas y después compras; a igual fecha se ordenan por
  símbolo, sin escoger retrospectivamente los ganadores. La entrada no añade
  repetidamente otros 1.000 € cuando la posición ya existe. Una nueva señal puede
  cancelar una orden pendiente; se contempla caducidad de catorce días naturales.
- Dividendos brutos devengados en exfecha, para quien tenía las acciones al cierre
  anterior. Se suman al valor total como derecho devengado, separados del efectivo;
  no se presume cobro inmediato ni se reinvierten. No se calculan impuestos.
- Se procesan splits y contrasplits conservando el coste de la posición. Se deshace
  primero el ajuste retrospectivo por splits de Yahoo sobre los precios históricos;
  no se usa Adj Close para luego volver a sumar dividendos. Las fracciones de
  acciones de un split se mantienen en el experimento. Otros eventos corporativos,
  derechos, fusiones y exclusiones requieren revisión.
- La referencia es `^IBEX`, **índice de precio sin dividendos ni costes**. La cartera
  incluye costes y dividendos devengados. Se explica la diferencia; no se declara
  que superar esa línea equivalga a superar un índice de rentabilidad total.
- Si faltan precios necesarios, se pausa la liquidación en la primera sesión
  incompleta. No se inventan precios. El saldo inicial no vuelve a crearse por un
  archivo corrupto, una modificación de reglas ni un historial incompleto.

La web distingue resultado de ventas, resultado pendiente de posiciones abiertas,
efectivo, dividendos y comisiones ya descontadas. La calculadora **Ensaya una compra
y una venta** permite variar cantidad, precios de ejecución y comisión para entender
una operación hipotética. Es un ensayo matemático separado de las operaciones
registradas automáticamente.

El archivo `latest/cartera.json` y las evidencias se guardan en la rama
`ibex-reports`. El workflow diario recupera el historial, liquida las instrucciones
anteriores y registra las recomendaciones nuevas, antes de publicar. Ambos workflows
comparten un bloqueo de concurrencia para no sobreescribir operaciones más recientes.
El workflow **Actualizar cartera virtual IBEX** permite refrescar la simulación sin
repetir el análisis de IA; también se ejecuta al actualizar sus archivos en main.
Pages publica el resultado después de cualquiera de los dos workflows.

La simulación no consume llamadas de Gemini ni añade servicios de pago. Su resultado
sirve para observar el experimento desde su inicio, con las limitaciones de datos y
supuestos indicadas; no garantiza una rentabilidad real ni futura.

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

Fuentes oficiales revisadas el 31/10 y el 01/11/2026:

- https://github.com/TauricResearch/TradingAgents
- https://www.bolsasymercados.es/dam/descargas/indices/composicion-ibex-35-es-en.pdf
- https://docs.github.com/en/actions/concepts/billing-and-usage
- https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
- https://ai.google.dev/gemini-api/docs/pricing
- https://ai.google.dev/gemini-api/docs/rate-limits
