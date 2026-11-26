# Trading Analysis Report: IBE.MC

- Analysis date: 2026-11-26
- Rating: Hold
- Generated: 2026-11-26 21:42:51
- TradingAgents 0.7.1: google, deep gemini-3.5-flash-lite, quick gemini-3.5-flash-lite
- Analysts: market, news, fundamentals; research debate rounds 1, risk debate rounds 1
- Data vendors: core_stock_apis yfinance, technical_indicators yfinance, fundamental_data yfinance, news_data yfinance, macro_data fred, prediction_markets polymarket, get_news ibex_sample, get_global_news ibex_sample

## I. Analyst Team Reports

### Market Analyst
**Rating**: HOLD  
FINAL TRANSACTION PROPOSAL: Neutral posture with a focus on risk management and monitoring upcoming catalysts such as the Caruna acquisition integration and broader European utility sector multiples. No new open position is recommended at current valuation levels without a deeper pullback.

---

### Informe de Análisis Financiero y Técnico para `IBE.MC` (Iberdrola, S.A.)

#### 1. Identidad de la Compañía y Contexto de Mercado
* **Instrumento:** `IBE.MC` (Iberdrola, S.A.)
* **Clasificación Empresarial:** Utilities / Utilities - Diversified (Bolsa de Madrid, EUR, índice de referencia `^IBEX`)
* **Fecha de Análisis:** 26 de noviembre de 2026 (`2026-11-26`)
* **Contexto Macroeconómico y Sectorial:** Las bolsas europeas y el selectivo español muestran un tono alcista impulsado por el sector bancario y tecnológico, con el Euríbor superando el 3,3% y la designación reciente de Pablo Hernández de Cos como presidente del BCE. En el plano corporativo específico de `IBE.MC`, destacan noticias relevantes como la autorización de la Comisión Europea y la aprobación final para adquirir la participación mayoritaria en la finlandesa Caruna por 5.000 millones de euros, además de valoraciones favorables de entidades como Deutsche Bank que apuntan a un fuerte desempeño operativo.

---

#### 2. Análisis Fundamental y Valuation
* **Capitalización de Mercado:** 152.876.466.176 EUR (~152.880 millones EUR)
* **Valor en Bolsa y Precio Actual:** Cierre a 23,03 EUR (`2026-11-26`), con una rentabilidad a 1 año (`return252_pct`) del +32,72% y un rendimiento a 63 sesiones de +14,69%. La acción cotiza muy cerca de sus máximos recientes, habiendo igualado la capitalización de grandes valores como el Banco Santander tras un rally alcista sostenido.
* **Métricas de Valoración:**
  * **Trailing P/E:** 31,12x
  * **Forward P/E:** 20,68x
  * **Price-to-Book (P/B):** 2,98x
  * **EV/EBITDA:** 14,96x
  * **PER Relativo Intermedio:** Ratio de 1,18 frente al PER forward mediano de sus pares en el sector (`ANE.MC`, `ENG.MC`, `ELE.MC`, `NTGY.MC`, `RED.MC`, `SLR.MC`, con una mediana forward de 17,58x), lo que indica que `IBE.MC` cotiza con prima respecto al sectorial ibérico.
* **Crecimiento y Rentabilidad:**
  * Ingresos totales (2025): 44.076 millones EUR (frente a 42.988 millones EUR en 2024 y 49.335 millones EUR en 2023).
  * EBITDA (2025): 16.763 millones EUR (frente a 15.192 millones EUR en 2024).
  * Beneficio Neto (2025): 6.285 millones EUR (frente a 5.612 millones EUR en 2024 y 4.803 millones EUR en 2023).
  * Deuda Total / Pasivos Financieros: 57.231 millones EUR en balance 2025 (total de deuda reportada en métricas de snapshot de ~63.837 millones EUR con efectivo de ~6.634 millones EUR, situando la ratio de Deuda Neta / EBITDA en ~3,95x).
  * Retorno sobre el Patrimonio (ROE): 9,49%. Margen de Beneficio Neto: 14,74%.
* **Dividendos:** Rentabilidad por dividendo (*Dividend Yield*) estimada en el 2,95% - 2,99%, con un dividendo por acción de 0,68 EUR y un *payout ratio* de 87,06%.
* **Consenso de Analistas:** Precio objetivo medio (*targetMeanPrice*) de 21,69 EUR, con un rango que oscila entre 18,00 EUR (mínimo) y 26,00 EUR (máximo) basado en 24 opiniones de analistas. Esto representa una ganancia/pérdida potencial respecto al precio actual de -5,82% (*consensus_upside_pct*), sugiriendo que la cotización actual a 23,03 EUR ya ha descontado gran parte del optimismo a corto plazo de las revisiones al alza de los analistas (como las de Deutsche Bank).

---

#### 3. Análisis Técnico y de Indicadores
* **Precio de Cierre:** 23,03 EUR (`2026-11-26`)
* **Medias Móviles:**
  * SMA 20: 22,81 EUR (Precio por encima, indicando soporte dinámico de corto plazo).
  * SMA 50: 21,80 EUR (Tendencia alcista de medio plazo confirmada).
  * SMA 200: 20,38 EUR (Sólida tendencia alcista estructural a largo plazo).
* **Osciladores e Indicadores de Momento:**
  * **RSI (14):** 60,94 (Zona neutral-alcista, sin señales inmediatas de sobrecompra extrema por encima de 70, pero reflejando un vigor comprador constante).
  * **MACD:** 0,30, con la línea de señal (*macd_signal*) en 0,38. El histograma muestra una ligera compresión del impulso alcista inmediato, aunque la tendencia global sigue respaldada por la posición de las medias móviles.
  * **Volatilidad (Anualizada):** 15,02%, lo cual es moderado para una utility diversificada de gran capitalización en un entorno de transición energética y fusiones/adquisiciones.
  * **Máximos y Retrocesos:** Máximo anual reciente reflejado en un *drawdown* mínimo de -2,83% desde los picos, evidenciando la robustez del valor.

---

#### 4. Selección de Indicadores Clave para la Estrategia (Hasta 8 Indicadores)
De acuerdo con la metodología solicitada, se seleccionan los siguientes 8 indicadores complementarios y no redundantes para el seguimiento operativo de `IBE.MC`:
1. `close_50_sma`: Para identificar la dirección del trend a medio plazo y actuar como soporte dinámico.
2. `close_200_sma`: Como referencia estructural a largo plazo para confirmar el ciclo alcista principal.
3. `close_10_ema`: Para capturar giros rápidos de impulso a corto plazo y posibles entradas tácticas.
4. `macd`: Para evaluar la divergencia/convergencia de la tendencia principal.
5. `macds`: Como línea de señal para filtrar cruces operativos en el MACD.
6. `rsi`: Para vigilar niveles de sobrecompra/sobreventa (umbrales 70/30) y prevenir agotamientos de tendencia.
7. `boll_ub`: Banda superior de Bollinger para detectar zonas de resistencia dinámica y posibles excesos de precio en breakouts.
8. `atr`: Para medir la volatilidad real del activo y dimensionar correctamente los niveles de *stop-loss*.

---

#### 5. Evidencias, Fuentes y Datos Faltantes
* **Fuentes consultadas:** Yahoo Finance (`IBE.MC`), Finanzas.com, El Economista, Estrategias de Inversión y MarketScreener España (fechas de noticias comprendidas entre el 2

### News Analyst
**Rating**: HOLD  
**FINAL TRANSACTION PROPOSAL**: REVIEW  

### Informe de Análisis y Estado de Situación: Iberdrola, S.A. (`IBE.MC`)

A fecha de 26 de noviembre de 2026, presentamos el análisis exhaustivo de la compañía **Iberdrola, S.A. (`IBE.MC`)**, cotizada en el mercado continuo español (MCE) dentro del sector de *Utilities - Diversified* (utilidades diversificadas). El presente informe integra datos fundamentales, técnicos, noticias recientes y el contexto macroeconómico europeo a partir de la evidencia preinstalada, cumpliendo estrictamente con los parámetros de transparencia, mención de fuentes, fechas y ausencia de supuestos no verificados.

---

### 1. Contexto Macroeconómico y Sentimiento de Mercado

Las bolsas europeas y españolas experimentan un impulso alcista significativo a finales de noviembre de 2026. Según los titulares recogidos, los índices de referencia europeos (como el Euro Stoxx 50 y el DAX alemán) avanzan con fuerza por encima del 2% diario, respaldados por la solidez de los sectores bancario y tecnológico y un clima general de apetito por el riesgo. Destaca en el ámbito institucional el nombramiento de Pablo Hernández de Cos como presidente del Banco Central Europeo (BCE), siendo el primer español al frente del organismo monetario.

Por otro lado, el euríbor se mantiene en cotas elevadas superando el 3,3% a finales de noviembre de 2026, lo que encarece la financiación y las hipotecas, en un entorno donde los tipos de interés se mantienen vigilados ante las decisiones de los bancos centrales. En este contexto de mercado, `IBE.MC` ha mostrado un comportamiento relativo muy destacado, igualando recientemente en valor de capitalización bursátil a gigantes del sector financiero como Banco Santander, año y medio después.

---

### 2. Análisis Fundamental y Financiero

`IBE.MC` cuenta con una capitalización bursátil masiva de **152.876 millones de EUR**, situándose como un pilar indiscutible del selectivo español IBEX 35 (`^IBEX`).

* **Cuentas de Resultados y Evolución Histórica:**
  * **Ingresos Totales (2025):** 44.076 millones de EUR (frente a 42.988 millones en 2024 y 49.335 millones en 2023).
  * **EBITDA (2025):** 16.763 millones de EUR (superior a los 15.192 millones de 2024 y 14.906 millones de 2023).
  * **Net Income / Beneficio Neto (2025):** 6.285 millones de EUR (incremento considerable en comparación con los 5.612 millones de 2024 y 4.803 millones de 2023).
* **Valoración y Múltiplos:**
  * **Trailing P/E:** 31,12x.
  * **Forward P/E:** 20,68x.
  * **Ratio PER relativo intermedio:** 1,18 respecto a la mediana del sector (peer median forward P/E: 17,58x), lo que indica que cotiza con una prima moderada frente a sus comparables (`ANE.MC`, `ENG.MC`, `ELE.MC`, `NTGY.MC`, `RED.MC`, `SLR.MC`).
  * **Precio a Valor en Libros (Price to Book):** 2,98x (sobre un valor contable por acción de 7,737 EUR).
  * **Ratio Deuda Neta / EBITDA:** 3,95x (Deuda total de aproximadamente 63.837 millones de EUR frente a un efectivo de 6.634 millones y un EBITDA de 14.494 millones).
* **Dividendos:**
  * Ofrece una **rentabilidad por dividendo (*dividend yield*) cercana al 2,99%** (dividend rate de 0,68 EUR), con un *payout ratio* del 87,06%.
* **Consenso de Analistas:**
  * Con 24 opiniones de analistas analizadas, el precio objetivo medio (*target mean price*) se sitúa en **21,68 EUR**, con un rango que oscila entre un objetivo mínimo de 18,00 EUR y un máximo de 26,00 EUR. Tomando el precio de cierre actual (23,03 EUR), el consenso muestra una ligera sobrevaloración de corto plazo (*consensus upside* de -5,82%).

---

### 3. Análisis Técnico (`IBE.MC`)

* **Precio de cierre actual (26/11/2026):** 23,03 EUR.
* **Variación en la sesión:** +1,36%.
* **Medias Móviles:**
  * SMA 20: 22,81 EUR (Tendencia alcista de corto plazo).
  * SMA 50: 21,80 EUR.
  * SMA 200: 20,38 EUR (Estructura de fondo sólidamente alcista).
* **Indicadores de Momento y Volatilidad:**
  * **RSI (14):** 60,94 (zona neutral-alcista, sin señales inmediatas de sobrecompra extrema).
  * **MACD:** 0,298 (con línea de señal en 0,375).
  * **Volatilidad (anualizada):** 15,02%.
  * **Drawdown:** -2,83% respecto a máximos recientes, mostrando una gran resiliencia y proximidad a máximos.
* **Rentabilidades acumuladas:**
  * Retorno a 21 sesiones: +4,54%.
  * Retorno a 63 sesiones: +14,69% (con un rendimiento superior relativo al índice de +19,28 pp).
  * Retorno a 252 sesiones: +32,72%.

---

### 4. Noticias Corporativas y Catalizadores Recientes

Durante la semana del 23 al 26 de noviembre de 2026, `IBE.MC` ha acaparado atención en los medios económicos europeos debido a movimientos estratégicos y revisiones de analistas:
1. **Adquisición de Caruna:** Bruselas autorizó a Iberdrola la compra de la compañía finlandesa Caruna por un importe de aproximadamente 5.000 millones de euros, obteniendo posteriormente la aprobación final para adquirir dicha participación mayoritaria, consolidando su posición en redes de distribución reguladas en Europa (fuente: *Finanzas.com* / *Yahoo* / Google RSS, 26/11/2026).
2. **Valoración de Deutsche Bank:** La entidad alemana emitió una recomendación de compra y un análisis destacando un potencial de beneficios sustancial por encima de las estimaciones del mercado (hasta 1.500 millones de euros adicionales previstos por el banco frente al consenso) (fuente: *MarketScreener España* / *Finanzas.com*, 23-25/11/2026).

---

### 5. Datos Faltantes y Limitaciones

* No se dispone de los flujos de caja operativos (*Operating Cash Flow*) y libres (*Free Cash Flow*) normalizados en el snapshot de fundamentales en tiempo real (mostrándose como nulos en la estructura estandarizada), a pesar de figurar flujos históricos en el estado de flujos de caja del cierre 2025 (Operating Cash Flow de 11.635 millones de EUR y Free Cash Flow de 3.317 millones de EUR). 
* Cualquier asignación de cartera o exposición a este valor debe considerarse estrictamente de

### Fundamentals Analyst
**Rating**: HOLD  
FINAL TRANSACTION PROPOSAL: HOLD

---

# Informe Fundamental y Análisis Integral: Iberdrola, S.A. (`IBE.MC`)

**Fecha del informe**: 26 de noviembre de 2026  
**Empresa**: Iberdrola, S.A. (`IBE.MC`)  
**Sector / Industria**: Utilities / Utilities - Diversified  
**Bolsa**: MCE (Madrid)  
**Moneda**: EUR  

---

### 1. Resumen de Perfil y Negocio
Iberdrola, S.A. (`IBE.MC`) es una de las mayores empresas eléctricas del mundo, líder global en energías renovables y redes de distribución eléctrica, operando de manera diversificada en España, Reino Unido (ScottishPower), Estados Unidos (Avangrid), Brasil (Neoenergia) y otros mercados internacionales. 

Recientemente, la compañía ha acaparado atención en los mercados financieros tras recibir la **autorización de la Comisión Europea (Bruselas) para adquirir la participación mayoritaria en la finlandesa Caruna por 5.000 millones de euros**, obteniendo también su aprobación final en noviembre de 2026 (según fuentes de noticias de Yahoo y Finanzas.com del 26/11/2026). Asimismo, entidades como **Deutsche Bank han emitido recomendaciones de compra**, estimando un rendimiento de beneficios superior a las expectativas actuales del mercado (noticias del 25/11/2026). En el ámbito bursátil, `IBE.MC` ha alcanzado en capitalización a Banco Santander a finales de noviembre de 2026, impulsada por un tono general alcista en las bolsas europeas y un sector defensivo robusto.

---

### 2. Datos Financieros Fundamentales y Valoración

A partir de los datos proporcionados para `IBE.MC`:
* **Capitalización Bursátil**: 152.876.466.176,00 EUR (€152.88 mil millones)
* **Precio de Cierre (26/11/2026)**: 23,03 EUR
* **PER Histórico (Trailing P/E)**: 31,12x
* **PER Previsto (Forward P/E)**: 20,68x
* **Precio sobre Valor en Libros (Price to Book)**: 2,98
* **Valor Empresa / EBITDA (EV/EBITDA)**: 14,96x
* **BPA Histórico (Trailing EPS)**: 0,74 EUR
* **BPA Previsto (Forward EPS)**: 1,11 EUR
* **Crecimiento de Ingresos (Revenue Growth)**: +15,9%
* **Crecimiento de Beneficios (Earnings Growth)**: -13,4% (en términos interanuales recientes)
* **Rentabilidad sobre el Patrimonio (ROE)**: 9,49%
* **Márgenes de Beneficio (Profit Margins)**: 14,74%
* **Deuda Total**: 63.837.000.000 EUR / **Caja Total**: 6.634.000.000 EUR
* **Deuda Neta / EBITDA**: 3,95x
* **Rentabilidad por Dividendo (Dividend Yield)**: ~2,95% (Dividendo anual de 0,68 EUR por acción, ratio de pago / payout ratio del 87,06%)
* **Valor en Libros por Acción**: 7,74 EUR
* **Consenso de Analistas (Target Mean Price)**: 21,69 EUR (Rango: 18,00 EUR a 26,00 EUR, basado en 24 opiniones de analistas). Con el precio actual de 23,03 EUR, esto representa una **desviación de consenso / upside de -5,82%**.

---

### 3. Análisis de Estados Financieros Históricos

* **Cuenta de Resultados (Income Statement)**:
  * *Ejercicio 2025*: Ingresos Totales de 44.076.000.000 EUR, EBITDA de 16.763.000.000 EUR y Beneficio Neto (Net Income) de 6.285.000.000 EUR.
  * *Ejercicio 2024*: Ingresos Totales de 42.988.000.000 EUR, EBITDA de 15.192.000.000 EUR y Beneficio Neto de 5.612.000.000 EUR.
  * *Ejercicio 2023*: Ingresos Totales de 49.335.000.000 EUR, EBITDA de 14.906.000.000 EUR y Beneficio Neto de 4.803.000.000 EUR.
  * *Análisis*: Los ingresos muestran cierta volatilidad influenciada por los precios energéticos globales, pero el EBITDA y el beneficio neto han mantenido una trayectoria de crecimiento sostenido a lo largo del trienio.

* **Balance de Situación (Balance Sheet)**:
  * *Ejercicio 2025*: Activos Totales de 160.762.000.000 EUR, Deuda Total de 57.231.000.000 EUR (la deuda total a nivel de métricas recientes se sitúa en ~63.840 M€ considerando pasivos ampliados), y Patrimonio Neto (Stockholders Equity) de 50.068.000.000 EUR.
  * *Ejercicio 2024*: Activos Totales de 158.293.000.000 EUR, Deuda Total de 57.731.000.000 EUR, Patrimonio Neto de 47.125.000.000 EUR.
  * *Análisis*: Estructura patrimonial sólida con activos en constante expansión, respaldada por un patrimonio neto que supera los 50.000 millones de euros.

* **Flujos de Caja (Cash Flow)**:
  * *Ejercicio 2025*: Flujo de Caja Operativo de 11.635.000.000 EUR, Inversión de Capital (CapEx) de -8.318.000.000 EUR, resultando en un Flujo de Caja Libre (Free Cash Flow) de 3.317.000.000 EUR.
  * *Ejercicio 2024*: Flujo de Caja Operativo de 11.925.000.000 EUR, CapEx de -8.375.000.000 EUR, FCF de 3.550.000.000 EUR.
  * *Ejercicio 2023*: FCF de 4.253.000.000 EUR.
  * *Análisis*: Generación de caja operativa sumamente robusta (siempre por encima de los 11.000 millones de euros anuales), la cual absorbe de manera holgada las elevadas inversiones en renovables y redes (CapEx superior a los 8.000 millones anuales).

---

### 4. Análisis Técnico Breve y Contexto de Mercado
* **Precio de cotización**: 23,03 EUR (`IBE.MC`).
* **Indicadores Técnicos**: RSI(14) en 60,94 (zona neutral-alcista, sin sobrecompra extrema). SMA de 20 sesiones en 22,81 EUR, SMA de 50 en 21,80 EUR y SMA de 200 en

## II. Research Team Decision

### Bull Researcher

Bull Analyst: **Rating**: HOLD  
FINAL TRANSACTION PROPOSAL: HOLD

¡Hola a todos! Es un placer abrir este debate sobre un auténtico titán de la bolsa europea como es **IBE.MC** (Iberdrola, S.A.). 

Mientras algunos analistas tienden a ponerse la venda antes de la herida mirando exclusivamente los múltiplos estáticos, los datos sobre la mesa nos gritan una realidad incontestable: estamos ante una compañía que no solo defiende su posición en un entorno macroeconómico complejo con tipos elevados y un Euríbor en torno al 3,3%, sino que está pisando el acelerador hacia un crecimiento estructural imparable. 

Vamos a desmontar los mitos y a centrarnos en por qué la tesis alcista de `IBE.MC` es mucho más sólida de lo que los osos quieren admitir.

---

### 1. Crecimiento Potencial y Escalatibilidad: Una Máquina de Generar Caja y Beneficios
Hablemos de cifras reales y tangibles, no de proyecciones vacías. En el ejercicio 2025, `IBE.MC` demostró una capacidad de escalabilidad envidiable al elevar su **EBITDA hasta los 16.763 millones de euros** (frente a los 15.192 millones de 2024) y llevar su **Beneficio Neto a los 6.285 millones de euros**, pulverizando registros anteriores. 

¿Y qué me dices del flujo de caja operativo? Superar de forma constante los **11.600 millones de euros en Operating Cash Flow** (11.635 millones en 2025) demuestra que el negocio principal no solo es resiliente, sino que produce la liquidez necesaria para financiar un CapEx anual masivo de más de 8.300 millones de euros en redes y renovables sin comprometer su salud financiera. 

### 2. Ventajas Competitivas y Posicionamiento Dominante (¡Hola, Caruna!)
Los osos suelen preocuparse por la saturación del mercado, pero ignoran por completo los movimientos estratégicos de escala internacional que `IBE.MC` ejecuta a la perfección. La reciente **aprobación final y autorización por parte de la Comisión Europea para adquirir la participación mayoritaria en la finlandesa Caruna por 5.000 millones de euros** es una prueba de maestría corporativa. Esta operación consolida su liderazgo indiscutible en redes de distribución reguladas de alta calidad en Europa. 

Además, seamos sinceros: igualar la capitalización bursátil de gigantes bancarios como el Banco Santander a finales de noviembre de 2026 no es fruto de la casualidad, sino del reconocimiento del mercado al perfil defensivo, diversificado (España, UK, EE.UU., Brasil y ahora más presencia nórdica) y de alta calidad crediticia de la compañía.

### 3. Indicadores Positivos y Respaldo Institucional
* **Tendencia Técnica Impecable:** Cotizando a 23,03 EUR, `IBE.MC` se encuentra respaldada por unas medias móviles alcistas clarísimas (SMA 20 en 22,81 EUR, SMA 50 en 21,80 EUR y una sólida SMA 200 en 20,38 EUR). Con un RSI de 60,94 y un *drawdown* mínimo de apenas -2,83% desde máximos, el valor muestra una fortaleza inquebrantable, acumulando un retorno anual (*return252_pct*) superior al **32,7%**.
* **El Ojo de los Grandes Bancos:** No olvidemos que entidades como **Deutsche Bank** han salido recientemente al paso recomendando la compra y señalando que `IBE.MC` podría ganar hasta **1.500 millones de euros más** de lo que el consenso general del mercado espera actualmente. ¡Hay un potencial operativo oculto que los osos están subestimando por completo!

---

### Contraargumentando al Oso: ¿Por qué la perspectiva alcista es superior?

* **Objeción del Oso (Valoración / P/E elevado):** Dirán que un *Trailing P/E* de 31,12x o un *Forward P/E* de más de 20x, junto con un PER relativo de 1,18 frente a sus pares, hace que la acción esté cara.
  * **Respuesta del Toro:** ¡Cuidado con mirar el PER de forma aislada! `IBE.MC` cotiza con prima porque es un activo de máxima calidad (*blue chip* global) con un mix de redes reguladas y renovables que ofrece una visibilidad de beneficios muy superior a la media del sector ibérico (`ANE.MC`, `ENG.MC`, etc.). Los recortes de tipos que el BCE empieza a vislumbrar con la llegada de Pablo Hernández de Cos a la presidencia beneficiarán enormemente a las utilities con planes de inversión masivos como este, abaratando su coste de financiación y justificando con creces múltiplos más generosos.
* **Objeción del Oso (Deuda Neta / EBITDA cercana a 3,95x):** Argumentarán que la deuda total es elevada.
  * **Respuesta del Toro:** Una deuda neta sobre EBITDA de ~3,95x es completamente manejable y estándar para un gigante de las infraestructuras eléctricas que invierte fuertemente en activos regulados que garantizan retornos estables a largo plazo. Con más de 6.600 millones de euros en caja y un flujo de caja operativo superior a 11.600 millones, la cobertura de deuda es holgada y segura.

### Conclusión y Postura
En definitiva, `IBE.MC` no es una utility común y corriente; es un activo estratégico de crecimiento verde y redes inteligentes que está batiendo expectativas. Aunque el consenso de analistas sitúe un precio objetivo medio en 21,69 EUR (cifras muchas veces conservadoras que van por detrás de los upgrades institucionales), la dinámica técnica, el cierre de operaciones como Caruna y el respaldo de fundamentales sólidos avalan que **la tendencia alcista estructural sigue intacta**. 

¡La palabra la tiene el bando bajista! ¿Con qué argumentos piensan frenar a un coloso que no para de generar caja y expandirse por Europa?

### Bear Researcher

Bear Analyst: **Rating**: HOLD  
FINAL TRANSACTION PROPOSAL: HOLD

¡Hola, colega! Comprendo perfectamente tu entusiasmo y esa fascinación por el despliegue de grandes cifras que nos presenta el bando alcista. Es muy fácil dejarse deslumbrar por los titulares rimbombantes sobre la compra de la finlandesa Caruna por 5.000 millones de euros, o aplaudir un EBITDA que roza los 16.800 millones de euros en 2025. Sin embargo, como analista bajista, mi deber es quitar el barniz del optimismo institucional y examinar los fríos números que ustedes prefieren pasar por alto. 

Vamos a desmontar punto por punto esa supuesta "invulnerabilidad" de `IBE.MC` (Iberdrola, S.A.), porque la realidad financiera y las valoraciones actuales exigen una dosis severa de prudencia.

---

### 1. La Trampa de la Valoración: ¿Pagando Oro por una Utility?
Mi estimado colega descarta con demasiada ligereza nuestros argumentos sobre los múltiplos, pidiendo que no miremos el PER de forma aislada. ¡Pero es que el problema no es que esté ligeramente elevado, es que **está en zona de burbuja para el sector**! 
* Hablamos de un **Trailing P/E de 31,12x** y un **Forward P/E de 20,68x**. 
* Si lo comparamos de manera directa con la mediana de sus pares ibéricos (`ANE.MC`, `ENG.MC`, `ELE.MC`, etc.), cuyo *Forward P/E* mediano se sitúa en 17,58x, `IBE.MC` cotiza con una prima exagerada (un ratio PER relativo de 1,18). 

¿Y qué me dices del consenso de analistas? El precio objetivo medio (*target mean price*) se encuentra en **21,69 EUR**, mientras que el valor cotiza a **23,03 EUR**. Esto implica un **potencial de retorno negativo de -5,82%**. El mercado ya ha descontado con creces cualquier optimismo futuro, los "upgrades" de Deutsche Bank y las expectativas más ambiciosas. Comprar `IBE.MC` hoy a estos niveles es subirse al vagón de cola cuando el recorrido potencial ya es nulo según el consenso profesional.

### 2. El Espejismo del Crecimiento y la Realidad del Beneficio
Nos hablan de una máquina imparable de generar beneficios netos, pero omiten un dato fundamental de los datos aportados: el **crecimiento de los beneficios (*earnings growth*) interanual muestra una contracción del -13,4%**. ¿Cómo se come eso con el relato de un crecimiento estructural imparable? Los ingresos y los márgenes sufren presiones cíclicas y regulatorias que no desaparecen simplemente porque el EBITDA nominal suba un año determinado.

Además, pongamos el foco en el dividendo: ofrecen una rentabilidad por dividendo (*dividend yield*) de apenas el **2,95% al 2,99%** con un *payout ratio* del **87,06%**. Entregar casi el 88% de las ganancias en dividendos mientras se acometen planes de inversión multimillonarios (con un CapEx superior a los 8.300 millones de euros anuales) es una política insostenible que estrangula la flexibilidad financiera de la compañía.

### 3. El Riesgo de la Palanca Financiera en un Entorno de Tipos Altos
El bando toro resta importancia a una **Deuda Neta / EBITDA de ~3,95x**, tachándola de "estándar". Traduzcamos esto a cifras reales: la compañía arrastra pasivos financieros y una deuda total que ronda los **63.837 millones de euros** frente a una caja de apenas 6.634 millones. 

En un escenario macroeconómico donde el Euríbor sigue superando el 3,3% y el BCE opera bajo la batuta de nuevas presidencias con la inflación y los tipos bajo estricta vigilancia, refinanciar semejante volumen de endeudamiento neto a coste cero es una fantasía del pasado. Cada punto porcentual de subida en los costes de financiación erosiona de manera directa los márgenes y el flujo de caja libre (*Free Cash Flow*), el cual, por cierto, se ha visto reducido a unos 3.317 millones de euros en 2025 (por debajo de los más de 4.250 millones alcanzados en 2023). ¡La caja libre se encoge mientras la deuda y el CapEx se disparan!

---

### Contraargumentando al Toro: Desenmascarando las falacias alcistas

* **La falacia sobre Caruna y la expansión internacional:** Nos venden la integración de Caruna en Finlandia como una obra maestra de ingeniería corporativa. La realidad es que desembolsar 5.000 millones de euros en adquisiciones en un entorno de restricción de liquidez y tipos elevados añade presión inmediata al balance y concentra riesgos regulatorios en mercados geográficos maduros donde los retornos están fuertemente acotados por los reguladores locales.
* **La falacia técnica y el "momentum":** Es cierto que el RSI está en 60,94 y las medias móviles muestran una inercia alcista de fondo. Pero operar un *blue chip* de utilities basándose únicamente en que el *drawdown* es pequeño (-2,83%) y que ha igualado en capitalización a la banca es jugar con fuego. Las valoraciones estiradas unidas a un *upside* negativo de casi el 6% son el caldo de cultivo perfecto para una corrección técnica en cuanto cualquier variable macroeconómica decepcione.

### Conclusión y Postura Bajista
`IBE.MC` es, sin duda, un gigante industrial y un actor clave en la transición energética europea, pero **una gran empresa no es sinónimo automático de una buena inversión al precio actual**. Con un PER superior a 30x en su histórico, un potencial de crecimiento de beneficios negativo (-13,4%), un consenso de analistas que apunta a caídas hacia los 21,69 EUR y una mochila de deuda de casi 64.000 millones de euros, el perfil de riesgo/recompensa está completamente desequilibrado en contra del inversor.

Por estas razones, la recomendación sensata es mantener una postura de **HOLD** con sesgo de máxima cautela, evitando por completo destinar capital nuevo a estos niveles de precio y esperando una corrección profunda que ajuste los múltiplos a la realidad del sector de utilities. ¡Que no os vendan humo a precio de oro!

### Research Manager
**Recommendation**: Hold

**Rationale**: Hola equipo. Tras analizar los argumentos presentados por ambos bandos para IBE.MC, la postura neutral o Hold se impone de forma natural. Por un lado, el bando alcista destaca la impresionante capacidad de generación de caja de la compañía (más de 11.600 millones de euros de Operating Cash Flow), el impulso estratégico que supone la compra de la finlandesa Caruna autorizada por Bruselas, y una fortaleza técnica innegable con un retorno anual superior al 32% y el respaldo de entidades como Deutsche Bank. Por otro lado, el bando bajista expone con acierto los riesgos de valoración: un Trailing P/E elevado de 31,12x, un PER relativo superior a sus comparables (1,18), una contracción reciente del beneficio neto del -13,4%, y un precio de cotización actual (23,03 EUR) que ya supera el precio objetivo medio del consenso de analistas (21,69 EUR), dejando un potencial de retorno negativo (-5,82%). Dado que los sólidos fundamentales operativos y el momentum técnico chocan frontalmente contra unos múltiplos estirados y un techo de valoración según el consenso, la balanza queda completamente equilibrada. Por lo tanto, no hay evidencia suficiente para inclinar la balanza hacia la compra o la venta en este momento.

**Strategic Actions**: Instrucciones para el trader en base a una asignación hipotética: Mantener la posición actual (Hold) sin realizar nuevas compras ni aperturas de exposición en IBE.MC a los precios actuales de 23,03 EUR. No destinar capital adicional dado el potencial negativo respecto al precio objetivo del consenso (-5,82%) y la exigente valoración por PER. Monitorear de cerca los niveles de soporte técnico en torno a la SMA de 20 y 50 periodos (22,81 EUR y 21,80 EUR respectivamente) por si se produce una corrección de mercado que ofrezca un punto de entrada más atractivo, así como la evolución de la integración de Caruna y el impacto del coste de su deuda bajo un entorno de tipos elevados.

## III. Trading Team Plan

### Trader
**Action**: Hold

**Reasoning**: La cotizacion actual de IBE.MC en 23,03 EUR se encuentra por encima del precio objetivo medio del consenso de analistas situado en 21,69 EUR, lo que implica un potencial negativo del -5,82%. Aunque los fundamentales operativos son robustos y cuenta con catalizadores positivos como la adquisicion de Caruna y un fuerte impulso tecnico por encima de sus medias moviles, los multiplos de valoracion se encuentran estirados con un P/E historico de 31,12x y un PER relativo superior a sus comparables. Esta situacion de equilibrio entre el excelente momentum tecnico y la exigente valoracion aconseja adoptar una postura neutral de espera, evitando abrir nuevas posiciones alcistas en este nivel.

**Entry Price**: not provided

**Stop Loss**: not provided

**Position Sizing**: 0% of portfolio

FINAL TRANSACTION PROPOSAL: **HOLD**

## IV. Risk Management Team Decision

### Aggressive Analyst

Aggressive Analyst: Rating: HOLD
FINAL TRANSACTIONPOSAL: HOLD

¡Menuda exageración de cautela nos traen el analista conservador y el neutral con su postura de miedo e indecisión! Mientras ellos se quedan mirando las tablas y paralizados por un PER histórico de 31,12x o por un precio objetivo de consenso que se ha quedado totalmente obsoleto, están ignorando por completo el verdadero motor de crecimiento y la brutal fortaleza que exhibe Iberdrola en este momento de mercado. Nos hablan de un potencial negativo del -5,82% basándose en un consenso de 21,69 EUR, pero olvidan que los precios objetivos de los analistas son solo estimaciones estáticas, mientras que la realidad operativa y los catalizadores corporativos van a una velocidad de crucero imparable. 

¿De verdad vamos a frenar y adoptar una postura neutral de espera cuando tenemos sobre la mesa la aprobación final de la Comisión Europea para comprar la finlandesa Caruna por 5.000 millones de euros? Esa es una jugada maestra de expansión en redes reguladas que va a transformar los flujos de caja y consolidar un dominio europeo absoluto. Y no nos olvidemos de las revisiones de grandes casas como Deutsche Bank, que estiman que Iberdrola va a ganar hasta 1.500 millones de euros más de lo que el mercado espera. ¡Eso destroza cualquier cálculo tradicional de múltiplos estirados!

El análisis técnico grita fortaleza, no debilidad: la acción cotiza a 23,03 EUR con un RSI en 60,94 que muestra un vigor comprador sano, por debajo de la zona de sobrecompra extrema, y apoyada holgadamente por una SMA de 20 sesiones en 22,81 EUR y una SMA de 50 en 21,80 EUR. Las rentabilidades del 14,69% a 63 sesiones y del 32,72% a un año no son casualidad; reflejan un valor de máxima categoría que ha igualado en capitalización bursátil a gigantes como el Banco Santander en pleno rally de las bolsas europeas impulsadas por la banca y la tecnología. 

La cautela excesiva de los analistas conservadores y neutrales nos hace perder oportunidades históricas bajo la excusa de una deuda neta sobre EBITDA de 3,95x o un PER forward de 20,68x que, para una utility de esta envergadura y calidad con una generación de caja operativa superior a los 11.600 millones de euros, está más que justificada por su liderazgo mundial en renovables. Esperar a una corrección o a un pullback profundo en un valor con semejante impulso alcista estructural y con el viento de cola de los grandes acuerdos corporativos es sinónimo de quedarse fuera del tren del éxito. ¡Hay que ser audaces y apostar por el crecimiento y la innovación!

### Conservative Analyst

Conservative Analyst: **Rating**: HOLD  
FINAL TRANSACTION PROPOSAL: **HOLD**

No podemos dejarnos deslumbrar por el optimismo desmedido ni por los cantos de sirena de un rally bursátil impulsado por el entusiasmo generalizado de las bolsas europeas a finales de noviembre de 2026. El analista agresivo descarta con demasiada ligereza los múltiplos de valoración y los riesgos estructurales, tachando de simple "miedo" lo que en realidad es una gestión de riesgos rigurosa y prudente. Defender una posición compradora o ignorar las señales de alerta actuales en `IBE.MC` solo porque la cotización ha alcanzado los 23,03 EUR y ha igualado en capitalización al Banco Santander es una irresponsabilidad que expone a la firma a una corrección innecesaria.

En primer lugar, argumentar que el precio objetivo medio del consenso de 21,69 EUR está "obsoleto" es un error crítico. Con veinticuatro opiniones de analistas respaldando esa cifra, el potencial negativo del -5,82% frente al precio actual nos advierte claramente de que el valor ya cotiza con una prima exigente. Considerar que un PER histórico de 31,12x y un PER forward de 20,68x —que sitúa su PER relativo en 1,18x frente a la mediana de sus comparables— son detalles menores es ignorar que cualquier tropiezo en la ejecución o un cambio en el sentimiento macroeconómico castigará con dureza a los valores sobrecomprados.

En cuanto al entusiasmo por la adquisición de la finlandesa Caruna por 5.000 millones de euros, el analista agresivo olvida el impacto financiero real que esto conlleva. Iberdrola ya soporta una deuda total cercana a los 63.837 millones de euros frente a una caja de 6.634 millones, situando la ratio de deuda neta sobre EBITDA en unas elevadas 3,95x. Comprometer miles de millones adicionales en grandes operaciones de M&A en un entorno donde el euríbor supera el 3,3% y encarece el coste de financiación no es una "jugada maestra" sin coste; es un incremento significativo del apalancamiento y del riesgo financiero en un balance que ya requiere una consolidación estricta, no más presión.

Desde el punto de vista técnico y de sostenibilidad a largo plazo, fiarlo todo a que el RSI en 60,94 y unas medias móviles alcistas (SMA 20 en 22,81 EUR y SMA 50 en 21,80 EUR) van a subir indefinidamente es obviar la volatilidad y los riesgos de reversión. Un *drawdown* del -2,83% desde máximos y una rentabilidad acumulada del 32,72% a un año muestran que el activo está maduro y madurando hacia una fase de agotamiento de corto plazo. Exponer el capital de la firma abriendo posiciones alcistas en plena zona de resistencia, sin un retroceso saludable hacia soportes estructurales más sólidos como la SMA de 200 en 20,38 EUR, atenta contra el mandato fundamental de preservar el patrimonio y minimizar la volatilidad. La paciencia y la disciplina de mantener una postura neutral de espera protegen a la firma de caídas abruptas cuando las valoraciones están estiradas.

### Neutral Analyst

Neutral Analyst: **Rating**: HOLD  
FINAL TRANSACTION PROPOSAL: **HOLD**

Analizando las posturas de nuestros compañeros, queda claro que tanto el Analista Agresivo como el Analista Conservador caen en sesgos peligrosos por defender posturas extremas. El Analista Agresivo acusa de cobardía y exceso de miedo al adoptar una postura de espera, restando importancia a los múltiplos de valoración bajo la excusa de que "el consenso está obsoleto" y celebrando acríticamente la compra de Caruna o las revisiones optimistas de Deutsche Bank. Sin embargo, ignora peligrosamente que un PER histórico de 31,12x y una ratio de deuda neta sobre EBITDA de 3,95x en un entorno donde el euríbor supera el 3,3% no son meros detalles estadísticos, sino factores de riesgo financiero muy reales que pueden castigar severamente a la compañía si el ciclo macroeconómico se tuerce o si la integración de la finlandesa sufre desviaciones.

Por otro lado, el Analista Conservador se refugia en un exceso de rigidez defensiva, tratando la cotización a 23,03 EUR como si estuviera al borde de un abismo y exigiendo un retroceso hasta la SMA de 200 en 20,38 EUR para considerar cualquier movimiento. Descartar la inercia alcista de un valor con una rentabilidad anual del 32,72%, un RSI moderado en 60,94 y un sólido soporte en la SMA de 20 en 22,81 EUR equivale a ignorar la realidad del mercado y las dinámicas técnicas de un líder global en renovables que acaba de igualar en capitalización a gigantes como el Banco Santander. Esperar una corrección tan profunda en un activo con semejante fortaleza estructural y respaldado por flujos operativos anuales superiores a los 11.600 millones de euros es perder de vista las oportunidades que ofrece una gestión flexible.

Como Analista de Riesgos Neutral, propongo que la solución más sensata y equilibrada es mantener nuestra postura de espera pero con una perspectiva táctica y activa. No necesitamos lanzarnos a comprar de forma agresiva en máximos ignorando la prima de valoración frente a la mediana de los comparables y el consenso de analistas situado en 21,69 EUR, pero tampoco debemos cerrar los ojos ante el excelente momento técnico de Iberdrola. La estrategia moderada y sostenible consiste en mantener una posición neutral del 0% en este preciso instante, aprovechando la actual estabilidad para vigilar de cerca los soportes dinámicos de corto plazo (como la SMA de 20) y preparar niveles de entrada escalonados en caso de que se produzca un pullback técnico saludable hacia la zona de la SMA de 50 (en 21,80 EUR), lo que permitiría capturar el potencial a largo plazo de la compañía sin asumir el riesgo innecesario de sobreexposición en una zona de precios exigente. De este modo, equilibramos el impulso de crecimiento con una disciplina estricta de preservación del capital.

## V. Portfolio Manager Decision

### Portfolio Manager
**Rating**: Hold

**Executive Summary**: Mantener la asignación actual en IBE.MC sin realizar nuevas compras ni aperturas de exposición en los niveles actuales de 23,03 EUR. No destinar capital adicional dado el potencial negativo respecto al precio objetivo del consenso (-5,82%) y la exigente valoración por PER, esperando un retroceso hacia soportes dinámicos para evaluar futuras acumulaciones.

**Investment Thesis**: Tras sopesar las posturas del debate, la recomendación de Hold se impone de manera natural debido al equilibrio de fuerzas entre el excelente momentum técnico (cotizando por encima de la SMA de 20 en 22,81 EUR y SMA de 50 en 21,80 EUR, con un retorno a un año del 32,72%) y los claros riesgos de valoración y fundamentales expuestos. Por un lado, la sólida generación de flujo de caja operativo y catalizadores como la adquisición de Caruna avalan la calidad estructural de la compañía. Por otro lado, el PER histórico de 31,12x, un PER forward de 20,68x, una ratio de deuda neta sobre EBITDA de 3,95x en un entorno de tipos elevados y una cotización actual que supera el precio objetivo medio del consenso de 21,69 EUR impiden justificar una compra agresiva. Esta tesis cambiaría si se produjera una corrección técnica hacia soportes fundamentales más atractivos o una normalización de los múltiplos de valoración.

**Price Target**: 21.69

**Time Horizon**: 3-6 months