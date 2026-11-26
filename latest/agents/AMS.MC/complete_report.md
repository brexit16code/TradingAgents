# Trading Analysis Report: AMS.MC

- Analysis date: 2026-11-26
- Rating: Overweight
- Generated: 2026-11-26 21:07:33
- TradingAgents 0.7.1: google, deep gemini-3.5-flash-lite, quick gemini-3.5-flash-lite
- Analysts: market, news, fundamentals; research debate rounds 1, risk debate rounds 1
- Data vendors: core_stock_apis yfinance, technical_indicators yfinance, fundamental_data yfinance, news_data yfinance, macro_data fred, prediction_markets polymarket, get_news ibex_sample, get_global_news ibex_sample

## I. Analyst Team Reports

### Market Analyst
**Rating**: HOLD  

### Análisis Integral de Amadeus IT Group, S.A. (`AMS.MC`)

#### 1. Contexto de Mercado y Entorno Macroeconómico
A fecha de 26 de noviembre de 2026, el valor cotiza en la bolsa de Madrid (`AMS.MC`) bajo el ticker correspondiente en el sector de Tecnología / Servicios de Tecnologías de la Información. Las bolsas europeas muestran un comportamiento alcista impulsado por el sector financiero y tecnológico, con el Euro Stoxx 50 y el DAX alemán avanzando más de un 2% en la sesión (referencia: *el boletin*, 2026-11-26). Paralelamente, el entorno macroeconómico europeo registra un euríbor superando el 3,3% (según *20 Minutos*, 2026-11-26) y la reciente elección de Pablo Hernández de Cos como presidente del Banco Central Europeo (*El Constitucional*, 2026-11-26), lo que mantiene la atención sobre la evolución de los tipos de interés en la Eurozona para finales de 2026 y 2027 (Bankinter).

#### 2. Acción del Precio y Datos Técnicos (`AMS.MC`)
El precio de cierre registrado para `AMS.MC` es de **61,90 EUR** (variación diaria de +1,51%). Las métricas técnicas clave muestran:
- **Medias Móviles Simples (SMA)**: La SMA de 20 periodos se sitúa en 60,69 EUR, la SMA de 50 periodos en 56,75 EUR y la SMA de 200 periodos en 52,96 EUR. La cotización se encuentra por encima de todas ellas, reflejando una estructura alcista sólida a corto, medio y largo plazo.
- **RSI (14)**: Se sitúa en **62,74**, indicando un sesgo alcista moderado sin alcanzar todavía condiciones extremas de sobrecompra (generalmente fijadas por encima de 70).
- **MACD**: El indicador MACD registra un valor de 1,198 frente a su línea de señal (`macds`) de 1,431. Aunque el MACD se mantiene en terreno positivo, la línea principal se sitúa ligeramente por debajo de su señal, sugiriendo un momento de consolidación o desaceleración temporal del impulso reciente.
- **Volatilidad y Retornos**: La volatilidad anualizada se ubica en el 26,05%, con un retorno a 21 sesiones del 9,79% y un retorno a 63 sesiones del 6,32%. El *drawdown* actual es leve (-2,45%).

#### 3. Fundamentales y Valoración Financiera
Con una capitalización de mercado de aproximadamente **26.000 millones de EUR**, los datos fundamentales reflejan la solidez financiera de la compañía:
- **Ingresos y Beneficios**: Los ingresos totales del ejercicio 2025 cerraron en 6.517 millones de EUR (frente a 6.141 millones en 2024 y 5.441 millones en 2023), con un beneficio neto de 1.335,7 millones de EUR (superando los 1.253 millones de 2024). El EBITDA de 2025 alcanzó los 2.534,7 millones de EUR.
- **Múltiplos de Valoración**: 
  - *Trailing P/E*: 19,90x
  - *Forward P/E*: 15,83x
  - *EV/EBITDA*: 11,24x
  - *Price-to-Book*: 5,21x
- **Rentabilidad y Dividendos**: Presenta un rendimiento sobre el capital (ROE) elevado del 26,44% y un margen de beneficio neto del 19,86%. Ofrece una rentabilidad por dividendo (*dividend yield*) estimada en torno al **2,49% - 2,53%**, con un dividendo por acción de 1,54 EUR y un ratio de pago (*payout ratio*) del 49,52%.
- **Deuda**: La deuda neta sobre EBITDA se sitúa en un nivel controlado de 1,03x (Deuda total de 3.500 millones de EUR frente a caja de 913 millones de EUR).
- **Consenso de Analistas**: El precio objetivo medio de consenso se sitúa en **71,47 EUR**, con un rango que oscila entre un mínimo de 53,00 EUR y un máximo de 82,00 EUR (basado en 23 opiniones de analistas), lo que arroja un potencial de revalorización (*consensus upside*) del **15,46%**.

#### 4. Selección de Indicadores Técnicos Recomendados
Siguiendo los criterios metodológicos, se seleccionan los siguientes 8 indicadores complementarios para el seguimiento operativo de `AMS.MC`:
1. `close_50_sma`: Para identificar la dirección del tendencia a medio plazo y actuar como soporte dinámico.
2. `close_200_sma`: Como referencia estructural a largo plazo para confirmar la macro-tendencia.
3. `close_10_ema`: Para capturar cambios rápidos de impulso a corto plazo.
4. `macd`: Para monitorizar la convergencia/divergencia de medias y detectar cambios de ciclo.
5. `macds`: Línea de señal para modular los cruces operativos junto con el MACD.
6. `rsi`: Para vigilar zonas de sobrecompra y sobreventa (70/30).
7. `boll`: Banda media de Bollinger (SMA 20) como referencia central de oscilación de precios.
8. `atr`: Para medir la volatilidad histórica y dimensionar correctamente los niveles de stop-loss.

#### 5. Datos Faltantes y Advertencias
- No se dispone de un desglose detallado de flujos intradía ni de carteras de inversión hipotéticas específicas, por lo que toda asignación mencionada es estrictamente teórica.
- Las fuentes de datos empleadas corresponden estrictamente al snapshot verificado a 2026-11-26 y a las referencias documentales adjuntas (Yahoo Finance / fuentes de noticias sindicadas).

---

### Resumen Clave en Tabla

| Concepto / Métrica | Valor Actual / Referencia | Comentario Analítico |
| :--- | :--- | :--- |
| **Ticker y Mercado** | `AMS.MC` (Bolsa de Madrid, EUR) | Compañía clasificada en Tecnología / IT Services. |
| **Precio de Cierre** | 61,90 EUR (26-11-2026) | Variación positiva diaria de +1,51%. |
| **Tendencia (Medias)** | Por encima de SMA20, SMA50 y SMA200 | Estructura alcista sólida en todos los horizontes temporales. |
| **Momentum (RSI 14)** | 62,74 | Zona alcista moderada, sin sobrecompra crítica. |
| **Valoración (P/E)** | 19,90x (Trailing) / 15,83x (Forward) | Valuación razonable frente a su crecimiento histórico. |
| **Dividendo** | ~2,49% (1,54 EUR por acción) | Payout moderado (~49,52%), sostenible. |
| **Consenso de Analistas** | 71,47 EUR (Objetivo medio) | Potencial alcista estimado del 15,46% respecto al precio actual. |
| **Deuda Neta / EBITDA** | 1,03x | Estructura de endeudamiento saneada y bajo control. |

FINAL TRANSACTION PROPOSAL: HOLD

### News Analyst
**Rating**: HOLD  

### Informe de Investigación y Análisis Macroeconómico - Amadeus IT Group, S.A. (`AMS.MC`)

#### 1. Contexto Macroeconómico y de Mercado
El análisis se sitúa a finales de noviembre de 2026. Durante la semana del 26 de noviembre de 2026, los mercados bursátiles europeos han registrado fuertes subidas impulsados principalmente por el sector bancario y tecnológico (con avances superiores al 2% en índices de referencia como el Euro Stoxx 50 y el DAX alemán). En el ámbito macroeconómico europeo, destaca el nombramiento de Pablo Hernández de Cos como presidente del Banco Central Europeo (BCE), siendo el primer español en asumir este cargo (anunciado el 26 de noviembre de 2026). Por otro lado, el Euríbor superó el umbral del 3,3%, encareciendo los costes hipotecarios y manteniendo un entorno de tipos de interés altos vigilado de cerca por los inversores.

#### 2. Análisis Fundamental y Técnico de `AMS.MC`
- **Identidad y Negocio:** Amadeus IT Group, S.A. (`AMS.MC`), cotizada en la Bolsa de Madrid (MCE) dentro del sector de Tecnología (Information Technology Services).
- **Precio y Datos Técnicos:** A fecha de 26 de noviembre de 2026, la acción cotiza a **61,90 EUR**, registrando una subida diaria del 1,51%. Su RSI de 14 períodos se sitúa en 62,74 (zona neutral-alcista sin sobrecompra extrema), con medias móviles en tendencia positiva (SMA20 en 60,69 EUR, SMA50 en 56,75 EUR y SMA200 en 52,97 EUR). Presenta una volatilidad del 26,05% y un descenso desde máximos recientes (drawdown) del -2,45%.
- **Valoración y Fundamentales:**
  - Capitalización bursátil: ~25.997 millones de EUR.
  - Per Trailing (PE): 19,90x; Forward PE: 15,83x.
  - Ratio Deuda Neta / EBITDA: 1,03x (total debt de ~3.500 millones de EUR frente a un EBITDA de ~2.500 millones de EUR).
  - Crecimiento de ingresos del 6,4% y de beneficios del 9,8%.
  - Rentabilidad por dividendo (*dividend yield*): ~2,49% (con un dividendo ordinario de 1,54 EUR y un *payout ratio* de 49,52%).
  - Consenso de analistas (*Target Mean Price*): 71,47 EUR (con un precio objetivo mínimo de 53,0 EUR y máximo de 82,0 EUR, basado en 23 opiniones de analistas), lo que implica un potencial alcista (*consensus upside*) del **15,46%**.

#### 3. Evidencia de Noticias y Fuentes
- **Noticias Corporativas y de Sector:** Cobertura reciente en Rankia sobre la operativa de acciones de Amadeus y su política de retribución al accionista (23 de noviembre de 2026). 
- **Fuentes:** Datos extraídos de Yahoo Finance (`https://finance.yahoo.com/quote/AMS.MC/`), estados financieros de la compañía y resúmenes de prensa económica de El Boletín, Negocios.com y El Constitucional.

#### 4. Asunciones, Método de Valoración y Datos Faltantes
- **Método de Valoración:** Basado en múltiplos de mercado (Forward PE de ~15,8x, EV/EBITDA de 11,24x) y consenso de analistas de Wall Street/mercado europeo (precio objetivo medio de 71,47 EUR). Los precios objetivo de los analistas constituyen estimaciones de consenso y no valores intrínsecos definitivos.
- **Datos Faltantes:** No se dispone de un desglose detallado pormenorizado de los flujos de caja operativos futuros más allá de los estados históricos cerrados a diciembre de 2025, ni un porfolio de asignación de activos privado (cualquier decisión al respecto es estrictamente hipotética).

| Componente Clave | Métrica / Dato Actual (`AMS.MC`) | Observaciones / Contexto |
| :--- | :--- | :--- |
| **Precio de Cierre** | 61,90 EUR | Cotización a 26 de noviembre de 2026. |
| **Precio Objetivo Medio** | 71,47 EUR | Consenso de analistas (23 opiniones). |
| **Upside de Consenso** | +15,46% | Potencial estimado frente al precio actual. |
| **Forward PE** | 15,83x | Valoración basada en beneficios estimados futuros. |
| **Ratio Deuda Neta / EBITDA** | 1,03x | Estructura de endeudamiento moderada y sana. |
| **Rentabilidad por Dividendo** | ~2,49% | Tasa de dividendo con *payout* del ~49,5%. |

FINAL TRANSACTION PROPOSAL: HOLD

### Fundamentals Analyst
**Rating**: HOLD  
FINAL TRANSACTION PROPOSAL: **HOLD** (Hipótesis analítica sin ejecución de órdenes ni asignación de cartera).

---

### Informe Fundamental Integral: Amadeus IT Group, S.A. (`AMS.MC`)

#### 1. Perfil de la Compañía y Negocio
* **Identidad Resuelta**: Amadeus IT Group, S.A. (`AMS.MC`)
* **Clasificación de Negocio**: Tecnología / Servicios de Tecnologías de la Información (Technology / Information Technology Services).
* **Bolsa de cotización**: Bolsas y Mercados Españoles (MCE - Madrid), cotizando en Euros (EUR) y benchmarked contra el índice `^IBEX`.
* **Resumen de Actividad**: Amadeus opera como un proveedor global de soluciones tecnológicas para la industria del turismo y los viajes. Su modelo de negocio se divide principalmente en distribución (conectando agencias de viajes con proveedores de contenido aéreo, hotelero y de transporte) y en soluciones informáticas para aerolíneas y gestores aeroportuarios (sistemas de servicio a pasajeros o PSS).

#### 2. Análisis de Estados Financieros (Histórico Reciente)
Basado en los datos suministrados correspondientes a los cierres de ejercicio plurianuales (2023, 2024 y 2025):

* **Cuenta de Resultados (Income Statement)**:
  * **Ingresos Totales (Total Revenue)**: Mostraron una trayectoria de crecimiento sostenido. En 2023 se situaron en 5.441,2 millones de euros, escalando en 2024 hasta los 6.141,7 millones de euros y cerrando 2025 con 6.517,0 millones de euros.
  * **EBITDA**: Acompañó la expansión operativa, pasando de 2.134,2 millones de euros en 2023 a 2.353,2 millones de euros en 2024 y alcanzando los 2.534,7 millones de euros en 2025.
  * **Beneficio Neto (Net Income)**: Los beneficios netos escalaron desde los 1.117,6 millones de euros (2023) hasta 1.253,0 millones de euros (2024) y 1.335,7 millones de euros (2025).

* **Balance de Situación (Balance Sheet)**:
  * **Activos Totales**: Se situaron en 10.795,4 millones de euros en 2023, 11.784,3 millones de euros en 2024 y cerraron 2025 en 11.470,9 millones de euros.
  * **Deuda Total (Total Debt)**: Presentó cifras estables o ligeramente decrecientes, registrando 3.308,5 millones de euros en 2023, 3.375,7 millones de euros en 2024 y 3.223,6 millones de euros en 2025 (la instantánea actual sitúa la deuda financiera total en unos 3.500,4 millones de euros frente a una caja de 913,1 millones de euros, resultando en una ratio Deuda Neta/EBITDA de aprox. 1.03x).
  * **Patrimonio Neto (Stockholders Equity)**: Evolución positiva desde los 4.483,4 millones de euros (2023) hasta 5.063,6 millones de euros en 2024, con un registro de 4.853,7 millones de euros al cierre de 2025.

* **Flujo de Caja (Cash Flow)**:
  * **Flujo de Caja Operativo (Operating Cash Flow)**: Creció de forma sólida desde 1.794,9 millones de euros en 2023, a 2.146,0 millones en 2024 y 2.200,9 millones de euros en 2025 (la instantánea de los últimos doce meses refleja 2.211,2 millones de euros).
  * **Inversión de Capital (Capex)**: -600,5 millones de euros en 2023, -788,1 millones en 2024 y -814,6 millones de euros en 2025.
  * **Flujo de Caja Libre (Free Cash Flow)**: 1.194,4 millones de euros en 2023, 1.357,9 millones en 2024 y 1.386,3 millones de euros en 2025 (la instantánea actual muestra 1.106,2 millones de euros).

#### 3. Métricas Financieras y Valoración Actual
* **Precio de Cierre**: 61,90 EUR (fecha de precio: 2026-11-26).
* **Capitalización de Mercado**: ~25.997,5 millones de EUR.
* **PER (Trailing P/E)**: 19.90x; **PER Adelantado (Forward P/E)**: 15.83x.
* **Precio/Valor en Libros (Price to Book)**: 5.21x.
* **Valor de Empresa / EBITDA (EV/EBITDA)**: 11.24x.
* **BPA (EPS Trailing)**: 3,11 EUR; **BPA Estimado (Forward EPS)**: 3,91 EUR.
* **Rentabilidad por Dividendos (Dividend Yield)**: ~2,49% (Dividendo por acción ordinario de 1,54 EUR con un *payout ratio* estimado del 49,52%).
* **Rentabilidad sobre Recursos Propios (ROE)**: 26,44%.
* **Márgenes de Beneficio**: Márgenes netos de explotación estables en torno al 19,86%.
* **Consenso de Analistas (Target Mean Price)**: El precio objetivo medio del consenso se sitúa en **71,47 EUR** (con un rango que va desde un mínimo de 53,00 EUR hasta un máximo de 82,00 EUR a partir de 23 opiniones de analistas), lo que arroja un potencial de revalorización (*consensus upside*) del **15,46%**.

#### 4. Análisis Técnico Breve y Contexto Macroeconómico Reciente
* **Indicadores Técnicos**: RSI de 14 periodos en 62,74 (zona neutral-alcista, sin sobrecompra extrema). Las medias móviles simples muestran una tendencia alcista a medio y largo plazo (SMA 20 en 60,69 EUR, SMA 50 en 56,75 EUR y SMA 200 en 52,96 EUR). El valor experimenta una volatilidad anualizada del 26,05% y acumula un retorno a 21 sesiones del 9,79% y del 6,32% a 63 sesiones.
* **Contexto de Noticias y Mercado (Noviembre de 2026)**: Las bolsas europeas han registrado fuertes subidas impulsadas por sectores como la banca y la tecnología (titulares del 26 de noviembre de 2026). Asimismo, se vigila el entorno macroeconómico europeo con el euríbor superando el 3,3% y el nombramiento de Pablo Hernández de Cos al frente del BCE. En el ámbito local, publicaciones especializadas como Rankia comentan la operativa y evolución de los títulos de Amadeus y el atractivo de su dividendo.

#### 5. Evidencia Faltante y Datos No Disponibles
* No se han suministrado transacciones recientes de iniciadores o información detallada desagregada de pasivos específicos a corto plazo más allá

## II. Research Team Decision

### Bull Researcher

Bull Analyst: ¡Hola a todos! Comprendo que nuestros colegas bajistas prefieran mantenerse cautelosos en este momento, pero mirar a **AMS.MC** sin reconocer el tremendo momento operativo y financiero que atraviesa es ignorar la realidad de un auténtico titán tecnológico global. Como analista alcista, defiendo firmemente que Amadeus IT Group no solo está bien posicionada, sino que ofrece una oportunidad de inversión excepcional en el sector de tecnologías de la información. 

Desglosemos por qué la tesis alcista es infinitamente superior y por qué los temores bajistas simplemente no se sostienen frente a los datos duros:

### 1. Crecimiento Potencial Comprobado y Escalabilidad Global
Mientras algunos intentan pintar un panorama de estancamiento para los gigantes de servicios tecnológicos, los números de **AMS.MC** hablan por sí solos. Cerraremos las dudas viendo los ingresos totales, que escalaron de 5.441 millones de euros en 2023 a unos sólidos **6.517 millones de euros al cierre de 2025**, acompañados por un EBITDA que superó los **2.534 millones de euros**. ¿Hablamos de escalabilidad? Su modelo de distribución global y sus soluciones tecnológicas para aerolíneas (PSS) operan con una infraestructura digital altamente escalable. A medida que el tráfico aéreo global y el turismo continúan su expansión secular, cada transacción adicional genera márgenes operativos extraordinarios sin requerir aumentos proporcionales en costes de estructura. 

### 2. Ventajas Competitivas Imbatibles (Moat)
Amadeus no es una empresa tecnológica más; es la columna vertebral de la industria global de viajes. Su red integrada de agencias de viajes, aerolíneas, hoteles y proveedores de transporte conforma un *network effect* (efecto de red) prácticamente imposible de replicar por competidores emergentes. Cambiar de proveedor tecnológico para una gran aerolínea o red global de agencias implica un riesgo operativo monumental, lo que otorga a **AMS.MC** una **fidelización de clientes envidiable** y barreras de entrada altísimas. ¿Dónde más encontramos una compañía tecnológica en Europa con un ROE (Return on Equity) del **26,44%** y un margen de beneficio neto cercano al **19,86%**? Simplemente juegan en otra liga.

### 3. Indicadores Positivos y Salud Financiera a Prueba de Balas
Frente al ruido macroeconómico europeo —como un Euríbor en torno al 3,3% y la atenta mirada al BCE bajo la presidencia de Pablo Hernández de Cos—, Amadeus demuestra una resiliencia financiera sobresaliente. Su ratio de **Deuda Neta sobre EBITDA se sitúa en un sanísimo 1,03x** (con una deuda total de 3.500 millones frente a una sólida posición de caja y un flujo de caja libre operativo que supera cómodamente los 1.100 millones de euros). 
Además, técnicamente el valor muestra una fortaleza incuestionable: cotiza a **61,90 EUR**, manteniéndose holgadamente por encima de sus medias móviles clave (SMA de 20, 50 y 200 periodos), con un RSI en 62,74 que refleja un sesgo alcista moderado y saludable sin incurrir en excesos de sobrecompra. Y no olvidemos el atractivo para el inversor paciente: un dividendo sostenible de 1,54 EUR por acción (*dividend yield* de ~2,49%) respaldado por un *payout* conservador del 49,52%. 

### 4. Rebatiendo los Argumentos Bajistas
Los osos suelen argumentar que los múltiplos de valoración (como un PER *trailing* de 19,90x) son elevados o que los costes de capital en Europa podrían frenar el consumo en viajes. ¡Pura falacia! Si miramos hacia adelante, el **Forward P/E se comprime hasta un atractivo 15,83x**, lo que demuestra que la compañía está abaratando su valoración a medida que sus beneficios estimados siguen creciendo (con un BPA previsto de 3,91 EUR). 
¿Preocupados por el entorno macro? Los flujos de caja operativos de Amadeus (más de 2.200 millones de euros) y su bajísimo apalancamiento le otorgan una independencia financiera total frente a la volatilidad de los tipos de interés. El mercado lo sabe: el consenso de analistas sitúa el precio objetivo medio en **71,47 EUR**, lo que representa un **potencial alcista (*consensus upside*) del 15,46%** desde los niveles actuales.

En resumen, los argumentos bajistas pecan de miopía cortoplacista. **AMS.MC** combina liderazgo de mercado, rentabilidad sobresaliente, solidez de balance y un potencial de revalorización innegable. 

**Rating**: BUY  
FINAL TRANSACTION PROPOSAL: HOLD

### Bear Researcher

Bear Analyst: ¡Hola colega! Entiendo perfectamente el entusiasmo con el que defiendes a **AMS.MC**, y es fácil dejarse seducir por los titulares rimbombantes sobre la "columna vertebral del turismo global" cuando los mercados europeos celebran subidas generalizadas. Pero levantar la copa y cantar victoria basándose únicamente en el tráfico aéreo pasado y en un par de múltiplos estelares es ignorar las grietas profundas que se están abriendo bajo los pies de Amadeus IT Group. 

Vamos a desmontar punto por punto esa supuesta "invulnerabilidad" y a poner los pies en la tierra con los datos reales que los alcistas prefieren barrer bajo la alfombra:

### 1. ¿Crecimiento secular o burbuja de expectativas?
Presumes alegremente de que los ingresos escalaron hasta los 6.517 millones de euros al cierre de 2025 y que el EBITDA superó los 2.534 millones. Suena de maravilla en un folleto comercial, pero la realidad económica es mucho más fría. Estamos hablando de una tasa de crecimiento de ingresos moderada en un entorno inflacionario donde mantener los márgenes operativos se vuelve un ejercicio de funambulismo. Además, el modelo de negocio de **AMS.MC** está peligrosamente atado a la macroeconomía del ocio y los viajes corporativos. Con un Euríbor que se mantiene por encima del 3,3% y la presión constante sobre los bolsillos de los consumidores europeos, asumir que la expansión del tráfico aéreo va a ser infinita y lineal es un acto de fe ciega, no de análisis financiero.

### 2. El mito del foso inexpugnable (*Moat*) y la vulnerabilidad tecnológica
Hablas de un efecto de red y de una fidelización "envidiable" porque cambiar de proveedor es un engorro operativo. ¡Cuidado con el exceso de confianza! Las grandes aerolíneas y los gigantes del turismo mundial están bajo una presión feroz para recortar costes y modernizar sus infraestructuras digitales de manera ágil. La amenaza de la desintermediación, el avance de las reservas directas y la presión de competidores tecnológicos más ágiles que integran inteligencia artificial y arquitecturas nativas en la nube están erosionando silenciosamente el monopolio histórico de los GDS (Global Distribution Systems). Que el *Price-to-Book* se sitúe en unas exigentes **5,21x** deja muy poco margen de error si la presión competitiva obliga a Amadeus a bajar comisiones o a realizar inversiones masivas en I+D solo para no perder cuota de mercado.

### 3. Salud financiera a prueba de balas... o apalancamiento latente
Es cierto que una ratio de Deuda Neta sobre EBITDA de 1,03x parece razonable sobre el papel, pero no podemos ignorar que la deuda total asciende a unos pesados **3.500 millones de euros** frente a una caja de apenas 913 millones. En un régimen de tipos de interés altos donde el BCE (ahora bajo la batuta de Pablo Hernández de Cos) vigila de cerca la estabilidad monetaria, refinanciar o sostener este nivel de pasivos encarece drásticamente la estructura de capital. Además, aunque el flujo de caja libre sea de unos respetables 1.100 millones de euros, la exigencia de un *Capex* recurrente cercano a los 800 millones limita severamente la flexibilidad financiera para acometer adquisiciones transformadoras o proteger el dividendo si hay un bache en el sector.

### 4. Rebatiendo la trampa del Forward P/E y el espejismo del consenso
Te agarras desesperadamente al *Forward P/E* de **15,83x** y al precio objetivo de consenso de 71,47 EUR para justificar un potencial alcista del 15,46% desde los 61,90 EUR actuales. Pero olvidemos los deseos de los analistas y miremos el gráfico y la realidad operativa. Con un RSI en 62,74, el valor está flirteando peligrosamente con zonas de agotamiento alcista tras un rebote del 9,79% en el último mes. Comprar en estos niveles es pagar una prima injustificada por una compañía cíclica disfrazada de tecnológica pura. Si el consumo en viajes sufre una desaceleración inesperada —algo muy probable si el coste de la vida y las hipotecas siguen apretando en la Eurozona—, esas estimaciones de beneficio por acción (BPA) de 3,91 EUR se desvanecerán rápidamente, y el múltiplo adelantado dejará de parecer tan "atractivo".

En resumen, **AMS.MC** es una excelente compañía, nadie lo niega, pero a estos precios y con un contexto macroeconómico cargado de incertidumbres en tipos y consumo, el perfil de riesgo-recompensa es simplemente desequilibrado. No es momento de comprar euforia; es momento de mantener la prudencia y quedarse al margen.

**Rating**: HOLD  
FINAL TRANSACTION PROPOSAL: HOLD

### Research Manager
**Recommendation**: Overweight

**Rationale**: El debate ha sido riguroso, pero la balanza se inclina claramente del lado alcista. El analista alcista ha demostrado con datos duros la solidez financiera de AMS.MC, destacando un crecimiento de ingresos hasta los 6.517 millones de euros, un EBITDA superior a 2.534 millones, un apalancamiento muy controlado con una deuda neta sobre EBITDA de 1,03x y un atractivo flujo de caja libre operativo que supera los 1.100 millones. Aunque el analista bajista advierte con razón sobre la presión del entorno macroeconómico europeo (con el Euríbor por encima del 3,3%) y los riesgos cíclicos del sector de viajes, sus temores no logran invalidar los sólidos fundamentales de la compañía, su ROE del 26,44% y su resiliencia operativa. El argumento alcista de que el Forward P/E se comprime a un atractivo 15,83x y que el consenso de analistas otorga un potencial alcista del 15,46% hacia los 71,47 EUR pesa más que la cautela defensiva de los osos. No obstante, dado el reciente rebote del 9,79% en 21 días y la proximidad de resistencias técnicas, optamos por una postura constructiva pero gradual de Overweight en lugar de una compra total inmediata.

**Strategic Actions**: Ejecutar una acumulación progresiva de AMS.MC en la zona actual de 61,90 EUR. Se recomienda iniciar la posición con un tramo inicial equivalente al 50% de la asignación estándar prevista para esta idea, reservando el 50% restante para posibles recortes tácticos hacia las medias móviles (SMA de 20 o 50 periodos). Establecer un nivel de vigilancia estricto ante cualquier desaceleración en el tráfico aéreo o variaciones adversas en el entorno de tipos del BCE.

## III. Trading Team Plan

### Trader
**Action**: Buy

**Reasoning**: AMS.MC presenta una estructura técnica alcista sólida encontrándose por encima de sus principales medias móviles y un atractivo potencial de revalorización del 15,46% hacia el objetivo de consenso de 71,47 EUR. Sus sólidos fundamentales, incluyendo un ROE del 26,44%, un apalancamiento controlado con deuda neta/EBITDA de 1,03x y un Forward P/E de 15,83x, justifican una recomendación de compra alineada con el plan de inversión Overweight. Se establece la entrada en el nivel actual de cotización con un stop-loss técnico por debajo de la media móvil de 50 sesiones para gestionar el riesgo de volatilidad a corto plazo.

**Entry Price**: 61.9

**Stop Loss**: 56.5

**Position Sizing**: 5% of portfolio

FINAL TRANSACTION PROPOSAL: **BUY**

## IV. Risk Management Team Decision

### Aggressive Analyst

Aggressive Analyst: ¡Atención todos! Mientras los analistas conservadores y neutrales se quedan parados analizando cada decimal y buscando excusas para quedarse de brazos cruzados, el mercado está ofreciendo una oportunidad de oro que no podemos ignorar. Es el momento de dejar atrás el miedo a la volatilidad y adoptar una estrategia audaz en **AMS.MC** (Amadeus IT Group, S.A.). 

Para empezar, las cifras hablan por sí solas. ¿De verdad van a ignorar un potencial de revalorización del 15,46% hacia el objetivo de consenso de 71,47 EUR respaldado por 23 analistas? Mientras otros dudan, el valor cotiza sólidamente a 61,90 EUR, manteniéndose por encima de sus medias móviles clave (SMA20 en 60,69 EUR, SMA50 en 56,75 EUR y la respetable SMA200 en 52,96 EUR). Esto no es una simple subida efímera; es una estructura técnica alcista robusta respaldada por un retorno a 21 sesiones del 9,79% y un RSI de 62,74 que muestra fuerza compradora pura, sin entrar todavía en peligrosos niveles de sobrecompra.

¿Y qué me dicen de los fundamentales? Nos enfrentamos a un titán tecnológico con un ROE excepcional del 26,44% y unos márgenes netos de casi el 20%. El apalancamiento está perfectamente controlado con una ratio de deuda neta sobre EBITDA de tan solo 1,03x. ¿Temen los tipos de interés o el entorno macroeconómico? Con un flujo de caja libre superior a los 1.100 millones de euros y un Forward P/E sumamente atractivo de 15,83x frente a sus beneficios estimados, la compañía cuenta con el músculo financiero necesario para financiar su crecimiento y superar cualquier turbulencia del Euríbor. 

Adoptar una postura conservadora o neutral en este punto significa perderse el tren del impulso alcista que estamos viendo en las bolsas europeas. Con una entrada ajustada en el nivel actual y un stop-loss técnico perfectamente delimitado por debajo de la media de 50 sesiones en 56,5 EUR, gestionamos el riesgo bajista mientras liberamos todo el potencial alcista de una asignación del 5% de la cartera. ¡Es hora de arriesgar para ganar, aprovechar el momento y apostar decididamente por la compra!

**Rating**: BUY

FINAL TRANSACTION PROPOSAL: **BUY**

### Conservative Analyst

Conservative Analyst: Colegas, entiendo perfectamente la euforia y el impulso que intentan transmitir al defender una compra inmediata en AMS.MC, pero como analista de riesgos, mi deber es mirar más allá de los titulares optimistas y proteger firmemente el capital de la firma ante cualquier vulnerabilidad oculta.

El analista agresivo nos insta a ignorar la cautela y lanzarnos a por ese potencial de revalorización del 15,46% hacia el objetivo de consenso de 71,47 EUR. Sin embargo, confunda el consenso de los analistas con una garantía matemática es un error fundamental. Los precios objetivo son meras estimaciones externas y no valores intrínsecos definitivos. Confiar ciegamente en que el valor alcanzará esos niveles expone a la cartera a correcciones severas si el sentimiento de mercado cambia repentinamente.

Además, se pasa por alto que la volatilidad anualizada de AMS.MC se sitúa en un significativo 26,05%. Aunque el RSI se encuentre en 62,74 y el precio cotice temporalmente por encima de sus medias móviles (SMA20 en 60,69 EUR y SMA50 en 56,75 EUR), entrar en este nivel con un stop-loss técnico fijado en los 56,5 EUR implica asumir un riesgo de caída directa de más del 8,5% sobre nuestra posición. Exponer un 5% del patrimonio de la cartera a una horquilla de pérdida tan pronunciada en un entorno macroeconómico tan frágil es, sencillamente, una gestión de activos deficiente. 

No podemos ignorar el panorama macroeconómico europeo actual: el euríbor supera con fuerza el 3,3%, encareciendo los costes de financiación y limitando el apetito por el riesgo a largo plazo, justo cuando las bolsas europeas experimentan rebotes eufóricos impulsados por sectores cíclicos y tecnológicos que podrían revertirse en cualquier momento. Aunque los fundamentales de AMS.MC muestran una ratio de deuda neta sobre EBITDA de 1,03x y un ROE del 26,44%, un múltiplo de valoración con un Price-to-Book de 5,21x y un Trailing P/E de casi 20x (19,90x) deja un margen de seguridad sumamente estrecho. Pagar múltiplos exigentes en momentos de máxima incertidumbre de tipos de interés es el camino más rápido hacia la destrucción de valor a largo plazo.

Por todo ello, la prudencia exige mantener una postura defensiva. En lugar de precipitarse en una compra impulsiva que compromete la estabilidad, debemos optar por esperar a correcciones más profundas o a señales de consolidación técnica más seguras que no pongan en jaque la seguridad de nuestros activos. La preservación del capital siempre debe primar sobre la búsqueda de ganancias especulativas a corto plazo.

**Rating**: HOLD
FINAL TRANSACTION PROPOSAL: **HOLD**

### Neutral Analyst

Neutral Analyst: Estimados compañeros, he escuchado atentamente tanto la postura excesivamente eufórica del analista agresivo como la extrema cautela defensiva del analista conservador respecto a Amadeus IT Group, S.A. (`AMS.MC`), y creo que ambos pecan de caer en sesgos peligrosos al evaluar la situación actual del valor a 61,90 EUR. 

Por un lado, el analista agresivo comete el error de ignorar el riesgo de mercado subyacente y la volatilidad real del activo. Lanzarse a una compra total basándose ciegamente en un precio objetivo de consenso de 71,47 EUR o en el impulso alcista actual de las bolsas europeas desatiende el hecho de que una volatilidad anualizada del 26,05% y un entorno macroeconómico complejo —marcado por un euríbor por encima del 3,3%— pueden desencadenar correcciones rápidas. Asumir un stop-loss en 56,5 EUR implica encajar una pérdida potencial superior al 8% en la posición, algo que no se puede despachar con triunfalismo.

Por otro lado, el analista conservador se refugia en una parálisis por análisis excesiva. Descartar la operación por completo exigiendo correcciones profundas significa ignorar la excelente salud fundamental de `AMS.MC`. No podemos pretender comprar una compañía de la categoría de Amadeus con un ROE del 26,44%, un flujo de caja libre superior a los 1.100 millones de euros y una ratio de deuda neta sobre EBITDA sumamente controlada de 1,03x a precios de saldo. Argumentar que un Forward P/E de 15,83x es prohibitivo ignora que estamos ante un líder tecnológico con un negocio de distribución y soluciones aéreas en plena recuperación estructural. 

La clave para equilibrar ambas posturas no es el blanco ni el negro, sino una gestión de riesgos moderada y sostenible. En lugar de descartar la oportunidad o sobreexponer el capital con una entrada masiva e inmediata al 5%, la estrategia equilibrada consiste en modular el riesgo mediante una asignación escalonada o un tamaño de posición inicial prudente (por ejemplo, dividiendo la entrada) y respetando estrictamente el soporte técnico de la media móvil de 50 sesiones en 56,75 EUR o el stop propuesto en 56,5 EUR. Esto nos permite capturar el potencial alcista del 15,46% que señalan los fundamentales sin quedar expuestos indefensos ante la volatilidad a corto plazo. Una perspectiva sensata aprovecha la fortaleza técnica sin ignorar los riesgos macroeconómicos, encontrando el punto óptimo entre crecimiento y preservación de capital.

**Rating**: HOLD

FINAL TRANSACTION PROPOSAL: **HOLD**

## V. Portfolio Manager Decision

### Portfolio Manager
**Rating**: Overweight

**Executive Summary**: Se establece una recomendación de Overweight sobre AMS.MC para incrementar progresivamente la exposición al valor. Se recomienda una estrategia de acumulación fraccionada aprovechando los niveles actuales en torno a 61,90 EUR, gestionando el riesgo con un stop-loss en 56,50 EUR y un horizonte temporal de 3 a 6 meses para capturar el consenso de 71,47 EUR.

**Investment Thesis**: La tesis alcista se impone al demostrar que la solidez fundamental de Amadeus IT Group, S.A. supera los riesgos macroeconómicos y tácticos señalados por la postura conservadora. Respaldada por un ROE del 26,44%, un apalancamiento controlado con una deuda neta sobre EBITDA de 1,03x y un flujo de caja libre superior a 1.100 millones de euros, la compañía justifica su Forward P/E de 15,83x y un potencial alcista de consenso del 15,46%. Aunque el analista conservador advierte acertadamente sobre una volatilidad anualizada del 26,05% y un euríbor superior al 3,3%, su enfoque conduce a una parálisis defensiva que ignora el foso competitivo y la estructura técnica favorable de la compañía (cotizando por encima de sus medias móviles clave con un RSI de 62,74). Para mitigar el riesgo de corrección a corto plazo y el impacto de un stop-loss amplio, se adopta una postura Overweight fraccionada en lugar de una compra total inmediata. Lo que cambiaría esta tesis sería un deterioro imprevisto en los flujos de caja operativos o la pérdida sostenida del soporte técnico de 56,50 EUR.

**Price Target**: 71.47

**Time Horizon**: 3-6 meses