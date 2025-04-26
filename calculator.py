import streamlit as st
import pandas as pd

st.set_page_config("Calculadora Trading Ans", page_icon="./logo.jpg")
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
        {"nombre": "US30 - Dow Jones"},
        {"nombre": "US100 - NASDAQ"},
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
    
    if indice := indice1 or indice2:
        st.divider()
        col1, col2 = st.columns(2)
        with col1:
            st.write("")
            st.write("")
            st.write("")
            st.header(f"\t**{indice['nombre']}**")
            if indice in forex:
                st.caption("Este par esta bajo proceso de revisión")
        with col2:
            cuenta = st.number_input("Tamaño de la cuenta", min_value=0.0,
                                     help="Cuál es el tamaño de tu cuenta?",
                                     value=None,
                                     format="%.2f")
            pips_sl = st.number_input("Tamaño de :red[stop loss]", min_value=0.00,
                                     help="Cuál es el tamaño de tu Stop Loss?",
                                     value=None,
                                     format="%.2f")
            if indice == bursatiles[0]:
                amd_toggle = st.toggle("Asistencia AMD")
        
        st.divider()
        if amd_toggle:
            pips_sl = 40
        
        if cuenta and cuenta > 0 and pips_sl and pips_sl > 0:
            col1, col2 = st.columns(2)
            with col1:
                plataforma = st.pills("Lotaje recomendado a utilizar en", 
                                        ["FTMO", "Doo Prime", "Otro"])
            with col2:
                if cuenta < 1001:
                    st.write("")
                    agresiva = st.toggle("Gestion agresiva")
                else:
                    agresiva = False
                    st.write("")

            uno_porciento = cuenta * 0.01
            if indice1:
                lot1 = uno_porciento / pips_sl / 10
            if indice2:
                lot1 = uno_porciento / pips_sl
            lot2 = lot1 / 2
            lot3 = lot1 / 3

            if plataforma == "Doo Prime":
                lot1 = lot1/10
                lot2 = lot2/10
                lot3 = lot3/10
                        
            if agresiva:
                lot1 = lot1*10
                lot2 = lot2*10
                lot3 = lot3*10
                data = pd.DataFrame({
                    "Arriesgar 10% de la cuenta": [f"{lot1:.2f}"],
                    "Arriesgar 5% de la cuenta": [f"{lot2:.2f}"],
                    "Arriesgar 3.3% de la cuenta": [f"{lot3:.2f}"]
                })
            else:
                data = pd.DataFrame(
                    {
                    "Arriesgar 1% de la cuenta": [f"{lot1:.2f}"],
                    "Arriesgar 0.5% de la cuenta": [f"{lot2:.2f}"],
                    "Arriesgar 0.33% de la cuenta": [f"{lot3:.2f}"]
                    }
                )

            if lot1 < 0.01:
                st.write("**Utilizar lotaje mínimo de 0.01**")
            st.dataframe(data, hide_index=True, use_container_width=True, )
            if plataforma == "Otro":
                st.write("**Lo mejor sería revisar estos lotajes antes de operar.**")

            if amd_toggle:
                st.divider()
                col1, col2 = st.columns(2)
                with col1:
                    st.write("")
                    st.write("")
                    st.header(f"\t**Asistencia AMD**")
                    st.caption("La estrategia utiliza :red[40 pips de SL] y :green[120 pips de TP].")
                with col2:
                    entrada = st.number_input("Punto de entrada", min_value=0.00,
                                            help="Cuál es el punto de entrada?",
                                            value=None,
                                            format="%.2f")
                    operacion = st.selectbox("Tipo de operación", ["Compras", "Ventas"],
                                            help="Tipo de operación.",
                                            placeholder="Compras o ventas",
                                            index=None)
                    sl, tp, tp2 = (0,0,0)
                    if operacion == "Ventas":
                        tp = entrada - 120
                        tp2 = entrada - 400
                        sl = entrada + 40
                    if operacion == "Compras":
                        tp = entrada + 120
                        tp2 = entrada + 400
                        sl = entrada - 40

                if operacion is not None and entrada is not None: 
                    st.write("")
                    st.write("")
                    st.write(f"""
                        Utiliza los siguientes datos para tu operación de AMD en **{operacion}**:
                        * **:red[SL]**: {sl}
                        * **:green[TP]**: {tp}
                        * **:green[TP 1:10]**: {tp2} _(Este en caso de que operes AMD 2.0)_

                        Selecciona, copia y pega en tu MetaTrader. 
                        
                        **Recordá:** Si utilizás varios MetaTrader, el punto de entrada puede variar y sea necesario repetir el cálculo.
                    """)

                    
                
                    


