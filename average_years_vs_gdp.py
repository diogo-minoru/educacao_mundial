import pandas as pd
import plotly.express as px

#########################################################################################################
# Análise média de anos de estudo vs pib per capita
#########################################################################################################
file2 = r"..\educacao_mundial\dataset\average-years-of-schooling-vs-gdp-per-capita.csv"

# Não utilizando a coluna "Continent", pois há vários valores nulos, será realizado join para trazer o nome do continente para o país
dataset2 = pd.read_csv(file2, 
                       usecols = ["Entity", "Code", "Year", "Combined - average years of education for 15-64 years male and female youth and adults", "GDP per capita, PPP (constant 2017 international $)", "Population (historical estimates)"])

dataset2 = dataset2.rename(columns = {"GDP per capita, PPP (constant 2017 international $)": "GDP", 
                           "Population (historical estimates)":"Population",
                           "Combined - average years of education for 15-64 years male and female youth and adults": "Average Years Study"}).set_index("Entity")
dataset2

# Criando dataset com o continente para cada país para realizar o join
entity_continent = pd.read_csv(file2)[["Entity", "Continent"]]
entity_continent = entity_continent[entity_continent["Continent"].notnull()].drop_duplicates().set_index("Entity")

entity_continent





# Ordenando o dataset por "Entity e "Year" para preencher os valores nulos com o valor não nulo anterior
dataset2_filtered = dataset2.sort_values(["Entity", "Year"])
# agrupado por "Entity", depois filtrando apenas os anos entre 1999 e 2024
dataset2_filtered = dataset2_filtered.groupby("Entity")[["Code", "Year", "Average Years Study", "GDP", "Population"]].ffill()
dataset2_filtered = dataset2_filtered.query("Year > 1999 and Year < 2024")
# fazendo left join, adicionando a coluna "Contnent"
dataset2_filtered = dataset2_filtered.join(entity_continent, how = "left")
# Removendo da coluna "Code" linhas que tenham o texto "OWID"
dataset2_filtered = dataset2_filtered[~dataset2_filtered["Code"].str.contains("OWID", na = False)]
# Fazendo com que a coluna "Entity" não seja mais a coluna índice do dataframe
dataset2_filtered = dataset2_filtered.reset_index()
# Removendo quaisquer outras linhas que sejam nulas
dataset2_filtered = dataset2_filtered.dropna()
# Verificando se ainda há alguma linha nula no dataset
dataset2_filtered.isnull().sum()

dataset2_filtered

# dataset2_filtered[dataset2_filtered.index == "Afghanistan"].head(60).sort_values("Year")
# dataset2_filtered[(dataset2_filtered.index == "Afghanistan") & (dataset2_filtered["Average Years Study"].notnull())].sort_values("Year")
# dataset2_filtered[(dataset2_filtered.index == "Afghanistan") & (dataset2_filtered["GDP"].notnull())].sort_values("Year")

# Teste para ver como estão preenchido os valores
# dataset2_filtered[dataset2_filtered["Continent"].isnull()]
# dataset2_filtered[dataset2_filtered.index.isin(["Abkhazia"])]

# Deixar a tabela apenas com os valores que a coluna "Code" não seja nulo e não contenha a palavra OWID
# dataset2_filtered[dataset2_filtered.index.isin(dataset2_filtered[dataset2_filtered["Population"].isnull()]["Code"].index)]



fig1 = px.scatter(
            data_frame = dataset2_filtered,
            y = "Average Years Study",
            x = "Year",
            size = "GDP",
            color = "Continent",
            hover_name = "Entity"
)

fig1.show()