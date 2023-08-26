
### **Fuentes de Datos**
Origen [API CoinGecko] https://www.coingecko.com

### **Archivos y carpetas**
- \data\* Contiene los archivos de datos extraídos
- \source\* Contiene las imágenes del presente archivo
- \ETL.ipnb Notebook con la extracción y transformación de los datos
- \EDA.ipynb Notebook con análisis exploratorio de los datos
- \README.md Este archivo

### **Lenguaje y librerías utilizadas** 
Para la extracción de datos (ETL) y la exploración (EDA) se utilizó Python 3 y las librerías MathPlotLib y Seaborn para graficar


## **INFORME** ##

### **Contexto del proyecto**
En mi rol de Analista de Datos de la empresa X, que presta servicios financieros, localizada en Argentina, se me solicita un análisis e informe sobre criptomonedas para evaluar la posibilidad de invertir en estos activos.


### **Monedas**
- Criterio de selección
    - Mayor volumen a la fecha
    - Mayor Capitalización de Mercado a la fecha
    - Se descartaron StableCoins (monedas atadas al valor de una moneda fiat u otro activo), ya que las más utilizadas no representan un atractivo a la hora de invertir
    - Se descartaron otras monedas arbitrariamente por no considerarlas de interés para los objetivos propuestos o similitidud con otras
    - Se seleccionaron 10 monedas para realizar el análisis
    -*Se puede ver la técnica utilizada en el siguiente notebook [ETL.ipynb](ETL.ipynb)*

- Período analizado: 5 Años (26-08-2018 / 25-08-2023)

- Monedas seleccionadas
  1. **Bitcoin (BTC)** ![Alt text](src/btc.png) es una criptomoneda descentralizada basada en tecnología blockchain, sin control central y con un suministro limitado de 21 millones de monedas, lo que ha generado interés como inversión y reserva de valor
  2. **Ether (ETH)** ![Alt text](src/eth.png) es la criptomoneda nativa de la plataforma Ethereum, utilizada para pagar por transacciones y servicios en la red, además de respaldar contratos inteligentes y aplicaciones descentralizadas, lo que le otorga utilidad en diversos casos de uso dentro del ecosistema blockchain
  3. **Binance Coin (BNB)** ![Alt text](src/bnb.png) es la criptomoneda nativa de la plataforma de intercambio de criptomonedas Binance. Se utiliza para pagar comisiones de trading en la plataforma y ofrece diversas utilidades, como participar en ventas de tokens y acceder a servicios dentro del ecosistema Binance
  4. **Staked Ether (STETH)** ![Alt text](src/stke.png) es una representación tokenizada de los Ether (ETH) depositados y apostados en la red Ethereum 2.0, que busca mejorar la escalabilidad y eficiencia de la blockchain mediante la tecnología de prueba de participación (PoS). STETH permite a los poseedores participar en el proceso de validación y ganar recompensas por mantener sus activos apostados
  5. **Cardano (ADA)** ![Alt text](src/ada.png) Cardano es una plataforma blockchain de tercera generación que se centra en la escalabilidad, sostenibilidad y seguridad, respaldada por su criptomoneda nativa ADA. Busca habilitar contratos inteligentes y aplicaciones descentralizadas mientras se apoya en investigaciones científicas y enfoques académicos para mejorar la tecnología blockchain
  6. **Dogecoin (DOGE)** ![Alt text](src/doge.png) es una criptomoneda originada como una broma en 2013, basada en un meme de un perro Shiba Inu. Aunque comenzó como una moneda humorística, ha ganado cierta popularidad y aceptación como una forma de microtransacciones en línea y donaciones caritativas
  7. **Solana (SOL)** ![Alt text](src/sol.png) es una plataforma blockchain de alto rendimiento que busca abordar problemas de escalabilidad, procesando un gran número de transacciones a velocidades rápidas y costos bajos, lo que la hace adecuada para aplicaciones descentralizadas y finanzas descentralizadas (DeFi)
  8. **Tron (TRX)** ![Alt text](src/trx.png) Tron es una plataforma blockchain que tiene como objetivo descentralizar la industria del entretenimiento y contenido digital, permitiendo a los usuarios crear, distribuir y consumir contenido directamente sin intermediarios
  9. **PolkaDot (DOT)** ![Alt text](src/dot.png) Polkadot es una plataforma de cadenas de bloques interoperables que permite a diferentes redes blockchain comunicarse y compartir información de manera eficiente, fomentando la innovación y colaboración entre proyectos descentralizados
  10. **Ripple (XRP)** ![Alt text](src/xrp.png) es una plataforma de pagos y soluciones financieras basada en blockchain, diseñada para facilitar transferencias de dinero globales de manera rápida y económica. XRP es su criptomoneda asociada, utilizada para facilitar transacciones en la red y como puente de liquidez


### **KPIs utilizados**
1 . **Cambio de precio porcentual:** Nos muestra el cambio en el precio de una criptomoneda en un período de tiempo específico. Nos permite evaluar la volatilidad y el rendimiento a corto plazo de una criptomoneda.

2 . **volumen de capitalización:** Compara la capitalización de mercado de una criptomoneda con su volumen de operaciones. Nos indica si una criptomoneda está sobrevalorada o infravalorada en función de la relación entre su capitalización de mercado y su volumen de operaciones.

3 . **Relación Precio/volumen:** Divide el precio actual por el volumen promedio para obtener una relación entre el precio y la actividad comercial. Esto puede ayudar a identificar si los movimientos de precios son respaldados por un volumen significativo.


### **Conclusiones**
* Dado el precio actual de las criptomonedas en general y sus valores máximos pueden resultar una buena inversión en el mediano / largo plazo, no tanto así en el corto plazo ya que se encuentran en un período de estancamiento de precios y tienen altibajos dentro de un rango de precios medios.
* De acuerdo a lo observado, es vital escoger bien tanto el momento de compra como el de venta de la moneda elegida, para poder capitalizar ganancias.
* Si bien casi todas las criptomonedas pueden ser convertidas a moneda corriente de forma casi inmediata, tener que venderlas en un mal momento puede generar pérdidas considerables.
* Al no haber invertido nunca en este tipo de activos, se recomienda seleccionar alguna de las monedas con mayor capitalización ya que brindan menores riesgos. Otra opción es diversificar la inversión en mas de una moneda.
* Teniendo en cuenta la situación económica-financiera de Argentina, el hecho de que las criptomonedas son convertibles a valor dólar, hace más atractiva la inversión ya que nos permite cubrirnos de la creciente inflación actual.


### **Observaciones**
* Un detalle a tener en cuenta es dónde se van a guardar las criptomonedas, ya que existen varias opciones, detallo las más comunes.
    * Billeteras frías: Más seguras, pero menos versátiles (sólo sirven para una moneda y existen sólo para algunas criptomonedas)
    * Billeteras calientes: Menos seguras, están conectadas a internet todo el tiempo
    * Plataformas de intercambio: Menos seguras, permiten invertir las monedas y obtener ganancias extra, pero hay que tener en cuenta que estas plataformas se convierten en las tenedoras de los activos, lo que implica un riesgo extra
