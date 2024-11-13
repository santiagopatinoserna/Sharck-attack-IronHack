import re
import pandas as pd
from fuzzywuzzy import process

#funcion seleccion columnas:
def seleccion_columnas(df):
    df=df[['date', 'type', 'country', 'state', 'location', 'name', 'sex', 'age', 'injury']]
    return df
#Funcion para limpiar fecha
def limpiar_fecha(fecha_str):
    """Función para estandarizar fechas usando regex"""
    
    # Diccionario de meses en diferentes idiomas
    meses = {
        'ene': '01', 'jan': '01', 'enero': '01', 'january': '01',
        'feb': '02', 'february': '02', 'febrero': '02',
        'mar': '03', 'march': '03', 'marzo': '03',
        'abr': '04', 'apr': '04', 'abril': '04', 'april': '04',
        'may': '05', 'mayo': '05',
        'jun': '06', 'june': '06', 'junio': '06',
        'jul': '07', 'july': '07', 'julio': '07',
        'ago': '08', 'aug': '08', 'agosto': '08', 'august': '08',
        'sep': '09', 'september': '09', 'septiembre': '09',
        'oct': '10', 'october': '10', 'octubre': '10',
        'nov': '11', 'november': '11', 'noviembre': '11',
        'dic': '12', 'dec': '12', 'december': '12', 'diciembre': '12'
    }
    
    # Convertir a string si no lo es
    fecha_str = str(fecha_str).lower().strip()
    
    # Remover hora si existe
    fecha_str = re.sub(r'\s+\d{1,2}:\d{2}:\d{2}.*$', '', fecha_str)
    
    # Patrón para formato compacto YYYYMMDD
    if re.match(r'^\d{8}$', fecha_str):
        return f"{fecha_str[:4]}-{fecha_str[4:6]}-{fecha_str[6:]}"
    
    # Reemplazar varios separadores por -
    fecha_str = re.sub(r'[./\s]', '-', fecha_str)

    #Remover "reported" si existe
    fecha_str = re.sub(r'^\s*reported[\s\-]*|[\s\-]*reported\s*$', '', fecha_str, flags=re.IGNORECASE)
    
    # Extraer componentes usando diferentes patrones
    patrones = [
        # YYYY-MM-DD
        r'^(\d{4})-(\d{1,2})-(\d{1,2})$',
        # DD-MM-YYYY
        r'^(\d{1,2})-(\d{1,2})-(\d{4})$',
        # DD-MMM-YYYY
        r'^(\d{1,2})-([a-z]{3,})-?(\d{4})$',
        # MM-DD-YY
        r'^(\d{1,2})-(\d{1,2})-(\d{2})$'
    ]
    
    for patron in patrones:
        match = re.match(patron, fecha_str)
        if match:
            grupos = match.groups()
            
            # Caso YYYY-MM-DD
            if len(grupos[0]) == 4:
                año = grupos[0]
                mes = grupos[1].zfill(2)
                dia = grupos[2].zfill(2)
            # Caso DD-MM-YYYY
            elif len(grupos[2]) == 4:
                año = grupos[2]
                # Verificar si el segundo grupo es un mes en texto
                if grupos[1].isalpha():
                    mes = meses.get(grupos[1][:3], '01')
                else:
                    mes = grupos[1].zfill(2)
                dia = grupos[0].zfill(2)
            # Caso MM-DD-YY
            else:
                año = f"20{grupos[2]}" if int(grupos[2]) < 50 else f"19{grupos[2]}"
                mes = grupos[0].zfill(2)
                dia = grupos[1].zfill(2)
            
            return f"{año}-{mes}-{dia}"
    
    return fecha_str



# Función para asignar una lesión a la categoría "Fatal" o "No Fatal"

palabras_fatal = ['fatal', 'death', 'fatality', 'drowned']
def categorizar_lesion(lesion, palabras_fatal):
    if pd.isna(lesion):
        return "Desconocido"
    else:
    # Comprobar si alguna de las palabras clave está en la lesión usando fuzzywuzzy
        max_score = 0
        for palabra in palabras_fatal:
            score = process.extractOne(palabra, [lesion])[1]  # Obtenemos el score de fuzzywuzzy
            if score > max_score:
                max_score = score
                if max_score > 80:  # Establecemos un umbral de coincidencia
                    return "Fatal"
    
    # Si no se encuentra una coincidencia suficientemente buena, la clasificamos como "No Fatal"
    return "No Fatal"

# Función para renombrar columnas
def renombrar_columnas(df):
    df = df.rename(columns={df.columns[n]: df.columns[n].strip().replace(" ", "_").lower() for n in range(len(df.columns))})
    return df

#Funcion cambiar tipo a fecha
def cambiar_tipo_fecha(df):
    df['date']= pd.to_datetime(df['date'], errors='coerce')
    return df

# Función para filtrar fechas mayores a '1970-01-01'
def filtrar_fecha(df):
    df = df.loc[df['date'] > '1970-01-01']
    return df

# Función para eliminar filas con valores nulos en todas las columnas
def eliminar_na(df):
    df = df.dropna(how="all")
    return df

# Función para resetear el índice
def resetear_indice(df):
    df = df.reset_index(drop=True)
    return df

# Función para convertir columna 'age' a numérico
def convertir_edad(df):
    df["age"] = pd.to_numeric(df['age'], errors="coerce")
    return df

# Función para capitalizar los valores de la columna 'country'
def capitalizar_country(df):
    df["country"] = df["country"].str.capitalize()
    return df

# Función para rellenar valores nulos de las columnas con valores específicos
def rellenar_nulos(df):
    df["name"] = df["name"].fillna("Unknown")
    df["sex"] = df["sex"].fillna("Unknown")
    df["state"] = df["state"].fillna("Unknown")
    df["type"] = df["type"].fillna("Unknown")
    df["location"] = df["location"].fillna("Unknown")
    df["age"] = df["age"].fillna("Unknown")
    return df

# Función para corregir valores erróneos en la columna 'sex'
def corregir_sex(df):
    df["sex"] = df["sex"].replace("lli", "M")
    df["sex"] = df["sex"].str.strip()
    return df

# Función para corregir valores en 'type'
def corregir_type(df):
    df["type"] = df["type"].str.strip()
    df["type"] = df["type"].replace(["Questionable", "?", "Unconfirmed", "Unverified", "Under investigation"], "Invalid")
    return df

# Función para eliminar filas con nulos en una columna específica
def eliminar_na_columna(df, columna):
    df = df.dropna(subset=[columna])
    return df

# Función para rellenar nulos en la columna 'date' usando backward fill (bfill)
def rellenar_fecha(df):
    df['date'] = df['date'].fillna(method='bfill')
    return df

# Función para extraer mes y año de la columna 'date'
def extraer_mes_year(df):
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    return df

# Función para eliminar columnas específicas
#def eliminar_columnas(df, columnas):
    df = df.drop(columnas, axis=1)
    return df

# Ahora aplicamos todas las funciones sobre el DataFrame df

def limpiar_dataframe(df):
    df = renombrar_columnas(df)
    df= seleccion_columnas(df)
    df["date"] = df["date"].apply(limpiar_fecha)
    df= cambiar_tipo_fecha(df)
    
    # Categorizar lesiones usando 'categorizar_lesion' y la lista 'palabras_fatal'
    df["category"] = df["injury"].apply(lambda x: categorizar_lesion(x, palabras_fatal))
    df = filtrar_fecha(df)
    df = eliminar_na(df)
    df = resetear_indice(df)  # Si quieres resetear el índice y eliminar la columna 'index'
    
    # Eliminar la columna 'injury'
    df = df.drop('injury', axis=1)
    df = convertir_edad(df)
    df = capitalizar_country(df)
    df = rellenar_nulos(df)
    df = corregir_sex(df)
    df = corregir_type(df)
    df = eliminar_na_columna(df, 'country')
    df = rellenar_fecha(df)
    df = extraer_mes_year(df)
  
    return df

