import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 

import pandas_datareader.data as web
import mplfinance as mpf
import datetime as dt
import requests
import panel as pn
pn.extension()
import ccxt
import os
import asyncio
from dotenv import load_dotenv
load_dotenv()

exchange_id = "ftx"
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class(
{
    "enableRateLimit": True,
    "apikey": os.environ.get("APIKey"),
    "secret": os.environ.get("APISecret"),
}
)
#/BTC/USD/trades?start_time=0000000000&end_time=9999999999
df = requests.get(
"https://ftx.com/api/markets"
).json()

df= pd.DataFrame(df["result"])

df_all = df.copy()
#print(df.head())


st.set_page_config(
    page_title = 'Real-Time Data Science Dashboard',
    page_icon = '✅',
    layout = 'wide'
)

# dashboard title

st.title("Criptomonedas: Alternativa de Inversión a Largo Plazo !")

# top-level filters 

moneda = st.selectbox("Elige moneda", pd.unique(df['name']))


# creating a single-element container.
placeholder = st.empty()

# dataframe filter 

df = df[df['name']==moneda]

for seconds in range(9000,12000):
#while True: 
    
    df['priceHigh24h'] = df['priceLow24h'] * np.random.choice(range(1,5))
    df['quoteVolume24h'] = df['volumeUsd24h'] * np.random.choice(range(1,5))

    # creating KPIs 
    avg_age = np.mean(df['priceHigh24h']) 

    count_incremento = int(df[(df["priceIncrement"]=='incremento')]['priceIncrement'].count() + np.random.choice(range(1,30)))
    
    balance = np.mean(df['quoteVolume24h'])

    with placeholder.container():
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs 
        kpi1.metric(label="PriceLow24 ⏳", value=round(avg_age), delta= round(avg_age) - 10)
        kpi2.metric(label="Conteo ", value= int(count_incremento), delta= - 10 + count_incremento)
        kpi3.metric(label="A/C Volume ＄", value= f"$ {round(balance,2)} ", delta= - round(balance/count_incremento) * 100)

        
        st.image(f'https://finviz.com/chart.ashx?t=APP')

        # create two columns for charts 

        fig_col1, fig_col2, fig_col3 = st.columns(3)
        with fig_col1:
            st.markdown("### Primera gráfica")
            fig1 = px.density_heatmap(data_frame=df, y = 'priceHigh24h', x = 'priceHigh24h')
            st.write(fig1)
        with fig_col2:
            st.markdown("### Segunda gráfica")
            fig2 = px.histogram(data_frame = df, y='priceLow24h', x = 'priceHigh24h')
            st.write(fig2)
        with fig_col3:
            start = dt.datetime(2020,6,1)
            end = dt.datetime(2020,7,1)    
            df_velas = web.DataReader('MSFT', 'yahoo', start, end )
            st.markdown("### Precios")
            velas= mpf.plot(df_velas, type='candle', style='charles', title='Varianza Precios', ylabel='Price High 24h')
            st.write(df_velas)
        
        st.markdown("### Vista detallada de los datos")
        st.dataframe(df_all)
        time.sleep(8)
    #placeholder.empty()        