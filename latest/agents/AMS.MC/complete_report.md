# Trading Analysis Report: AMS.MC

- Analysis date: 2026-11-01
- Rating: Hold
- Generated: 2026-11-01 20:38:28
- TradingAgents 0.7.1: google, deep gemini-3.5-flash-lite, quick gemini-3.5-flash-lite
- Analysts: market, news, fundamentals; research debate rounds 1, risk debate rounds 1
- Data vendors: core_stock_apis yfinance, technical_indicators yfinance, fundamental_data yfinance, news_data yfinance, macro_data fred, prediction_markets polymarket, get_news ibex_sample, get_global_news ibex_sample

## I. Analyst Team Reports

### Market Analyst
**Rating**: HOLD  
FINAL TRANSACTION PROPOSAL: Mantener posición actual con stop-loss dinámico basado en volatilidad, vigilando soportes clave en torno a la media de 50 sesiones y la resistencia psicológica del objetivo de consenso.

---

### Informe Técnico y Fundamental de Amadeus IT Group, S.A. (`AMS.MC`)

#### 1. Contexto de Mercado y Datos Identificados
Amadeus IT Group, S.A. (`AMS.MC`) cotiza en el mercado continuo de Madrid dentro del sector tecnológico (Servicios de Tecnologías de la Información). Según la instantánea verificada a fecha **31 de octubre de 2026** (con cierre de sesión a 30 de octubre de 2026), el valor presenta un precio de cierre de **56,76 EUR**, experimentando una ligera variación diaria del **-0,77%**. 

La compañía cuenta con una capitalización bursátil de aproximadamente **23.838 millones de EUR**, un PER estimado forward de **14,62** y un PER histórico (*trailing*) de **18,73**. El dividendo ofrece una rentabilidad por dividendo (*dividend yield*) del **2,71%** (tasa de 1,54 EUR por acción con un *payout ratio* del 50,83%).

#### 2. Análisis Técnico y Selección de Indicadores
Para el análisis de `AMS.MC`, se han seleccionado 8 indicadores clave que cubren diferentes dimensiones del mercado (tendencia, momento, volatilidad y volumen), evitando redundancias:

1. **`close_50_sma`** (50 SMA): Indicador de tendencia a medio plazo. Se sitúa en **55,04 EUR**, sirviendo como soporte dinámico inmediato para el precio actual (56,76 EUR).
2. **`close_200_sma`** (200 SMA): Benchmark de tendencia a largo plazo. Registrado en **52,22 EUR**, lo que confirma que la cotización se mantiene en una estructura alcista de fondo a largo plazo.
3. **`close_10_ema`** (10 EMA): Media móvil exponencial corta para capturar giros rápidos de impulso (su valor orientativo acompaña la zona de corto plazo donde la SMA de 20 se sitúa en 54,61 EUR).
4. **`macd`** (MACD): Con un valor de **0,84**, muestra divergencias positivas frente a su línea de señal.
5. **`macds`** (MACD Signal): Situado en **0,50**, se encuentra por debajo de la línea MACD, validando un impulso comprador activo a corto plazo.
6. **`rsi`** (RSI de 14 periodos): En un valor de **59,56**, indica un sesgo moderadamente alcista sin haber alcanzado zonas de sobrecompra extrema (fijadas habitualmente en 70), lo que deja margen de continuidad al movimiento.
7. **`atr`** (Average True Range): Refleja la volatilidad histórica y actual (volatilidad anualizada del **24,28%**), útil para el dimensionamiento de posiciones y colocación de *stop-loss*.
8. **`vwma`** (Volume-Weighted Moving Average): Integra la acción del precio con el volumen negociado, confirmando la solidez de los rebotes recientes (como el retorno a 21 sesiones del **+8,94%**).

*Evidencia técnica adicional:* El RSI de 14 periodos se encuentra en 59,56, el MACD es positivo (0,84) y cruza por encima de su señal (0,50), y el retroceso máximo reciente (*drawdown*) se sitúa en el **-14,05%**.

#### 3. Análisis Fundamental y Financiero
De acuerdo con los estados financieros e informes de ingresos:
- **Ingresos Totales (2025):** 6.517 millones de EUR (frente a 6.141,7 millones en 2024 y 5.441,2 millones en 2023).
- **EBITDA (2025):** 2.534,7 millones de EUR (crecimiento sostenido desde los 2.134,2 millones en 2023).
- **Beneficio Neto (2025):** 1.335,7 millones de EUR (superior a los 1.253 millones de 2024).
- **Flujo de Caja Libre (2025):** 1.386,3 millones de EUR (consistente con los 1.357,9 millones de 2024).
- **Deuda Neta / EBITDA:** Se sitúa en un saludable **1,06x** (deuda total de 3.607 millones de EUR frente a una caja de 976 millones de EUR y un EBITDA de 2.479,7 millones de EUR).

El consenso de analistas (basado en 22 opiniones) establece un precio objetivo medio (*targetMeanPrice*) de **69,58 EUR**, con un precio mínimo de **51,00 EUR** y un máximo de **82,00 EUR**, lo que arroja un potencial alcista de consenso (*consensus upside*) del **22,58%**.

#### 4. Noticias Recientes y Contexto Macroeconómico
Las noticias recientes de finales de octubre de 2026 señalan una volatilidad contenida en el IBEX 35 ante las dudas sobre el sector tecnológico y las decisiones del Banco Central Europeo (BCE), que mantuvo los tipos de interés en el **2,5%** en su reunión de finales de octubre de 2026 (con expectativas de seguimiento de cara a diciembre). Asimismo, la prensa especializada destaca que las acciones de Amadeus IT Group podrían experimentar movimientos estimados en torno al **2,5%** condicionados por la publicación de resultados y el comportamiento general de las bolsas europeas mixtas por la inteligencia artificial y los datos macroeconómicos.
- *Fechas y fuentes de noticias de referencia:* 
  - 30-10-2026: *Investing.com España* ("Las acciones de Amadeus IT Group podrían moverse un 2,5% tras resultados").
  - 28-10-2026: *Estrategias de Inversión* ("Algo se mueve en Amadeus: sus indicadores dan un salto y NVIDIA entra en escena").
  - 29/30-10-2026: Cobertura de reuniones del BCE (*Bankinter*, *El Boletín*).

#### 5. Datos Faltantes y Limitaciones
No se dispone de un desglose detallado diario del libro de órdenes de alta frecuencia ni de proyecciones analíticas internas independientes que difieran del consenso de mercado recogido. La valoración descansa en los datos suministrados por la plataforma y los estados financieros auditados a cierre de 2025.

---

### Resumen Estructurado de Indicadores y Métricas Clave

| Categoría | Métrica / Indicador | Valor Actual (`AMS.MC`) | Implicación Operativa |
| :--- | :--- | :--- | :--- |
| **Precio y Tendencia** | Cierre Actual | 56,76 EUR | Por encima de la SMA 50 (55,04) y SMA 200 (52,22). |
| **Tendencia Med. Plazo** | `close_50_sma` | 55,04 EUR | Soporte dinámico clave de medio plazo. |
| **Tendencia Larg. Plazo**| `close_200_sma` | 52,22 EUR | Confirma tendencia alcista estructural a largo plazo. |
| **Momento** | `rsi` (14) | 59,56 | Impulsor alcista moderado sin sobrecompra. |
| **Momento /

### News Analyst
**Rating**: HOLD  

### Análisis Fundamental y de Mercado de Amadeus IT Group, S.A. (`AMS.MC`)

#### 1. Contexto de Mercado y Evolución Reciente
Amadeus IT Group (`AMS.MC`), cotizada en el mercado continuo de Madrid (`MCE`) dentro del sector tecnológico (Servicios de Tecnologías de la Información), cotiza a un precio de **56,76 EUR** (al cierre del 30 de octubre de 2026). La compañía experimentó recientemente movimientos corporativos e informativos derivados de la temporada de resultados a finales de octubre de 2026, con analistas y medios (como *Investing.com* el 30/10/2026) apuntando a volatilidades moderadas en torno a sus publicaciones financieras. En el plano macroeconómico europeo, el Banco Central Europeo (BCE) mantuvo los tipos de interés en el 2,5% a finales de octubre de 2026, mientras los mercados bursátiles europeos se muestran mixtos y condicionados por la evolución del sector tecnológico y la incertidumbre geopolítica e inflacionaria.

#### 2. Fundamentos Financieros y Valoración
Los datos financieros más recientes de `AMS.MC` muestran una sólida posición operativa:
* **Capitalización de Mercado:** ~23.840 millones de EUR.
* **Ingresos (2025):** 6.517 millones de EUR (frente a los 6.141 millones de EUR en 2024 y 5.441 millones de EUR en 2023), reflejando un crecimiento constante de la cifra de negocios.
* **EBITDA (2025):** 2.534,7 millones de EUR (Enterprise to EBITDA de ~10,68x).
* **Beneficio Neto (2025):** 1.335,7 millones de EUR.
* **PER:** Trailing P/E de 18,73x y Forward P/E de 14,62x, lo que sugiere una valoración atractiva de cara a las estimaciones de beneficios futuros.
* **Endeudamiento:** Deuda total de aproximadamente 3.223,6 millones de EUR (con una ratio de Deuda Neta sobre EBITDA de ~1,06x), lo cual indica un balance saludable y manejable.
* **Flujo de Caja Libre (FCF):** 1.386,3 millones de EUR en el ejercicio 2025, respaldando un sólido perfil de conversión de caja.
* **Retribución al Accionista:** Ofrece una rentabilidad por dividendo (*dividend yield*) del **2,71%**, con una tasa de pago (*payout ratio*) aproximada del 50,8%.

#### 3. Análisis Técnico y Consenso de Analistas
* **Indicadores Técnicos:** El precio de la acción se encuentra por encima de sus medias móviles clave (SMA20 en 54,61 EUR, SMA50 en 55,04 EUR y SMA200 en 52,22 EUR). El RSI de 14 días se sitúa en 59,56, denotando un sesgo neutral-alcista sin señales inmediatas de sobrecompra. La volatilidad histórica de 24,28% y una rentabilidad a 21 días del 8,94% reflejan un tono de recuperación a corto plazo, aunque el retorno a 252 días sigue en terreno negativo (-11,44%).
* **Consenso de Mercado:** El precio objetivo medio de los analistas (*target mean price*) se sitúa en **69,58 EUR**, con un rango que va desde un mínimo de 51,00 EUR hasta un máximo de 82,00 EUR (basado en 22 opiniones de analistas). Esto arroja un potencial de revalorización (*consensus upside*) del **22,58%** respecto al precio actual de 56,76 EUR.

#### 4. Evidencia, Datos Faltantes y Asunciones
* **Fuentes y URLs:** 
  * Yahoo Finance Quote & Financials: `https://finance.yahoo.com/quote/AMS.MC/` y `https://finance.yahoo.com/quote/AMS.MC/financials/`
  * Cobertura de noticias (Investing.com): `https://news.google.com/rss/articles/...` (publicadas el 30-10-2026).
* **Datos Faltantes:** No se dispone de un desglose detallado de los márgenes por segmentos geográficos exactos más allá de los estados consolidados y los indicadores cuantitativos provistos en el snapshot. No se ha suministrado cartera de inversión propia (toda asignación es hipotética).
* **Asunciones:** Se asume la continuidad del entorno macroeconómico europeo con tipos oficiales estabilizados por el BCE en el 2,5% y la resiliencia en la demanda del sector de viajes y reservas tecnológicas.

---

### Resumen de Datos Clave (`AMS.MC`)

| Métrica / Concepto | Valor / Estado | Fuente / Observaciones |
| :--- | :--- | :--- |
| **Ticker y Bolsa** | `AMS.MC` (MCE - España) | Yahoo Finance / Contexto Preload |
| **Precio Actual** | 56,76 EUR (30-10-2026) | Cierre de sesión bursátil |
| **Capitalización Bursátil** | ~23.838 millones de EUR | Datos fundamentales |
| **Ingresos Totales (2025)** | 6.517 millones de EUR | Estados financieros consolidados |
| **EBITDA (2025)** | 2.534,7 millones de EUR | Estados financieros consolidados |
| **PER (Trailing / Forward)** | 18,73x / 14,62x | Ratio de valoración |
| **Rentabilidad por Dividendo** | 2,71% | `dividend_yield_pct` |
| **Precio Objetivo Consenso** | 69,58 EUR (+22,58% potencial) | Media de 22 analistas |
| **Medias Móviles (SMA20/50/200)**| 54,61 / 55,04 / 52,22 EUR | Indicadores técnicos |
| **RSI (14)** | 59,56 | Zona neutral-alcista |

FINAL TRANSACTION PROPOSAL: HOLD

### Fundamentals Analyst
**Rating**: HOLD  
FINAL TRANSACTION PROPOSAL: HOLD

---

### **Informe Fundamental Exhaustivo: Amadeus IT Group, S.A. (`AMS.MC`)**

Fecha de referencia de los datos: **1 de noviembre de 2026**  
Cotización actual (`AMS.MC`): **56,76 EUR** (al cierre del 30 de octubre de 2026).

---

### **1. Perfil de la Compañía y Negocio**
Amadeus IT Group, S.A. (`AMS.MC`) es una empresa líder cotizada en la Bolsa de Madrid dentro del sector tecnológico, clasificada específicamente en **Servicios de Tecnología de la Información** (`Technology / Information Technology Services`). Proporciona soluciones tecnológicas avanzadas para la industria global de los viajes y el turismo, conectando a proveedores de viajes (aerolíneas, hoteles, empresas de alquiler de coches, etc.) con los distribuidores (agencias de viajes y plataformas de reservas online) y gestionando sistemas críticos de transacciones y distribución.

---

### **2. Análisis Financiero y Estados Financieros**

A partir de la información financiera provista (cierre del ejercicio fiscal completado hasta diciembre de 2025), se observa una sólida evolución en los ingresos y flujos de caja de la compañía:

#### **Cuenta de Resultados (Income Statement)**
* **Ingresos Totales (Total Revenue):**
  * Ejercicio 2025: **6.517,0 millones de EUR** (frente a 6.141,7 millones de EUR en 2024 y 5.441,2 millones de EUR en 2023). Muestra una expansión constante de la cifra de negocios.
* **EBITDA:**
  * Ejercicio 2025: **2.534,7 millones de EUR** (frente a 2.353,2 millones de EUR en 2024 y 2.134,2 millones de EUR en 2023).
* **Beneficio Neto (Net Income):**
  * Ejercicio 2025: **1.335,7 millones de EUR** (frente a 1.253,0 millones de EUR en 2024 y 1.117,6 millones de EUR en 2023).

#### **Balance de Situación (Balance Sheet)**
* **Activos Totales:** 11.470,9 millones de EUR (2025) vs 11.784,3 millones de EUR (2024).
* **Deuda Total:** 3.223,6 millones de EUR (2025), mejorando desde los 3.375,7 millones de EUR registrados en 2024.
* **Patrimonio Neto (Stockholders Equity):** 4.853,7 millones de EUR (2025).

#### **Flujo de Caja (Cash Flow)**
* **Flujo de Caja Operativo (Operating Cash Flow):** 2.200,9 millones de EUR en 2025 (creciendo de forma sostenida desde los 1.794,9 millones de EUR de 2023).
* **Gasto de Capital (Capital Expenditure - CapEx):** -814,6 millones de EUR en 2025.
* **Flujo de Caja Libre (Free Cash Flow):** **1.386,3 millones de EUR** en 2025 (por encima de los 1.357,9 millones de EUR en 2024 y 1.194,4 millones de EUR en 2023).

---

### **3. Fundamentales y Valoración Actual**

* **Capitalización de Mercado:** ~23.838,4 millones de EUR.
* **PER (Trailing P/E):** 18,73x.
* **PER Adelantado (Forward P/E):** 14,61x (sobre un BPA estimado de 3,88 EUR, frente al BPA histórico de 3,03 EUR).
* **Valor Contable por Acción (Book Value):** 10,89 EUR (Precio sobre Valor en Libros de 5,21x).
* **Ratio Deuda Neta / EBITDA:** **1,06x** (`net_debt_ebitda` de 1,06), lo que refleja un perfil de endeudamiento moderado y saludable.
* **Rentabilidad por Dividendo (Dividend Yield):** **2,71%** (dividendo anual de 1,54 EUR por acción, con un *payout ratio* del 50,83%).
* **Rentabilidad sobre Recursos Propios (ROE):** 26,47%, demostrando una alta eficiencia en la generación de valor para los accionistas.
* **Consenso de Analistas (Target Prices):** 
  * Precio objetivo medio (*targetMeanPrice*): **69,58 EUR**.
  * Rango de precios: Mínimo 51,00 EUR / Máximo 82,00 EUR.
  * Número de opiniones de analistas: 22.
  * **Potencial de revalorización estimado (Consensus Upside):** **+22,58%** respecto al precio actual de 56,76 EUR.

---

### **4. Indicadores Técnicos y Contexto de Mercado**
* **Precio de Cierre (30/10/2026):** 56,76 EUR.
* **Medias Móviles:** SMA20 en 54,61 EUR, SMA50 en 55,04 EUR y SMA200 en 52,22 EUR (tendencia de medio plazo alcista al cotizar por encima de las medias principales).
* **RSI (14):** 59,56 (zona neutral-fuerte, sin sobrecompra ni sobreventa).
* **MACD:** 0,84 (por encima de su línea de señal 0,50, indicando impulso positivo).
* **Volatilidad (24,28%)** y un *drawdown* actual de -14,05% desde máximos recientes.
* **Titulares recientes:** La compañía ha acaparado atención en el ámbito bursátil español e internacional debido al inicio de temporada de resultados corporativos de finales de octubre de 2026, donde se estimaba una volatilidad intradía en torno al 2,5% según fuentes de Investing.com (30 de octubre de 2026). El contexto macroeconómico general del IBEX 35 muestra cautela en el sector tecnológico y presión en la banca, conviviendo con las decisiones sobre tipos de interés del BCE (mantenidos en el 2,5% a finales de octubre de 2026).

---

### **5. Evidencia y Datos Faltantes (Missing Data)**
* **Datos faltantes:** No se dispone en la instantánea analítica de las transacciones de *insiders* recientes (`get_insider_transactions`) ni de comparativas sectoriales detalladas automatizadas más allá de las métricas principales de múltiplos de valoración provistas.

---

### **6. Insights Accionables para Traders**
1. **Potencial Alcista por Consenso:** Con un precio objetivo medio de 69,58 EUR y un potencial de subida superior al 22%, `AMS.MC` ofrece un atractivo margen de seguridad fundamental para inversores orientados al crecimiento a medio plazo.
2. **Sólida Generación de Caja:** La capacidad de la compañía para escalar su Free Cash Flow por encima de los 1.380 millones de EUR y mantener una estructura de pasivo controlada (ratio Deuda Neta/EBITDA de 1,06x) avala la sostenibilidad de su política de dividendos y la inversión en innovación tecnológica.
3. **Estrategia Técnica:** Las medias móviles de 2

## II. Research Team Decision

### Bull Researcher

Bull Analyst: ¡Hola a todos! Es un verdadero placer abrir este debate para defender a **AMS.MC** (Amadeus IT Group, S.A.), una de las joyas tecnológicas indiscutibles del mercado europeo y del IBEX 35. Mientras el analista bajista seguro intentará ponernos nerviosos con los vaivenes macroeconómicos recientes de finales de octubre de 2026 o la cautela general de las bolsas, los datos fundamentales y operativos de Amadeus hablan por sí solos y demuestran por qué estamos ante una oportunidad de inversión sobresaliente. 

¡Vamos al grano y destaquemos por qué el bando alcista tiene la sartén por el mango!

### 1. Crecimiento Potencial y Escalabilidad Financiera Brillante
Para empezar, el que dude del crecimiento de `AMS.MC` solo tiene que mirar los estados financieros consolidados:
* **Ingresos al alza constante:** Pasamos de 5.441,2 millones de EUR en 2023 a 6.141,7 millones en 2024, hasta coronar los **6.517 millones de EUR en 2025**. 
* **Rentabilidad y Beneficio Neto:** El beneficio neto se ha disparado hasta los **1.335,7 millones de EUR** en 2025, superando con creces los 1.253 millones del ejercicio anterior.
* **Generación de Caja masiva:** El flujo de caja libre (*Free Cash Flow*) alcanzó los **1.386,3 millones de EUR** en 2025. Esto demuestra una capacidad de conversión de caja envidiable y una escalabilidad operativa formidable a medida que el tráfico aéreo y la digitalización global del turismo siguen expandiéndose.

### 2. Ventajas Competitivas Útiles y Dominio de Mercado
Amadeus no es una tecnológica cualquiera; opera en un foso defensivo (*moat*) altísimo. Su posición como el puente tecnológico crítico entre proveedores de viajes (aerolíneas, hoteles) y distribuidores globales le otorga un monopolio de facto o un oligopolio muy consolidado. Cambiar de proveedor de GDS o de sistemas de pasajeros (PSS) para una aerolínea gigante es un riesgo titánico que nadie quiere correr. Esa dependencia estructural asegura flujos de ingresos recurrentes y ultra-estables.

### 3. Indicadores Positivos y Salud Financiera a Prueba de Balas
Si miramos el balance y los indicadores de mercado actuales:
* **Endeudamiento muy bajo:** La ratio de Deuda Neta sobre EBITDA se sitúa en un cómodo **1,06x** (con una deuda total de unos 3.223 millones de EUR frente a un EBITDA de más de 2.479 millones y una caja considerable). Lejos de estar ahogados por la deuda, la gestionan con total holgura.
* **Valoración Atractiva (Forward P/E):** Cotizando a **56,76 EUR**, presenta un PER *forward* estimado de apenas **14,62x** (frente a un PER histórico de 18,73x), lo que indica que el mercado aún no ha descontado del todo el verdadero valor intrínseco de sus beneficios futuros.
* **Consenso de Analistas:** 22 expertos avalan su potencial, fijando un precio objetivo medio de **69,58 EUR**, lo que representa un **potencial alcista (*consensus upside*) superior al 22%** desde los niveles actuales. ¡Y ojo! El rango alto alcanza los 82,00 EUR.
* **Salud Técnica:** Las medias móviles respaldan la tendencia. El precio actual está holgadamente por encima de su SMA de 50 sesiones (55,04 EUR) y de su SMA de 200 sesiones (52,22 EUR), con un RSI en terreno neutral-alcista (59,56) que deja todo el espacio del mundo para seguir escalando.

### 4. Respondiendo al Oso (Bear Counterpoints)
Si mi colega bajista intenta argumentar que la volatilidad bursátil de octubre de 2026, la pausa de tipos del BCE al 2,5% o las dudas sobre el sector tecnológico van a frenar a Amadeus, le diré tres cosas:
1. **Resiliencia operativa frente a los tipos:** Con un balance tan robusto y una ratio de deuda neta sobre EBITDA de 1.06x, Amadeus no sufre las tensiones de financiación que ahogan a las empresas ultra-endeudadas. Los tipos estabilizados por el BCE eliminan la incertidumbre macroeconómica pesada.
2. **Crecimiento real, no expectativas vacías:** No estamos hablando de una startup tecnológica queme efectivo; hablamos de un gigante con más de 1.380 millones de EUR de FCF real y un ROE del **26,47%**. Su rentabilidad sobre recursos propios destroza cualquier argumento bajista sobre ineficiencia.
3. **El mercado ya está premiando su solidez:** El retorno a 21 sesiones del **+8,94%** demuestra que los compradores están acumulando con fuerza en los soportes técnicos clave.

En definitiva, `AMS.MC` combina un negocio con ventajas competitivas insuperables, métricas financieras saneadas, un crecimiento de beneficios indiscutible y un dividendo atractivo (2,71% de rendimiento). Los osos pueden buscar fantasmas donde no los hay, pero los números cantan.

**Rating**: HOLD  
FINAL TRANSACTION PROPOSAL: Mantener posición actual con stop-loss dinámico basado en volatilidad, vigilando soportes clave en torno a la media de 50 sesiones y la resistencia psicológica del objetivo de consenso.

### Bear Researcher

Bear Analyst: ¡Hola colega! Comprendo perfectamente tu entusiasmo y tu lectura optimista de los números de **AMS.MC**, pero creo que estás viendo el vaso medio lleno y olvidando los nubarrones oscuros que se ciernen sobre el sector y la propia estructura de valoración de la compañía. ¿Un crecimiento brillante? Vamos a diseccionar esos datos con lupa, porque la realidad de Amadeus IT Group, S.A. no es tan idílica como nos la pintas.

### 1. El espejismo del crecimiento y la desaceleración subyacente
Presumes de que los ingresos escalaron hasta los 6.517 millones de EUR en 2025 y de un beneficio neto de 1.335,7 millones. Pero si analizamos los datos con frialdad corporativa, la realidad es que **el crecimiento de los ingresos se ha ralentizado de forma alarmante**: la tasa de crecimiento de ingresos (*revenue growth*) se sitúa en un pírrico **1,5%**, y el crecimiento de los beneficios (*earnings growth*) registra incluso una **contracción del -2,6%**. 

¿Qué nos dice esto? Que la recuperación post-pandémica y el rebote inicial del tráfico aéreo ya se han agotado por completo. Amadeus ha tocado techo en su mercado principal (GDS tradicional). Pretender que estamos ante una tecnológica de alto crecimiento cuando su expansión de ventas roza el estancamiento es, cuando menos, engañoso.

### 2. Vulnerabilidades Competitivas y Amenazas de Desintermediación
Hablas de un foso defensivo (*moat*) inexpugnable y de un oligopolio consolidado. ¡Cuidado con confiarse en los laureles del pasado! La industria de los viajes está sufriendo una transformación radical:
* **El auge del NDC (New Distribution Capability):** Las aerolíneas más grandes del mundo (como el grupo Lufthansa o IAG) llevan años intentando puentear a los sistemas GDS tradicionales de Amadeus para comercializar sus billetes y servicios auxiliares directamente o a través de conexiones API más baratas, reduciendo drásticamente las comisiones que pagan a intermediarios como `AMS.MC`.
* **La presión de los gigantes tecnológicos y las OTAs:** Las agencias de viajes online (OTAs) y los metabuscadores están internalizando sus propias tecnologías de agregación. Depender de un modelo de negocio de comisiones por transacciones de billetes aéreos en un entorno donde las aerolíneas buscan recortar costes a toda costa es una vulnerabilidad estratégica enorme.

### 3. Diseccionando los Contrapuntos del Toro: ¿Tan "Blindada" Está?
Me desafías diciendo que la empresa es impermeable al entorno macroeconómico y que su ratio de deuda neta sobre EBITDA de 1.06x (con una deuda total que ronda los 3.600 millones de EUR) y su FCF de 1.386 millones de EUR la salvan de todo. Permíteme disentir punto por punto:
1. **El impacto de los tipos de interés:** Aunque el BCE haya pausado los tipos en el 2,5% a finales de octubre de 2026, nos encontramos en un régimen de tipos de interés estructuralmente más alto que la década pasada. Para una empresa con más de 3.200 millones de EUR de pasivo financiero, el coste de refinanciación y el servicio de la deuda pesan directamente sobre el beneficio neto disponible para el accionista, limitando la agresividad en fusiones, adquisiciones o recompra de acciones.
2. **Una valoración exigente frente a su baja inercia:** Cotizando a 56,76 EUR con un PER *forward* de 14,62x y un ratio Precio/Valor en Libros (*Price to Book*) desbocado de **5,21x**, el inversor está pagando una prima considerable por una compañía cuyas ganancias netas acusan un decrecimiento del -2,6%. ¿Dónde está la ganga? Con un rendimiento por dividendo del **2,71%**, tampoco estamos ante un valor refugio por retribución al accionista que compense los riesgos de mercado.
3. **El espejismo técnico:** Mencionas que el retorno a 21 sesiones del +8,94% y el RSI en 59,56 son señales inequívocas de compra. Sin embargo, si miramos el **retorno a 252 días (anual), `AMS.MC` acumula una caída del -11,44%**, y su *drawdown* se sitúa en el **-14,05%**. El valor está atrapado en un rango lateral-bajista a medio plazo, y los rebotes recientes son meros alivios técnicos dentro de una estructura de mercado dubitativa, especialmente cuando el IBEX 35 sufre por las dudas tecnológicas y la inestabilidad europea.

### Conclusión Bajista
Amadeus es una gran empresa, nadie lo niega, pero **un gran negocio no siempre es una buena inversión al precio actual**. Su crecimiento se ha frenado en seco, su modelo tradicional de intermediación aérea sufre presiones seculares por parte de las aerolíneas, y su valoración descuenta un optimismo que sus fundamentales recientes (con beneficios a la baja) no justifican. 

Por todo ello, sugiero prudencia extrema y desconfiar del "consenso alcista" de los analistas que siempre buscan sobreestimar los precios objetivos. 

**Rating**: HOLD  
FINAL TRANSACTION PROPOSAL: Mantener cautela estricta, evitando ampliar posiciones en `AMS.MC` ante la desaceleración de beneficios y el riesgo de ruptura de los soportes dinámicos de las medias móviles si el contexto macroeconómico europeo se tuerce.

### Research Manager
**Recommendation**: Hold

**Rationale**: El debate entre el analista alcista y el bajista pone de manifiesto una divergencia fundamental en la lectura de AMS.MC (Amadeus IT Group, S.A.). El bando alcista defiende la solidez operativa de la compañía, destacando sus ingresos crecientes que alcanzaron los 6.517 millones de EUR en 2025, un beneficio neto de 1.335,7 millones de EUR, un flujo de caja libre (*Free Cash Flow*) de 1.386,3 millones de EUR, un bajo endeudamiento con una ratio de deuda neta sobre EBITDA de 1,06x y un atractivo potencial alcista de consenso superior al 22% con un PER forward de 14,62x. Por otro lado, el bando bajista contrarresta con argumentos sólidos sobre la desaceleración del negocio: la tasa de crecimiento de los ingresos se ha frenado a un pírrico 1,5% y los beneficios registran una contracción del -2,6%, advirtiendo además sobre presiones competitivas como el NDC de las aerolíneas, un ratio Precio/Valor en Libros elevado de 5,21x y un rendimiento anual a 252 días negativo (-11,44%) con un drawdown del -14,05%. Al sopesar ambos lados, aunque los fundamentales de caja y la rentabilidad sobre recursos propios (ROE del 26,47%) apoyan la calidad de la empresa, la desaceleración en los beneficios y el contexto técnico lateral-bajista a un año vista neutralizan las señales alcistas a corto plazo. Ninguno de los dos bandos logra inclinar la balanza de forma decisiva para justificar una compra o una venta agresiva, por lo que la recomendación equilibrada es Hold.

**Strategic Actions**: Mantener la exposición actual en AMS.MC sin realizar nuevas ampliaciones de cartera. Se recomienda instruir al trader para que establezca un stop-loss dinámico vigilando de cerca los soportes clave en torno a la media móvil de 50 sesiones (55,04 EUR) y de 200 sesiones (52,22 EUR). Cualquier asignación debe considerarse de manera estrictamente hipotética y neutral dentro de un portafolio estándar, a la espera de observar una aceleración real en el crecimiento de los beneficios que rompa el actual rango lateral.

## III. Trading Team Plan

### Trader
**Action**: Hold

**Reasoning**: La recomendación de mantenimiento se fundamenta en la contraposición entre unos sólidos fundamentales de flujo de caja y rentabilidad sobre recursos propios (ROE del 26,47%) y una desaceleración en el crecimiento de beneficios (-2,6%) junto con un entorno técnico lateral-alcista a corto plazo respaldado por el RSI de 59,56. Ante la divergencia entre la infravaloración respecto al precio objetivo de consenso (69,58 EUR) y los riesgos de desaceleración en la tasa de crecimiento de ingresos (1,5%), se aconseja no incrementar la exposición en este momento.

**Entry Price**: not provided

**Stop Loss**: 52.22

**Position Sizing**: 5% of portfolio

FINAL TRANSACTION PROPOSAL: **HOLD**

## IV. Risk Management Team Decision

### Aggressive Analyst

Aggressive Analyst: ¡Atención a todos los analistas de la mesa! Mientras la postura conservadora y la neutral se ahogan en un exceso de cautela y temen fantasmas donde solo hay oportunidades de oro, nosotros, desde la perspectiva agresiva, vemos el verdadero motor del crecimiento en `AMS.MC`. 

El analista conservador y el neutral se escudan en una supuesta desaceleración de los beneficios del -2,6% y en un crecimiento de ingresos del 1,5% para justificar la inacción, sugiriendo una postura de "esperar y ver". ¡Qué error tan monumental! Están ignorando por completo la increíble robustez operativa y los fundamentales de primera categoría que tiene Amadeus IT Group, S.A. ¿Acaso están ciegos ante un ROE espectacular del 26,47%? ¿Desprecian un flujo de caja libre que supera los 1.386 millones de EUR y una ratio de deuda neta sobre EBITDA sumamente sana de 1,06x? Amigos, una compañía con esta capacidad de generación de caja no se estanca: se está blindando y acumulando la potencia de fuego necesaria para aplastar a la competencia en cuanto el sector tecnológico despegue con fuerza.

Además, su miedo ante una ligera desaceleración temporal pasa por alto el dato clave que los analistas institucionales tienen sobre la mesa: el consenso apunta a un precio objetivo medio de 69,58 EUR. ¡Estamos hablando de un potencial alcista del 22,58% desde los actuales 56,76 EUR! Conformarse con un simple "Hold" sin buscar ampliar posiciones o capitalizar este recorrido es regalar rentabilidad en bandeja de plata. 

En el frente técnico, sus dudas son igual de infundadas. El RSI se encuentra en un saludable 59,56, perfectamente equilibrado, sin rastro de sobrecompra, y el MACD en 0,84 cruzando por encima de su señal confirma un impulso comprador totalmente vigente. El precio cotiza cómodamente por encima de la media móvil de 50 sesiones (55,04 EUR) y de la de 200 sesiones (52,22 EUR), lo que demuestra que la tendencia alcista de fondo está más viva que nunca. Pararse a dudar justo cuando los indicadores técnicos muestran fortaleza y el Forward P/E se comprime atractivamente a 14,62x es perder el tren de la innovación y la disrupción tecnológica en la industria de viajes.

Mantenerse pasivos ante un activo con semejante margen de crecimiento y con catalizadores tan claros es el verdadero riesgo. No podemos permitirnos la parálisis por análisis cuando `AMS.MC` está lista para romper resistencias y darnos enormes alegrías bursátiles. ¡Hay que ser audaces y posicionarse para capturar ese +22% de upside!

**Rating**: BUY
FINAL TRANSACTION PROPOSAL: BUY

### Conservative Analyst

Conservative Analyst: Estimado colega agresivo, entiendo perfectamente el entusiasmo que despierta un ROE del 26,47% y una generación de flujo de caja libre superior a los 1.386 millones de EUR en Amadeus IT Group, S.A., pero su análisis obvia el principio fundamental de nuestra mesa: proteger el capital de la firma ante cualquier eventualidad adversa. Calificar nuestra prudencia de "parálisis" es ignorar las señales claras de desaceleración que ya lastran los beneficios de `AMS.MC`, con una tasa de crecimiento de ganancias del -2,6% y un crecimiento de ingresos estancado en el 1,5%. 

Confiar ciegamente en el precio objetivo de consenso de 69,58 EUR es un error de análisis imperdonable para la gestión de riesgos; los objetivos de los analistas son estimaciones teóricas, no valores intrínsecos garantizados, y asumir un potencial alcista del 22,58% en un entorno macroeconómico europeo tan frágil —donde el BCE mantiene los tipos en el 2,5% y las bolsas se mueven de forma mixta y dubitativa— expone a la cartera a una volatilidad innecesaria. 

Aunque los indicadores técnicos como el RSI en 59,56 y el MACD positivo muestran cierta fortaleza a corto plazo, la rentabilidad a 252 días sigue registrando un retroceso del -11,44% y el valor arrastra un *drawdown* del -14,05%. Exigir una expansión de posición en este momento, tal como propone la postura agresiva, es asumir un riesgo de capital desmedido ante la menor señal de debilidad en el sector tecnológico. La estabilidad y la seguridad a largo plazo se construyen manteniendo la disciplina y protegiendo los activos con un estricto stop-loss, no persiguiendo rebotes impulsivos. Por tanto, reafirmamos que la única decisión sensata para salvaguardar el patrimonio de la firma es mantener una postura cautelosa.

**Rating**: HOLD
FINAL TRANSACTION PROPOSAL: HOLD

### Neutral Analyst

Neutral Analyst: Escuchando tanto al analista agresivo como al conservador sobre `AMS.MC`, resulta evidente que ambos cometen el error de llevar sus posturas al extremo, ignorando los matices que ofrece la realidad de los datos. 

Por un lado, el analista agresivo peca de un optimismo desmedido al exigir una expansión inmediata de la cartera. Ignora por completo que un crecimiento de ingresos del 1,5% y una contracción de beneficios del -2,6% no son datos menores; son señales de advertencia sobre la madurez temporal del ciclo operativo de Amadeus IT Group, S.A.. Dar por sentado que el precio objetivo de consenso de 69,58 EUR se materializará de forma lineal es un acto de fe injustificado, sobre todo cuando el valor arrastra un *drawdown* del -14,05% y una rentabilidad a 252 días del -11,44%. Comprar de forma agresiva en este contexto técnico lateral-alcista, sin confirmar una aceleración real en la demanda, es exponerse a una volatilidad innecesaria en un entorno macroeconómico europeo donde el BCE mantiene los tipos estables en el 2,5% y las bolsas muestran dudas generalizadas.

Por otro lado, el analista conservador se refugia en una cautela excesiva que roza la parálisis. Desecha el enorme valor intrínseco que reflejan un ROE del 26,47%, una conversión de flujo de caja libre superior a los 1.386 millones de EUR y una ratio de deuda neta sobre EBITDA sumamente sana de 1,06x. Calificar el escenario como un peligro inminente es pasar por alto que la compañía no está en decadencia, sino en una fase de consolidación respaldada por medias móviles clave —como la de 50 sesiones en 55,04 EUR y la de 200 sesiones en 52,22 EUR— y un RSI de 59,56 que muestra un impulso comprador perfectamente saludable y sin sobrecompra. Quedarse estáticos por miedo a la macroeconomía global implica ignorar que la calidad fundamental de `AMS.MC` merece un voto de confianza operativo, no un rechazo defensivo.

La verdadera estrategia óptima y equilibrada se encuentra en el término medio: mantener la posición actual sin arriesgar nuevo capital (un 5% de asignación hipotética ya es una exposición razonable), protegiendo estrictamente la operativa con el stop-loss situado en 52,22 EUR. Esto nos permite capturar el potencial alcista de la compañía hacia la zona de consenso y aprovechar su sólida generación de caja sin asumir el riesgo desmedido de incrementar compras en medio de una desaceleración de beneficios a corto plazo.

**Rating**: HOLD
FINAL TRANSACTION PROPOSAL: **HOLD**

## V. Portfolio Manager Decision

### Portfolio Manager
**Rating**: Hold

**Executive Summary**: Mantener la exposición actual en AMS.MC sin realizar nuevas ampliaciones de cartera ante la desaceleración de beneficios. Se recomienda instruir al trader para fijar un stop-loss en 52,22 EUR y limitar cualquier asignación hipotética al 5% del portafolio, adoptando un horizonte de 3 a 6 meses.

**Investment Thesis**: El debate entre el analista agresivo, el conservador y el neutral pone de manifiesto una divergencia fundamental en la lectura de AMS.MC. Por un lado, el bando alcista destaca la solidez de los fundamentales de calidad: un ROE del 26,47%, un flujo de caja libre superior a 1.386 millones de EUR, una ratio de deuda neta sobre EBITDA muy sana de 1,06x, un Forward P/E de 14,62x y un potencial alcista de consenso superior al 22% frente a un objetivo de 69,58 EUR. Asimismo, los indicadores técnicos muestran un RSI en 59,56 y una cotización holgada por encima de la media móvil de 50 sesiones (55,04 EUR) y de la de 200 sesiones (52,22 EUR). Por otro lado, la postura conservadora y neutral advierte con razón sobre la desaceleración operativa, evidenciada por un crecimiento de ingresos estancado en el 1,5% y una contracción de beneficios del -2,6%, además de un rendimiento a 252 días del -11,44% y un drawdown del -14,05% en un entorno macroeconómico europeo dubitativo con tipos del BCE en el 2,5%. Al sopesar las evidencias, aunque la calidad financiera e industrial de Amadeus IT Group, S.A. es incuestionable, la debilidad en el crecimiento de los beneficios y la persistencia de un perfil técnico lateral a un año vista neutralizan los argumentos para una compra agresiva. Dado que el balance entre los riesgos de desaceleración a corto plazo y la solidez de caja genera un escenario equilibrado, la recomendación fundamentada es Hold.

**Price Target**: 69.58

**Time Horizon**: 3-6 months