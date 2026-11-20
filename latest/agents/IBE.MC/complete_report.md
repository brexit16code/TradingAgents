# Trading Analysis Report: IBE.MC

- Analysis date: 2026-11-20
- Rating: Hold
- Generated: 2026-11-20 21:17:08
- TradingAgents 0.7.1: google, deep gemini-3.5-flash-lite, quick gemini-3.5-flash-lite
- Analysts: market, news, fundamentals; research debate rounds 1, risk debate rounds 1
- Data vendors: core_stock_apis yfinance, technical_indicators yfinance, fundamental_data yfinance, news_data yfinance, macro_data fred, prediction_markets polymarket, get_news ibex_sample, get_global_news ibex_sample

## I. Analyst Team Reports

### Market Analyst
**Rating**: HOLD
**FINAL TRANSACTION PROPOSAL**: Mantenimiento de posición (HOLD) en niveles de máximos históricos, vigilando la zona de soporte clave de la media móvil de 50 sesiones y gestionando el riesgo ante un PER relativo elevado frente a peers.

---

### Informe de Análisis Técnico y Fundamental: Iberdrola (`IBE.MC`)

#### 1. Contexto de Mercado y Datos Fundamentales
A fecha de 20 de noviembre de 2026, la compañía energética española **Iberdrola, S.A.** (`IBE.MC`), cotizada en las Bolsas de Madrid (MCE) dentro del sector de Utilities diversificadas, muestra una capitalización bursátil de aproximadamente **150.486 millones de euros** (con referencias recientes en prensa situándola por encima de los 158.000 millones en máximos históricos de noviembre de 2026). La acción cotiza a un precio de cierre de **22,67 EUR**.

*   **Valoración y Múltiplos:** El PER histórico (*trailing PE*) se sitúa en **30.64x**, mientras que el PER estimado a futuro (*forward PE*) desciende a **20.36x**, apoyado en un beneficio por acción (*forward EPS*) estimado de 1,11 EUR. El ratio *Enterprise Value to EBITDA* (EV/EBITDA) se encuentra en **14.90x**. 
*   **Comparativa Sectorial (Peer Comparison):** Según el análisis de valoración relativa proporcionado, el PER adelantado de `IBE.MC` muestra un ratio respecto a la mediana del sector (*peer median forward PE* de 16.87x) de **1.21**, lo que indica que cotiza con una prima de valoración superior (*PER relativo superior*) frente a sus comparables en el mercado español (tales como Endesa, Naturgy, Redia, etc.).
*   **Solvencia y Dividendos:** La compañía presenta una deuda total de 63.837 millones de euros (una deuda neta sobre EBITDA de **3.95x**). Ofrece una rentabilidad por dividendo (*dividend yield*) del **3,01%** (con un dividendo anual de 0,68 EUR por acción y un *payout ratio* del 87,06%).
*   **Consenso de Analistas:** El precio objetivo medio de consenso se sitúa en **21,57 EUR** (con un rango entre 18,00 EUR y 26,00 EUR basado en 24 opiniones de analistas), lo que representa una ligera corrección potencial implícita (*consensus downside*) del **-4,86%** respecto al precio de cotización actual de 22,67 EUR.

---

#### 2. Análisis Técnico e Indicadores de Momento
La acción de `IBE.MC` mantiene una estructura alcista de medio y largo plazo muy sólida, respaldada por la siguiente evidencia técnica recogida en el snapshot verificado a 20 de noviembre de 2026:

*   **Tendencia de Mediano y Largo Plazo:** El precio de cierre (22,67 EUR) se mantiene cómodamente por encima de sus principales medias móviles:
    *   **SMA 20:** 22,64 EUR
    *   **SMA 50:** 21,58 EUR (actúa como soporte dinámico intermedio)
    *   **SMA 200:** 20,32 EUR (confirma la tendencia alcista estructural de fondo)
*   **Momento y Osciladores:**
    *   **RSI (14 periodos):** Se sitúa en **55,68**, una lectura neutral-alcista que descarta condiciones de sobrecompra extrema (por encima de 70) a pesar de las recientes cotas récord, dejando margen operativo.
    *   **MACD:** Se sitúa en **0,38** con su línea de señal (*macd_signal*) en **0,45**, mostrando un ligero tono plano o de consolidación a corto plazo tras las subidas.
*   **Volatilidad y Drawdown:** La volatilidad anualizada a 511 sesiones se sitúa en un moderado **15,09%**, mientras que el retroceso desde máximos (*drawdown_pct*) es de apenas un **-4,35%**, lo que refleja una baja fricción bajista y una alta resiliencia en la cotización.
*   **Rentabilidades Históricas:** Acumula una rentabilidad a 21 sesiones (*return21_pct*) del **+4,28%**, a 63 sesiones (*return63_pct*) del **+12,62%** (con un rendimiento relativo positivo frente al índice de referencia *^IBEX* de +18,52 pp), y a 252 sesiones (*return252_pct*) del **+29,99%**.

---

#### 3. Evidencia de Noticias y Contexto Macroeconómico
*   **Hitos Bursátiles:** Durante la primera quincena de noviembre de 2026, `IBE.MC` ha registrado máximos históricos consecutivos en bolsa, impulsando su capitalización por encima de los 158.000 millones de euros (según fuentes como *Merca2.es* y *El Periódico de la Energía* del 13 de noviembre de 2026).
*   **Operativa de Insiders:** Se ha reportado actividad de venta por parte de miembros de la directiva (ej. el vicepresidente aprovechando las subidas históricas para realizar operaciones de venta por valor de 2,3 millones de euros, según *Economía Digital* del 15 de noviembre de 2026), un factor a tener en cuenta en zonas de máximos.
*   **Litigios y Riesgos Legales:** Destaca la demanda interpuesta por Repsol contra las principales energéticas del país (Iberdrola, Endesa, Naturgy y Red Eléctrica) por daños relacionados con un apagón (*Radio Intereconomía*, 16 de noviembre de 2026), cuyo impacto fundamental a medio plazo sigue bajo monitorización.
*   **Entorno Macroeconómico:** El contexto general de los mercados europeos sigue condicionado por las perspectivas de los tipos de interés del Banco Central Europeo (BCE) y la evolución de la inflación en la Eurozona a finales de 2026.

---

#### 4. Selección Óptima de Indicadores Técnicos
Para complementar el análisis técnico y de riesgo sin redundancias, se han priorizado los siguientes 8 indicadores clave de la plataforma:
1.  `close_50_sma`: Para identificar la dirección del soporte dinámico a medio plazo.
2.  `close_200_sma`: Como referencia estructural de largo plazo para la confirmación de tendencia.
3.  `rsi`: Para la medición del impulso y control de umbrales de sobrecompra/sobreventa.
4.  `macd`: Para la detección de divergencias y cruces de impulso.
5.  `macds`: Como línea de señal suavizada para validar los cambios del MACD.
6.  `atr`: Para la medición de la volatilidad real orientada al cálculo de stops dinámicos y gestión del riesgo.
7.  `boll_ub`: Para delimitar la banda superior de resistencia en zonas de máximos históricos.
8.  `boll_lb`: Para identificar la banda inferior en caso de correcciones severas de mercado.

---

#### 5. Resumen y Tabla Clave

| Concepto Clave | Valor / Dato | Implicación para el Inversor |
| :--- | :--- | :--- |
| **Precio Actual (`close`)** | 22,67 EUR | Cotización en zona de máximos históricos recientes. |
| **Tendencia (SMA 50 / 200)** | 21,58 EUR / 20,32 EUR | Estructura alcista intacta; el precio cot

### News Analyst
**Reporte de Investigación Financiera y Macroeconómica**

**Instrumento:** `IBE.MC` (Iberdrola, S.A.)  
**Fecha del reporte:** 20 de noviembre de 2026  
**Identidad resuelta:** Iberdrola, S.A. | Utilidades / Servicios Públicos Diversificados | Bolsa de Madrid (MCE) en EUR, benchmark `^IBEX`.  

---

### 1. Resumen Ejecutivo y Estado Actual de Mercado
Iberdrola (`IBE.MC`) cotiza a **22.67 EUR** por acción a fecha de 20 de noviembre de 2026, mostrando una ligera variación positiva reciente (cambio de +0.35%). La compañía se sitúa cerca de sus máximos históricos recientes, habiendo superado una capitalización bursátil de 158.000 millones de euros a mediados de noviembre (la capitalización actual registrada se sitúa en torno a los 150.490 millones de EUR debido a fluctuaciones de mercado). 

El valor presenta un comportamiento técnico fuerte, manteniéndose por encima de sus medias móviles clave (SMA 20 en 22.64 EUR, SMA 50 en 21.58 EUR y SMA 200 en 20.32 EUR), con una rentabilidad a 12 meses (`return252_pct`) del 29.99%. El RSI de 14 sesiones se encuentra neutral en 55.68, lo que indica ausencia de sobrecompra extrema a pesar de la reciente racha alcista.

### 2. Fundamentos Financieros y Valoración
Los datos fundamentales extraídos de los estados financieros muestran un desempeño sólido:
- **Ingresos (2025):** 44.076 millones de EUR (comparado con 42.988 millones de EUR en 2024 y 49.335 millones de EUR en 2023).
- **EBITDA (2025):** 16.763 millones de EUR (frente a 15.192 millones de EUR en 2024).
- **Beneficio Neto (2025):** 6.285 millones de EUR (incremento desde los 5.612 millones de EUR de 2024 y 4.803 millones de EUR de 2023).
- **Ratio PER (Trailing PE):** 30.64x, mientras que el PER Adelantado (Forward PE) se sitúa en 20.36x, reflejando una expectativa de crecimiento de beneficios por acción (`forwardEps` estimado en 1.11 EUR).
- **Deuda y Solvencia:** Deuda total de 63.840 millones de EUR (con una deuda neta sobre EBITDA de aproximadamente 3.95x) y un efectivo total de 6.634 millones de EUR. El total de activos asciende a 160.762 millones de EUR al cierre de 2025.
- **Dividendo:** Ofrece un dividendo por acción de 0.68 EUR, lo que representa una rentabilidad por dividendo (*dividend yield*) de aproximadamente el 3.00%, con un ratio de pago (*payout ratio*) del 87.06%.

### 3. Contexto Macroeconómico y Noticias Recientes
El panorama macroeconómico en la Eurozona se mantiene bajo la lupa de los inversores ante los movimientos de política monetaria del Banco Central Europeo (BCE). A mediados de noviembre de 2026, la atención se centra en la evolución de los tipos de interés reales, la emisión de deuda de los hogares (letras) y las perspectivas de los tipos para 2026-2027.

En el ámbito corporativo y de noticias recientes para `IBE.MC`:
- **Máximos históricos:** A mediados de noviembre (13 de noviembre de 2026), `IBE.MC` marcó máximos históricos bursátiles superando los 158.000 millones de euros de capitalización ("Iberdrola marca nuevos máximos históricos en Bolsa", *Merca2.es* / *El Periódico de la Energía*).
- **Venta de acciones por directivos:** El vicepresidente de Iberdrola aprovechó la subida histórica en bolsa para realizar ventas de acciones por valor de 2,3 millones de euros (*Economía Digital*, 15 de noviembre de 2026).
- **Litigios y sector:** Destaca la demanda interpuesta por Repsol contra Iberdrola, Endesa, Naturgy y Red Eléctrica en relación con los daños del apagón (*Radio Intereconomía*, 16 de noviembre de 2026). Asimismo, el valor experimentó una ligera recogida de beneficios que lo llevó a perder momentáneamente la cota psicológica de los 20.000 puntos del Ibex 35 junto a Solaria (*Yahoo Finanzas*, 16 de noviembre de 2026).

### 4. Consenso de Analistas y Missing Data
- **Precio Objetivo Consenso:** El precio objetivo medio de los analistas (`targetMeanPrice`) es de **21.57 EUR**, con un rango que va desde los 18.00 EUR (*targetLowPrice*) hasta los 26.00 EUR (*targetHighPrice*), basado en la opinión de 24 analistas. 
- Dado el precio actual de mercado de 22.67 EUR, el potencial de retorno implícito según el consenso (*consensus upside pct*) es de aproximadamente **-4.86%**, lo que sugiere que la acción cotiza ligeramente por encima de la valoración media de los analistas tras su reciente rally alcista.
- **Datos faltantes:** No se dispone en la instantánea actual de flujos de caja operativos (*operating cash flow*) ni flujos de caja libre (*free cash flow*) formalmente actualizados para el último periodo en las métricas resumidas de flujo de caja, aunque se cuenta con los datos de los estados anuales cerrados de 2025 (donde el FCF reportado fue de 3.317 millones de EUR).

---

### Tabla Resumen de Puntos Clave

| Categoría | Métrica / Dato Clave | Valor / Detalle | Fuente / Referencia |
| :--- | :--- | :--- | :--- |
| **Precio y Técnica** | Precio de Cierre (`IBE.MC`) | 22.67 EUR (+0.35%) | Yahoo Finance (`IBE.MC`), 2026-11-20 |
| **Técnica** | Medias Móviles (SMA 20 / 50 / 200) | 22.64 / 21.58 / 20.32 EUR | Datos técnicos internos, 2026-11-20 |
| **Valoración** | Capitalización Bursátil | ~150.490 millones de EUR | Datos fundamentales, 2026-11-20 |
| **Valoración** | PER / Forward PER | 30.64x / 20.36x | Datos fundamentales, 2026-11-20 |
| **Rentabilidad** | Dividend Yield / Dividendo | ~3.00% / 0.68 EUR | Datos fundamentales, 2026-11-20 |
| **Consenso** | Precio Objetivo Medio (Mean Target) | 21.57 EUR (Upside: -4.86%) | 24 analistas, Yahoo Finance |
| **Fundamental** | Ingresos / EBITDA / Net Income (2025) | 44.076M / 16.763M / 6.285M EUR | Estados Financieros anuales 2025 |
| **Noticias** | Máximos Históricos | Capitalización

### Fundamentals Analyst
**Análisis Fundamental Exhaustivo y Perspectivas de Inversión – Iberdrola, S.A. (`IBE.MC`)**

Fecha de referencia: 20 de noviembre de 2026.

---

### 1. Perfil de la Empresa y Contexto de Negocio
**Iberdrola, S.A. (`IBE.MC`)** es una compañía energética global de referencia, líder en el sector de **Utilities (Utilities - Diversified)** y uno de los mayores productores de energía renovable del mundo. Con sede en España y cotizando en la Bolsa de Madrid (integrada en el selectivo principal `^IBEX`), la compañía destaca por su sólida posición en redes de distribución eléctrica, generación verde (solar, eólica terrestre y marina) y soluciones comerciales para clientes en Europa, Estados Unidos, América Latina y el Reino Unido.

---

### 2. Análisis Financiero y Evolución Histórica

Basado en los estados financieros consolidados de la compañía (cifras expresadas en EUR):

#### A. Cuenta de Resultados (Income Statement)
* **Ingresos Totales (Total Revenue):**
  * Ejercicio 2023: 49.335 millones de EUR.
  * Ejercicio 2024: 42.988 millones de EUR.
  * Ejercicio 2025: 44.076 millones de EUR (muestra una recuperación y crecimiento interanual de los ingresos del orden del +15,9% en el último tramo reportado).
* **EBITDA:**
  * Ejercicio 2023: 14.906 millones de EUR.
  * Ejercicio 2024: 15.192 millones de EUR.
  * Ejercicio 2025: 16.763 millones de EUR.
* **Beneficio Neto (Net Income):**
  * Ejercicio 2023: 4.803 millones de EUR.
  * Ejercicio 2024: 5.612 millones de EUR.
  * Ejercicio 2025: 6.285 millones de EUR.

#### B. Balance de Situación (Balance Sheet)
* **Activos Totales:** Evolución positiva desde los 150.033 millones de EUR (2023) hasta los 160.762 millones de EUR al cierre de 2025.
* **Deuda Total (Total Debt):** 
  * 2023: 61.646 millones de EUR.
  * 2024: 57.731 millones de EUR.
  * 2025: 57.231 millones de EUR (el ratio de deuda financiera neta sobre EBITDA se sitúa en torno a **3,95x**, un nivel razonable y manejable para una utility intensiva en capital).
* **Patrimonio Neto (Stockholders Equity):** Ha mostrado un crecimiento sostenido, pasando de 43.111 millones de EUR en 2023 a 50.068 millones de EUR al cierre de 2025.

#### C. Flujo de Caja (Cash Flow)
* **Flujo de Caja Operativo (Operating Cash Flow):** 12.130 millones de EUR (2023), 11.925 millones de EUR (2024) y 11.635 millones de EUR (2025).
* **Inversión en CapEx (Capital Expenditure):** 7.877 millones de EUR (2023), 8.375 millones de EUR (2024) y 8.318 millones de EUR (2025).
* **Flujo de Caja Libre (Free Cash Flow):** 4.253 millones de EUR (2023), 3.550 millones de EUR (2024) y 3.317 millones de EUR (2025), reflejando una sólida capacidad de generación de caja a pesar del fuerte ritmo inversor en transición energética.

---

### 3. Valoración y Métricas de Mercado Actuales (`IBE.MC`)

* **Capitalización Bursátil:** 150.486,7 millones de EUR.
* **Precio de Cotización:** 22,67 EUR (con fecha de precio a 20 de noviembre de 2026).
* **Múltiplos de Valoración:**
  * **PER Histórico (Trailing P/E):** 30,64x.
  * **PER Estimado (Forward P/E):** 20,36x (basado en un EPS estimado de 1,11 EUR).
  * **Ratio Precio/Valor en Libros (Price-to-Book):** 2,93x.
  * **EV/EBITDA:** 14,90x.
* **Valoración Relativa Sectorial:** El ratio frente a la mediana de PER adelantado del sector de peers en España (`ANE.MC`, `ENG.MC`, `ELE.MC`, `NTGY.MC`, `RED.MC`, `SLR.MC`) se sitúa en **1,21x**, lo que indica que `IBE.MC` cotiza con prima frente a sus comparables domésticos debido a su diversificación geográfica y perfil de crecimiento superior.
* **Política de Retribución al Accionista:**
  * **Rentabilidad por Dividendo (Dividend Yield):** ~3,00% (con un dividendo anual de 0,68 EUR por acción y un ratio de pago o *payout ratio* del 87,06%).
* **Consenso de Analistas:**
  * Precio objetivo medio (*Target Mean Price*): 21,57 EUR (con un rango entre un mínimo de 18,00 EUR y un máximo de 26,00 EUR basado en 29 opiniones de analistas). Esto implica una ligera corrección teórica a corto plazo de **-4,86%** respecto al precio actual de 22,67 EUR.

---

### 4. Datos Técnicos y Contexto Reciente

* **Momentum Técnico:** `IBE.MC` cotiza cerca de sus máximos históricos, habiendo superado recientemente los 158.000 millones de capitalización de mercado en sesiones previas a mediados de noviembre de 2026. 
* **Medias Móviles:** Las medias móviles simples muestran una clara tendencia alcista de medio y largo plazo (SMA20 en 22,64 EUR, SMA50 en 21,58 EUR y SMA200 en 20,32 EUR). El RSI de 14 sesiones se sitúa en 55,68 (zona neutral-favorable sin sobrecompra extrema).
* **Noticias y Eventos Recientes:**
  * Se han registrado operaciones corporativas internas de venta de acciones por parte de miembros directivos (ej. vicepresidente aprovechando los máximos históricos en bolsa para realizar ventas por valor de 2,3 millones de euros).
  * En el ámbito legal y de mercado, la compañía figura en noticias recientes relativas a demandas cruzadas en el sector energético español (como la interpuesta por Repsol a grandes energéticas por incidencias de apagones). No obstante, el impacto fundamental de estos litigios a corto plazo es limitado frente a la marcha operativa del negocio regulado y renovable.

---

### 5. Datos Faltantes y Limitaciones
* No se dispone de las estimaciones detalladas de desgloses geográficos específicos para los trimestres avanzados de 2026 más allá de los cierres consolidados anuales hasta 2025 y las previsiones de consenso general.

---

### 6. Conclusión y Recomendación para Traders

`IBE.MC` presenta unos fundamentos excelentes, una generación de caja operativa superior a los 11.000 millones de euros anuales

## II. Research Team Decision

### Bull Researcher

Bull Analyst: **Rating**: HOLD
**FINAL TRANSACTION PROPOSAL**: Mantenimiento táctico en zonas de máximos históricos, priorizando la resiliencia del modelo de redes reguladas y renovables frente a valoraciones exigentes de corto plazo.

---

¡Hola, compañero! Entiendo perfectamente que el oso mire con recelo los gráficos actuales de **IBE.MC**. Es innegable que estamos hablando de niveles muy exigentes: la acción cotiza en **22,67 EUR**, rozando los máximos históricos alcanzados en noviembre de 2026 y superando los 150.000 millones de euros de capitalización bursátil. Sé que el argumento bajista se apoya en que el consenso de analistas marca un precio objetivo medio en los **21,57 EUR** (lo que implica un *consensus downside* teórico de algo más del -4%), y que ver al vicepresidente realizando ventas de acciones por 2,3 millones de euros en máximos puede encender alguna que otra señal de alarma. 

Sin embargo, limitarse a ver el vaso medio vacío por el simple hecho de que `IBE.MC` esté batiendo récords es ignorar la calidad intrínseca y la brutal escalabilidad que justifican esa prima de valoración. ¡Vamos a desglosarlo con datos firmes!

### 1. Crecimiento Real y Solidez Financiera: Cifras que Silencian al Oso
El argumento de que la compañía está estancada se cae por su propio peso al revisar los estados financieros consolidados. ¿De verdad podemos hablar de debilidad cuando el **Beneficio Neto de 2025 cerró en 6.285 millones de EUR**, escalando fuertemente desde los 5.612 millones de 2024 y los 4.803 millones de 2023? Estamos ante un crecimiento compuesto de los beneficios envidiable para una *utility*. 

Además, la capacidad de generación de caja operativa se mantiene blindada por encima de los **11.600 millones de EUR** anuales (11.635 millones al cierre de 2025), soportando un plan de inversiones (*CapEx*) de más de 8.300 millones destinados a la transición energética y redes inteligentes. La ratio de deuda neta sobre EBITDA se sitúa en un prudente **3,95x**, un nivel perfectamente manejable para un gigante con un balance total superior a los 160.700 millones de EUR. El oso grita que el PER *trailing* está alto en **30.64x**, pero olvida mirar el **PER adelantado (*forward PE*)**, que se contrae hasta los **20.36x** gracias al dinamismo de sus beneficios estimados (`forwardEps` de 1,11 EUR).

### 2. Ventajas Competitivas inexpugnables
¿Por qué cotiza `IBE.MC` con un PER relativo superior (un ratio de 1.21x frente a la mediana de sus comparables sectoriales)? Simple y llanamente porque Iberdrola no es una utility convencional. Su diversificación geográfica masiva (con posiciones dominantes en el Reino Unido, Estados Unidos, Brasil y España) y su apuesta pionera por las redes reguladas le otorgan unos flujos de caja predecibles y protegidos frente a la volatilidad macroeconómica. 

Mientras los competidores sufren para mantener márgenes en entornos de transición convulsa, el liderazgo indiscutible de Iberdrola en renovables y redes inteligentes actúa como un foso defensivo (*moat*) impenetrable. Las noticias sobre litigios puntuales, como la demanda de Repsol por el apagón, son ruido puramente coyuntural que no daña la estructura de contratos regulados a largo plazo.

### 3. Positivos Indicadores Técnicos y de Mercado
El mercado habla con contundencia a través de los precios. Lejos de mostrar un agotamiento bajista, la estructura técnica de `IBE.MC` es una obra de arte alcista:
* Cotiza holgadamente por encima de su **SMA 50 (21,58 EUR)** y de su **SMA 200 (20,32 EUR)**.
* El RSI de 14 sesiones está en unos equilibrados **55,68**, lo que demuestra que **no hay sobrecompra extrema**, dejando un amplio colchón para que el impulso continúe.
* Su rentabilidad acumulada a 252 sesiones roza el **+30%**, batiendo de manera sistemática al índice de referencia (`^IBEX`) con un diferencial positivo superior a los 18 puntos porcentuales en el medio plazo.

### En Resumen: ¿Por qué el Toro gana esta partida?
Compañero oso, entiendo tu cautela ante la cercanía de los máximos históricos y la reciente venta de *insiders* (algo perfectamente normal para diversificar patrimonios personales tras un rally brillante). Pero basar una tesis bajista en el retroceso hacia el precio objetivo del consenso es ignorar que los objetivos de los analistas suelen ir por detrás de la curva en mercados alcistas sólidos. 

Iberdrola ofrece un dividendo fiable (rentabilidad del **3,01%** con un dividendo de 0.68 EUR) respaldado por un crecimiento real de doble dígito en su beneficio neto histórico. No estamos ante una burbuja especulativa, sino ante un valor refugio de máxima calidad industrial que justifica cada céntimo de su cotización actual. ¡El toro sigue mandando en `IBE.MC`!

### Bear Researcher

Bear Analyst: **Rating**: REDUCE
**FINAL TRANSACTION PROPOSAL**: Reducción de exposición y toma de beneficios en `IBE.MC` ante una valoración sobre extendida (PER de 30.64x y prima sectorial), un potencial de retorno negativo frente al consenso de analistas y crecientes riesgos regulatorios y de litigio.

---

¡Hola, compañero! Admiro el optimismo con el que defiendes el "súper estatus" de `IBE.MC`, pero estás intentando tapar el sol con un dedo. Es muy bonito enumerar los máximos históricos en los que se mueve la acción a **22,67 EUR** y aplaudir el volumen de beneficios, pero los árboles no crecen hasta el cielo. Agarrarse a que el PER adelantado baja a **20.36x** es un ejercicio de fe en unas estimaciones de beneficios que el propio mercado empieza a cuestionar. 

Vamos a desmontar poco a poco ese castillo de naipes que has montado, porque los números fríos y la realidad de los riesgos operativos cuentan una historia muy diferente.

### 1. ¿Calidad indiscutible o burbuja de valoración por sobreprecio?
Me hablas de un crecimiento envidiable y de un beneficio neto de 6.285 millones de euros para 2025. ¡Perfecto! Pero el mercado ya ha descontado no solo ese crecimiento, sino tres años más de perfección operativa. Un **PER histórico (*trailing PE*) de 30.64x** para una compañía de servicios públicos (*utility*) es sencillamente disparatado. Estás pagando múltiplos de empresa tecnológica de alto crecimiento por un gigante maduro y altamente intensivo en capital.

Además, ignoras el elefante en la habitación: el **consenso de analistas sitúa el precio objetivo medio en 21,57 EUR**, lo que arroja un **potencial de retorno negativo (*consensus downside*) del -4,86%** respecto al precio actual. Los analistas profesionales que cubren el valor ya advierten que `IBE.MC` cotiza por encima de su valor fundamental intrínseco. ¿Y qué me dices de la prima sectorial? Con un ratio de PER relativo frente a sus pares de **1.21x**, Iberdrola está carísima en comparación con otras alternativas del mercado europeo. Cuando una compañía cotiza con tanta prima, cualquier pequeño tropiezo se paga con fuertes correcciones.

### 2. El dinero inteligente (*Insiders*) huye de los máximos
No intentes justificar la reciente venta de acciones del vicepresidente de Iberdrola por valor de 2,3 millones de euros como un simple trámite para "diversificar". Cuando los principales directivos de una corporación aprovechan los máximos históricos para vaciar parte de su cartera, están mandando un mensaje alto y claro al mercado: **el valor actual está caro y es momento de recoger beneficios**. 

A esto hay que sumarle nubarrones operativos y legales que restas importancia con demasiada ligereza. Las noticias recientes sobre la demanda de Repsol contra Iberdrola y otras grandes energéticas por los daños del apagón no son "ruido coyuntural"; abren la puerta a responsabilidades patrimoniales, sanciones regulatorias y un escrutinio político cada vez mayor sobre las grandes eléctricas en España. 

### 3. Fragilidad Financiera y Cargas de Capital
Presumes de una sólida generación de caja operativa, pero olvidas mirar el esfuerzo titánico que exige mantener la maquinaria en marcha. `IBE.MC` arrastra una **deuda total superior a los 63.800 millones de euros** (con una ratio de deuda neta sobre EBITDA de casi **3.95x**). En un entorno macroeconómico donde los tipos de interés de la Eurozona siguen presionando el coste de financiación y las reservas mínimas de los bancos aumentan por la presión del BCE, un perfil de endeudamiento cercano a los 64.000 millones no es moco de pavo. 

Cada euro destinado a cubrir ese pasivo y a financiar un *CapEx* anual superior a los 8.300 millones de euros estrangula la flexibilidad financiera. Y hablando del dividendo, esa modesta **rentabilidad por dividendo del 3,01%** con un *payout* exigente del **87,06%** deja a la compañía con muy poco margen de maniobra si los flujos de caja sufren cualquier contratiempo regulatorio. Con las letras del tesoro y los activos libres de riesgo ofreciendo alternativas atractivas, un 3% mal escaso en máximos históricos no compensa el riesgo de corrección.

### 4. El espejismo técnico: Cuidado con el giro de tendencia
Es cierto que las medias móviles (SMA 50 en 21,58 EUR y SMA 200 en 20,32 EUR) siguen orientadas al alza, y que el RSI en 55,68 no muestra todavía una sobrecompra extrema. Pero los indicadores de impulso son los últimos en enterarse de los cambios de ciclo. Cuando una acción rompe la directriz alcista tras agotar su recorrido en zona de máximos, el retrocorreceso hacia la media de 50 sesiones (o incluso hacia la zona de soporte de los 20 EUR) es rápido y doloroso.

### Conclusión del Oso
Compañero, tu visión de toro está cegada por el brillo de los récords bursátiles de noviembre de 2026. Invertir hoy en `IBE.MC` a 22,67 EUR es comprar en la parte más alta del ciclo, asumiendo una valoración excesiva (PER > 30x), ignorando el aviso de los propios directivos al vender acciones, y pasando por alto un consenso de mercado que ya ve la acción sobrevalorada. 

El riesgo de bajada (*downside*) supera con creces cualquier expectativa optimista de corto plazo. ¡Es hora de ser prudentes, asegurar ganancias y adoptar una postura de reducción de riesgo en este valor!

### Research Manager
**Recommendation**: Hold

**Rationale**: El debate entre el toro y el oso en IBE.MC está fuertemente polarizado por el dilema entre la excelente calidad fundamental de la compañía y su exigente valoración actual en máximos históricos. Por un lado, el toro defiende con acierto el dinamismo operativo de Iberdrola: un crecimiento sólido del beneficio neto (6.285 millones de EUR en 2025), una sólida generación de caja operativa superior a los 11.600 millones de EUR, un PER adelantado que se contrae a unas razonables 20.36x y una robusta estructura técnica que mantiene la cotización holgadamente por encima de sus medias móviles de 50 y 200 sesiones. Por otro lado, el oso argumenta con datos objetivos que la acción cotiza a un PER histórico elevado de 30.64x, superando con creces la mediana sectorial, y que el precio objetivo medio del consenso de analistas (21,57 EUR) implica un potencial de retorno negativo de aproximadamente -4.86% respecto al precio actual de 22,67 EUR, a lo que se suman alertas como la venta reciente de acciones por parte de directivos y una carga de deuda total superior a los 63.800 millones de EUR. Al sopesar ambos argumentos, los riesgos de una valoración sobreextendida y el sesgo negativo frente al consenso neutralizan la fuerte inercia alcista de los fundamentos operativos, impidiendo justificar una recomendación de compra o sobreponderar, pero sin invalidar la calidad de un líder sectorial como para justificar una venta o infraponderación precipitada. Por consiguiente, la evidencia permanece equilibrada, decantando la decisión final hacia un mantenimiento prudente.

**Strategic Actions**: Mantener la asignación actual de la cartera en IBE.MC sin realizar nuevas compras en los niveles de máximos históricos de 22,67 EUR. Se recomienda al operador establecer alertas de precio en la zona de soporte de la media móvil de 50 sesiones (aproximadamente en 21,58 EUR) para evaluar posibles reentradas si el mercado corrige hacia el precio objetivo del consenso, y monitorizar de cerca la evolución del apalancamiento financiero frente al coste de financiación actual.

## III. Trading Team Plan

### Trader
**Action**: Hold

**Reasoning**: La cotizacion de IBE.MC se encuentra en zona de maximos historicos operando a 22.67 EUR, respaldada por una solida tendencia alcista por encima de su media movil de 50 sesiones (21.58 EUR) y un robusto flujo de caja. Sin embargo, su PER historico de 30.64x y su prima frente al sector de utilities, junto con un precio objetivo de consenso inferior en 21.57 EUR, limitan el potencial alcista a corto plazo. Ante este equilibrio entre fortaleza tecnica y valoracion exigente, se recomienda mantener la posicion actual y evitar nuevas compras en estos niveles.

**Entry Price**: not provided

**Stop Loss**: 21.58

**Position Sizing**: Mantenimiento de la posicion actual en cartera

FINAL TRANSACTION PROPOSAL: **HOLD**

## IV. Risk Management Team Decision

### Aggressive Analyst

Aggressive Analyst: **Rating**: HOLD
FINAL TRANSACTION PROPOSAL: **HOLD**

¡Vaya por delante que mantener la posición en `IBE.MC` en estos niveles es una decisión sensata para consolidar el capital, pero permitidme sacudir un poco el pesimismo de los analistas conservadores y neutrales que solo ven fantasmas donde hay una aparente fortaleza titánica! 

Mientras el sector y la media del mercado miran con recelo que Iberdrola cotice en zona de máximos históricos a 22,67 EUR, con un PER histórico de 30.64x y un precio objetivo de consenso anclado en los 21,57 EUR, la realidad fundamental y técnica nos grita una historia completamente distinta de crecimiento y resiliencia. ¿De verdad os vais a asustar por una prima de valoración del 1.20 frente a unos peers nacionales estancados? ¡Señores, la excelencia se paga! Estamos hablando de un gigante con una capitalización superior a los 150.000 millones de euros, unos ingresos que rozan los 44.076 millones y un EBITDA consolidado de más de 16.700 millones de euros en el último ejercicio completo. ¿Dónde está la burbuja cuando la caja operativa supera los 11.600 millones y se destinan más de 8.300 millones anuales a CapEx en transición energética? 

La postura neutral y conservadora se escuda en el "consenso bajista del -4,86%" y en que el vicepresidente haya vendido 2,3 millones en acciones aprovechando los máximos. ¡Por favor! Que un directivo diversifique puntualmente una minúsculas milésimas de su patrimonio en máximos históricos es pura higiene financiera, no una señal de colapso apocalíptico. ¡Ignoráis por completo que la tendencia es vuestra amiga! El precio está holgadamente por encima de la SMA de 50 sesiones (21,58 EUR) y de una robusta SMA de 200 sesiones en 20,32 EUR. El RSI está en un comodísimo 55,68, lo que demuestra que *no hay sobrecompra extrema*; el mercado tiene un apetito voraz y el motor alcista a 252 sesiones muestra un impresionante +29,99% de rendimiento. 

Decir que hay que frenar las compras solo porque estamos en máximos es el clásico error del inversor mediocre que se pierde el verdadero tramo parabólico de los valores de máxima calidad. Las grandes empresas ganadoras de mercado rompen máximos históricos para marcar nuevos estándares, no para desplomarse. Aunque apoyamos tácticamente mantener la posición actual en cartera para dejar correr los beneficios sin sobreexponer liquidez en este exacto micro-instante, mi visión agresiva os advierte: quedarse al margen o temer una corrección menor por el ruido de litigios sectoriales o ruidos de prensa os va a dejar fuera de la jugada cuando `IBE.MC` rompa con fuerza el techo de los analistas hacia los 26,00 EUR. ¡No subestiméis el poder de la bestia renovable de las utilities globales!

### Conservative Analyst

Conservative Analyst: **Rating**: HOLD

**FINAL TRANSACTION PROPOSAL**: **HOLD**

Colegas, respeto el entusiasmo del analista agresivo por la solidez operativa de Iberdrola, pero calificar de "mediocre" una postura de extrema cautela cuando operamos en zona de máximos históricos es un error imperdonable de gestión de riesgos. Decir que la excelencia siempre se paga por cara que sea pasa por alto que la volatilidad y los múltiplos exigentes castigan con dureza a los inversores en cuanto el entorno macroeconómico cambia de rumbo. 

El analista agresivo resta importancia al PER histórico de 30.64x y a la prima del 21% frente a la mediana de nuestros *peers* del sector, argumentando que la calidad justifica cualquier precio. Olvida que un ratio de valoración tan elevado, combinado con un PER adelantado de 20.36x, deja a `IBE.MC` con un margen de error peligrosamente estrecho. No podemos ignorar que el precio objetivo medio de consenso de los analistas se sitúa en los 21.57 EUR, lo que implica un potencial de corrección teórica del -4.86% respecto al precio actual de 22.67 EUR. Cuando el mercado cotiza por encima de lo que estiman los expertos fundamentales, el riesgo de un reajuste bajista por simple compresión de múltiplos es real e inminente.

Asimismo, restar importancia a la venta de acciones por valor de 2,3 millones de euros por parte de la vicepresidencia aprovechando precisamente estos máximos históricos es una temeridad analítica. Los directivos que conocen la letra pequeña del negocio y los desafíos regulatorios no suelen desinvertir por casualidad justo cuando el valor marca récords bursátiles. A esto sumamos nubes negras en el horizonte legal y sectorial, como la demanda interpuesta por Repsol contra los gigantes energéticos nacionales por los daños derivados del apagón, un factor de riesgo litigioso que los optimistas prefieren barrer bajo la alfombra.

Por último, aunque es cierto que técnicamente el valor se mantiene por encima de la media móvil de 50 sesiones en 21.58 EUR y que el RSI en 55.68 no marca una sobrecompra extrema, apoyarse ciegamente en una rentabilidad anual del 29.99% para justificar nuevas compras o asumir un optimismo desaforado es descuidar la preservación del capital. Los árboles no crecen hasta el cielo. Defender un perfil conservador no significa tener miedo al éxito, sino blindar la cartera frente a correcciones imprevistas en un contexto donde los tipos de interés reales en la Eurozona y la evolución de la política del BCE siguen generando incertidumbre. Mantener la posición actual sin incrementar exposición es la única decisión prudente para proteger el patrimonio de la firma sin exponernos a un giro brusco del mercado.

### Neutral Analyst

Neutral Analyst: **Rating**: HOLD
FINAL TRANSACTION PROPOSAL: **HOLD**

Escuchando las posturas de ambos, queda claro que tanto el analista agresivo como el conservador caen en sesgos evidentes al evaluar a `IBE.MC`. Por un lado, el optimismo desmedido del analista agresivo ignora imprudentemente las señales de advertencia del mercado: desestima el riesgo de una compresión de múltiplos y descarta con demasiada ligereza la venta de títulos por parte de la vicepresidencia en máximos y la presión litigiosa reciente. Las valoraciones importan, y asumir que la calidad exime a un valor de sufrir correcciones por valoración exigente es una receta para el desastre en carteras diversificadas. 

Por otro lado, el analista conservador se refugia en un exceso de cautela que roza el inmovilismo paralizante. Agitar el fantasma de un colapso inminente basándose únicamente en que el precio supera ligeramente el precio objetivo medio de consenso de 21.57 EUR o en que existe un PER histórico de 30.64x ignora la realidad estructural de una compañía que genera más de 16.000 millones de EBITDA y destina más de 8.300 millones anuales a CapEx en transición verde con una sólida cobertura técnica por encima de su media móvil de 50 sesiones en 21.58 EUR. 

Desde una perspectiva analítica neutral, la solución equilibrada no es comprar más de manera agresiva ignorando el riesgo de mercado, ni tampoco vender o entrar en pánico por ruidos corporativos y regulatorios puntuales. La recomendación moderada y sostenible es un mantenimiento estricto de la posición (`HOLD`). Esto permite beneficiarse del sólido momentum alcista de medio plazo y de la estabilidad de la compañía sin sobreexponer capital a múltiplos exigentes, utilizando la media móvil de 50 sesiones como un límite disciplinado de gestión de riesgos para proteger los beneficios acumulados sin sacrificar la exposición a uno de los líderes globales de las utilities.

## V. Portfolio Manager Decision

### Portfolio Manager
**Rating**: Hold

**Executive Summary**: Se recomienda mantener la posicion actual en IBE.MC sin realizar nuevas compras en la zona de maximos historicos de 22.67 EUR. La estrategia se basa en proteger el capital existente utilizando un stop loss dinamico alineado con la media movil de 50 sesiones en 21.58 EUR, esperando una correccion hacia el objetivo de consenso para evaluar futuras entradas.

**Investment Thesis**: El analisis detallado de la deuda, la valoracion y el debate entre analistas revela una situacion de equilibrio donde la excelente calidad fundamental y la solidez operativa de Iberdrola (EBITDA superior a 16.000 millones de EUR y caja operativa de mas de 11.600 millones) se ven contrarrestadas por una valoracion exigente. Con un PER historico de 30.64x, una prima sectorial del 20.6% y un precio objetivo medio de consenso en 21.57 EUR que se situa ligeramente por debajo de la cotizacion actual, el margen de seguridad a corto plazo es limitado. Adicionalmente, factores como la venta de acciones por parte de la vicepresidencia en maximos y los riesgos derivados de litigios sectoriales neutralizan la fuerte inercia tecnica alcista por encima de las medias moviles. Esta balanza equilibrada de argumentos justifica mantener la exposicion actual sin incurrir en compras precipitadas ni ventas inmotivadas.

**Price Target**: 21.57

**Time Horizon**: 3-6 months