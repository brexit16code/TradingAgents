# Trading Analysis Report: IBE.MC

- Analysis date: 2026-11-14
- Rating: Hold
- Generated: 2026-11-14 21:06:30
- TradingAgents 0.7.1: google, deep gemini-3.5-flash-lite, quick gemini-3.5-flash-lite
- Analysts: market, news, fundamentals; research debate rounds 1, risk debate rounds 1
- Data vendors: core_stock_apis yfinance, technical_indicators yfinance, fundamental_data yfinance, news_data yfinance, macro_data fred, prediction_markets polymarket, get_news ibex_sample, get_global_news ibex_sample

## I. Analyst Team Reports

### Market Analyst
**Análisis Técnico y Fundamental de Iberdrola, S.A. (`IBE.MC`)**

### 1. Resumen de la Situación Actual y Contexto de Mercado
A fecha de 14 de noviembre de 2026, la cotización de **Iberdrola, S.A. (`IBE.MC`)** se sitúa en **23.70 EUR** (precio de cierre al 13 de noviembre de 2026, según la instantánea de mercado verificada). El valor ha experimentado una fuerte tendencia alcista, encadenando diez semanas consecutivas de subidas y rompiendo máximos históricos que sitúan su capitalización bursátil por encima de los **158.000 millones de euros** (`https://news.google.com/rss/articles/CBMi5wFBVV95cUxPRlNiTGxxaVVFOFBuLVlZMDNoYnlVU3JrMHM5QmJoQUJxMll3dGFtT3VOaDYwX1ZpcktrQ0hLb01WemRBYkVvVFR2S2tCd2llaDZsZ20xZ19FZ2xiMGpSN3J2UG83VEl3akpvY3lVazlWWFBmU2tlLXNHWk1BNEY3T0IxZkNZSEhrTmphVTdWaUxWcThodC1UNndzLUhha1pWdmZFOHFKSkcxUEZwcWhKU2I2VkFnRHl1MmFNYnFlbHdMTWN3V2xYTS1MT2tZdXNFUHZGdlY4ejZOeVdiQlFseWpuOTFGUFE?oc=5`).

El contexto macroeconómico europeo muestra presiones inflacionarias persistentes en la eurozona (con la inflación rondando el 4% anual, según noticias fechadas el 13 de noviembre de 2026 en *El Economista* y *Negocios.com*), lo que mantiene un escenario de tipos de interés restrictivos y ahorros con rentabilidades reales negativas. A pesar de este trasfondo macro, los valores defensivos de alta capitalización y utilities diversificadas como Iberdrola han mostrado un comportamiento excepcional, respaldados además por revisiones al alza de precios objetivo por parte de analistas (como Bankinter tras sus resultados, según *MarketScreener España* del 11 de noviembre de 2026).

---

### 2. Análisis Técnico
Basándonos en los datos técnicos oficiales proporcionados en la instantánea de mercado:
* **Precio de cierre**: 23.70 EUR (`2026-11-13`).
* **Medias Móviles**: 
  * SMA 20: **22.32 EUR**
  * SMA 50: **21.30 EUR**
  * SMA 200: **20.22 EUR**
  * El alineamiento alcista de las medias móviles (SMA 20 > SMA 50 > SMA 200) confirma una tendencia alcista primaria muy sólida a medio y largo plazo.
* **Momentum y Osciladores**:
  * **RSI (14)**: **82.54**, lo que denota una condición de **sobrecompra clara** y extrema. Si bien refleja una fuerza compradora inusitada, los valores en estos niveles suelen ser vulnerables a correcciones técnicas de corto plazo o consolidaciones.
  * **MACD**: **0.585** frente a su línea de señal (`macd_signal`) de **0.491**, confirmando la continuidad del impulso alcista.
* **Volatilidad y Retornos**:
  * Volatilidad anualizada del **13.93%**, moderada para el sector.
  * Retorno a 21 sesiones: **+10.08%**; retorno a 252 sesiones: **+36.20%**. El *drawdown* actual se sitúa en **0.0%**, puesto que el valor cotiza en máximos históricos.

---

### 3. Análisis Fundamental y Valuation
* **Capitalización de Mercado**: 157.320 millones de EUR.
* **PER (Trailing)**: **32.03x** / **Forward P/E**: **21.28x**, reflejando una valoración exigente sustentada en su calidad crediticia, su perfil diversificado en redes y renovables, y su plan estratégico.
* **Ratio P/B (Precio/Valor en Libros)**: **3.06x** (con un valor contable por acción de 7.74 EUR).
* **Deuda y Apalancamiento**: Deuda total de aproximadamente 63.840 millones de EUR, con un ratio de **Net Debt / EBITDA de 3.95x**.
* **Dividendos**: Ofrece un rendimiento por dividendo (*dividend yield*) del **2.87%** (con un dividendo anual de 0.68 EUR y un *payout ratio* del 87.06%).
* **Consenso de Analistas**: El precio objetivo medio de consenso se sitúa en **21.57 EUR** (con un rango entre 18.00 EUR y 26.00 EUR y 24 opiniones analíticas). Dado que el precio actual en mercado es de 23.70 EUR, el valor cotiza actualmente un **-8.99% por encima** de la estimación media de consenso (*consensus downside*), lo que sugiere que gran parte del optimismo a corto plazo ya se encuentra descontado en precios.

---

### 4. Selección de Indicadores Técnicos Relevantes
De acuerdo con la estrategia de selección de indicadores complementarios (sin redundancias), los más idóneos para monitorizar la operativa en `IBE.MC` bajo las condiciones actuales de sobrecompra son:
1. `close_200_sma`: Para confirmar la tendencia macro y el sesgo secular a largo plazo.
2. `close_50_sma`: Para vigilar posibles soportes dinámicos en caso de corrección a medio plazo.
3. `close_10_ema`: Para capturar giros rápidos de impulso a muy corto plazo ante la extrema sobrecompra.
4. `macd`: Para evaluar la divergencia de tendencia y la fortaleza del impulso comprador.
5. `macds`: Como línea de activación para cruces con el MACD.
6. `macdh`: Para visualizar el debilitamiento o aceleración del histograma de momento.
7. `rsi`: Clave en este escenario para vigilar la intensidad de la zona de sobrecompra (>70).
8. `atr`: Esencial para dimensionar el riesgo, fijar *stop-losses* y ajustar el tamaño de posición ante la elevada verticalidad del movimiento alcista.

---

### 5. Tabla Resumen de Datos Clave

| Métrica / Indicador | Valor | Comentario / Implicación |
| :--- | :--- | :--- |
| **Ticker** | `IBE.MC` (Iberdrola, S.A.) | Mercado Continuo Español (MCE), Sector Utilities |
| **Precio de Cierre** | 23.70 EUR (13/11/2026) | Nuevos máximos históricos de cotización |
| **Capitalización Bursátil** | ~157.320 Millones EUR | Sólido respaldo institucional y gran tamaño |
| **RSI (14)** | 82.54 | Condición de sobrecompra extrema |
| **MACD vs Señal** | 0.585 / 0.491 | Impulso alcista vigente pero vigilante |
| **SMA 50 / SMA 200** | 21.30 EUR / 20.22 EUR | Estructura alcista primaria perfectamente alineada |
| **PER Forward / Trailing** | 2

### News Analyst
**Rating**: HOLD  
**FINAL TRANSACTION PROPOSAL**: HOLD  

### Informe de Investigación y Análisis Macroeconómico / Bursátil (`IBE.MC`)

#### 1. Contexto de Mercado y Evolución Reciente
A fecha de noviembre de 2026, **Iberdrola, S.A. (`IBE.MC`)** cotiza en máximos históricos tras encadenar diez semanas consecutivas de alzas en la bolsa española, situando su capitalización bursátil por encima de los **158.000 millones de euros** (precio de cierre de **23,70 EUR** a 13 de noviembre de 2026). Este impulso alcista viene respaldado por la presentación de sus resultados financieros y la posterior revisión al alza de sus previsiones por parte de entidades como Bankinter, así como por el atractivo de su dividendo (con una rentabilidad por dividendo de aproximadamente el **2,87%** y un dividendo de 0,68 EUR).

No obstante, desde una perspectiva técnica y fundamental, el título presenta señales mixtas:
* **Indicadores Técnicos**: El valor muestra una fuerte sobrecompra con un RSI de **82,54**, encontrándose por encima de sus medias móviles de corto y largo plazo (SMA 20 en 22,32 EUR, SMA 50 en 21,29 EUR y SMA 200 en 20,21 EUR). La volatilidad histórica de 511 sesiones se sitúa en **13,93%**.
* **Valoración Fundamental**: Cotiza a un PER estimado (*forward P/E*) de **21,28** y un PER histórico (*trailing P/E*) de **32,03**, reflejande una prima considerable frente a la mediana de sus comparables sectoriales (*peer median forward PE* de **16,98**, ratio de **1,25**). El precio objetivo medio de consenso de los analistas se sitúa en **21,57 EUR** (con un rango entre 18,00 EUR y 26,00 EUR), lo que implica un potencial de caída respecto a los precios actuales (*consensus upside* de **-8,99%**).

#### 2. Entorno Macroeconómico y Sectorial en Europa
El contexto macroeconómico europeo hacia mediados de noviembre de 2026 está marcado por la persistencia de presiones inflacionistas:
* **Inflación en la Eurozona**: Los datos recientes sitúan la inflación en la eurozona alrededor del **4%**, un nivel que los analistas consideran incompatible con una moderación en las subidas de tipos de interés (titulares de *El Economista* y *Vozpopuli* señalan que los tipos reales negativos penalizan el ahorro).
* **Impacto en Utilities**: En un entorno de tipos elevados o persistentes para combatir la inflación, los sectores intensivos en capital y con rentabilidades por dividendo comparables a la renta fija sufren presión por descuento de flujos de caja futuros, aunque valores refugio con sólidas posiciones financieras como `IBE.MC` continúan captando flujos de inversores institucionales y minoristas.

#### 3. Estados Financieros y Fundamentales
De acuerdo con los estados financieros consolidados:
* **Ingresos y EBITDA**: En el ejercicio cerrado a 31 de diciembre de 2025, Iberdrola registró unos ingresos totales de **44.076 millones de euros** (frente a 42.988 millones en 2024 y 49.335 millones en 2023) y un EBITDA de **16.763 millones de euros** (15.192 millones en 2024).
* **Beneficio Neto**: El beneficio neto en 2025 ascendió a **6.285 millones de euros**, mejorando los 5.612 millones de 2024 y los 4.803 millones de 2023.
* **Deuda y Solvencia**: La deuda total se sitúa en **57.231 millones de euros** (balance a cierre de 2025), con un apalancamiento que refleja una ratio de deuda neta sobre EBITDA de **3,95x**. El patrimonio neto (*Stockholders Equity*) asciende a **50.068 millones de euros**.
* **Flujo de Caja**: El flujo de caja operativo en 2025 fue de **11.635 millones de euros**, con unas inversiones de capital (*CapEx*) de **8.318 millones de euros**, resultando en un flujo de caja libre (*Free Cash Flow*) de **3.317 millones de euros**.

#### 4. Datos Faltantes e Incertidumbres
* No se dispone de las estimaciones detalladas de desgloses de flujo de caja operativo intradiario posteriores a los cierres anuales auditados.
* Faltan proyecciones cuantitativas de los impactos regulatorios específicos en mercados internacionales (EE. UU., Reino Unido y Brasil) para los ejercicios 2027 y posteriores.

---

### Tabla Resumen de Datos Clave

| Concepto / Métrica | Valor Actual / Referencia | Fuente / Contexto |
| :--- | :--- | :--- |
| **Ticker y Empresa** | `IBE.MC` (Iberdrola, S.A.) | Registro oficial / MCE |
| **Precio de Cierre** | 23,70 EUR | Sesión de mercado al 13/11/2026 |
| **Capitalización Bursátil** | ~158.324 millones EUR | Datos de mercado / Noticias |
| **PER Estimado (Forward P/E)** | 21,28x | Fundamentos de mercado |
| **PER Histórico (Trailing P/E)** | 32,03x | Fundamentos de mercado |
| **Precio Objetivo de Consenso** | 21,57 EUR (Upside: -8,99%) | Consenso de analistas (24 opiniones) |
| **Rentabilidad por Dividendo** | 2,87% (0,68 EUR por acción) | Fundamentos de mercado |
| **EBITDA (Cierre 2025)** | 16.763 millones EUR | Estados Financieros / Cuenta de Resultados |
| **Beneficio Neto (Cierre 2025)**| 6.285 millones EUR | Estados Financieros / Cuenta de Resultados |
| **Deuda Total (Cierre 2025)** | 57.231 millones EUR | Balance General |
| **RSI (14 sesiones)** | 82,54 (Zona de sobrecompra) | Datos Técnicos (`IBE.MC`) |
| **Contexto Inflacionario UE** | ~4,0% (Noviembre 2026) | Titulares macroeconómicos europeos |

### Fundamentals Analyst
**Análisis Fundamental de Iberdrola, S.A. (`IBE.MC`)**

**1. Perfil de la Empresa y Contexto de Negocio**
Iberdrola, S.A. (`IBE.MC`) es una de las mayores empresas energéticas del mundo, clasificada dentro del sector de **Utilities (Utilities - Diversified)** y cotizando en la Bolsa de Madrid (MCE) en euros (EUR). Con una capitalización bursátil récord que supera los **158.000 millones de euros** (snapshot del 14/11/2026), la compañía se encuentra cotizando en máximos históricos tras encadenar 10 semanas consecutivas de subidas apalancadas en sus sólidos resultados y la mejora de perspectivas de los analistas (como las revisiones al alza de Bankinter tras sus publicaciones recientes de noviembre de 2026).

**2. Análisis de los Estados Financieros Históricos (2023 - 2025)**
Los datos financieros extraídos de los estados contables oficiales muestran una evolución positiva y resiliente:

*   **Cuenta de Resultados (Ingresos, EBITDA y Net Income):**
    *   *2023:* Total Revenue de 49.335M€, EBITDA de 14.906M€ y Net Income de 4.803M€.
    *   *2024:* Total Revenue de 42.988M€, EBITDA de 15.192M€ y Net Income de 5.612M€.
    *   *2025:* Total Revenue de 44.076M€, EBITDA de 16.763M€ y Net Income de 6.285M€.
    *   *Tendencia:* Se observa un crecimiento sostenido en la rentabilidad neta y del EBITDA a pesar de la fluctuación en los ingresos brutos totales, reflejando una mayor eficiencia operativa y un control de márgenes robusto (profit margins del 14,74%).
*   **Balance de Situación:**
    *   *Activos Totales:* Pasaron de 150.033M€ en 2023 a 160.762M€ al cierre de 2025.
    *   *Patrimonio Neto (Stockholders Equity):* Incremento continuo desde 43.111M€ (2023) hasta 50.068M€ (2025), fortaleciendo la solvencia patrimonial.
    *   *Deuda Total:* Se ha situado en 57.231M€ al cierre de 2025 (la ratio de deuda neta sobre EBITDA se sitúa en torno a 3,95x).
*   **Flujo de Caja (Cash Flow):**
    *   *2023:* Operating Cash Flow de 12.130M€, CapEx de -7.877M€ (Free Cash Flow de 4.253M€).
    *   *2024:* Operating Cash Flow de 11.925M€, CapEx de -8.375M€ (Free Cash Flow de 3.550M€).
    *   *2025:* Operating Cash Flow de 11.635M€, CapEx de -8.318M€ (Free Cash Flow de 3.317M€).
    *   *Tendencia:* Generación de caja operativa robusta por encima de los 11.600 millones anuales, aunque con un flujo de caja libre ligeramente constreñido por un ambicioso plan de inversiones (CapEx superior a los 8.300M€ anuales).

**3. Valoración y Múltiplos Fundamentales**
*   **PER (Trailing P/E):** 32,03x
*   **PER Adelantado (Forward P/E):** 21,28x (con un Forward EPS estimado de 1,11€).
*   **Ratio frente a Peers:** El ratio de valoración sectorial indica un PER relativo superior frente a la mediana de sus comparables (`ANE.MC`, `ENG.MC`, `ELE.MC`, `NTGY.MC`, `RED.MC`, `SLR.MC`), concretamente de 1,25x, lo que evidencia que el mercado premia su calidad, diversificación geográfica y perfil defensivo.
*   **Precio a Valor en Libros (Price-to-Book):** 3,06x (con un valor en libros por acción de 7,74€).
*   **Rentabilidad por Dividendo (Dividend Yield):** 2,87% (con un dividendo rate de 0,68€ y un payout ratio del 87,06%).
*   **Consenso de Analistas:** El precio objetivo medio de consenso se sitúa en 21,57€ (con un rango entre un mínimo de 18,00€ y un máximo de 26,00€ a partir de 24 opiniones de analistas), lo que representa una **consensual upside/downside de -8,99%** respecto al precio de cotización actual en los 23,70€ (al 13/11/2026), debido al fuerte rally alcista reciente que ha superado las previsiones medias previas.

**4. Información Técnica Reciente y Noticiario (Semana al 14/11/2026)**
*   **Precio actual:** 23,70 € (con una subida diaria del +1,54%).
*   **Indicadores Técnicos:** RSI de 14 en zona de sobrecompra clara (82,54), MACD positivo (0,585), cotizando holgadamente por encima de sus medias móviles de 20, 50 y 200 sesiones (SMA20: 22,32€; SMA50: 21,29€; SMA200: 20,22€). Ausencia total de retroceso reciente (drawdown del 0,0%).
*   **Noticias Relevantes:**
    *   *Valencia Plaza y El Boletín (13/11/2026):* Informan que Iberdrola alcanza nuevos máximos históricos en bolsa impulsada por 10 semanas consecutivas de alzas y superando los 158.000 millones de capitalización.
    *   *MarketScreener España / Finanzas.com (11/11/2026 - 12/11/2026):* Destacan la revisión al alza de precios objetivos por parte de entidades como Bankinter tras los resultados y la solidez de su política de retribución al accionista.
    *   *Contexto Macro:* Entorno europeo marcado por presiones inflacionarias (inflación de la eurozona rondando el 4% en noviembre de 2026) y tipos reales negativos, lo que refuerza el atractivo de valores refugio y utilities de alta capitalización como `IBE.MC`.

**5. Datos Faltantes**
*   No se dispone de desglose detallado de transacciones de insiders (insider transactions) en el snapshot analizado.
*   Las cifras de flujos de caja operativos y libres desglosados en el último periodo trimestral intermedio exacto muestran valores nulos o no reportados directamente en las métricas de resumen operativo, aunque sí constan en los cierres anuales auditados hasta 2025.

**6. Insights Accionables para Traders**
*   **Riesgo de Corto Plazo (Técnico):** El valor se halla en un estado de sobrecompra técnica muy acusada (RSI > 82), cotizando un ~9% por encima del precio objetivo medio del consenso de analistas (21,57€).

## II. Research Team Decision

### Bull Researcher

Bull Analyst: ¡Hola a todos! Comprendo perfectamente que el analista bajista intente asustar a los inversores mirando fríamente el gráfico técnico o escudándose en que `IBE.MC` cotiza ligeramente por encima del precio objetivo medio de consenso (esos 21,57 EUR frente a los 23,70 EUR actuales). Pero seamos sinceros: **cuando una compañía es un líder mundial absoluto, el mercado recompensa su excelencia**, y quedarse mirando sólo una media o un número de consenso es perderse la película completa. ¡Iberdrola acaba de encadenar diez semanas consecutivas de subidas pulverizando máximos históricos y superando los 158.000 millones de euros de capitalización! *(Valencia Plaza / El Boletín, 13 de noviembre de 2026)*. Eso no es especulación; eso es un reconocimiento rotundo del mercado a una máquina de hacer caja.

Respondamos punto por punto a las dudas que los osos suelen poner sobre la mesa:

### 1. Crecimiento Potencial y Escalabilidad frente al "Pico de Cotización"
Los bajistas dirán que el valor está "demasiado caro" o en sobrecompra extrema (con un RSI en 82,54). ¡Por favor! Un RSI elevado solo demuestra una **fuerza compradora brutal e inusitada** respaldada por fundamentales de hierro. Miremos la realidad de los estados financieros: el EBITDA ha escalado desde los 14.906 millones de euros en 2023 hasta unos impresionantes **16.763 millones de euros al cierre de 2025**, mientras que el beneficio neto escaló hasta los **6.285 millones de euros**. La compañía no para de escalar su negocio en redes y energías limpias a escala global (EE. UU., Reino Unido, Brasil y España), demostrando una capacidad de crecimiento inalcanzable para el resto del sector. Bankinter acaba de elevar su precio objetivo tras sus últimos resultados porque los números superan cualquier previsión pesimista *(MarketScreener España, 11/11/2026)*.

### 2. Ventajas Competitivas y el Foso Defensivo (*Moat*)
¿Por qué `IBE.MC` merece cotizar con una prima (un PER forward de 21,28x frente a la mediana de peers)? Sencillamente porque es la referencia mundial indiscutible en la transición energética. Su diversificación geográfica le aísla de los sobresaltos regulatorios locales, y su músculo inversor (con un CapEx anual superior a los 8.300 millones de euros perfectamente respaldado por un flujo de caja operativo que supera los 11.600 millones) garantiza que nadie puede competir con su tamaño ni con su acceso a financiación. Mientras la inflación en la eurozona ronda el 4% y los ahorradores sufren tipos reales negativos en sus depósitos *(Vozpopuli, noviembre de 2026)*, invertir en `IBE.MC` con su dividendo del **2,87%** (0,68 EUR por acción) no es una opción: es el auténtico refugio inteligente.

### 3. Derribando el Argumento de la Deuda y los Tipos de Interés
Los osos siempre intentan asustar con la deuda total (unos 57.231 millones de euros según el balance de 2025). Analicémoslo con rigor: la ratio de deuda neta sobre EBITDA se sitúa en un saneadísimo **3,95x**, totalmente bajo control para una utility diversificada de esta dimensión. Además, con un patrimonio neto (*Stockholders Equity*) que ha crecido hasta los **50.068 millones de euros**, la solvencia de la compañía es blindada. Pretender aplicarles las mismas reglas de apalancamiento que a un promotor inmobiliario o ignorar su inmensa capacidad de generar más de 11.600 millones de caja operativa es simplemente hacer trampa con los datos.

En resumen: `IBE.MC` está cara porque es **magnífica**, no porque esté sobrevalorada. En un entorno macroeconómico europeo complejo e inflacionario, apostar por el gigante líder es la jugada ganadora. 

**Rating**: BUY  
**FINAL TRANSACTION PROPOSAL**: HOLD

### Bear Researcher

Bear Analyst: ¡Hola a todos! Escuchando al compañero alcista, parece que nos quiere vender la moto de que `IBE.MC` es invulnerable simplemente porque ha encadenado diez semanas de subidas bursátiles y supera los 158.000 millones de capitalización (*Valencia Plaza / El Boletín*, 13 de noviembre de 2026). ¡Cuidado con confundir calidad empresarial con un precio de entrada razonable! Comprar una acción exclusivamente porque está de moda en máximos históricos es la receta perfecta para quedarse atrapado en la cúspide. 

Desmontemos esa narrativa de "la perfección no tiene precio" punto por punto:

### 1. ¿Fuerza compradora o sobrecompra alarmante e insostenible?
El compañero se burla de que mencionemos el RSI en **82,54** y lo disfraza de "fuerza compradora brutal". Los datos técnicos no mienten: un RSI por encima de 80 denota una **sobrecompra extrema**. Históricamente, estos niveles extremos en valores de gran capitalización actúan como un elástico estirado al máximo; tarde o temprano, la corrección técnica para purgar los excesos llega de golpe. Además, pretender ignorar que `IBE.MC` cotiza en los **23,70 EUR**, un **-8,99% por encima del precio objetivo medio del consenso de analistas** (situado en **21,57 EUR**), es meter la cabeza en la arena. El mercado ya ha descontado no solo los buenos resultados, sino varios años de optimismo futuro. ¿Margen de seguridad? Nulo.

### 2. El espejismo de los múltiplos y el castigo del PER relativo
Nos habla maravillas de los 16.763 millones de EBITDA o los 6.285 millones de beneficio neto de 2025. Nadie niega que Iberdrola es un gigante industrial envidiable. El problema no es el negocio, es **lo que se paga por él**. `IBE.MC` cotiza a un PER forward de **21,28x** (y un PER histórico de **32,03x**), lo que representa un **PER relativo de 1,25x** frente a la mediana de sus comparables sectoriales (*peers* en 16,98x). Pagar una prima tan desproporcionada en un entorno donde la inflación de la eurozona ronda el 4% y los tipos de interés se mantienen restrictivos (*El Economista*, noviembre de 2026) es un riesgo enorme. Si la rentabilidad por dividendo es de apenas un **2,87%** (0,68 EUR), cualquier ligera decepción en los flujos de caja futuros hará que los inversores institucionales huyan despavoridos hacia alternativas de renta fija u otros sectores defensivos más baratos.

### 3. La realidad sobre la soga de la deuda y el CapEx asfixiante
El toro intenta quitar hierro a los **57.231 millones de euros de deuda total** (con una ratio de deuda neta sobre EBITDA de **3,95x**) escudándose en el tamaño de la compañía. Pero olvidan un detalle clave: el modelo de negocio de `IBE.MC` es intensivo en capital por definición. Con un plan de inversiones (*CapEx*) que supera sistemáticamente los **8.300 millones de euros anuales** frente a un flujo de caja libre que se ha contraído hasta los **3.317 millones de euros** al cierre de 2025, la capacidad de maniobra se estrecha. En un escenario macroeconómico europeo con tipos reales penalizadores y presiones inflacionarias persistentes, financiar un CapEx mastodóntico con ese nivel de apalancamiento no es un paseo militar; es un riesgo financiero latente que el mercado está ignorando alegremente en plena euforia alcista.

En definitiva, comprar `IBE.MC` hoy en día a estos precios de vértigo, con el consenso de analistas aconsejando cautela y los indicadores técnicos al rojo vivo, es asumir un riesgo asimétrico completamente desfavorable. ¡No pagues oro por un activo que ya brilla demasiado!

**Rating**: SELL  
FINAL TRANSACTION PROPOSAL: SELL

### Research Manager
**Recommendation**: Hold

**Rationale**: El debate entre el analista alcista y el bajista expone una tensión clara entre la excelente calidad operativa de Iberdrola, S.A. (`IBE.MC`) y su valoración actual de mercado. Por un lado, el toro defiende con acierto los sólidos fundamentales de la compañía, destacando el incremento de su EBITDA hasta los 16.763 millones de euros al cierre de 2025, un beneficio neto de 6.285 millones y su posición como líder indiscutible en la transición energética con flujos de caja operativos superiores a los 11.600 millones. Por otro lado, el oso aporta argumentos técnicos y de valoración contundentes: `IBE.MC` cotiza en máximos históricos tras diez semanas de subidas a 23,70 EUR, lo que se traduce en un RSI de 82,54 (sobrecompra extrema) y una cotización un -8,99% por encima del precio objetivo medio del consenso (21,57 EUR). Asimismo, el PER forward de 21,28x refleja una prima significativa frente a la mediana del sector (PER relativo de 1,25x), mientras el flujo de caja libre se contrajo a 3.317 millones frente a un CapEx superior a 8.300 millones y una deuda neta/EBITDA de 3,95x en un contexto de inflación en la eurozona del 4%. Sopesando ambas posturas, aunque la calidad del negocio justifica su prima histórica, la sobrecompra técnica extrema y el hecho de cotizar por encima del consenso impiden justificar una compra en este nivel, al igual que los excelentes fundamentales y el impulso alcista actual impiden un posicionamiento vendedor. Por consiguiente, se adopta una postura neutral de mantenimiento.

**Strategic Actions**: Mantener la asignación actual en cartera sobre `IBE.MC` en un tamaño estándar (1.0x). No realizar nuevas compras en los niveles actuales de 23,70 EUR dado el riesgo derivado de la sobrecompra técnica (RSI de 82,54) y la valoración por encima del objetivo de consenso. Esperar a una corrección técnica hacia las medias móviles (como la SMA20 en 22,32 EUR) o hacia la zona de consenso antes de evaluar un incremento de exposición.

## III. Trading Team Plan

### Trader
**Action**: Hold

**Reasoning**: Iberdrola, S.A. (IBE.MC) cotiza en máximos históricos a 23.70 EUR con una condición de sobrecompra extrema (RSI de 82.54) y un precio superior al objetivo medio de consenso de 21.57 EUR. Aunque sus fundamentales y su liderazgo en la transición energética respaldan la calidad de la compañía, la valoración exigente (PER forward de 21.28x) y la divergencia frente al consenso aconsejan mantener la posición existente sin realizar nuevas compras en estos niveles.

**Entry Price**: not provided

**Stop Loss**: not provided

**Position Sizing**: 1.0x de la asignación estándar en cartera

FINAL TRANSACTION PROPOSAL: **HOLD**

## IV. Risk Management Team Decision

### Aggressive Analyst

Aggressive Analyst: ¡Vaya manera de asustarse ante la grandeza! Escucho a los analistas conservadores y neutrales temblar ante un RSI de 82.54 y esconderse detrás de un precio objetivo medio de consenso de 21.57 EUR que ya ha quedado totalmente obsoleto frente a la realidad del mercado. ¡Despertad! Los precios objetivos de consenso son una foto fija del pasado, mientras que Iberdrola S.A. (`IBE.MC`) está escribiendo el futuro energético de Europa en tiempo real con una capitalización que ya supera los 158.000 millones de euros. 

Pretender frenar el impulso de un gigante que encadena diez semanas consecutivas de subidas y cotiza en máximos históricos en los 23.70 EUR solo porque las métricas tradicionales os parecen "exigentes" es renunciar deliberadamente a la verdadera creación de valor. Nos hablan de un PER forward de 21.28x como si fuera un pecado mortal, ignorando por completo que la compañía acaba de reportar un beneficio neto de 6.285 millones de euros al cierre de 2025 y un EBITDA monstruoso de 16.763 millones. ¿De verdad queréis dejar pasar el liderazgo indiscutible en la transición energética y una generación de caja operativa superior a los 11.600 millones anuales por un simple miedo a la volatilidad de corto plazo?

La cautela excesiva de mis compañeros analistas ignora el contexto macroeconómico real: estamos en un entorno inflacionario en la eurozona que ronda el 4%, donde los tipos reales negativos castigan implacablemente el ahorro estéril. En este escenario, los inversores institucionales no buscan medianías; buscan activos refugio de máxima calidad crediticia que ofrezcan crecimiento estructural y protección contra la devaluación monetaria. El "consensus downside" del -8.99% del que tanto se lamentan no es más que la prueba irrefutable de que `IBE.MC` está superando las expectativas del mercado una y otra vez, obligando a entidades como Bankinter a revisar constantemente sus valoraciones al alza. 

Mientras los conservadores se paralizan ante una condición de sobrecompra técnica, los inversores audaces sabemos que una fuerza compradora tan inusitada refleja un momentum imparable y una demanda institucional masiva. El alineamiento perfecto de las medias móviles —con la SMA 20 en 22.32 EUR, la SMA 50 en 21.30 EUR y la SMA 200 en 20.22 EUR— demuestra que la tendencia alcista primaria es blindada y secular. Las correcciones superficiales son para quienes no tienen estómago para ganar en grande. Apostar por la solidez y la innovación de `IBE.MC` manteniendo una posición firme o buscando expansiones agresivas es la única jugada lógica para batir al mercado. ¡Basta de mirar el retrovisor; la verdadera oportunidad está en surfear esta ola histórica de crecimiento!

**Rating**: BUY  
FINAL TRANSACTION PROPOSAL: **BUY**

### Conservative Analyst

Conservative Analyst: Escucho los argumentos del analista agresivo con total escepticismo, ya que calificar de "miedo" lo que es una estricta gestión profesional del riesgo es una irresponsabilidad financiera mayúscula. Pretender ignorar que Iberdrola, S.A. (`IBE.MC`) cotiza en unos flamantes 23.70 EUR con un RSI extremo de 82.54 y un desfase del -8.99% frente al precio objetivo medio de consenso de 21.57 EUR es cerrar los ojos ante la realidad matemática de los mercados. Defender una compra agresiva en máximos históricos tras diez semanas consecutivas de alzas no es visión de futuro; es especulación ciega que expone a nuestra firma a una corrección técnica inminente. 

El colega agresivo descarta el PER forward de 21.28x y el PER histórico de 32.03x como si fueran meros detalles estéticos, olvidando que la compañía soporta una deuda total de 57.231 millones de euros y una ratio de deuda neta sobre EBITDA de 3.95x. En un entorno macroeconómico europeo con una inflación persistente alrededor del 4% y tipos de interés restrictivos que castigan los flujos de caja futuros, sobrepagar por un activo intensivo en capital que ya descuenta todo el optimismo posible es un disparate. Los sólidos fundamentales de Iberdrola, S.A. (`IBE.MC`) —como su EBITDA de 16.763 millones de euros y sus 11.635 millones de caja operativa al cierre de 2025— son indiscutibles, pero la calidad de una empresa no justifica comprar en el punto más álgido de sobrecompra sin margen de seguridad. 

Atribuir la cautela al "miedo" es despreciar el deber fiduciario de proteger el capital contra volatilidades innecesarias. Cuando el mercado opera un 9% por encima de la valoración media de los analistas y los osciladores gritan sobrecompra, la única alternativa sensata para preservar el patrimonio es mantener la disciplina y rechazar la euforia compradora. La estabilidad a largo plazo se construye evitando trampas de valoración, no persiguiendo máximos históricos cegados por el entusiasmo temporal.

**Rating**: HOLD
FINAL TRANSACTION PROPOSAL: **HOLD**

### Neutral Analyst

Neutral Analyst: He estado escuchando atentamente tanto la euforia desmedida de nuestro analista agresivo como la rigidez defensiva del conservador, y creo que ambos están cayendo en posturas extremas que no hacen justicia a la realidad de Iberdrola, S.A. (`IBE.MC`). 

Por un lado, el analista agresivo descarta con demasiada ligereza el riesgo técnico y la valoración exigente. Tildar de "miedo" lo que es una lectura de mercado basada en datos concretos es una temeridad. Ignorar que el RSI está en un nivel extremo de 82.54 y que cotizamos un 8.99% por encima del precio objetivo medio de consenso de 21.57 EUR es cerrar los ojos ante la alta probabilidad de una consolidación a corto plazo. No se puede justificar una compra impulsiva en máximos históricos simplemente apelando al "momentum", especialmente cuando el PER forward se sitúa en 21.28x y la ratio de deuda neta sobre EBITDA roza las 3.95x en un entorno europeo con tipos e inflación persistentes alrededor del 4%.

Por otro lado, el analista conservador se refugia tanto en el pesimismo de los múltiplos que corre el riesgo de paralizar cualquier estrategia de cartera rentable. Pretender que una posición sólida en un gigante de la transición energética con una capitalización superior a los 158.000 millones de euros y un EBITDA de 16.763 millones de euros deba ser tratada con recelo absoluto es ignorar la fortaleza estructural de la compañía. Las correcciones técnicas o las valoraciones elevadas no invalidan la calidad de un activo excelente; simplemente exigen paciencia táctica y una gestión milimétrica del riesgo, no una huida o un bloqueo operativo.

La postura verdaderamente inteligente y equilibrada no es comprar a ciegas ni tampoco estancarse en el inmovilismo: es mantener la posición existente (HOLD). Esto nos permite surfear la robusta tendencia alcista a largo plazo —respaldada por unas medias móviles impecables donde la SMA 20, 50 y 200 están perfectamente alineadas— sin exponernos al riesgo de sobreallocación en un momento de sobrecompra técnica evidente. En lugar de pecar de soberbia alcista o de miedo paralizante, la prudencia dictamina retener lo que tenemos, observar cómo el mercado absorbe estos máximos históricos y esperar una corrección saludable hacia soportes dinámicos antes de plantearse cualquier ampliación de cartera.

**Rating**: HOLD
FINAL TRANSACTION PROPOSAL: **HOLD**

## V. Portfolio Manager Decision

### Portfolio Manager
**Rating**: Hold

**Executive Summary**: Mantener la asignación actual en cartera sobre IBE.MC en un tamaño estándar (1.0x). No se deben realizar nuevas compras en los niveles actuales de 23,70 EUR debido a la sobrecompra técnica extrema (RSI de 82,54) y a una valoración que supera el objetivo medio de consenso.

**Investment Thesis**: El debate entre los analistas refleja una tensión evidente entre la excelente calidad fundamental de Iberdrola, S.A. (IBE.MC) y los riesgos técnicos y de valoración a corto plazo. Por un lado, el analista agresivo destaca la robustez de los fundamentales con un EBITDA de 16.763 millones de euros, un beneficio neto de 6.285 millones y un sólido liderazgo en la transición energética respaldado por un fuerte impulso alcista y medias móviles alineadas. Por otro lado, los analistas conservador y neutral advierten acertadamente que el valor cotiza en máximos históricos a 23,70 EUR, con un RSI de 82,54 que denota sobrecompra extrema, un PER forward de 21,28x y una cotización un -8,99% por encima del precio objetivo medio del consenso (21,57 EUR), además de una deuda neta sobre EBITDA de 3,95x en un contexto de inflación en la eurozona del 4%. Sopesando los argumentos, la evidencia de sobrecompra y la prima sobre el consenso impiden justificar una compra agresiva en este momento, pero la calidad estructural del negocio y el momentum secular descartan una venta. Por tanto, se adopta una postura de mantenimiento hasta que una corrección técnica brinde un mejor punto de entrada.

**Price Target**: 21.57

**Time Horizon**: 3-6 meses