import streamlit as st
import pandas as pd

st.logo("./logo.jpg", size="large", icon_image="./logo.jpg")
st.title("Calculadora Trading Ans")

SINTETICOS = "Índices sintéticos"
BURSATILES = "Forex y bursátiles"

modo = st.pills("Tipo de mercado", [SINTETICOS, BURSATILES])

if modo == SINTETICOS:
    volatilities = [
        {"nombre": "Volatility 10 (1s)", "min": 0.5, "max": 100},
        {"nombre": "Volatility 10", "min": 0.5, "max": 100},
        {"nombre": "Volatility 25 (1s)", "min": 0.005, "max": 1},
        {"nombre": "Volatility 25", "min": 0.5, "max": 150},
        {"nombre": "Volatility 50 (1s)", "min": 0.005, "max": 1},
        {"nombre": "Volatility 50", "min": 4, "max": 1000},
        {"nombre": "Volatility 75 (1s)", "min": 0.05, "max": 10},
        {"nombre": "Volatility 75", "min": 0.001, "max": 1},
        {"nombre": "Volatility 100 (1s)", "min": 0.2, "max": 50},
        {"nombre": "Volatility 100", "min": 0.5, "max": 100},
    ]
    crash_boom = [
        {"nombre": "Crash 300", "min": 0.5, "max": 15},
        {"nombre": "Crash 500", "min": 0.2, "max": 80},
        {"nombre": "Crash 1000", "min": 0.2, "max": 80},
        {"nombre": "Boom 300", "min": 1, "max": 100},
        {"nombre": "Boom 500", "min": 0.2, "max": 50},
        {"nombre": "Boom 1000", "min": 0.2, "max": 50},
    ]
    col1, col2 = st.columns(2)
    with col1:
        indice1 = st.selectbox("Volatilities",
                               volatilities,
                               index = None, 
                               placeholder="Vas a usar un Volatility?",
                               help="Selecciona uno si vas a operar un Volatility.",
                               format_func=lambda a: a["nombre"])
    with col2:
        indice2 = st.selectbox("Crash y Boom",
                               crash_boom,
                               index = None,
                               placeholder="Vas a usar un Crash o Boom?",
                               help="Selecciona uno si vas a operar un Crash o Boom.",
                               format_func=lambda a: a["nombre"])
    
    if indice := indice1 or indice2:
        st.divider()
        col1, col2 = st.columns(2)
        with col1:
            st.header(f"**{indice['nombre']}**")
        with col2:
            st.write(f"**Lotaje mínimo**: {indice['min']}")
            st.write(f"**Lotaje máximo**: {indice['max']}")
    
        st.divider()
        col1, col2 = st.columns(2)
        with col1:
            cuenta = st.number_input("Tamaño de la cuenta", min_value=0.0,
                                     help="Cuál es el tamaño de tu cuenta?",
                                     value=None,
                                     format="%.2f")
        with col2:
            pips_sl = st.number_input("Tamaño de :red[stop loss]", min_value=0.00,
                                     help="Cuál es el tamaño de tu Stop Loss?",
                                     value=None,
                                     format="%.2f")
            
        if cuenta and cuenta > 0 and pips_sl and pips_sl > 0:
            uno_porciento = cuenta * 0.01
            lot1 = uno_porciento / pips_sl
            lot2 = lot1 / 2
            lot3 = lot1 / 3

            st.markdown("<h5><u>Lotaje recomendado a utilizar</u></h5>", unsafe_allow_html=True)

            if lot1 < indice["min"]:
                st.write("Utilizar lotaje mínimo.")
            
            else:
                data = pd.DataFrame(
                    {
                    "Arriesgar 1% de la cuenta": [f"{lot1:.2f}"],
                    "Arriesgar 0.5% de la cuenta": [f"{lot2:.2f}"],
                    "Arriesgar 0.33% de la cuenta": [f"{lot3:.2f}"]
                    }
                )

                s1 = dict(selector='th', props=[('text-align', 'center')])
                s2 = dict(selector='td', props=[('text-align', 'center')])
                s3 = dict(selector='td', props=[('width', '100vw')])

                # you can include more styling paramteres, check the pandas docs
                table = data.style.set_table_styles([s1,s2,s3]).hide(axis=0).to_html()     
                st.write(f'{table}', unsafe_allow_html=True)

if modo == BURSATILES:
    forex = [
        {"nombre": "EUR/USD"},
        {"nombre": "USD/JPY"},
        {"nombre": "GBP/USD"},
        {"nombre": "USD/CHF"},
        {"nombre": "USD/CAD"},
        {"nombre": "AUD/USD"},
        {"nombre": "NZD/USD"}
    ]
    bursatiles = [
        {"nombre": "US30"},
        {"nombre": "US100"},
        {"nombre": "S&P500"}
    ]
    col1, col2 = st.columns(2)
    with col1:
        indice1 = st.selectbox("Pares de Forex",
                               forex,
                               index = None, 
                               placeholder="Vas a usar un par de divisas?",
                               help="Selecciona uno si vas a operar un par de divisas.",
                               format_func=lambda a: a["nombre"])
    with col2:
        indice2 = st.selectbox("Índices bursátiles",
                               bursatiles,
                               index = None,
                               placeholder="Vas a usar un indice bursátil?",
                               help="Selecciona uno si vas a operar un índice bursátil.",
                               format_func=lambda a: a["nombre"])
    
    if indice1 or indice2:
        st.divider()
        col1, col2 = st.columns(2)
        with col1:
            st.write("")
            st.write("")
            st.header(f"\t**{indice1['nombre']}**")
    
        with col2:
            cuenta = st.number_input("Tamaño de la cuenta", min_value=0.0,
                                     help="Cuál es el tamaño de tu cuenta?",
                                     value=None,
                                     format="%.2f")
            pips_sl = st.number_input("Tamaño de :red[stop loss]", min_value=0.00,
                                     help="Cuál es el tamaño de tu Stop Loss?",
                                     value=None,
                                     format="%.2f")
        st.divider()
        if cuenta and cuenta > 0 and pips_sl and pips_sl > 0:
            uno_porciento = cuenta * 0.01
            if indice1:
                lot1 = uno_porciento / pips_sl / 10
            if indice2:
                lot1 = uno_porciento / pips_sl
            lot2 = lot1 / 2
            lot3 = lot1 / 3

            st.markdown("<h5><u>Lotaje recomendado a utilizar</u></h5>",
                        unsafe_allow_html=True)

            if lot1 < 0.01:
                st.write("Utilizar lotaje mínimo (0.01)")
            
            else:
                data = pd.DataFrame(
                    {
                    "Arriesgar 1% de la cuenta": [f"{lot1:.2f}"],
                    "Arriesgar 0.5% de la cuenta": [f"{lot2:.2f}"],
                    "Arriesgar 0.33% de la cuenta": [f"{lot3:.2f}"]
                    }
                )

                s1 = dict(selector='th', props=[('text-align', 'center')])
                s2 = dict(selector='td', props=[('text-align', 'center')])
                s3 = dict(selector='td', props=[('width', '100vw')])

                # you can include more styling paramteres, check the pandas docs
                table = data.style.set_table_styles([s1,s2,s3]).hide(axis=0).to_html()     
                st.write(f'{table}', unsafe_allow_html=True)