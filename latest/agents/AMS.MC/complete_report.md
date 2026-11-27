# Trading Analysis Report: AMS.MC

- Analysis date: 2026-11-27
- Rating: Hold
- Generated: 2026-11-27 20:57:22
- TradingAgents 0.7.1: google, deep gemini-3.5-flash-lite, quick gemini-3.5-flash-lite
- Analysts: market, news, fundamentals; research debate rounds 1, risk debate rounds 1
- Data vendors: core_stock_apis yfinance, technical_indicators yfinance, fundamental_data yfinance, news_data yfinance, macro_data fred, prediction_markets polymarket, get_news ibex_sample, get_global_news ibex_sample

## I. Analyst Team Reports

### Market Analyst
**Rating**: BUY  
FINAL TRANSACTION PROPOSAL: Comprar con asignación hipotética parcial aprovechando la tendencia alcista de medio plazo y la fortaleza técnica actual, manteniendo disciplina mediante stops basados en volatilidad.

### Informe de Análisis Financiero y Técnico para Amadeus IT Group, S.A. (`AMS.MC`)

#### 1. Contexto de Mercado y Datos Fundamentales
Amadeus IT Group, S.A. (`AMS.MC`) cotiza en la bolsa de Madrid (MCE) dentro del sector de Tecnología (Information Technology Services). Con una capitalización bursátil de aproximadamente **26.360 millones de EUR**, la compañía mantiene sólidas métricas fundamentales:
* **Ingresos (2025):** 6.517 millones de EUR, frente a los 6.141 millones de EUR en 2024.
* **Beneficio Neto (2025):** 1.335,7 millones de EUR (crecimiento interanual sostenido desde los 1.253 millones en 2024).
* **Márgenes y Rentabilidad:** Margen de beneficio neto del 19,86% y un ROE (Return on Equity) elevado del 26,44%.
* **Valoración:** PER histórico (*trailing PE*) de 20,18x y un PER estimado a futuro (*forward PE*) de 16,04x. La compañía ofrece un dividendo por acción de 1,54 EUR, lo que representa una rentabilidad por dividendo (*dividend yield*) del **2,49%** (ratio de pago o *payout ratio* del 49,52%).
* **Deuda y Solvencia:** Deuda total de 3.500 millones de EUR (con una deuda neta sobre EBITDA de **1,03x**, nivel moderado y saludable). El flujo de caja libre (*free cash flow*) asciende a unos 1.106 millones de EUR.
* **Consenso de Analistas:** El precio objetivo medio de consenso se sitúa en **71,47 EUR** (con un rango entre 53,00 EUR y 82,00 EUR basado en 23 opiniones de analistas), lo que implica un potencial alcista (*consensus upside*) del **13,88%** respecto al precio actual de cierre.

---

#### 2. Análisis Técnico y Dinámica de Precios
Según la instantánea de mercado de fecha **27 de noviembre de 2026**, el valor cerró en **62,76 EUR**, experimentando una subida diaria del **1,39%**. 

* **Medias Móviles:** El precio se encuentra holgadamente por encima de sus principales referencias de tendencia:
  * SMA de 20 sesiones: **60,99 EUR**
  * SMA de 50 sesiones: **56,90 EUR**
  * SMA de 200 sesiones: **53,05 EUR**  
  Esta alineación refleja una estructura alcista clara tanto a corto, medio como largo plazo.
* **Momentum e Indicadores:** 
  * RSI (14 periodos) en **65,98**, reflejando un tono de fortaleza compradora pero sin entrar todavía en zona de sobrecompra crítica (>70).
  * MACD en **1,26** y línea de señal en **1,40**, mostrando convergencia positiva tras el impulso reciente de las últimas sesiones.
* **Volatilidad y Retornos:** La volatilidad histórica anualizada se sitúa en el **25,03%**, con un rendimiento a 21 sesiones del **9,72%** y a 63 sesiones del **11,87%**, superando al índice de referencia (`^IBEX`) en el medio plazo (rendimiento relativo de +14,08 puntos porcentuales a 63 sesiones). El valor se encuentra a solo un **1,09%** de sus máximos recientes (drawdown mínimo).

---

#### 3. Selección de Indicadores Complementarios
Para un seguimiento óptimo y libre de redundancias en la estrategia sobre `AMS.MC`, se seleccionan los siguientes 8 indicadores clave de las categorías permitidas:

1. **`close_50_sma`**: Indicador de tendencia a medio plazo. Permite identificar la dirección general y actúa como soporte dinámico en correcciones técnicas.
2. **`close_200_sma`**: Punto de referencia a largo plazo para confirmar la estructura macro alcista y descartar cambios de ciclo estructurales.
3. **`close_10_ema`**: Media móvil exponencial rápida para capturar entradas tácticas y cambios rápidos de inercia a muy corto plazo.
4. **`macd`**: Oscilador de impulso basado en la divergencia/convergencia de medias exponenciales para detectar puntos de giro e intensidades de tendencia.
5. **`rsi`**: Mide la velocidad del cambio de precios para supervisar zonas de sobrecompra o sobreventa (con referencia en los umbrales de 70/30).
6. **`boll_ub` (Banda Superior de Bollinger)**: Delimitador superior de volatilidad (2 desviaciones típicas sobre la SMA 20) útil para monitorizar zonas de resistencia dinámica y rupturas alcistas.
7. **`boll_lb` (Banda Inferior de Bollinger)**: Delimitador inferior de volatilidad para identificar escenarios de sobreventa temporal o suelos de corto plazo.
8. **`atr` (Average True Range)**: Medida absoluta de la volatilidad para dimensionar correctamente el riesgo y fijar niveles de *stop-loss* adaptativos.

---

#### 4. Evidencia y Fuentes
* **Cotización y Datos Técnicos/Fundamentales:** Extraídos del snapshot verificado con fecha de referencia `2026-11-27` y fuentes adjuntas de Yahoo Finance (`https://finance.yahoo.com/quote/AMS.MC/`).
* **Noticias Macroeconómicas y del Sector:** Cobertura de prensa financiera en España de fecha 26-27 de noviembre de 2026 (Rankia, Merca2.es, Bolsamania, Negocios.com), destacando el tono positivo generalizado en bolsas europeas y valores tecnológicos e industriales.
* **Datos Faltantes / Limitaciones:** No se dispone de un desglose por segmentos de negocio hiperdetallado en tiempo real dentro del extracto automatizado, ni de un portfolio de asignación de capital propio (toda mención de riesgo o dimensionamiento es puramente hipotética). Los precios objetivos son estimaciones de consenso de analistas, no valoraciones intrínsecas cerradas.

---

#### 5. Resumen Clave en Formato Tabla

| Categoría | Métrica / Indicador | Valor / Estado Actual | Interpretación Operativa para `AMS.MC` |
| :--- | :--- | :--- | :--- |
| **Precio y Tendencia** | Cierre Actual (`AMS.MC`) | 62,76 EUR (+1,39%) | Tendencia alcista sólida, apoyada en rebote europeo de finales de noviembre de 2026. |
| **Medias Móviles** | SMA 50 / SMA 200 | 56,90 EUR / 53,05 EUR | Alineación alcista clara; el precio cotiza netamente por encima de ambas directrices clave. |
| **Momentum** | RSI (14) | 65,98 | Fuerza compradora activa, sin señales extremas de sobrecompra inmediata. |
| **Valoración** | PER Estimado (Forward PE) | 16,04x | Valoración razonable frente a su crecimiento de beneficios y márgenes operativos (ROE 26%). |
| **Consenso** | Precio Objetivo Medio | 71,47 EUR | Margen de revalorización potencial estimado por el consenso de analistas del ~13,88%. |
| **Solvencia** | Deuda Neta / EBITDA | 1

### News Analyst
**Rating**: REVIEW

### Informe de Análisis Macroeconómico y de Mercado para `AMS.MC`

#### 1. Resumen Ejecutivo y Entorno Macroeconómico Global (Noviembre 2026)
El análisis actual se enmarca en un contexto de rebote generalizado de las bolsas europeas y tecnológicas a finales de noviembre de 2026, a pesar de señales de desaceleración económica en ciertas economías clave como Francia y la moderación del IPC en noviembre de 2026 (descendiendo al 4,1%, según referencias de Rankia del 27/11/2026). Las bolsas europeas y tecnológicas han prolongado las subidas semanales, firmando los mejores registros desde 2022 para algunos índices globales y avanzando con fuerza impulsadas por tecnología y banca. 

Para `AMS.MC` (Amadeus IT Group, S.A.), cotizada en el mercado continuo de Madrid (`MCE`) dentro del sector de Tecnología y Servicios de Tecnologías de la Información, este entorno de optimismo bursátil coincide con una sólida posición técnica y fundamental.

#### 2. Análisis Fundamental y Financiero de `AMS.MC`
Con los datos financieros más recientes correspondientes al cierre fiscal y las estimaciones actualizadas al 27/11/2026:
* **Capitalización de Mercado**: ~26.360 millones de EUR.
* **Precio de Cierre**: 62,76 EUR (con fecha 27/11/2026), experimentando una variación diaria positiva del +1,39%.
* **Valoración y Beneficios**: Presenta un PER histórico (*trailing P/E*) de 20,18x y un PER adelantado (*forward P/E*) de 16,04x. El beneficio por acción (*EPS*) estimado a futuro es de 3,91 EUR frente a los 3,11 EUR históricos.
* **Crecimiento e Ingresos**: Los ingresos totales alcanzaron los 6.517 millones de EUR en el ejercicio cerrado a diciembre de 2025, superando los 6.141 millones de 2024. El EBITDA se sitúa en 2.534,7 millones de EUR para 2025.
* **Solvencia y Deuda**: La deuda neta sobre EBITDA se mantiene en un nivel moderado y manejable de aproximadamente 1,03x (Deuda total de ~3.224 millones de EUR frente a un efectivo de ~913 millones de EUR en el balance más reciente).
* **Flujo de Caja y Dividendos**: El flujo de caja libre (*free cash flow*) asciende a 1.386 millones de EUR (ejercicio 2025), apoyando una rentabilidad por dividendo (*dividend yield*) estimada en el rango del 2,45% - 2,49%, con una ratio de pago (*payout ratio*) cercana al 49,5%.

#### 3. Situación Técnica
* **Indicadores de Momento y Tendencia**: El valor cotiza en 62,76 EUR, superando holgadamente sus medias móviles clave (SMA20 en 60,99 EUR, SMA50 en 56,90 EUR y SMA200 en 53,05 EUR), lo que confirma una tendencia alcista clara en el medio y largo plazo.
* **RSI y Osciladores**: El RSI de 14 sesiones se sitúa en 65,98, reflejando un tono alcista robusto sin entrar de lleno en zona de sobrecompra extrema. El MACD se encuentra en 1,26 con su línea de señal en 1,40.
* **Rentabilidad Reciente**: Registra una rentabilidad a 21 sesiones del +9,72% y a 63 sesiones del +11,87%, superando al índice de referencia (`^IBEX`) en rendimiento relativo a 63 días en 14,08 puntos porcentuales.
* **Consenso de Analistas**: El precio objetivo medio de consenso (*targetMeanPrice*) se ubica en 71,47 EUR, con un rango que va desde un mínimo de 53,00 EUR hasta un máximo de 82,00 EUR (basado en 23 opiniones de analistas), lo que implica un potencial alcista estimado (*consensus upside*) del 13,88% desde los niveles actuales.

#### 4. Evidencia y Datos Faltantes
* **Evidencia de Soporte**: Datos bursátiles y financieros exactos extraídos de la instantánea de `AMS.MC` con fecha 27/11/2026. Titulares macroeconómicos y sectoriales de la prensa financiera española (Merca2.es, Bankinter, Rankia, Negocios.com, Bolsamania, El Boletín) comprendidos entre el 26 y el 27 de noviembre de 2026.
* **Datos Faltantes**: No se dispone de un desglose detallado en tiempo real de las operaciones intradía posteriores al cierre del 27 de/11/2026 ni de las actas completas de la próxima junta directiva. No se ha suministrado cartera de inversión previa (toda asignación hipotética debe ser evaluada individualmente).

| Componente de Análisis | Estado / Métrica Clave (`AMS.MC`) | Observaciones Relevantes |
| :--- | :--- | :--- |
| **Precio Actual** | 62,76 EUR (27/11/2026) | Variación diaria de +1,39%; por encima de SMA20, SMA50 y SMA200. |
| **Valoración (PER)** | 20,18x (Trailing) / 16,04x (Forward) | Mejora en la eficiencia de beneficios esperados para los próximos periodos. |
| **Solvencia y Deuda** | Deuda Neta / EBITDA ~1.03x | Estructura financiera sólida con pasivos controlados. |
| **Consenso de Mercado** | 71,47 EUR (Precio Objetivo Medio) | Potencial alcista estimado de ~13,88% con 23 analistas cubriendo el valor. |
| **Entorno Macroeconómico** | Rebote bursátil europeo / IPC noviembre al 4,1% | Contexto favorable para activos de riesgo y tecnología a finales de noviembre de 2026. |

FINAL TRANSACTION PROPOSAL: REVIEW

### Fundamentals Analyst
**Rating**: HOLD  
FINAL TRANSACTION PROPOSAL: NO ACTION / REVIEW  

---

### **Informe Fundamental y de Mercado: Amadeus IT Group, S.A. (`AMS.MC`)**

#### **1. Perfil de la Empresa y Contexto de Negocio**
* **Compañía:** Amadeus IT Group, S.A. (`AMS.MC`)
* **Negocio principal:** Tecnología / Servicios de Tecnologías de la Información (proveedor de soluciones tecnológicas para la industria global de los viajes y el turismo).
* **Bolsa / Divisa:** Bolsa de Madrid (MCE) / EUR.
* **Fecha de referencia del análisis:** 27 de noviembre de 2026.

---

#### **2. Análisis Técnico y Comportamiento Bursátil recientes**
* **Precio de cierre actual:** 62.76 EUR (`AMS.MC`, cotización a 27 de noviembre de 2026).
* **Rentabilidad a corto y medio plazo:** 
  * Variación en la última sesión: +1.39%.
  * Retorno a 21 sesiones: +9.72%.
  * Retorno a 63 sesiones: +11.87% (superando al índice de referencia en 14.08 puntos porcentuales).
  * Retorno a 52 semanas (252 sesiones): +4.92%.
* **Indicadores Técnicos:**
  * **RSI (14):** 65.98 (situado en zona moderadamente alcista, sin entrar todavía en sobrecompra extrema).
  * **MACD:** 1.259 (por debajo de su línea de señal en 1.396, sugiriendo un ligero proceso de consolidación tras las recientes subidas).
  * **Medias Móviles:** El precio cotiza holgadamente por encima de su SMA de 20 sesiones (60.99 EUR), SMA de 50 sesiones (56.90 EUR) y SMA de 200 sesiones (53.05 EUR), confirmando una estructura de tendencia alcista consolidada a medio y largo plazo.
  * **Volatilidad (anualizada):** 25.03%.
  * **Drawdown actual:** -1.09% (cercano a máximos recientes).

---

#### **3. Estados Financieros e Historial Financiero**
Basado en los datos consolidados y los estados financieros provistos para `AMS.MC`:

* **Cuenta de Resultados (Ingresos y Beneficios):**
  * **Ingresos Totales:** 6,517.0 millones de EUR (cierre de ejercicio 2025), frente a 6,141.7 millones de EUR en 2024 y 5,441.2 millones de EUR en 2023. Muestra un crecimiento sostenido de la cifra de negocio.
  * **EBITDA:** 2,534.7 millones de EUR en 2025 (vs. 2,353.2 millones de EUR en 2024 y 2,134.2 millones de EUR en 2023).
  * **Beneficio Neto (Net Income):** 1,335.7 millones de EUR (2025), comparado con 1,253.0 millones de EUR (2024) y 1,117.6 millones de EUR (2023).
* **Balance de Situación:**
  * **Activos Totales:** 11,470.9 millones de EUR (2025).
  * **Deuda Total:** 3,223.6 millones de EUR (2025), descendiendo desde los 3,375.7 millones de EUR registrados en 2024.
  * **Patrimonio Neto (Stockholders Equity):** 4,853.7 millones de EUR (2025).
* **Flujo de Caja (Cash Flow):**
  * **Flujo de Caja Operativo:** 2,200.9 millones de EUR en 2025 (superando los 2,146.0 millones de EUR de 2024).
  * **Inversión en CapEx:** -814.6 millones de EUR (2025).
  * **Flujo de Caja Libre (Free Cash Flow):** 1,386.3 millones de EUR (2025), incrementándose de manera constante desde los 1,357.9 millones de EUR de 2024 y los 1,194.4 millones de EUR de 2023.

---

#### **4. Fundamentales y Valoración Actual**
* **Capitalización de mercado:** 26,358.7 millones de EUR (`AMS.MC`).
* **Múltiplos de Valoración:**
  * **PER histórico (Trailing P/E):** 20.18x.
  * **PER estimado (Forward P/E):** 16.04x (calculado con un BPA estimado de 3.91 EUR frente al BPA histórico de 3.11 EUR).
  * **Precio sobre Valor en Libros (Price-to-Book):** 5.29x.
  * **EV/EBITDA:** 11.39x.
* **Solvencia y Endeudamiento:**
  * **Deuda Neta / EBITDA:** ~1.03x (ratio saludable y manejable para una compañía tecnológica de gran capitalización).
* **Rentabilidad y Dividendos:**
  * **ROE (Return on Equity):** 26.44%, reflejando una excelente eficiencia en la asignación de capital a los accionistas.
  * **Margen de Beneficio (Profit Margins):** 19.86%.
  * **Crecimiento:** Crecimiento interanual de ingresos del 6.4% y de beneficios del 9.8%.
  * **Dividendo:** Rentabilidad por dividendo (*dividend yield*) del 2.45% - 2.49%, con un dividendo por acción de 1.54 EUR y un *payout ratio* moderado del 49.52%.
* **Consenso de Analistas y Precios Objetivo:**
  * **Precio objetivo medio (*Target Mean Price*):** 71.47 EUR.
  * **Precio objetivo bajo / alto:** 53.00 EUR / 82.00 EUR.
  * **Número de analistas:** 23.
  * **Potencial alcista según consenso (*Consensus Upside*):** +13.88% respecto al precio de cotización actual (62.76 EUR).

---

#### **5. Información Externa y Noticias Recientes**
* Las bolsas europeas y los valores tecnológicos han mostrado un tono positivo y de rebote generalizado a finales de noviembre de 2026 (impulsadas por expectativas macroeconómicas favorables en Europa y datos de inflación a la baja), lo que favorece el impulso técnico reciente de `AMS.MC`.
* Publicaciones especializadas recientes (como *Rankia* el 23 de noviembre de 2026) monitorizan de cerca las estrategias de inversión, fiscalidad y políticas de dividendo de Amadeus desde España.

---

#### **6. Conclusión, Evidencia Faltante y Perspectiva de Inversión**
* **Argumentos a favor (Supporting Evidence):** Sólida generación de flujo de caja libre (superior a 1.380 millones de EUR en 2025), un ROE elevado (26.4%), un ratio de endeudamiento moderado (Deuda Neta/EBITDA en torno a 1.03x) y un potencial de revalorización de doble dígito según el consenso de analistas (+13.88% hasta los 71.47

## II. Research Team Decision

### Bull Researcher

Bull Analyst: ¡Hola a todos! Comprendo perfectamente que algunos analistas prefieran adoptar una postura de cautela u optar por un "HOLD / REVIEW" ante el entorno macroeconómico global, pero como analista alcista de **`AMS.MC`**, creo que mirar de reojo los riesgos nos está haciendo pasar por alto una de las tesis de inversión más sólidas y rentables del sector tecnológico europeo actual. 

Vamos a debatir con datos en la mano y desmontar por qué el bando bajista se está quedando corto frente a la realidad operativa y bursátil de la compañía.

---

### 1. Crecimiento Potencial y Escalatividad: Los números hablan por sí solos
El argumento de que el crecimiento podría estancarse simplemente no se sostiene al revisar los estados financieros consolidados. ¿De qué estancamiento hablamos cuando los ingresos totales pasaron de 5.441 millones de EUR en 2023 a 6.141 millones en 2024, y escalaron hasta los **6.517 millones de EUR** al cierre de 2025? 

Además, la compañía traduce este crecimiento comercial en una máquina de generar caja: el **Free Cash Flow (FCF)** alcanzó los **1.386 millones de EUR** en 2025 (por encima de los 1.357 millones de 2024 y los 1.194 millones de 2023). Con un margen neto cercano al **19,86%** y un **ROE (Return on Equity) sobresaliente del 26,44%**, Amadeus demuestra que su modelo de negocio es altamente escalable. No estamos ante una promesa tecnológica queme caja; estamos ante un líder consolidado que monetiza cada euro invertido con una eficiencia envidiable.

### 2. Ventajas Competitivas y Posicionamiento Dominante
Se suele argumentar que la competencia en servicios de TI e infraestructura de viajes es feroz. Sin embargo, Amadeus opera en un foso defensivo (*moat*) casi impenetrable. Su tecnología conecta a aerolíneas, hoteles, agencias de viajes y pasajeros a una escala global donde los costes de cambio (*switching costs*) para los clientes corporativos son prohibitivos. Su infraestructura es el sistema nervioso central de la industria turística global. Esta posición dominante es la que le permite mantener un EBITDA superior a los **2.534 millones de EUR** (cierre de 2025) y una **ratio de deuda neta sobre EBITDA de apenas 1,03x**, un nivel de apalancamiento sumamente conservador y saludable que disipa cualquier fantasma sobre su solvencia financiera.

### 3. Indicadores Positivos y Momentum Técnico
¿Ignoramos el comportamiento del mercado? Los datos técnicos con fecha a 27 de noviembre de 2026 muestran a **`AMS.MC`** cotizando en **62,76 EUR**, apoyada por un rebote generalizado en las bolsas europeas y tecnológicas. 
* El valor cotiza holgadamente por encima de sus medias móviles clave: la SMA de 20 sesiones (60,99 EUR), la de 50 sesiones (56,90 EUR) y la de 200 sesiones (53,05 EUR).
* Su rendimiento a 63 sesiones (+11,87%) supera con creces al índice de referencia (`^IBEX`) por más de 14 puntos porcentuales.
* Con un **RSI en 65,98**, el valor muestra una fuerza compradora limpia, sin estar en zona de sobrecompra crítica, y un PER estimado a futuro (*forward P/E*) muy atractivo de **16,04x** (frente a un PER histórico de 20,18x), lo que indica que el beneficio por acción esperado (que sube hasta los 3,91 EUR) hará que la acción esté aún más barata en términos relativos.

### 4. Respondiendo al Oso: ¿Por qué el argumento bajista falla?
Los osos suelen argumentar que la valoración actual (con un múltiplo de precio sobre valor en libros de 5,29x) es exigente y que cualquier bache macroeconómico en el consumo de viajes podría castigar el valor. Pero olvida tres realidades clave:
1. **La deuda está bajo absoluto control:** Con una deuda total de 3.223 millones de EUR frente a una caja y flujos operativos robustos (más de 2.200 millones de EUR de flujo de caja operativo en 2025), Amadeus no sufre por los tipos de interés elevados. Su estructura de pasivo es modélica.
2. **El consenso apunta al doble dígito alcista:** No soy solo yo; el consenso de los **23 analistas** que cubren el valor sitúa el precio objetivo medio en **71,47 EUR**, lo que representa un **potencial alcista del 13,88%** desde los niveles actuales, con techos de hasta 82,00 EUR.
3. **Retribución al accionista:** Ofrece una rentabilidad por dividendo (*dividend yield*) del **2,49%** con un *payout* sostenible del 49,52%, combinando crecimiento y retribución directa al inversor.

### Conclusión y Propuesta
En resumen, quedarse al margen (*review* o *hold*) cuando una compañía con un ROE del 26%, un flujo de caja libre superior a 1.380 millones y una posición técnica impecable está rompiendo resistencias es perderse el movimiento alcista de medio plazo. La tendencia es clara y los fundamentales son de roca. 

**Rating**: BUY  
FINAL TRANSACTION PROPOSAL: Comprar con asignación hipotética parcial en `AMS.MC`, aprovechando la sólida estructura técnica por encima de sus medias móviles y el potencial de revalorización hacia el objetivo de consenso, protegiendo la posición con una gestión de riesgo basada en la volatilidad actual.

### Bear Researcher

Bear Analyst: ¡Hola, colega! Admiro tu optimismo y reconozco que los números de **`AMS.MC`** a primera vista parecen relucir, pero te estás dejando cegar por un espejo retrovisor. Agarrarse a las cifras de un rebote coyuntural a finales de noviembre de 2026 y a un flujo de caja pasado es ignorar los nubarrones estructurales y macroeconómicos que se ciernen sobre el valor. Vamos a desarmar punto por punto esa tesis alcista tan complaciente.

### 1. ¿Crecimiento sostenible o trampa de madurez y saturación?
Presumes de que los ingresos escalaron hasta los 6.517 millones de EUR en 2025 y hablas de una escalabilidad envidiable. Pero miremos la realidad bajo el capó: el crecimiento interanual de los ingresos se desacelera a un modesto **6,4%**, un ritmo bastante mediocre para una compañía que cotiza con un múltiplo de **Price-to-Book de 5,29x** y un PER histórico superior a 20x (**20,18x**). 

Estás pagando una prima de crecimiento tecnológico por un negocio que, en el fondo, depende de los volúmenes globales de viajes. Con una economía europea cojeando —recuerda los avisos de desaceleración en Francia y un IPC que lucha por estabilizarse al 4,1%—, el sector turístico global se enfrenta a una fatiga del consumidor inevitable. ¿Qué pasará con ese codiciado *Free Cash Flow* de 1.386 millones si la demanda de vuelos y reservas sufre un frenazo por la erosión del poder adquisitivo? El margen de error a estos múltiplos es peligrosamente estrecho.

### 2. El "Foso Defensivo" (*Moat*) tiene goteras: Vulnerabilidad competitiva e innovación
Hablas de un foso defensivo impenetrable y de costes de cambio prohibitivos para las aerolíneas y agencias. ¡Cuidado con la complacencia! La industria de la distribución de viajes y la tecnología TI (GDS) está sufriendo presiones seculares por parte de la desintermediación directa (las aerolíneas impulsando sus propias conexiones NDC) y la irrupción de soluciones nativas en la nube y basadas en inteligencia artificial más ágiles. 

Amadeus es un gigante pesado. Mantener esa infraestructura mastodóntica requiere inversiones de capital (*CapEx*) crecientes —más de 814 millones de EUR en 2025— que erosionan la conversión real de caja a largo plazo. Confundir posición histórica dominante con inmunidad tecnológica frente a competidores más ágiles es un error de bulto en el sector tecnológico.

### 3. Espejismo técnico y sobreextensión
Te aferras a que **`AMS.MC`** cotiza en **62,76 EUR** por encima de sus medias móviles (SMA 20 en 60,99 EUR, SMA 50 en 56,90 EUR) y celebras un RSI en **65,98**. Pero precisamente esos niveles indican que el activo está **técnicamente sobreextendido** tras el rally generalizado de las bolsas europeas. 

Con una volatilidad anualizada del **25,03%** y cotizando a un escaso **1,09%** de sus máximos recientes (drawdown mínimo), el perfil de riesgo/recompra actual es pésimo para nuevas entradas. Un pequeño susto macroeconómico o una recogida de beneficios institucional romperá con facilidad la frágil zona de soporte de corto plazo, dejando atrapados a los inversores que compran en la cúspide del entusiasmo estacional.

### 4. Desmontando el "consenso infalible"
Te escudas en que los 23 analistas del consenso apuntan a un precio objetivo medio de **71,47 EUR** (un supuesto potencial del 13,88%). Pero los precios objetivos de consenso son estimaciones retrospectivas que suelen llegar tarde, persiguiendo al mercado en los tramos finales de los rebotes alcistas. 
* ¿Y si el entorno de tipos de interés y la presión sobre los costes operativos aprietan los márgenes netos (actualmente en el 19,86%)? 
* ¿Y si la deuda total de **3.500 millones de EUR** (con una deuda neta sobre EBITDA de 1,03x) empieza a pesar más de la cuenta si el coste de refinanciación se mantiene elevado? 

Una rentabilidad por dividendo del **2,49%** (con un *payout* del 49,52%) está muy lejos de ser un atractivo colchón defensivo frente a la volatilidad bursátil del 25% que arrastra el título.

### Conclusión y Advertencia Bajista
Comprar **`AMS.MC`** ahora mismo basándose en que "los números del año pasado fueron buenos" es ignorar los riesgos cíclicos y la valoración exigente. Con un PER adelantado de 16,04x y un entorno macro europeo frágil, el potencial alcista está agotado y el riesgo de corrección técnica es elevado. No es momento de subirse al carro del optimismo ciego, sino de adoptar una postura defensiva o bajista.

**Rating**: SELL  
FINAL TRANSACTION PROPOSAL: Evitar nuevas posiciones compradoras en `AMS.MC` y considerar la infraponderación o cobertura de cartera ante el riesgo inminente de agotamiento del rebote técnico y compresión de múltiplos.

### Research Manager
**Recommendation**: Hold

**Rationale**: El debate entre el analista alcista y el bajista pone de manifiesto una divergencia clara pero equilibrada sobre AMS.MC. Por un lado, el bando alcista destaca con datos sólidos la excelente generación de caja de la compañía (Free Cash Flow superior a 1.386 millones de EUR en 2025), un ROE sobresaliente del 26,44%, un apalancamiento bajo control con una ratio de deuda neta sobre EBITDA de 1,03x y un momentum técnico favorable con la cotización situada en 62,76 EUR por encima de sus medias móviles clave y un PER forward atractivo de 16,04x. Por otro lado, el bando bajista argumenta de manera convincente que el crecimiento de los ingresos se está desacelerando hasta un modesto 6,4%, advierte sobre la valoración exigente (Price-to-Book de 5,29x), la volatilidad anualizada del 25,03%, los riesgos cíclicos de la macroeconomía europea y la presión competitiva en la industria de la distribución de viajes. Al sopesar ambas posturas, aunque los fundamentales y la rentabilidad de Amadeus son incuestionables, la sobreextensión técnica a corto plazo y las incertidumbres macroeconómicas contrarrestan el potencial alcista a corto plazo del consenso (71,47 EUR). Por consiguiente, la evidencia permanece equilibrada, justificando una postura neutral de mantenimiento sin forzar una dirección alcista o bajista prematura.

**Strategic Actions**: Maintain the current neutral stance on AMS.MC with a standard allocation weight (e.g., neutral market weight). Do not initiate new long positions at current overextended technical levels (RSI at 65.98 near recent highs) given the 25.03% volatility. Wait for a pullback toward the 20-session SMA (60.99 EUR) or 50-session SMA (56.90 EUR) to reassess risk-reward before altering exposure.

## III. Trading Team Plan

### Trader
**Action**: Hold

**Reasoning**: Aunque Amadeus IT Group presenta unos fundamentos sólidos, excelente rentabilidad con un ROE del 26,44% y un apalancamiento moderado con una deuda neta sobre EBITDA de 1,03x, la cotización actual se encuentra técnicamente sobreextendida con un RSI en 65,98 y una volatilidad anualizada del 25,03%. La desaceleración en el crecimiento de los ingresos al 6,4% y los riesgos cíclicos de la macroeconomía europea contrarrestan el atractivo del PER forward de 16,04x y el potencial de consenso hacia 71,47 EUR. Por consiguiente, se recomienda mantener la posición neutral actual y esperar a un retroceso hacia la media móvil de 20 sesiones en 60,99 EUR antes de replantear nuevas entradas tácticas.

**Entry Price**: not provided

**Stop Loss**: not provided

**Position Sizing**: Mantener ponderación neutral de mercado

FINAL TRANSACTION PROPOSAL: **HOLD**

## IV. Risk Management Team Decision

### Aggressive Analyst

Aggressive Analyst: **Rating**: BUY  
FINAL TRANSACTION PROPOSAL: **BUY**

¡Despertemos de una vez de esa parálisis por análisis que frena a los prudentes y a los indecisos! Analicemos la realidad de Amadeus IT Group, S.A. (`AMS.MC`) sin miedos infundados. Nos encontramos ante una auténtica joya tecnológica de la bolsa de Madrid con un retorno sobre el capital (ROE) sobresaliente del 26,44% y márgenes de beneficio neto cercanos al 20%. Mientras el analista conservador y el neutral tiemblan ante una tasa de crecimiento de los ingresos del 6,4% o miran con recelo un RSI en casi 66, están ignorando por completo el motor de combustión interna de esta compañía: ¡una generación de flujo de caja libre que supera los 1.386 millones de EUR y una ratio de deuda neta sobre EBITDA de apenas 1,03x! 

Pretender esperar pacientemente un retroceso hasta la media móvil de 20 sesiones en los 60,99 EUR es una fantasía táctica que nos hará perder el tren de un rebote europeo arrollador y de un potencial alcista de consenso situado en los 71,47 EUR, lo que representa un jugoso upside del 13,88%. ¿De verdad vamos a frenar la cartera por miedo a una volatilidad anualizada del 25% cuando el mercado global y el sector tecnológico están firmando su mejor inercia alcista? La fortaleza compradora en `AMS.MC` es innegable: cotiza por encima de sus medias de 20, 50 y 200 sesiones, superando al propio índice de referencia con un rendimiento relativo extraordinario. 

La cautela excesiva de los analistas neutrales y conservadores deja escapar el valor real de la innovación y del liderazgo de mercado de Amadeus en la industria global de viajes. Quedarse al margen o mantener una postura neutral neutraliza las oportunidades de crecimiento. ¡Es el momento de arriesgar, aprovechar esta dinámica de precios y apostar firmemente por la ruptura alcista!

### Conservative Analyst

Conservative Analyst: **Rating**: HOLD  
FINAL TRANSACTION PROPOSAL: **HOLD**

Estimado colega agresivo, su entusiasmo por lanzarse a comprar `AMS.MC` ignorando los riesgos técnicos y macroeconómicos actuales pone en grave peligro la estabilidad de nuestros activos. Calificar nuestra prudencia de parálisis es no entender los fundamentos de la gestión de riesgos. Decir que un RSI de 65,98 y una volatilidad anualizada del 25,03% son datos menores es un error imperdonable que expone a la cartera a correcciones severas e innecesarias. 

Es cierto que Amadeus IT Group, S.A. cuenta con fortalezas innegables, como un ROE del 26,44%, un flujo de caja libre de 1.386 millones de EUR y una deuda neta sobre EBITDA contenida en 1,03x. Nadie discute la solidez fundamental de la compañía. Sin embargo, su argumento de que debemos ignorar el contexto y comprar en los máximos locales ignora que el crecimiento de los ingresos se ha moderado al 6,4% en un entorno cíclico europeo todavía incierto y frágil. 

Lanzarse a comprar a ciegas solo porque el precio actual cotiza por encima de sus medias móviles —la SMA de 20 sesiones en 60,99 EUR, la de 50 en 56,90 EUR y la de 200 en 53,05 EUR— es perseguir el mercado en el peor momento técnico posible, justo cuando el indicador de momento muestra síntomas de agotamiento a corto plazo. Esperar un retroceso hacia la media móvil de 20 sesiones no es una fantasía táctica, sino una disciplina de capital indispensable para minimizar el riesgo de bajada y optimizar la relación riesgo-beneficio, protegiéndonos frente al riesgo de comprar en la cúspide de un impulso impulsado por el rebote general de las bolsas de finales de noviembre de 2026. 

Confiar ciegamente en que el precio objetivo medio del consenso de 71,47 EUR garantiza ganancias inmediatas olvida que las estimaciones de los analistas son solo eso, expectativas sujetas a revisión ante cualquier sobresaltos macroeconómicos o datos de inflación imprevistos en Europa. Proteger los activos exige paciencia, disciplina y evitar la euforia compradora. Por todo ello, mantener una postura neutral y prudente esperando un punto de entrada técnicamente seguro en `AMS.MC` es la única opción sensata para preservar el capital de nuestra firma.

### Neutral Analyst

Neutral Analyst: **Rating**: HOLD  
FINAL TRANSACTION PROPOSAL: **HOLD**

Escuchando la apasionada defensa del analista agresivo y las advertencias tan prudentes del analista conservador, creo que ambos extremos pecan de falta de flexibilidad táctica ante la realidad que presenta `AMS.MC`. 

Por un lado, el compañero agresivo acierta al señalar que Amadeus IT Group es una compañía de altísima calidad fundamental. Con un ROE del 26,44% y una generación de flujo de caja libre que supera los 1.386 millones de EUR, descartar el valor por completo o quedarse en una postura pasiva podría hacernos perder la inercia alcista de un mercado europeo que, a finales de noviembre de 2026, muestra una fortaleza remarcable y un rendimiento relativo muy superior al índice de referencia. Sin embargo, su propuesta de lanzarse a comprar de forma incondicional al precio actual de 62,76 EUR ignora el riesgo técnico de sobreextensión. Entrar sin una estrategia de mitigación en un valor con una volatilidad anualizada del 25,03% y un RSI en casi 66 es asumir un riesgo de corto plazo innecesario.

Por otro lado, el analista conservador tiene toda la razón al exigir disciplina de capital y al recordar que el crecimiento de los ingresos se ha moderado al 6,4% en un contexto europeo todavía frágil. No obstante, su propuesta de inmovilismo absoluto hasta que el precio colapse y retroceda exactamente hasta la media móvil de 20 sesiones en los 60,99 EUR puede ser una trampa de paciencia excesiva. Si el impulso alcista del sector tecnológico europeo continúa, es muy probable que `AMS.MC` no conceda ese retroceso tan limpio, dejándonos fuera de un potencial de consenso hacia los 71,47 EUR que ofrece un atractivo margen del 13,88%.

Como analista de riesgos neutral, propongo el término medio que armoniza ambas posturas: mantener una posición neutral estructurada pero con una orden de acumulación escalonada y prudente. En lugar de arriesgar todo el capital de golpe o quedarnos congelados esperando un soporte que quizás nunca llegue, la estrategia más sensata consiste en mantener la ponderación actual de mercado, permitiendo una asignación hipotética parcial solo si se producen pequeños alivios tácticos intradía, y estableciendo estrictos controles de riesgo basados en la volatilidad. Así evitamos la euforia compradora del analista agresivo sin caer en la parálisis total del analista conservador, logrando un equilibrio óptimo entre la captura de valor y la protección de los activos.

## V. Portfolio Manager Decision

### Portfolio Manager
**Rating**: Hold

**Executive Summary**: Mantener la postura neutral en AMS.MC sin ampliar exposicion en los niveles actuales de 62,76 EUR. Se recomienda adoptar una estrategia de espera tactica hasta presenciar un retroceso hacia las medias moviles de soporte (como la SMA de 20 sesiones en 60,99 EUR) para optimizar la relacion riesgo-beneficio, resguardando el capital frente a una volatilidad anualizada del 25,03%.

**Investment Thesis**: El debate entre el analista agresivo, el conservador y el neutral expone un equilibrio de fuerzas en AMS.MC que justifica mantener una postura de Hold. Por un lado, la solidez fundamental defendida por los partidarios del valor es indiscutible: un ROE sobresaliente del 26,44%, un flujo de caja libre superior a los 1.386 millones de EUR, un apalancamiento bajo control con una ratio de deuda neta sobre EBITDA de 1,03x y un atractivo PER forward de 16,04x respaldan el potencial alcista de consenso hacia los 71,47 EUR. Sin embargo, los argumentos del analista conservador y el neutral resultan decisivos al señalar que la cotización se encuentra técnicamente sobreextendida con un RSI en 65,98 y una volatilidad anualizada del 25,03%, todo ello en un contexto donde el crecimiento de los ingresos se ha moderado al 6,4% y persisten riesgos macroeconómicos cíclicos en Europa. Comprar de forma agresiva en estos niveles ignora la prudencia táctica necesaria, mientras que un inmovilismo absoluto podría ignorar la inercia del mercado. Por consiguiente, la evidencia permanece equilibrada, haciendo imperativo mantener la posición actual y esperar a correcciones ordenadas antes de reevaluar la exposición. Lo que cambiaría esta tesis sería una ruptura técnica sostenida por debajo de los soportes clave o un deterioro imprevisto en los flujos de caja operativos.

**Price Target**: 71.47

**Time Horizon**: 3-6 meses