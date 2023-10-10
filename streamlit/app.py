from typing import List, Tuple

import pandas as pd
import plotly.express as px
import streamlit as st

graficos = {'Precio':'prices', 'Capitalización de Mercado':'market_caps', 'Volúmen':'total_volumes'}


def set_page_config():
    st.set_page_config(
        page_title="Análisis Criptomonedas",
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)

@st.cache_data
def load_data() -> pd.DataFrame:
    data = pd.read_csv('data/cotizaciones.csv')
    data['id_coin'] = data['id_coin'].str.title()
    data['date'] = pd.to_datetime(data['date'])
    return data



def redondear(numero:float):
    lint = len(str(int(numero)))
    decimales = 0 if lint > 3 else 4 - lint
    return round(numero, decimales)




@st.cache_data
def display_kpi_metrics(data: pd.DataFrame) -> List[float]:

    precio_desde = data['prices'].iloc[0]
    precio_hasta = data['prices'].iloc[-1]
    kpi_varicion = round(((precio_hasta-precio_desde) / precio_desde) * 100, 2)

    volumen = data['total_volumes'].iloc[-1]
    capitalizacion = data['market_caps'].iloc[-1]

    
    kpi_volumen_cap = round(volumen / capitalizacion  * 100,2)

    data['precio_vol'] = data['prices'] * data['total_volumes']
    precio = data['precio_vol'].sum()
    volumen = data['total_volumes'].sum()
    kpi_precio_volumen = redondear(precio / volumen)

    help_kpi1 = "Este KPI nos muestra el cambio en el precio de una criptomoneda en un período de tiempo específico. Nos permite evaluar la volatilidad y el rendimiento a corto plazo de una criptomoneda"
    help_kpi2 = "Este KPI compara la capitalización de mercado de una criptomoneda con su volumen de operaciones. Nos indica si una criptomoneda está sobrevalorada o infravalorada en función de la relación entre su capitalización de mercado y su volumen de operaciones a una fecha, en este caso la última seleccionada"
    help_kpi3 = "Este KPI no permite obtener una relación entre el precio y la actividad comercial. Esto puede ayudar a identificar si los movimientos de precios son respaldados por un volumen significativo"
    col_kpi1, col_kpi2, col_kpi3 = st.columns(3)
    with col_kpi1:
        st.markdown(f"<h1 style='text-align: left;font-size: 18px;'>Variación Precio %</h1>", unsafe_allow_html=True, help=help_kpi1)        
        st.markdown(f"<h1 style='text-align: left; color: blue;font-size: 24px;'>{kpi_varicion}</h1>", unsafe_allow_html=True)
    with col_kpi2:
        st.markdown(f"<h1 style='text-align: left;font-size: 18px;'>Volúmen de Capitalización</h1>", unsafe_allow_html=True, help=help_kpi2)        
        st.markdown(f"<h1 style='text-align: left; color: blue;font-size: 24px;'>{kpi_volumen_cap}</h1>", unsafe_allow_html=True)
    with col_kpi3:
        st.markdown(f"<h1 style='text-align: left;font-size: 18px;'>Precio/Volumen</h1>", unsafe_allow_html=True, help=help_kpi3)        
        st.markdown(f"<h1 style='text-align: left; color: blue;font-size: 24px;'>{kpi_precio_volumen}</h1>", unsafe_allow_html=True)





def display_sidebar(data: pd.DataFrame):
    st.sidebar.header('Filtros')
    st.sidebar.divider() 
    moneda = data['id_coin'].unique()
    moneda_seleccion = st.sidebar.selectbox('**Moneda**', moneda)
    st.sidebar.divider() 
    desde = pd.Timestamp(st.sidebar.date_input("**Fecha Desde**", data['date'].min().date()))
    hasta = pd.Timestamp(st.sidebar.date_input("**Fecha Hasta**", data['date'].max().date()))
    st.sidebar.divider() 
    grafico = st.sidebar.selectbox('**Valor a Graficar:**', graficos)

    return moneda_seleccion, desde, hasta, grafico



def display_charts(data: pd.DataFrame, grafico: str):

    # Dividir la pantalla en dos columnas
    graf1, graf2 = st.columns(2)

    with graf1:
        colores = ['green', 'blue', 'orange']
        valor_y = graficos[grafico]
        fig = px.line(data, x='date', y=valor_y, width=900, height=450)
        color = colores[list(graficos.keys()).index(grafico)]
        fig.update_traces(line=dict(color=color))    
        fig.update_layout(title_text=f'{grafico} en el tiempo',
                    title_font=dict(size=18))
        fig.update_xaxes(title_text='')    
        fig.update_yaxes(title_text=grafico,       titlefont = dict(
            family = 'Arial, sans-serif',
            size = 18
        ))        
        fig.update_layout(margin=dict(l=20, r=20, t=50, b=20))
        fig.update_xaxes(rangemode='tozero', showgrid=False)
        fig.update_yaxes(rangemode='tozero', showgrid=True)

        st.plotly_chart(fig, use_container_width=True)

    with graf2:

        capitalizacion = load_data()
        ultima = capitalizacion['date'].iloc[-1]
        capitalizacion = capitalizacion[capitalizacion['date']==ultima]
        capitalizacion = capitalizacion[['id_coin', 'market_caps']].sort_values(by='market_caps', ascending=False)
        fig = px.bar(capitalizacion, x='market_caps', y='id_coin', color='id_coin')

        fig.update_layout(title_text=f"Capitalización de Mercado al {ultima.date().strftime('%m-%d-%Y')}",
                    title_font=dict(size=18))
        fig.update_xaxes(title_text='Capitalización', titlefont = dict(
            family = 'Arial, sans-serif',
            size = 18
        ))            
        fig.update_yaxes(title_text='Moneda', titlefont = dict(
            family = 'Arial, sans-serif',
            size = 18
        ))        

        st.plotly_chart(fig, use_container_width=True)




def display_selections(data: pd.DataFrame):
    moneda = data['id_coin'].iloc[0]
    precio = redondear(data['prices'].iloc[-1]) 
    fecha_desde = data['date'].iloc[0].date().strftime('%m-%d-%Y')          
    fecha_hasta = data['date'].iloc[-1].date().strftime('%m-%d-%Y')      
    periodo = fecha_desde + " / " + fecha_hasta 

    col_moneda, col_precio, col_periodo = st.columns(3)

    with col_moneda:
        st.markdown(f"<h1 style='text-align: left;font-size: 18px;'>Moneda</h1>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: left; color: blue;font-size: 24px;'>{moneda}</h1>", unsafe_allow_html=True)

    with col_precio:
        st.markdown(f"<h1 style='text-align: left;font-size: 18px;'>Precio al {fecha_hasta}</h1>", unsafe_allow_html=True)        
        st.markdown(f"<h1 style='text-align: left; color: blue;font-size: 24px;'>{precio}</h1>", unsafe_allow_html=True)

    with col_periodo:
        st.markdown(f"<h1 style='text-align: left;font-size: 18px;'>Período</h1>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: left; color: blue;font-size: 24px;'>{periodo}</h1>", unsafe_allow_html=True)





def main():
    set_page_config()

    data = load_data()
    st.header(":chart_with_upwards_trend: Análisis Criptomonedas")


    moneda_seleccion, desde, hasta, valor_y = display_sidebar(data)
 
    df_filtrado = data.copy()
    df_filtrado = df_filtrado[(df_filtrado['id_coin']==moneda_seleccion)\
                              & (df_filtrado['date']>=desde)\
                              & (df_filtrado['date']<=hasta)]




    display_selections(df_filtrado)

    st.divider() 
    display_kpi_metrics(df_filtrado)
    st.divider() 
    display_charts(df_filtrado, valor_y)


if __name__ == '__main__':
    main()