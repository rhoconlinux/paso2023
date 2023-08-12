import pandas as pd
import gdown

#url = "https://docs.google.com/spreadsheets/d/1r8k3yu4SjegdwVhGgLbDjDPgcxE1zL2uuGRvi2bxLZY/export?format=xlsx"
#output_path = "data.xlsx"
#gdown.download(url, output_path, quiet=False)
#df = pd.read_excel(output_path, header=None)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.width', None)

# SECCION
contains_text = df.iloc[0].str.contains("Sección, Circuito, Mesa\\n \\[ Número \\] \\n \\[ Sección ]")
columns_to_replace = df.columns[contains_text]
df[columns_to_replace] = df[columns_to_replace].replace("Sección, Circuito, Mesa\\n \\[ Número \\] \\n \\[ Sección ]", "SECCION", regex=True)

# CIRCUITO
contains_text = df.iloc[0].str.contains("Sección, Circuito, Mesa\\n \\[ Número \\] \\n \\[ Circuito ]")
columns_to_replace = df.columns[contains_text]
df[columns_to_replace] = df[columns_to_replace].replace("Sección, Circuito, Mesa\\n \\[ Número \\] \\n \\[ Circuito ]", "CIRCUITO", regex=True)

# MESA
contains_text = df.iloc[0].str.contains("Sección, Circuito, Mesa\\n \\[ Número \\] \\n \\[ Mesa ]")
columns_to_replace = df.columns[contains_text]
df[columns_to_replace] = df[columns_to_replace].replace("Sección, Circuito, Mesa\\n \\[ Número \\] \\n \\[ Mesa ]", "MESA", regex=True)

# CIUDADANOS
contains_text = df.iloc[0].str.contains("Cuidadanos que votaron\\n \\[ Número \\] \\n \\[ Ciudadanos que han votado \\]")
columns_to_replace = df.columns[contains_text]
df[columns_to_replace] = df[columns_to_replace].replace("Cuidadanos que votaron\\n \\[ Número \\] \\n \\[ Ciudadanos que han votado \\]", "CIUDADANOS", regex=True)

# SOBRES
contains_text = df.iloc[0].str.contains("Cuidadanos que votaron\\n \\[ Número \\] \\n \\[ Cantidad de sobres utilizados \\]")
columns_to_replace = df.columns[contains_text]
df[columns_to_replace] = df[columns_to_replace].replace("Cuidadanos que votaron\\n \\[ Número \\] \\n \\[ Cantidad de sobres utilizados \\]", "SOBRES", regex=True)

# DIFERENCIA
contains_text = df.iloc[0].str.contains("Cuidadanos que votaron\\n \\[ Número \\] \\n \\[ Diferencia \\]")
columns_to_replace = df.columns[contains_text]
df[columns_to_replace] = df[columns_to_replace].replace("Cuidadanos que votaron\\n \\[ Número \\] \\n \\[ Diferencia \\]", "DIFERENCIA", regex=True)

row_index = 0  
column_index = 21  
new_value = "13.13 - MOVIMIENTO AL SOCIALISMO - Presidente"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 22  
new_value = "13.13 - MOVIMIENTO AL SOCIALISMO - Parlasur"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 23  
new_value = "13.13 - MOVIMIENTO AL SOCIALISMO - Diputados"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 24  
new_value = "13.13 - MOVIMIENTO AL SOCIALISMO - Parlasur_reg"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 25  
new_value = "20 - UNION DEL CENTRO DEMOCRATICO - Presidente"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 43  
new_value = "40 - MOVIMIENTO LIBRES DEL SUR - Presidente"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 44  
new_value = "40 - MOVIMIENTO LIBRES DEL SUR - Parlasur"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 45  
new_value = "57 - MOVIMIENTO DE ACCIÓN VECINAL - Presidente"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 46  
new_value = "57 - MOVIMIENTO DE ACCIÓN VECINAL - Parlasur"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 60  
new_value = "BORRARRR"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 61  
new_value = "94.C - PROYECTO JOVEN (Todex) - Presidente"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 62  
new_value = "94.C - PROYECTO JOVEN (Todex) - Parlasur"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 93  
new_value = "135.212 - LA LIBERTAD AVANZA / REPUBLICANOS UNIDOS - Presidente"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 102  
new_value = "136.504.B - FRENTE DE IZQUIERDA Y DE TRABAJADORES (Unidad de Luchadores y la Izquierda) - Presidente"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 103  
new_value = "136.504.B - FRENTE DE IZQUIERDA Y DE TRABAJADORES (Unidad de Luchadores y la Izquierda) - Parlasur"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 104  
new_value = "136.504.B - FRENTE DE IZQUIERDA Y DE TRABAJADORES (Unidad de Luchadores y la Izquierda) - Diputados"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 105  
new_value = "136.504.B - FRENTE DE IZQUIERDA Y DE TRABAJADORES (Unidad de Luchadores y la Izquierda) - Parlasur_reg"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 111  
new_value = "137.B - PRINCIPIOS Y VALORES (Transformar) - Parlasur"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 53  
new_value = "92 - POLITICA OBRERA - Presidente"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 54  
new_value = "92 - POLITICA OBRERA - Parlasur"
df.iat[row_index, column_index] = new_value


row_index = 0  
column_index = 184  
new_value = "TOTALES - Presidente"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 185  
new_value = "TOTALES - Parlasur"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 186  
new_value = "TOTALES - Diputados"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 187  
new_value = "TOTALES - Parlasur_reg"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 188  
new_value = "TOTAL VOTOS AGRUPACIONES POLÍTICAS - Presidente"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 189  
new_value = "TOTAL VOTOS AGRUPACIONES POLÍTICAS - Parlasur"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 190  
new_value = "TOTAL VOTOS AGRUPACIONES POLÍTICAS - Diputados"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 191  
new_value = "TOTAL VOTOS AGRUPACIONES POLÍTICAS - Parlasur_reg"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 192  
new_value = "VOTOS NULOS - Presidente"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 193  
new_value = "VOTOS NULOS - Parlasur"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 194  
new_value = "VOTOS NULOS - Diputados"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 195  
new_value = "VOTOS NULOS - Parlasur_reg"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 196  
new_value = "VOTOS RECURRIDOS - Presidente"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 197  
new_value = "VOTOS RECURRIDOS - Parlasur"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 198  
new_value = "VOTOS RECURRIDOS - Diputados"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 199  
new_value = "VOTOS RECURRIDOS - Parlasur_reg"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 200  
new_value = "VOTOS EN BLANCO - Presidente"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 201  
new_value = "VOTOS EN BLANCO - Parlasur"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 202  
new_value = "VOTOS EN BLANCO - Diputados"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 203  
new_value = "VOTOS EN BLANCO - Parlasur_reg"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 164  
new_value = "SOBRES DE IDENTIDIDAD IMPUGNADA"
df.iat[row_index, column_index] = new_value

row_index = 0  
column_index = 168  
new_value = "SOBRES VOTO COMANDO ELECTORAL"
df.iat[row_index, column_index] = new_value

#fix df column index
df.columns = df.iloc[0]
df = df.drop(index=0).reset_index(drop=True)


#limpio
nan_counts = pd.DataFrame({
    'Column Name': df.columns,
    'NaN Count': df.isna().sum()
})

# Replace NaN counts with 0
nan_counts['NaN Count'] = nan_counts['NaN Count'].apply(lambda x: 0 if pd.isna(x) else x)
pd.set_option('display.max_rows', None)
non_zero_nan_counts = nan_counts[nan_counts['NaN Count'] > 0]
#borra lo que tiene NAN
for index, row in non_zero_nan_counts.iterrows():
    column_name = row['Column Name'].strip()
    matching_columns = [col for col in df.columns if column_name in col]
    if matching_columns:
        df.drop(matching_columns[0], axis=1, inplace=True)


df.columns = df.columns.str.replace(r'^.*\n \[', '', regex=True)
df.columns = df.columns.str.replace(r'] \n \[ Presidente \]', '- Presidente', regex=True)
df.columns = df.columns.str.replace(r'] \n \[ Parlasur \]', '- Parlasur', regex=True)
df.columns = df.columns.str.replace(r'] \n \[ Diputados \]', '- Diputados', regex=True)
df.columns = df.columns.str.replace(r'] \n \[ Parlasur_reg \]', '- Parlasur_reg', regex=True)
df.columns = df.columns.str.replace(r' ]$', '', regex=True)
df.columns = df.columns.str.replace(r'Número \] \n \[ Sección \]', 'Sección', regex=True)
df.columns = df.columns.str.replace(r'Número \] \n \[ Circuito \]', 'Circuito', regex=True)
df.columns = df.columns.str.replace(r'Número \] \n \[ Mesa \]', 'Mesa', regex=True)
df.columns = df.columns.str.replace(r'Número \] \n \[ Ciudadanos que han votado \]', 'Ciudadanos que han votado', regex=True)
df.columns = df.columns.str.replace(r'Número \] \n \[ Cantidad de sobres utilizados \]', 'Cantidad de sobres utilizados', regex=True)
df.columns = df.columns.str.replace(r'Número \] \n \[ Diferencia \]', 'Diferencia', regex=True)

df.columns = df.columns.str.strip()


# List of columns to move
columns_to_move = [
    'SECCION',
    'CIRCUITO',
    'MESA',
    'CIUDADANOS',
    'SOBRES',
    'DIFERENCIA'
]
# Create a list of column names with the desired order
new_column_order = [
    'Response ID',
    'Response started',
    'Response completed',
    'IP address'
] + columns_to_move + [col for col in df.columns if col not in columns_to_move + ['Response ID', 'Response started', 'Response completed', 'IP address']]
# Reorder the columns in the DataFrame
df = df[new_column_order]

new_column_order = [
    'Response ID',
    'Response started',
    'Response completed',
    'IP address',
    'NOMBRE'
] + [col for col in df.columns if col not in ['Response ID', 'Response started', 'Response completed', 'IP address', 'NOMBRE']]
df = df[new_column_order]

# List of columns to move
columns_to_move = [
    'TOTALES - Presidente',
    'TOTALES - Parlasur',
    'TOTALES - Diputados',
    'TOTALES - Parlasur_reg'
]

# Find the index of the column 'VOTOS EN BLANCO - Parlasur_reg'
index_of_votos_en_blanco = df.columns.get_loc('VOTOS EN BLANCO - Parlasur_reg')

# Insert the columns to move before the 'VOTOS EN BLANCO - Parlasur_reg' column
for column in columns_to_move:
    df.insert(index_of_votos_en_blanco, column, df.pop(column))


# List of columns to move
columns_to_move = [
    'SOBRES DE IDENTIDIDAD IMPUGNADA',
    'SOBRES VOTO COMANDO ELECTORAL',
]

# Find the index of the column 'VOTOS EN BLANCO - Parlasur_reg'
index_of_votos_en_blanco = df.columns.get_loc('VOTOS EN BLANCO - Parlasur_reg')

# Insert the columns to move before the 'VOTOS EN BLANCO - Parlasur_reg' column
for column in columns_to_move:
    df.insert(index_of_votos_en_blanco, column, df.pop(column))

df['CIUDAD'] = ''
df.loc[df['MESA'].between(1, 227), 'CIUDAD'] = 'USHUAIA'
df.loc[df['MESA'].between(228, 500), 'CIUDAD'] = 'RIO GRANDE'
df.loc[df['MESA'].between(509, 530), 'CIUDAD'] = 'TOLHUIN'

df.to_csv("survey_streamlit.csv")
