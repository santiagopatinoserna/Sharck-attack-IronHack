import re

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

from fuzzywuzzy import process
import pandas as pd

# Lista de lesiones (ejemplo)
lesiones = [
    "Right leg severed below knee",
    "30cm (1ft) bite to lower calf",
    "Bite to left arm",
    "Head right arm and leg severed",
    "Minor injury to left foot",
    "FATAL",
    "Injury to lower left leg",
    "Bite to lower back",
    "Leg bitten",
    "Sharks bit their inflatable boats"
]



# Función para asignar una lesión a la categoría "Fatal" o "No Fatal"
def categorizar_lesion(lesion, palabras_fatal):
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

