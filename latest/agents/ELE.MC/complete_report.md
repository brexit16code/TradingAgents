# Trading Analysis Report: ELE.MC

- Analysis date: 2026-11-27
- Rating: Underweight
- Generated: 2026-11-27 21:20:12
- TradingAgents 0.7.1: google, deep gemini-3.5-flash-lite, quick gemini-3.5-flash-lite
- Analysts: market, news, fundamentals; research debate rounds 1, risk debate rounds 1
- Data vendors: core_stock_apis yfinance, technical_indicators yfinance, fundamental_data yfinance, news_data yfinance, macro_data fred, prediction_markets polymarket, get_news ibex_sample, get_global_news ibex_sample

## I. Analyst Team Reports

### Market Analyst
**Rating**: REVIEW

**FINAL TRANSACTION PROPOSAL**: HOLD

---

### Análisis detallado y Nuanceado de Tendencia para Endesa, S.A. (`ELE.MC`)

#### 1. Contexto de Mercado y Datos de Cotización
A fecha de 27 de noviembre de 2026, las acciones de Endesa (`ELE.MC`) cotizan a un precio de **43,74 EUR** en la bolsa española (MCE), registrando un incremento diario de 0,97% en la última sesión y una capitalización de mercado cercana a los 44.380 millones de euros. El valor muestra una sólida recuperación a medio y largo plazo, con una rentabilidad a 252 sesiones (anual) del **47,39%**, situándose holgadamente por encima de su media móvil de 200 sesiones (`close_200_sma` en 38,95 EUR).

#### 2. Análisis Técnico e Indicadores Seleccionados
De acuerdo con las directrices de análisis técnico e integración de indicadores complementarios y no redundantes, se evalúan las métricas clave disponibles:

* **Medias Móviles (`close_50_sma` y `close_200_sma`)**: 
  * La media móvil de 50 sesiones se sitúa en **43,13 EUR**, mientras que la cotización actual (43,74 EUR) gravita ligeramente por encima de la misma, confirmando un sesgo alcista a medio plazo.
  * La media móvil de 200 sesiones (`38,95 EUR`) confirma la tendencia alcista estructural de fondo a largo plazo. La distancia entre el precio actual y la SMA de 200 refleja un avance sostenido, aunque con un nivel de *drawdown* actual de -4,89% desde máximos recientes.
* **Momentum y Convergencia (`rsi`, `macd`, `macd_signal`, `macd_histogram`)**:
  * El Índice de Fuerza Relativa de 14 períodos (`rsi14`) se encuentra en **51,71**, un nivel neutral que indica ausencia de condiciones de sobrecompra o sobreventa inmediatas, sugiriendo consolidación tras las recientes subidas.
  * El indicador MACD (`-0,03`) y su línea de señal (`0,14`) muestran un ligero cruce bajista o de compresión lateral a corto plazo, respaldado por un histograma plano o ligeramente negativo, lo que aconseja cautela ante una posible fase de estancamiento temporal en el corto plazo.
* **Volatilidad y Bandas (`volatility_pct`, `atr` implícito a través de bandas y desviación)**:
  * La volatilidad histórica anualizada se sitúa en el **19,79%**, un nivel moderado/estándar para el sector de utilities reguladas en Europa. El precio se halla próximo a su media de Bollinger de 20 sesiones (`sma20` en 43,98 EUR), lo que indica un rango operativo estrecho a la espera de un nuevo catalizador volumétrico.

#### 3. Fundamentales y Valoración
* **Valuación y Beneficios**: Endesa presenta un PER histórico (*trailing P/E*) de **18,38x** y un PER adelantado (*forward P/E*) de **18,07x**, con un beneficio por acción estimado (*forward EPS*) de 2,42 EUR. La ratio *Enterprise Value to EBITDA* (`enterpriseToEbitda`) se sitúa en **10,09x**, lo cual denota una valoración razonable frente al sector de *Utilities - Regulated Electric*.
* **Solvencia y Deuda**: La deuda neta sobre EBITDA se sitúa en un saludable **2,10x** (con una deuda total de 11.905 millones de euros frente a un EBITDA de 5.636 millones de euros al cierre de los datos más recientes), evidenciando un perfil financiero robusto y disciplinado en materia de inversión de capital (*CapEx* de 1.844 millones de euros en 2025 con un flujo de caja libre de 2.207 millones de euros).
* **Política de Dividendos**: Endesa destaca por su atractivo retribución al accionista. Recientemente se ha anunciado el pago de un dividendo a cuenta de **0,50 euros por acción**, previsto para el próximo **12 de enero de 2027** (según anuncios de prensa especializada de noviembre de 2026), respaldando una rentabilidad por dividendo (*dividend yield*) estimada en torno al **3,61%** a 3,66%.
* **Consenso de Analistas**: El precio objetivo medio de consenso de los analistas se sitúa en **36,89 EUR** (con un rango entre 26,20 EUR y 44,30 EUR basado en 23 opiniones), lo que arroja una divergencia negativa implícita de **-15,67%** respecto al precio de cotización actual de 43,74 EUR, sugiriendo que el título cotiza actualmente por encima de la valoración media consensuada de analistas, justificando una postura de revisión y prudencia.

#### 4. Evidencias Externas y Contexto Macroeconómico
El contexto bursátil general en Europa y España al cierre de noviembre de 2026 muestra un tono de rebote en los mercados de renta variable (como señalan las crónicas de Merca2.es y Bolsamania del 26-27 de noviembre de 2026 sobre la evolución de las bolsas europeas y tecnológicas). Asimismo, la tasa de inflación en España (IPC de noviembre de 2026) se moderó al 4,1%, según informes de Rankia. 

#### 5. Datos Faltantes y Advertencias
* No se dispone de un desglose detallado diario de volúmenes de negociación intradiarios exactos para el cálculo de VWMA personalizado más allá de los agregados de caja y flujos operativos anuales (`operatingCashflow` de 4.081 millones de euros).
* Se recuerda que los precios objetivos de los analistas son estimaciones de consenso y no valores intrínsecos definitivos.

---

### Resumen Clave en Tabla

| Métrica / Indicador | Valor Actual / Referencia | Implicación para el Trading / Análisis |
| :--- | :--- | :--- |
| **Precio de Cierre (`close`)** | 43,74 EUR (27-Nov-2026) | Cotización estable por encima de la SMA de 50 y 200 sesiones. |
| **RSI (14)** | 51,71 | Neutralidad técnica; sin señales extremas de sobrecompra o sobreventa. |
| **MACD y Señal** | MACD: -0,03 / Señal: 0,14 | Momento a corto plazo ligeramente plano/bajista; requiere confirmación. |
| **Medias Móviles (SMA 50 / 200)** | 43,13 EUR / 38,95 EUR | Tendencia principal alcista consolidada a medio y largo plazo. |
| **Volatilidad (1 año)** | 19,79% | Volatilidad moderada, típica del sector de servicios públicos regulados. |
| **PER Adelantado (*Forward PE*)** | 18,07x | Valoración intermedia en línea con sus comparables sectoriales. |
| **Deuda Neta / EBITDA** | 2,10x | Estructura de capital saneada y controlada. |
| **Consenso de Analistas** | 36,89 EUR (Upside: -15,67%) | El precio de mercado supera la media de consenso, limitando el potencial a corto plazo. |

### News Analyst
**Rating**: REVIEW

### Informe de Investigación y Análisis Macroeconómico - Endesa, S.A. (`ELE.MC`)

**Fecha de análisis:** 27 de noviembre de 2026  
**Entorno de mercado:** Acciones cotizadas en la Bolsa de Madrid (MCE), denominadas en EUR, bajo el ticker `ELE.MC` (Endesa, S.A., sector: *Utilities / Utilities - Regulated Electric*).

---

### 1. Contexto Macroeconómico Global y Sectorial
Durante la última semana de noviembre de 2026, los mercados bursátiles europeos y globales han prolongado su tono alcista, impulsados principalmente por el sector tecnológico y bancario, a pesar de las señales de desaceleración económica en economías clave como la francesa. 
* **Inflación en la Eurozona:** Se ha reportado que el IPC de noviembre de 2026 se moderó hasta el 4,1% (según datos publicados por fuentes financieras como Rankia el 27 de noviembre de 2026). Este nivel inflacionario sigue exigiendo cautela en las políticas de rentabilidad real de los ahorradores y en los costes de capital del sector de servicios públicos (*utilities*).
* **Perspectivas del Mercado:** Instituciones como Ostrum AM estiman subidas adicionales del orden del 10% en las bolsas europeas para el año 2027, aunque bajo un régimen de riesgos renovado.

---

### 2. Análisis Fundamental y Situación Financiera de Endesa (`ELE.MC`)
Tomando como base los datos financieros e informes recientes:
* **Capitalización Bursátil:** 44.380,84 millones de EUR.
* **Métricas de Valoración:** 
  * PER Histórico (*Trailing P/E*): 18.38x
  * PER Adelantado (*Forward P/E*): 18.07x
  * Ratio frente a peers: Se sitúa en un PER relativo intermedio con un ratio de 1.02 frente a la mediana de sus comparables (`ANE.MC`, `ENG.MC`, `IBE.MC`, `NTGY.MC`, `RED.MC`, `SLR.MC`).
* **Ingresos y Rentabilidad:** Los ingresos totales alcanzaron los 21.020 millones de EUR al cierre del ejercicio 2025, con un beneficio neto de 2.198 millones de EUR y un EBITDA de 5.314 millones de EUR. Presenta una sólida rentabilidad sobre el capital propio (*Return on Equity* - ROE) del 27,21% y márgenes de beneficio neto de entorno al 10,9%.
* **Endalbe y Solvencia:** La deuda total se sitúa en 11.905 millones de EUR (con una deuda neta sobre EBITDA de aproximadamente 2.10x), lo cual refleja una estructura de apalancamiento razonable y estable para una empresa de servicios públicos regulados.
* **Consenso de Analistas:** El precio objetivo medio de consenso (*Target Mean Price*) se sitúa en **36,89 EUR** (con un rango entre un mínimo de 26,20 EUR y un máximo de 44,30 EUR según 23 opiniones de analistas). Con la cotización actual a **43,74 EUR** (cierre del 27 de noviembre de 2026), esto implica un potencial de retorno respecto al consenso (*consensus upside*) de aproximadamente **-15,67%**, advirtiendo que la acción cotiza actualmente por encima de la media de los analistas.

---

### 3. Análisis Técnico
* **Precio de Cierre (27/11/2026):** 43,74 EUR (variación diaria de +0,97%).
* **Medias Móviles:** El precio se encuentra ligeramente por debajo de su SMA de 20 sesiones (43,98 EUR), pero por encima de su SMA de 50 sesiones (43,13 EUR) y muy por encima de su SMA de 200 sesiones (38,95 EUR), lo que confirma una tendencia alcista estructural a mediano y largo plazo.
* **Indicadores Técnicos:** RSI de 14 períodos en 51,71 (zona neutral, sin sobrecompra ni sobreventa). MACD ligeramente negativo (-0.03) con línea de señal en 0.14, sugiriendo una fase de consolidación a corto plazo tras el fuerte rendimiento a 1 año (+47,39%).
* **Volatilidad:** Volatilidad del período del 19,79% y un *drawdown* actual del -4,89% desde sus máximos recientes.

---

### 4. Eventos Corporativos Recientes y Dividendos
Según las noticias publicadas entre el 24 y el 25 de noviembre de 2026 (por medios como Finect, Estrategias de Inversión, Bolsamania y Valencia Plaza):
* Endesa ha anunciado el pago de un **dividendo a cuenta de 0,50 euros brutos por acción**.
* **Fechas Clave:** El abono de este dividendo se hará efectivo el próximo **12 de enero de 2027**. Esto mantiene el atractivo por dividendo de la compañía, que cuenta con una rentabilidad por dividendo (*dividend yield*) estimada en torno al 3,61% - 3,66%.

---

### 5. Datos Faltantes y Limitaciones
* No se dispone de un desglose detallado de los flujos de caja proyectados más allá del cierre anual 2025 (FCP reportado en 2.207 millones de EUR en 2025).
* Las opiniones de consenso de analistas muestran un precio objetivo medio inferior al precio actual de mercado, lo que requiere prudencia ante posibles valoraciones estiradas por el rally reciente.

---

### Resumen en Tabla

| Componente | Detalle / Métrica Clave | Fuente / Referencia |
| :--- | :--- | :--- |
| **Ticker y Empresa** | `ELE.MC` (Endesa, S.A.) | Registro MCE / Datos suministrados |
| **Precio Actual** | 43,74 EUR (al 27/11/2026) | Yahoo Finance / Snapshot |
| **PER Adelantado** | 18.07x (Ratio sectorial: 1.02) | Datos Fundamentales |
| **Precio Objetivo Consenso**| 36,89 EUR (Upside: -15,67%) | Consenso de 23 analistas |
| **Dividendo Reciente** | 0,50 EUR por acción (Pago: 12/01/2027) | Comunicados de prensa (24-25 Nov 2026) |
| **Tendencia Técnica** | Alcista a largo plazo (por encima de SMA200 de 38,95 EUR) | Indicadores técnicos |
| **Contexto Macro** | IPC Noviembre Zona Euro al 4,1%; bolsas al alza | Noticias macroeconómicas (27/11/2026) |

**Rating**: REVIEW

FINAL TRANSACTION PROPOSAL: No transaction or portfolio allocation executed. Read-only research report.

### Fundamentals Analyst
**Rating**: REVIEW

**ANÁLISIS FUNDAMENTAL Y TÉCNICO DE ENDESA, S.A. (`ELE.MC`)**

Fecha de referencia: 27 de noviembre de 2026.  
Mercado: MCE (Bolsa de Madrid, EUR).  
Sector: Utilities / Utilities - Regulated Electric.  

---

### 1. Perfil de la Compañía y Contexto de Negocio
Endesa, S.A. (`ELE.MC`) es uno de los operadores eléctricos líderes en España y Portugal, enfocado en la generación, distribución y comercialización de electricidad, así como en actividades de gas natural. Como componente del sector de *utilities* reguladas, su perfil se caracteriza históricamente por la estabilidad de flujos de caja y una atractiva política de retribución al accionista. 

### 2. Información Financiera Histórica y Reciente
A partir de los estados financieros suministrados, se observa la evolución de Endesa, S.A. en los últimos ejercicios fiscales anuales:

*   **Cuenta de Resultados (Income Statement):**
    *   **2023:** Ingresos Totales de 25.064 millones de EUR; EBITDA de 3.324 millones de EUR; Beneficio Neto (*Net Income*) de 742 millones de EUR.
    *   **2024:** Ingresos Totales de 20.927 millones de EUR; EBITDA de 4.949 millones de EUR; Beneficio Neto de 1.888 millones de EUR.
    *   **2025:** Ingresos Totales de 21.020 millones de EUR; EBITDA de 5.314 millones de EUR; Beneficio Neto de 2.198 millones de EUR.
    *   *Comentario:* Se evidencia una fuerte recuperación y crecimiento de la rentabilidad neta y del EBITDA entre 2023 y 2025, a pesar de una ligera contracción inicial de los ingresos totales en 2024 estabilizados en 2025.

*   **Balance de Situación (Balance Sheet):**
    *   **2023:** Activos Totales de 41.283 millones de EUR; Deuda Total de 13.727 millones de EUR; Patrimonio Neto (*Stockholders Equity*) de 7.017 millones de EUR.
    *   **2024:** Activos Totales de 37.345 millones de EUR; Deuda Total de 10.963 millones de EUR; Patrimonio Neto de 8.110 millones de EUR.
    *   **2025:** Activos Totales de 37.482 millones de EUR; Deuda Total de 10.895 millones de EUR; Patrimonio Neto de 8.522 millones de EUR.
    *   *Comentario:* Proceso de desapalancamiento disciplinado, reduciendo la deuda total de forma sostenida desde más de 13.700 millones en 2023 hasta por debajo de los 10.900 millones en 2025, fortaleciendo el patrimonio neto de la compañía.

*   **Flujo de Caja (Cash Flow):**
    *   **2023:** Flujo Operativo de 4.697 millones de EUR; CAPEX de -2.284 millones de EUR; Flujo de Caja Libre (FCF) de 2.413 millones de EUR.
    *   **2024:** Flujo Operativo de 3.567 millones de EUR; CAPEX de -1.846 millones de EUR; FCF de 1.721 millones de EUR.
    *   **2025:** Flujo Operativo de 4.051 millones de EUR; CAPEX de -1.844 millones de EUR; FCF de 2.207 millones de EUR.

### 3. Métricas Financieras y de Valoración Actuales
*   **Capitalización Bursátil:** ~44.381 millones de EUR.
*   **Precio de Cierre (27/11/2026):** 43,74 EUR.
*   **PER (Trailing):** 18,38x | **PER (Forward):** 18,07x.
*   **Ratio Precio/Valor en Libros (P/B):** 5,70x.
*   **EV/EBITDA:** 10,09x.
*   **Deuda Neta / EBITDA:** ~2,10x (Deuda total de 11.905 millones de EUR frente a un EBITDA de 5.636 millones de EUR).
*   **Rentabilidad por Dividendo (*Dividend Yield*):** ~3,61% - 3,66% (con un dividendo por acción previsto/tasa de 1,58 EUR y un *payout ratio* aproximado del 66,5%).
*   **Consenso de Analistas:** Precio objetivo medio (*target mean price*) de 36,89 EUR (con un rango entre 26,20 EUR y 44,30 EUR a partir de 23 opiniones de analistas). Esto arroja una **sobrevaloración teórica frente al consenso** de un -15,67% (consenso de precio objetivo por debajo de la cotización actual de 43,74 EUR).
*   **Valoración relativa:** PER relativo intermedio frente al sector, con una ratio de 1,02 frente a la mediana de los *peers* (17,69x).

### 4. Información Reciente y Eventos Corporativos (Noviembre de 2026)
*   A finales de noviembre de 2026, Endesa ha anunciado el pago de un dividendo a cuenta de **0,50 euros por acción**, fijando como fecha de abono el próximo **12 de enero de 2027** (según publicaciones de Bolsamania, Estrategias de Inversión y Rankia del 24-25 de noviembre de 2026).
*   El contexto macroeconómico reciente muestra un tono positivo en las bolsas europeas ("Bolsas y tecnología prolongan el rebote", 27/11/2026) junto con una moderación de la inflación en noviembre de 2026 al 4,1%.

### 5. Análisis Técnico (`ELE.MC`)
*   **Precio Actual:** 43,74 EUR (variación diaria de +0,97%).
*   **Medias Móviles:** SMA20 en 43,98 EUR; SMA50 en 43,13 EUR; SMA200 en 38,95 EUR. La cotización se encuentra firmemente por encima de su media de 200 sesiones, confirmando tendencia alcista a medio-largo plazo.
*   **Osciladores:** RSI(14) en 51,71 (zona neutral). MACD en -0,03 con línea de señal en 0,14 (ligero sesgo plano/consolidación a corto plazo).
*   **Rentabilidades recientes:** +0,64% a 21 sesiones; +4,09% a 63 sesiones; +47,39% a 252 sesiones (fuerte revalorización anual).
*   **Drawdown:** -4,89% desde máximos recientes, con una volatilidad del 19,79%.

### 6. Datos Faltantes y Limitaciones
*   No se dispone de desglose detallado de operaciones de iniciados (*insider transactions*) en el conjunto de datos estáticos precargados.
*   Los objetivos de analistas reflejan un consenso estático que se sitúa por debajo de la cotización actual de mercado (43,74 EUR vs. objetivo medio de 36,

## II. Research Team Decision

### Bull Researcher

Bull Analyst: ¡Hola! Comprendo perfectamente que el oso mire el consenso de analistas de 36,89 EUR y grite "sobrevalorada" frente a los 43,74 EUR de cotización actual de `ELE.MC`. Pero dejemos a un lado las cifras estáticas y miremos la realidad operativa y financiera que está impulsando a Endesa. ¡Aquí hay una tesis alcista sólida y de altísima calidad que los osos están pasando por alto!

### 1. Crecimiento Real y Solidez Financiera indiscutible
El oso se obsesiona con una media de analistas que muchas veces llega tarde a los cambios de ciclo, pero ignora los datos fundamentales duros de la compañía. ¿Dónde ves debilidad cuando el **Beneficio Neto** pasó de 742 millones de EUR en 2023 a unos impresionantes **2.198 millones de EUR** en 2025? ¡Eso es un salto colosal en rentabilidad! 
Además, la escala del negocio es impecable: Endesa generó **4.051 millones de EUR** en flujo de caja operativo y un flujo de caja libre (*FCF*) de **2.207 millones de EUR** al cierre de 2025. Con un ratio de endeudamiento (*Deuda Neta/EBITDA*) contenido en un saludable **2,10x** (habiendo reducido la deuda total desde más de 13.700 millones en 2023 hasta los 10.895 millones), estamos ante una máquina bien engrasada y financieramente blindada.

### 2. Ventajas Competitivas y Posicionamiento de Mercado
En un entorno macroeconómico donde la inflación en la Eurozona se modera al 4,1% (noviembre de 2026) y los mercados exigen refugios seguros pero con capacidad de generar retornos reales, las *utilities* integradas como Endesa tienen una posición dominante inigualable. Su combinación de regulación eléctrica y capacidad de adaptación le otorga un PER *forward* muy razonable de **18,07x**, perfectamente alineado con la mediana de sus comparables sectoriales pero respaldado por un **ROE del 27,21%**. ¿Cuántas empresas del sector pueden fardar de un retorno sobre el capital propio del 27% manteniendo semejante disciplina de balance? Ninguna de las que el oso suele aplaudir.

### 3. Indicadores Positivos y Catalizadores Inmediatos
¿Qué dice la técnica? El precio de `ELE.MC` cotiza firmemente por encima de su media móvil de 200 sesiones (**38,95 EUR**) y de la de 50 sesiones (**43,13 EUR**), acumulando una rentabilidad anualizada sobresaliente del **47,39%**. El RSI en 51,71 nos muestra un descanso técnico completamente sano, sin sobrecompra, listo para el siguiente tramo alcista. 
Y para rematar, ¿qué pasa con la retribución al accionista? Endesa no decepciona: el reciente anuncio del dividendo a cuenta de **0,50 euros por acción**, pagadero el próximo **12 de enero de 2027**, demuestra que la directiva prioriza al inversor y ofrece una rentabilidad por dividendo (*dividend yield*) cercana al **3,61% - 3,66%**, justo cuando los ahorradores buscan proteger su capital de la inflación.

El oso puede seguir anclado en su gráfico teórico y en un consenso desactualizado, pero los fundamentales de Endesa, su desapalancamiento ejemplar y su capacidad de generar caja imbatible justifican de sobra que `ELE.MC` mantenga su cotización en estos niveles y busque nuevos máximos. ¡La fortaleza manda!

---

**Rating**: REVIEW

FINAL TRANSACTION PROPOSAL: HOLD

### Bear Researcher

Bear Analyst: ¡Hola, colega! Admiro tu optimismo y tu capacidad para entusiasmarte con el salto en el beneficio neto de 2025 o con ese ROE del 27,21%. Pero vamos a poner los pies en la tierra y a mirar la realidad fría de los datos y del mercado para `ELE.MC`. Estás cometiendo el clásico error de extrapolación alcista, ignorando las señales de alerta roja que gritan prudencia (o más bien, salida) en este preciso instante. 

Déjame desmontar punto por punto esa tesis de "máquina bien engrasada":

### 1. El espejismo del Beneficio y la realidad del Consenso de Analistas
Te agarras al salto de los 742 millones de EUR en 2023 a los casi 2.200 millones en 2025 como si fuera una tendencia lineal infinita. Olvidas que el sector energético es sumamente cíclico y volátil en función de los precios mayoristas del *pool* eléctrico y las regulaciones gubernamentales. ¿Y sabes quién no pasa eso por alto? Los 23 analistas profesionales que cubren la compañía. Descartar el consenso diciendo que "llega tarde" es una huida hacia adelante: el precio objetivo medio se sitúa en **36,89 EUR**, mientras que `ELE.MC` cotiza a **43,74 EUR**. ¡Eso implica una **desconexión del -15,67%** respecto a la valoración fundamental de los expertos! Estás pagando una prima exagerada (un PER *forward* de 18,07x y un P/B estirado de 5,70x) por una *utility* que ya ha descontado todo el optimismo posible en su brutal rally anual del **47,39%**.

### 2. El peligro del agotamiento técnico y la falsa "consolidación sana"
Hablas de un RSI neutral en 51,71 y de una pausa técnica saludable por encima de la media de 50 sesiones (**43,13 EUR**). Pero mira con atención el indicador MACD: está en **-0,03** con una línea de señal en **0,14**, mostrando un claro sesgo de compresión bajista a corto plazo y un histograma plano. Tras una subida de casi el 48% a 252 sesiones, el valor está pidiendo a gritos una corrección lógica de mean-reversion hacia su media de 200 sesiones (**38,95 EUR**). Comprar `ELE.MC` aquí arriba, con un *drawdown* de -4,89% desde sus máximos y la presión de cotizar muy por encima de su valor intrínseco consensuado, es jugársela a cara o cruz en la parte alta del ciclo.

### 3. ¿Dividendos atractivos o trampa de rendimiento en un entorno inflacionario?
Presumes del dividendo a cuenta de **0,50 euros por acción** que se abonará el próximo **12 de enero de 2027**, defendiendo una rentabilidad por dividendo (*dividend yield*) del **3,61% - 3,66%**. ¡Despierta! Con una inflación en la Eurozona que ronda el **4,1%** (según los datos de noviembre de 2026), esa rentabilidad por dividendo **es nominalmente negativa en términos reales**. Tus ahorros pierden poder adquisitivo frente al coste de la vida, y para colmo, el *payout ratio* ya se sitúa en un elevado **66,55%**. Forzar la retribución al accionista con un endeudamiento neto sobre EBITDA de **2,10x** (casi 11.900 millones de euros de deuda total) en un escenario macroeconómico global repleto de incertidumbres y nuevas cargas de riesgo para 2027 limita la capacidad de maniobra y el crecimiento orgánico futuro de Endesa.

No se trata de odiar a Endesa como compañía, sino de ser lúcidos con los precios. A 43,74 EUR, `ELE.MC` está sobrecomprada frente a su valor real de consenso, ofrece un dividendo que pierde contra la inflación real y se enfrenta a un agotamiento técnico evidente. El riesgo bajista supera con creces cualquier expectativa de recorrido adicional. ¡Cuidado con quedarse atrapados en el vagón de cola de este rally!

**Rating**: REVIEW

FINAL TRANSACTION PROPOSAL: HOLD

### Research Manager
**Recommendation**: Underweight

**Rationale**: El debate pone de manifiesto una fuerte contradicción entre los sólidos fundamentales operativos y de caja de Endesa (ELE.MC) en 2025 y la exigente valoración de mercado actual. Por un lado, el analista alcista destaca la mejora drástica del beneficio neto (hasta 2.198 millones de EUR), un FCF robusto de 2.207 millones, un ROE del 27,21% y la continuidad en la retribución al accionista con el dividendo de 0,50 EUR para enero de 2027. Por otro lado, el analista bajista argumenta de forma contundente que el precio de cotización (43,74 EUR) se encuentra un 15,67% por encima del precio objetivo medio del consenso (36,89 EUR), acumulando un rally anual del 47,39% con un PER forward de 18,07x y un ratio P/B elevado de 5,70x, además de un dividendo real que se ve superado por una inflación del 4,1%. La balanza se inclina hacia la cautela: aunque la compañía es financieramente sólida, el precio actual descuenta de sobra las buenas noticias y presenta un riesgo considerable de reversión a la media respecto al consenso de analistas, justificando una postura de infraponderación.

**Strategic Actions**: Para implementar la recomendación de Underweight sobre ELE.MC, el trader debe reducir gradualmente la exposición actual en caso de mantener posiciones largas, situándola por debajo de una asignación estándar de cartera. Se aconseja no abrir nuevas posiciones de compra a los niveles actuales de 43,74 EUR dada la divergencia negativa del 15,67% con el precio objetivo de consenso (36,89 EUR). Establecer alertas de precio en niveles cercanos a la media móvil de 200 sesiones (38,95 EUR) para reevaluar la tesis de acumulación si se produce una corrección técnica saludable.

## III. Trading Team Plan

### Trader
**Action**: Sell

**Reasoning**: Endesa (ELE.MC) cotiza actualmente a 43,74 EUR, lo que representa una prima del 15,67% por encima del precio objetivo medio de consenso de los analistas situado en 36,89 EUR, tras un rally anual del 47,39% y un PER adelantado exigente de 18,07x. Aunque los fundamentales operativos y la generación de flujo de caja son sólidos, la valoración actual descuenta en exceso las buenas noticias y supera ampliamente los niveles de soporte a corto plazo, justificando la ejecución de una recomendación de venta enmarcada en la postura de infraponderación.

**Entry Price**: 43.74

**Stop Loss**: 46.5

**Position Sizing**: 3% of portfolio

FINAL TRANSACTION PROPOSAL: **SELL**

## IV. Risk Management Team Decision

### Aggressive Analyst

Aggressive Analyst: ¡Atención todos! Vamos a dejarnos de parálisis por análisis y de mirar el retrovisor con miedo. Como analista de riesgo agresivo, tengo muy claro que el mercado recompensa a los valientes que saben capitalizar las oportunidades, no a los que se encierran en la trinchera del inmovilismo. 

Veamos los datos fríos y contundentes de Endesa (`ELE.MC`). La compañía cotiza a 43,74 EUR respaldada por un año excepcional con una rentabilidad del 47,39% y un flujo de caja libre verdaderamente envidiable que alcanzó los 2.207 millones de euros al cierre de 2025, todo ello mientras reduce su deuda total por debajo de los 10.900 millones. Hablamos de un coloso energético con fundamentos operativos impecables y una disciplina de capital ejemplar (deuda neta sobre EBITDA en unos sólidos 2,10x). Además, la retribución al accionista sigue siendo un imán de capital, con ese jugoso dividendo a cuenta de 0,50 euros por acción previsto para el próximo 12 de enero de 2027.

Si los analistas conservadores o neutrales se escandalizan porque el precio actual supera el consenso de 36,89 EUR o porque el PER adelantado se sitúa en 18,07x, están cometiendo el error clásico de confundir la media del pasado con el valor de la innovación y el impulso de mercado. El mercado europeo y español está prolongando un rebote técnico robusto (con las bolsas al alza y una inflación que se modera al 4,1%), y quedarse fuera de un valor con este momento técnico —sostenido holgadamente por encima de su media móvil de 200 sesiones en 38,95 EUR— solo por miedo a una corrección menor es perderse el verdadero crecimiento.

Aceptar una postura de venta o de simple revisión estática cuando la tendencia estructural es claramente alcista y la compañía genera caja de sobra para financiar su transición y remunerar al inversor es una estrategia cobarde que deja dinero sobre la mesa. ¡Hay que arriesgar para ganar, y Endesa (`ELE.MC`) tiene la fuerza y el respaldo operativo para seguir desafiando las previsiones más pesimistas!

Rating: REVIEW

FINAL TRANSACTION PROPOSAL: SELL

### Conservative Analyst

Conservative Analyst: Como Analista de Riesgo Conservador, mi deber principal es proteger el capital de la firma y evitar la exposición a caídas innecesarias de mercado, y debo advertir enérgicamente contra el exceso de optimismo que acaban de plantear. Confundir la euforia alcista a corto plazo con una oportunidad de inversión segura es un error crítico de gestión de riesgos.

Es cierto que Endesa (`ELE.MC`) presenta una sólida generación de caja libre de 2.207 millones de euros al cierre de 2025 y un endeudamiento controlado con una ratio de deuda neta sobre EBITDA de 2,10x. Sin embargo, apelar ciegamente al rendimiento anual del 47,39% y a un precio de cotización actual de 43,74 EUR ignorando los fundamentos de valoración es una imprudencia inaceptable. ¿Cómo podemos justificar ignorar que el precio de mercado actual se encuentra un 15,67% por encima del precio objetivo medio de consenso de los analistas, fijado en 36,89 EUR? El consenso de 23 expertos refleja claramente que el valor actual descuenta en exceso las buenas noticias y se encuentra sobreextendido. 

Asimismo, defender un PER adelantado de 18,07x y un ratio Precio/Valor en Libros de 5,70x bajo la premisa de que "hay que arriesgar para ganar" pone de manifiesto una desconexión total con la realidad del riesgo de reversión a la media. Aunque el valor se mantenga por encima de su media móvil de 200 sesiones (38,95 EUR), un RSI de 14 períodos en 51,71 y un MACD ligeramente negativo (-0,03) apuntan a una clara fatiga en el impulso alcista a corto plazo, con un drawdown actual del -4,89% desde máximos que evidencia la fragilidad de esos niveles.

Aferrarse a un dividendo a cuenta de 0,50 euros por acción previsto para el 12 de enero de 2027 no compensa el riesgo de corrección de una acción que cotiza muy por encima de su valor fundamental de consenso, especialmente en un entorno macroeconómico donde la inflación en la Eurozona sigue en el 4,1% y la volatilidad histórica del título ronda el 19,79%. Exponer un 3% de la cartera a este nivel de sobrevaloración técnica y fundamental expone a la firma a un retroceso injustificado. La prudencia exige asegurar beneficios y mantener una postura de estricta protección de activos.

Rating: REVIEW

FINAL TRANSACTION PROPOSAL: SELL

### Neutral Analyst

Neutral Analyst: He estado escuchando atentamente tanto al analista agresivo como al conservador, y creo que ambos caen en extremos que no hacen justicia a la realidad actual de Endesa (`ELE.MC`). 

Por un lado, el analista agresivo tacha de cobarde la cautela y descarta los riesgos de valoración basándose únicamente en el impulso alcista y en el dividendo. Es cierto que la compañía muestra una salud operativa envidiable, con un flujo de caja libre de 2.207 millones de euros al cierre de 2025 y una deuda neta sobre EBITDA muy controlada en 2,10x. Sin embargo, ignorar que la acción cotiza a 43,74 EUR —un 15,67% por encima del precio objetivo medio de consenso de los analistas de 36,89 EUR— y pretender que un PER adelantado de 18,07x y un P/B de 5,70x no importan es una postura temeraria que ignora el riesgo evidente de una reversión a la media.

Por otro lado, el analista conservador se aferra al miedo a la sobrevaloración para exigir una venta precipitada, pero minimiza la fortaleza estructural de fondo que sostiene a la compañía. Descartar el dividendo a cuenta de 0,50 euros por acción que se pagará el próximo 12 de enero de 2027 y calificar de inaceptable mantener una exposición hipotética del 3% en un líder regulado del sector eléctrico es caer en una parálisis defensiva. El RSI de 14 períodos en 51,71 y la posición de la cotización holgadamente por encima de su media móvil de 200 sesiones (38,95 EUR) demuestran que no estamos ante una burbuja inminente, sino ante un valor consolidando tras un rally anual del 47,39%.

La perspectiva verdaderamente equilibrada y moderada nos enseña que no hay que elegir entre la euforia ciega y el pánico defensivo. Una estrategia sensata y sostenible no requiere liquidar de inmediato la posición ni asumir un riesgo desmedido, sino gestionar la asignación con prudencia y paciencia táctica. Dado que el precio de mercado supera el consenso de analistas y muestra una ligera fatiga técnica a corto plazo con el MACD en terreno negativo, lo más razonable es adoptar una postura de revisión y mantenimiento selectivo, protegiendo los beneficios acumulados sin deshacerse prematuramente de un activo con sólidos fundamentales operativos y un atractivo dividendo en el horizonte.

Rating: REVIEW

FINAL TRANSACTION PROPOSAL: HOLD

## V. Portfolio Manager Decision

### Portfolio Manager
**Rating**: Underweight

**Executive Summary**: Se recomienda reducir la exposición actual en ELE.MC para asegurar beneficios tras el rally anual del 47,39%. El precio actual de 43,74 EUR supera en un 15,67% el precio objetivo medio de consenso (36,89 EUR), lo que indica una valoración estirada con un PER forward de 18,07x y un ratio P/B de 5,70x, aconsejando limitar la asignación a un 3% o menos.

**Investment Thesis**: La tesis bajista y de cautela se impone fundamentada en la clara divergencia entre la cotización actual y el valor fundamental de consenso. Aunque el analista agresivo destaca la sólida generación de flujo de caja libre (2.207 millones de EUR) y la atractiva retribución al accionista con el dividendo de 0,50 EUR previsto para enero de 2027, el analista conservador y el neutral evidencian que el precio de 43,74 EUR descuenta en exceso las buenas noticias. Con un PER adelantado de 18,07x, un ratio P/B de 5,70x y un MACD ligeramente negativo que apunta a fatiga en el impulso, el riesgo de una reversión a la media hacia la media móvil de 200 sesiones (38,95 EUR) supera el potencial de ganancia a corto plazo. La tesis cambiaría si se produce una mejora drástica en el crecimiento de los beneficios o una corrección técnica saludable que alinee la valoración con los objetivos de los analistas.

**Price Target**: 36.89

**Time Horizon**: 3-6 meses