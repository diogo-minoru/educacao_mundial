import pandas as pd
import plotly.express as px
import numpy as np

file_male = r"..\educacao_mundial\dataset\mean-years-of-schooling-male.csv"
file_female = r"..\educacao_mundial\dataset\mean-years-of-schooling-female.csv"

dataset4_male = pd.read_csv(file_male)
dataset4_female = pd.read_csv(file_female)

# Renomeando o campo de média de anos de estudo
dataset4_male = dataset4_male.rename(columns = {"UIS: Mean years of schooling (ISCED 1 or higher), population 25+ years, male": "Average Years"})
dataset4_female = dataset4_female.rename(columns = {"UIS: Mean years of schooling (ISCED 1 or higher), population 25+ years, female": "Average Years"})


# Verificando se há campos nulos nos datasets
dataset4_male.isnull().sum()
dataset4_female.isnull().sum()

dataset4_male
dataset4_female

#################################################################################################################
# Análise da nota do público masculino
#################################################################################################################

"""
    Aqui será criado um dataset novo, pois muitos países não possuem registro da nota para alguns anos,
    enquanto outros países possuem. Para contornar o problema, o valor da última nota de um países em um
    determinado ano, será repetido para o ano seguinte que não possui uma nota
"""

# Criando variáveis para identificar o menor e o maior ano do dataset do público masculino
min_year_male = int(dataset4_male["Year"].min())
max_year_male = int(dataset4_male["Year"].max())

# Criando uma série de dados do intervalo entre o menor e maior ano do dataset
every_year_dataset_male = np.arange(min_year_male, max_year_male)
every_year_dataset_male

# Criando uma lista de todos os países do dataset
every_country_dataset_male = dataset4_male["Entity"].unique()
every_country_dataset_male

# Sintaxe para criar um dataset onde cada país da lista será atribuído todos os anos possíveis da lista de anos
temp_dataset4_male = pd.DataFrame([(country, year) for country in every_country_dataset_male for year in every_year_dataset_male], columns = ["Entity", "Year"])

# Realizando join entre as tabelas, preservando as notas e repetindo a nota para os anos onde não foi avaliado
merged = pd.merge(temp_dataset4_male, dataset4_male, how = "left", on = ["Entity", "Year"]).sort_values(["Entity", "Year"]).ffill()
merged.dropna()

fig1 = px.choropleth(
    data_frame = merged.sort_values(["Year"]),
    locations = "Code",
    color = "Average Years",
    hover_name = "Entity",
    animation_frame = "Year"
)

fig1.show()

#################################################################################################################
# Análise da nota do público feminino
#################################################################################################################

min_year_female = int(dataset4_female["Year"].min())
max_year_female = int(dataset4_female["Year"].max())

every_year_dataset_female = np.arange(min_year_female, max_year_female)
every_year_dataset_female

every_country_dataset_female = dataset4_female["Entity"].unique()
every_country_dataset_female

temp_dataset4_female = pd.DataFrame([(country, year) for country in every_country_dataset_female for year in every_year_dataset_female], columns = ["Entity", "Year"])
temp_dataset4_female

merged_female = pd.merge(temp_dataset4_female, dataset4_female, how = "left", on = ["Entity", "Year"]).sort_values(["Entity", "Year"]).ffill().dropna()
merged_female

fig2 = px.choropleth(
    data_frame = merged_female.sort_values("Year"),
    locations = "Code",
    hover_name = "Entity",
    color = "Average Years",
    animation_frame = "Year"
)

fig2.show()