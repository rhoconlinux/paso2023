import pickle
from pathlib import Path
import pandas as pd  # pip install pandas openpyxl plotly-express streamlit
import plotly.express as px  
import streamlit as st  
import requests
import gdown
from datetime import datetime
import time
import plotly.express as px
import plotly.graph_objects as go

# EXCEL TEST: https://docs.google.com/spreadsheets/d/1r8k3yu4SjegdwVhGgLbDjDPgcxE1zL2uuGRvi2bxLZY/edit#gid=0
st.set_page_config(page_title="Resultados Provisorios PASO 2023", page_icon="", layout="wide")

 Hard-coded usernames and passwords
 credentials = {
     "user": "123",
     "Usuario_Alto_Nivel": "Acc3d#r",
     "Usuario": "acceso_resultados123"
 }
 
 session_state = st.session_state
 if 'logged_in' not in session_state:
     session_state.logged_in = False
 if not session_state.logged_in:
     st.title("Login")
     username = st.text_input("Username")
     password = st.text_input("Password", type="password")
     if st.button("Login"):  # Existing login button
         if username in credentials and credentials[username] == password:
             st.success("Acceso correcto!")
             session_state.logged_in = True
             st.experimental_rerun()  # Add this line to force rerun of the script after successful login
         else:
             st.error("Username/password is incorrect")
 else:

#if 1==2:
#    page_title="loco"
#else:           

    # ---- READ EXCEL ----
   #the Google Sheet (converted to CSV download link)
    url = "https://docs.google.com/spreadsheets/d/1r8k3yu4SjegdwVhGgLbDjDPgcxE1zL2uuGRvi2bxLZY/export?format=xlsx"
    output_path = "data.xlsx"
    
    def load_data():
        gdown.download(url, output_path, quiet=False)
        df = pd.read_excel(output_path, header=None)
        return df
    
    df = load_data()
    exec(open("procesos_limpieza.py").read())
    
    refresh_interval = 1 * 60  # 2 (1) minutes in seconds
    # Function to update data
    
    
#########################################################
#preprocessing...

    # ---- MAINPAGE ----
    st.markdown("<h1 align='center'>Resultados Provisorios PASO 2023</h1>", unsafe_allow_html=True)

    # Define the columns for centering the button
    col1, col2, col3 = st.columns([5, 2, 5])

    # Place the button in the middle column
    with col2:
        if st.button('Actualizar datos'):
            df = load_data()
            exec(open("procesos_limpieza.py").read())
        else:
            df = load_data()
            exec(open("procesos_limpieza.py").read())

    st.markdown("<hr>", unsafe_allow_html=True)

    
    
    
    
############### resumen top
    # Counting occurrences of "MESA"
    mesa_count = df["MESA"].count()

    # Calculate the time since last update
    last_update_time = datetime.now()  # Replace this with the actual timestamp of data update
    current_time = datetime.now()
    time_difference = current_time - last_update_time
    time_since_update = f"{time_difference.seconds} segundos"
    #formatted_last_update = last_update_time.strftime("%Y-%m-%d %H:%M:%S")
    formatted_last_update = last_update_time.strftime("%H:%M:%S")
#
#    st.write(
#        "<div style='display: flex; border: none; padding: 0; text-align: center;'>"
#        f"<div style='flex: 1; border: none;'>Última actualización: <span style='color: #FF4B4B; font-size: 18px;'><b>{formatted_last_update}</b></span></div>"
#        f"<div style='flex: 1; border: none;'>Mesas Escrutinadas: <span style='color: #FF4B4B; font-size: 18px;'><b>{mesa_count}</b></span></div>"
#        f"<div style='flex: 1; border: none;'>% Mesas Escrutinadas: <span style='color: #FF4B4B; font-size: 18px;'><b>{mesa_count/500*100:.2f}</b></span></div>"
#        "</div>",
#        unsafe_allow_html=True
#    )


############### TABLA Y PIE POR LISTA

    # Bloque to Nombre_Bloque mapping
    bloque_mapping = {
        "90": "MOVIMIENTO IZQUIERDA",
        "137": "PRINCIPIOS Y VALORES",
        "57": "ACCIÓN VECINAL",
        "57 ": "ACCIÓN VECINAL",
        "131": "FRENTE LIBER.AR",
        "94": "PROYECTO JOVEN",
        "132": "JUNTOS POR EL CAMBIO",
        "136": "FRENTE DE IZQUIERDA",
        "95": "FRENTE PATRIOTA FEDERAL",
        "40": "MOVIMIENTO LIBRES DEL SUR",
        "134": "UNION POR LA PATRIA",
        "20": "UNION DEL CENTRO DEMOCRATICO",
        "20 ": "UNION DEL CENTRO DEMOCRATICO",
        "13": "MOVIMIENTO AL SOCIALISMO",
        "135": "REPUBLICANOS UNIDOS",
        "133": "HACEMOS POR NUESTRO PAÍS",
        "133 ": "HACEMOS POR NUESTRO PAÍS",
        "92": "POLITICA OBRERA",
        "92 ": "POLITICA OBRERA",
        "57": "ACCION VECINAL",
        "40 ": "LIBRES DEL SUR",
    }
    
    candidatos_mapping = {
        "132.502.A - JUNTOS POR EL CAMBIO / TDF (El cambio de nuestras vidas)": "Larreta - Morales",
        "132.502.B - JUNTOS POR EL CAMBIO / TDF (La fuerza del cambio)": "Bullrich - Petri",
        "133 - HACEMOS POR NUESTRO PAÍS": "Schiaretti - Randazzo",
        "134.501.A - UNION POR LA PATRIA (Celeste y blanca)": "Massa - Rossi",
        "134.B - UNION POR LA PATRIA (Justa y Soberana)": "Grabois - Abal Medina",
        "135.212 - LA LIBERTAD AVANZA / REPUBLICANOS UNIDOS": "Milei - Villaruel",
        "136.504.A - FRENTE DE IZQUIERDA Y DE TRABAJADORES (Unir y fortalecer la izquierda)": "Bregman - Del Caño",
        "136.504.B - FRENTE DE IZQUIERDA Y DE TRABAJADORES (Unidad de Luchadores y la Izquierda)": "Solano - Ripoll"
        # Add more mappings here if needed
    }
    
    
    
    # Function to extract the Bloque identifier
    def get_bloque(list_name):
        bloque = list_name.split('.')[0]
        # If the Bloque identifier does not contain a dot, extract only the numeric part
        if '.' not in list_name:
            bloque = list_name.split('-')[0]
        return bloque

    # Function to generalize the case for different groups
    def get_summary_table(group_suffix):
        group_columns = [col for col in df.columns if col.endswith(group_suffix)]
        summary_table = pd.DataFrame({
            'Lista': group_columns,
            'Votos_totales': [df[col].sum() for col in group_columns],
        })
        summary_table['Lista'] = summary_table['Lista'].str.replace(group_suffix, '')
        summary_table['Bloque'] = summary_table['Lista'].apply(get_bloque)
        total_votes = df[f"TOTALES{group_suffix}"].sum()
        summary_table['Porcentaje'] = summary_table['Votos_totales'] / total_votes
        summary_table['Nombre_Bloque'] = summary_table['Bloque'].map(bloque_mapping)
        summary_table = summary_table.sort_values(by='Votos_totales', ascending=False)
        return summary_table




    summary_table = get_summary_table(" - Presidente")

    bloque_summary = summary_table.groupby('Bloque').agg({
        'Votos_totales': 'sum',
        'Porcentaje': 'sum'
    }).reset_index()
    summary_table = summary_table.merge(bloque_summary, on='Bloque', suffixes=('', '_Bloque'))

    exclude_list = [
        "TOTALES",
        "TOTAL VOTOS AGRUPACIONES POLÍTICAS",
        "VOTOS NULOS",
        "VOTOS RECURRIDOS",
        "VOTOS EN BLANCO",
    ]
    
    #MAIN TABLE    
    main_table = summary_table[~summary_table['Lista'].isin(exclude_list)]
    main_table['Candidatos_Presidente'] = main_table['Lista'].map(candidatos_mapping)
    desired_columns_order = ["Nombre_Bloque", "Lista", "Votos_totales", "Porcentaje", "Candidatos_Presidente", "Porcentaje_Bloque", "Votos_totales_Bloque"]
    main_table = main_table[desired_columns_order]
    sintesis_table = summary_table[summary_table['Lista'].isin(exclude_list)][['Lista', 'Votos_totales', 'Porcentaje']]

    # Síntesis Table
    # Place the table in the middle column
    col1, col2, col3 = st.columns([2, 5, 1])
    with col1:
        st.markdown("""
            <div style='padding-top: 40%; text-align: center;'>
                <span style='font-size: 16px; text-align: center;'>Síntesis <br>(sólo votos Presidente)</span>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.write(sintesis_table.style.set_properties(**{'text-align': 'center'}))



    st.write(
        "<div style='display: flex; border: none; padding: 0; text-align: center;'>"
        f"<div style='flex: 1; border: none;'>Última actualización: <span style='color: #FF4B4B; font-size: 18px;'><b>{formatted_last_update}</b></span></div>"
        f"<div style='flex: 1; border: none;'>Mesas Escrutinadas: <span style='color: #FF4B4B; font-size: 18px;'><b>{mesa_count}</b></span></div>"
        f"<div style='flex: 1; border: none;'>% Mesas Escrutinadas: <span style='color: #FF4B4B; font-size: 18px;'><b>{mesa_count/500*100:.2f}</b></span></div>"
        "</div>",
        unsafe_allow_html=True
    )
    st.markdown("<hr>", unsafe_allow_html=True)

#################################################################


######## TABLA
    # Define the group_suffix and group_name for the Detail Table
    group_suffix = " - Presidente"
    group_name = group_suffix.split('-')[1].strip()
    
    # Define the columns for the short table view
    short_columns = ['Nombre_Bloque', 'Votos_totales_Bloque', 'Porcentaje_Bloque']
    
    show_details = st.checkbox("Ver detalles por lista")
    
    collapsed_table = main_table.groupby('Nombre_Bloque', as_index=False).agg({
        'Votos_totales_Bloque': 'sum',
        'Porcentaje_Bloque': 'sum'
    })
    st.markdown("<h4 style='text-align: center;'>Resultados ({})</h4>".format(group_name), unsafe_allow_html=True)
    if show_details:
        columns_to_display = main_table.columns
        st.write(main_table[columns_to_display].style.set_properties(**{'text-align': 'center'}))
    else:
        columns_to_display = short_columns
        col1, col2, col3 = st.columns([2, 7, 1])
        with col2:
            st.write(collapsed_table[columns_to_display].style.set_properties(**{'text-align': 'center'}))

    # Display the collapsed and aggregated table


### TORTA
    # Pie chart
    # Create a pie chart using Plotly
    # Select the top 10 blocks and group the rest as 'Otros'
    top_blocks = main_table.nlargest(10, 'Votos_totales_Bloque')
    other_blocks = main_table[~main_table['Nombre_Bloque'].isin(top_blocks['Nombre_Bloque'])]
    other_votos_total = other_blocks['Votos_totales_Bloque'].sum()
    # Create a new DataFrame for 'Otros' data
    otros_data = pd.DataFrame({'Nombre_Bloque': ['Otros'], 'Votos_totales_Bloque': [other_votos_total], 'Porcentaje_Bloque': [0]})
    # Concatenate 'Otros' data with top_blocks DataFrame
    top_blocks = pd.concat([top_blocks, otros_data], ignore_index=True)
    # Create the label strings with 'Nombre_Bloque' and 'Votos_totales_Bloque'
    label_strings = [f"{row['Nombre_Bloque']} - {row['Votos_totales_Bloque']}" for index, row in top_blocks.iterrows()]

    fig = go.Figure(data=[go.Pie(
        labels=label_strings,  # Use the label strings we created
        values=top_blocks['Votos_totales_Bloque'],
        hole=0.4,
        textinfo='percent+label',  # Show percentage and label
        textposition='outside',
         textfont_size=18,
    )])

    # Update layout for better label appearance and larger graph
    fig.update_layout(title_text='Distribución de Votos por Bloque', title_x=0.4, showlegend=False)
    fig.update_traces(textfont_size=12, marker=dict(line=dict(color='#000000', width=2)))
    fig.update_layout(autosize=False, width=800, height=600)  # Set width and height

    # Display the pie chart
    st.plotly_chart(fig, use_container_width=True)




#### BARRAS CANDIDATOS
  #### BARRAS CANDIDATOS
   # Creating custom color mapping for specific candidates
    color_mapping = {
        "Massa - Rossi": "azure",
        "Grabois - Abal Medina": "deepskyblue",
        "Bregman - Del Caño": "firebrick",
        "Solano - Ripoll": "red",
        "Bullrich - Petri": "yellow",
        "Larreta - Morales": "gold",
        "Milei - Villaruel": "palevioletred",
    }
        # Create bar_data including all non-null values from main_table
    bar_data = main_table[main_table['Candidatos_Presidente'].notna()]
    bar_data = bar_data[['Candidatos_Presidente', 'Votos_totales']]
    bar_data['color'] = bar_data['Candidatos_Presidente'].map(color_mapping)

    # Create the horizontal bar chart using Plotly Express
    fig = px.bar(bar_data,
                x='Votos_totales',
                y='Candidatos_Presidente',
                title='Total Votes for Each Candidate in the Presidente Category',
                text='Votos_totales',
                orientation='h',
                height=900,
                color='Candidatos_Presidente',  # Use this column for color mapping
                color_discrete_sequence=[color_mapping.get(candidate, 'gray') for candidate in bar_data['Candidatos_Presidente']])

    # Customize the appearance
    fig.update_traces(texttemplate='%{text:.3s}', textposition='outside', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5)
    fig.update_layout(showlegend=False,
                    xaxis_title='Total Votes',
                    yaxis_title='Candidates for Presidente',
                    font=dict(size=14),
                    autosize=False,
                    width=1000)

    # Display the plot
    st.plotly_chart(fig)




###### Graph Bar
    # Selecting the columns for candidates and total votes
    bar_data = main_table[['Lista', 'Votos_totales']]

    # Creating the bar chart using Plotly Express
    fig = px.bar(bar_data,
                x='Lista',  # Candidates on the x-axis
                y='Votos_totales',  # Total votes on the y-axis
                title='Total Votes for Each Candidate in the Presidente Category',
                text='Votos_totales',  # Displaying the total votes on top of each bar
                color='Votos_totales',  # Coloring the bars based on total votes
                height=900)  # Increased height

    # Customize the appearance
    fig.update_traces(texttemplate='%{text:.3s}', textposition='outside', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5)
    fig.update_layout(showlegend=False,
                    xaxis_title='Candidates for Presidente',
                    yaxis_title='Total Votes',
                    xaxis=dict(tickmode='array', tickvals=list(range(len(bar_data['Lista']))), ticktext=bar_data['Lista'], tickangle=45),  # 45-degree angle for x-axis labels
                    font=dict(size=14),
                    autosize=False,  # Disable autosizing to set custom width
                    width=1200)  # Custom width, three times bigger

    # Display the plot
    st.plotly_chart(fig)











    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
####################### SIDEBAR EXTRAS ###################################   
###### TABLA PRESIDENTE ########
    # Filtering columns that end with " - Presidente"
    presidente_columns = [col for col in df.columns if col.endswith(" - Presidente")]
    summary_table_presidente = pd.DataFrame({
        'Lista': presidente_columns,
        'Votos_totales': [df[col].sum() for col in presidente_columns],
    })
    # Calculating the third column by dividing each sum by the value of "TOTALES - Presidente"
    total_presidente = df["TOTALES - Presidente"].sum()
    summary_table_presidente['Porcentaje'] = summary_table_presidente['Votos_totales'] / total_presidente
    pd.set_option('display.max_rows', None)
    summary_table_presidente.to_string(index=False)
    # Sort 
    summary_table_presidente = summary_table_presidente.sort_values(by='Votos_totales', ascending=False)
    #st.dataframe(summary_table_presidente, width=500)
    
    # Add a checkbox in the sidebar to toggle the display
    st.sidebar.info("Datos en detalle")
    display_table = st.sidebar.checkbox("(Tabla) Totales por Lista - Presidente")
    if display_table:
        # Add a title to the sidebar
        st.title("Totales por Lista - Presidente")
        st.write('<style>div.row-widget.stTitle > h1 { font-size: 9px; }</style>', unsafe_allow_html=True)
        st.dataframe(summary_table_presidente, width=800)




###### TABLA parlasur ########
    # Filtering columns that end with " - Presidente"
    parlasur_columns = [col for col in df.columns if col.endswith(" - Parlasur")]
    summary_table_parlasur = pd.DataFrame({
        'Lista': parlasur_columns,
        'Votos_totales': [df[col].sum() for col in parlasur_columns],
    })
    # Calculating the third column by dividing each sum by the value of "TOTALES - Parlasur"
    total_parlasur = df["TOTALES - Parlasur"].sum()
    summary_table_parlasur['Porcentaje'] = summary_table_parlasur['Votos_totales'] / total_parlasur
    pd.set_option('display.max_rows', None)
    summary_table_parlasur.to_string(index=False)
    # Sort 
    summary_table_parlasur = summary_table_parlasur.sort_values(by='Votos_totales', ascending=False)
    #st.dataframe(summary_table_parlasur, width=500)
    
    # Add a checkbox in the sidebar to toggle the display
    display_table = st.sidebar.checkbox("(Tabla) Totales por Lista - Parlasur")
    if display_table:
        # Add a title to the sidebar
        st.title("Totales por Lista - Parlasur")
        st.write('<style>div.row-widget.stTitle > h1 { font-size: 9px; }</style>', unsafe_allow_html=True)
        st.dataframe(summary_table_parlasur, width=800)




###### TABLA diputados ########
    # Filtering columns that end with " - diputados"
    diputados_columns = [col for col in df.columns if col.endswith(" - Diputados")]
    summary_table_diputados = pd.DataFrame({
        'Lista': diputados_columns,
        'Votos_totales': [df[col].sum() for col in diputados_columns],
    })
    # Calculating the third column by dividing each sum by the value of "TOTALES - diputados"
    total_diputados = df["TOTALES - Diputados"].sum()
    summary_table_diputados['Porcentaje'] = summary_table_diputados['Votos_totales'] / total_diputados
    pd.set_option('display.max_rows', None)
    summary_table_diputados.to_string(index=False)
    # Sort 
    summary_table_diputados = summary_table_diputados.sort_values(by='Votos_totales', ascending=False)
    #st.dataframe(summary_table_diputados, width=500)
    
    # Add a checkbox in the sidebar to toggle the display
    display_table = st.sidebar.checkbox("(Tabla) Totales por Lista - Diputados")
    if display_table:
        # Add a title to the sidebar
        st.title("Totales por Lista - Diputados")
        st.write('<style>div.row-widget.stTitle > h1 { font-size: 9px; }</style>', unsafe_allow_html=True)
        st.dataframe(summary_table_diputados, width=800)



###### TABLA Parlasur Provincia ########
    # Filtering columns that end with " - diputados"
    parlasur_reg_columns = [col for col in df.columns if col.endswith(" - Parlasur Provincia")]
    summary_table_parlasur_reg = pd.DataFrame({
        'Lista': parlasur_reg_columns,
        'Votos_totales': [df[col].sum() for col in parlasur_reg_columns],
    })
    # Calculating the third column by dividing each sum by the value of "TOTALES - parlasur_reg"
    total_parlasur_reg = df["TOTALES - Parlasur_reg"].sum()
    summary_table_parlasur_reg['Porcentaje'] = summary_table_parlasur_reg['Votos_totales'] / total_parlasur_reg
    pd.set_option('display.max_rows', None)
    summary_table_parlasur_reg.to_string(index=False)
    # Sort 
    summary_table_parlasur_reg = summary_table_parlasur_reg.sort_values(by='Votos_totales', ascending=False)
    #st.dataframe(summary_table_parlasur_reg, width=500)
    
    # Add a checkbox in the sidebar to toggle the display
    display_table = st.sidebar.checkbox("(Tabla) Totales por Lista - Parlasur Provincia")
    if display_table:
        # Add a title to the sidebar
        st.title("Totales por Lista - Parlasur Provincia")
        st.write('<style>div.row-widget.stTitle > h1 { font-size: 9px; }</style>', unsafe_allow_html=True)
        st.dataframe(summary_table_diputados, width=800)

        










##########################################    
    # ---- HIDE STREAMLIT STYLE ----
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)
        
        

################################################################################################
################################################################################################



