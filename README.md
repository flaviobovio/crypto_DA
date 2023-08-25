### Contexto
En mi rol de Analista de Datos de la empresa X, que presta servicios financieros, localizada en Argentina, se me solicita un análisis e informe sobre criptomonedas para evaluar la posibilidad de invertir en estos activos.

### Fuente de Datos 
- Origen [CoinGecko] https://www.coingecko.com
- Período analizado 24-08-2018 - 24-08-2023
- Criterio de selección de tokens
    - Mayor volúmen 
    - Mayor Capitalización de Mercado
    - Se descartaron StableCoins (monedas atadas al valor de una moneda fiat u otro activo), ya que las más utilizadas no representan un atractivo a la hora de invertir
    - Se descartaron monedas similares
    - Se seleccionaron 10 monedas para realizar el análisis

### Archivos y carpetas    
- \data\* Contiene los archivos de datos extraídos
- \source\* Contiene las imágenes del presente archivo
- \ETL.ipnb Notebook con la extración y transformación de los datos
- \EDA.ipynb Notebook con análisis exploratorio de los datos
- \README.md Este archivo


### Monedas seleccionadas
 1. **Bitcoin** ![Alt text](src/btc.png)
 2. **Ethereum** ![Alt text](src/eth.png)
 3. **Staked-Ether** ![Alt text](src/stke.png)
 4. **Cardano** ![Alt text](src/ada.png)
 5. **Dogecoin** ![Alt text](src/doge.png)
 6. **Solana** ![Alt text](src/sol.png)
 7. **Tron** ![Alt text](src/trx.png)
 8. **PolkaDot** ![Alt text](src/dot.png)
 9. **Matic** ![Alt text](src/matic.png)
10. **Ripple** ![Alt text](src/xrp.png)





### KPIs ###
1 . Cambio de precio porcentual: Este KPI muestra el cambio en el precio de una criptomoneda en un período de tiempo específico. Puede ser útil para evaluar la volatilidad y el rendimiento a corto plazo de la criptomoneda.


2 . Volumen de capitalización: compara la capitalización de mercado de una criptomoneda con su volumen de operaciones. Puede indicar si una criptomoneda está sobrevalorada o infravalorada en función de la relación entre su capitalización de mercado y su volúmen de operaciones.

Fórmula: Volumen de capitalización = Capitalización de mercado / Volumen de operaciones


3 . Retorno de la inversión (ROI): El ROI es uno de los KPIs más básicos y se calcula como el porcentaje de ganancia o pérdida en relación con la inversión inicial. La fórmula es: ROI = ((Valor final de la inversión - Valor inicial de la inversión) / Valor inicial de la inversión) * 100.


### Conclusiones ###
* Dado el precio actual de las criptomonedas en general y sus valores máximos históricos pueden resultar una buena inversión en el mediano / largo plazo, no tanto así en el corto plazo ya que se encuentran en un período de estancamiento los precios.
* Al no haber invertido nunca en este tipo de activos, se recomienda seleccionar algunas de las monedas con mayor capitalización ya que brindan menores riegos. Otra opción sería diversificar la inversión.
* De acuerdo a lo observado, es vital escoger bien tanto el momento de la compra como el de la venta, para poder capitalizar ganancias.
* Teniendo en cuenta la situación económica-financiera de Argentina, el hecho de que las criptomonedas son convertibles a valor dólar, hace más atractiva la inversión.


### Observaciones ###
* Un detalle a tener en cuenta es dónde se van a guardar las criptomonedas, ya que existen varias opciones, detallo las más comunes.
    * Billeteras frías: Más seguras, pero menos versátiles (sólo sirven para una moneda)
    * Billeteras calientes: Menos seguras, están conectadas a internet todo el tiempo
    * Plataformas de intercambio: Menos seguras, permiten invertir las monedas y obtener ganancias extra, pero estas, se convierten en las tenedoras de los activos




