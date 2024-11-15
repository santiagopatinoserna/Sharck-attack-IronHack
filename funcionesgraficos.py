def plot_attacks_by_location(df):
    """
    Creación de gráfico para filtrar las primeras diez ubicaciones
    """
    import matplotlib.pyplot as plt
    attacks_by_location = df['country'].value_counts().head(10)
    attacks_by_location.plot(kind='bar', title='Top 10 Ubicaciones de Ataques', xlabel='País', ylabel='Cantidad de Ataques')
    plt.show()

def plot_attacks_by_country_pie(df):
    """
    Luego de ver que sobre el top 10 de las ubicaciones se destacaban 3, 
    creamos este pie para remarcar las mismas
    """
    import matplotlib.pyplot as plt
    # Contar la cantidad de ataques por país, limitando a los 3 primeros
    attacks_by_country = df['country'].value_counts().nlargest(3)
    plt.figure(figsize=(8, 6))
    attacks_by_country.plot.pie(autopct='%1.1f%%', startangle=140)
    plt.title('Distribución de Ataques por País (Top 3)')
    plt.ylabel('')  # Oculta la etiqueta del eje y para que se vea más limpio
    plt.show()

def plot_attacks_by_month(df):
    """
    Funcion para realizar gráfico de ataques por meses en los 3 páises
    que mas sufren ataques, importando librerias necesaria para la unión de los meses y ataques
    y creación de gráfico.    
    """
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    # Definir la lista de países dentro de la función
    countries = ['Usa', 'South africa', 'Australia']
    
    # Filtrar los datos por los países especificados en la lista 'countries'
    country_df = df[df['country'].isin(countries)]
    
    # Agrupar por mes y contar los ataques
    attacks_by_month = country_df.groupby(['month', 'country']).size().reset_index(name='attacks')
    
    # Asegurarnos de que todos los meses estén presentes en el gráfico (del 1 al 12)
    all_months = pd.DataFrame({'month': range(1, 13)})  # Creando un DataFrame con los meses del 1 al 12
    attacks_by_month = pd.merge(all_months, attacks_by_month, on='month', how='left')
    
    # Crear gráfico combinado con Seaborn
    plt.figure(figsize=(14, 7))  # Aumentar aún más el tamaño del gráfico
    sns.barplot(x='month', y='attacks', data=attacks_by_month, palette='viridis', hue='country')

    # Personalizar gráfico combinado
    plt.title(f'Ataques de Tiburones por Mes en los Países Seleccionados', fontsize=16)
    plt.xlabel('Mes')
    plt.ylabel('Cantidad de Ataques')
    plt.xticks(range(0, 12), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])  # Meses
    
    # Ajustar la leyenda y evitar el warning
    plt.legend(title="País", loc='upper right', bbox_to_anchor=(1.05, 1))  # Mejor ubicación para la leyenda
    plt.tight_layout()  # Para evitar que la leyenda se corte
    
    # Mostrar gráfico combinado
    plt.show()

    # Crear gráficos individuales para cada país
    for country in countries:
        # Filtrar los datos para el país actual
        country_data = attacks_by_month[attacks_by_month['country'] == country]

        # Crear gráfico individual para el país
        plt.figure(figsize=(14, 7))
        sns.barplot(x='month', y='attacks', data=country_data, palette='viridis', hue="month")

        # Personalizar gráfico individual
        plt.title(f'Ataques de Tiburones por Mes en {country}', fontsize=16)
        plt.xlabel('Mes')
        plt.ylabel('Cantidad de Ataques')
        plt.xticks(range(0, 12), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])  # Meses

        # Mostrar gráfico individual
        plt.show()



def plot_attacks_by_category(df):
    """
    Gráfico para ataques divididos por categorias,
    donde se cuentan cantidad de ataques y se muestra en un gráfico de barras.
    """
    import matplotlib.pyplot as plt
    attacks_by_category = df['category'].value_counts()
    attacks_by_category.plot(kind='bar', title='Distribución de Ataques por Categoría', xlabel='Categoría', ylabel='Cantidad de Ataques')
    plt.show()

def plot_attacks_by_type(df):
    """
    Gráfico para ataques divididos por causa,
    donde se cuentan cantidad de ataques y se muestra en un gráfico de barras.
    """
    import matplotlib.pyplot as plt
    attacks_by_type = df['type'].value_counts()
    attacks_by_type.plot(kind='bar', title='Causa de los ataques', xlabel='Tipo de Ataque', ylabel='Cantidad de Ataques')
    plt.show()




def creacion_de_graficos(df):
    plot_attacks_by_location(df)
    plot_attacks_by_country_pie(df)
    plot_attacks_by_month(df)
    plot_attacks_by_category(df)
    plot_attacks_by_type(df)

