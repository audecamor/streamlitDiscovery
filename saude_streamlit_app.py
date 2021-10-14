import streamlit as st
import pandas as pd

st.title('Hello Wilders, welcome to my application!')

st.write("I enjoy to discover streamlit possibilities")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

# "magic commands":
df_cars

# limite du dataset: REGEX pour écriture d'un sous titre.
annee_min= df_cars['year'].min()
annee_max= df_cars['year'].max()
st.subheader(
    f"""Le dataset "cars" recense des modèles de l'année {annee_min} à l'année {annee_max}\.""")

# 1er graph: Heatmap

st.header('1. Analyse des correlations entre variables pour le dataset "cars"')

#Heatmap
import seaborn as sns

viz_correlation= sns.heatmap(df_cars.corr(), 
            center=0,
            cmap = sns.color_palette("RdGy", as_cmap=True,),
            annot= True, fmt=".1f",
           )
st.pyplot(viz_correlation.figure)

comment_11= 'On constate des corrélations fortes: positives entre les variables (cylinders & cubicinches); (cylinders & weightlbs), (cubicinches & weightlbs), (cylinders & hp), '
comment_12= ' négatives fortes entre les variables (cylinders/mpg, cubicinches/ mpg, hp/ mpg, weightlbs/mpg'
st.write(comment_11, "\n", comment_12)

#2. graph:

st.header('2. Correlation "consommation / poids des véhicules", et distribution des effectifs par variable')
#conso=f(poids), avec filtres régions

sns.set(style= "white", color_codes= True)
sns.set_palette("ocean", 4)
sns.color_palette()
viz_consoPoids= sns.jointplot(data= df_cars, x= 'weightlbs', y= 'mpg',  kind= "reg", line_kws= {'color': 'red'} )

st.pyplot(viz_consoPoids)

st.write('On observe une correlation négative de la consommation et du poids du véhicule: dans les années 70-80, les petits véhicules consommaient plus que les gros véhicules')

# 3 eme graph: Representation par continent
st.header('3.1_Représentation par CONTINENT, de la Correlation "consommation / poids des véhicules", et distribution des effectifs par variable')

sns.set(style= "white", color_codes= True)
sns.set_palette("YlGnBu", 3)
sns.color_palette()
viz_consoPoids2= sns.jointplot(data= df_cars, x= 'weightlbs', y= 'mpg', hue= 'continent')
st.pyplot(viz_consoPoids2)


# 4eme graph: Représentation avec filtre par Continent:
st.header('3.2_Correlation "consommation / poids des véhicules", et distribution des effectifs par variable, selon le continent sélectionné :')
#conso=f(poids), avec filtres régions

# on crée le bouton de choix du filtre :
import numpy as np
list_continent= np.sort(df_cars['continent'].unique())
option_continent= st.selectbox("Sélectionnez le continent", list_continent)
# on selectionne un "sous-dataframe" selon le critère de filtre
df_cars_option= df_cars[df_cars['continent']== option_continent]
# on utilise ce sous-datframe dans le graphique

sns.set(style= "white", color_codes= True) # fait des séparations blanches entre les barres, sinon noir : moche)
sns.set_palette("ocean", 4)
sns.color_palette()
viz_consoPoids4= sns.jointplot(data= df_cars_option, x= 'weightlbs', y= 'mpg',  kind= "reg", line_kws= {'color': 'red'} )

st.pyplot(viz_consoPoids4)

#commentaire:
st.write('On observe une correlation négative de la consommation et du poids du véhicule: dans les années 70-80, les petits véhicules consommaient plus que les gros véhicules')
