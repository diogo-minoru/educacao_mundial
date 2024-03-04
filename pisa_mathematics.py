import pandas as pd
import plotly.express as px

file3 = r"..\educacao_mundial\dataset\pisa-test-score-mean-performance-on-the-mathematics-scale.csv"

dataset3 = pd.read_csv(file3).dropna()

dataset3 = dataset3.rename(columns = {"Upper bound of performance of 15-year-old  on the mathematics scale": "Upper Bound",
                           "Average performance of 15-year-old students on the mathematics scale": "Average",
                           "Lower bound of performance of 15-year-old  on the mathematics scale": "Lower Bound"})

dataset3

# Filtrar os 10 países que tiveram a maior média de nota no último teste
max_year = dataset3["Year"].max()
top10_countries = dataset3[dataset3["Year"] == max_year].sort_values("Average", ascending = False)["Entity"].head(10)
dataset3_top10_contries = dataset3[dataset3["Entity"].isin(top10_countries)].sort_values(["Entity", "Year"])
dataset3_top10_contries["Pct Difference"] = dataset3_top10_contries.groupby("Entity")["Average"].pct_change()

# Adicionar coluna com variação na nota em relação ao ano anterior

dataset3_top10_contries

fig1 = px.line(
    data_frame = dataset3_top10_contries,
    hover_name = "Entity",
    hover_data = "Pct Difference",
    x = "Year",
    y = "Average",
    color = "Entity",
    markers = True,
    title = "Average Top 10 Countries Pisa Score Performance on Mathematics",
    labels = {
        "Year": "",
        "Average": "Average Score"
    }
)

fig1.show()


# Filtrar os 10 países que tiveram a menor média de nota no último teste
bottom10_countries = dataset3[dataset3["Year"] == max_year].sort_values("Average")["Entity"].head(10)
dataset3_bottom10_countries = dataset3[dataset3["Entity"].isin(bottom10_countries)].sort_values(["Entity", "Year"])
dataset3_bottom10_countries["Pct Difference"] = dataset3_bottom10_countries.groupby("Entity")["Average"].pct_change()
dataset3_bottom10_countries

fig2 = px.line(
    data_frame = dataset3_bottom10_countries,
    x = "Year",
    y = "Average",
    color = "Entity",
    markers = True,
    labels = {
        "Year": "",
        "Average": "Average Score"
    },
    title = "Bottom 10 Countries Pisa Score Performance on Mathematics"
)

fig2.show()


# Analisar os 10 países que tiveram maior variação em relação ao último teste
top10_increase_dataset3 = dataset3.sort_values(["Entity", "Year"])
top10_increase_dataset3["Pct Difference"] = top10_increase_dataset3.groupby("Entity")["Average"].pct_change() * 100



top10_incresce_filter = top10_increase_dataset3[top10_increase_dataset3["Year"] == max_year].sort_values("Pct Difference", ascending = False).head(10)
top10_incresce_filter

top10_increase_dataset3 = top10_increase_dataset3[top10_increase_dataset3["Entity"].isin(top10_incresce_filter["Entity"])]
top10_increase_dataset3

fig3 = px.line(
    data_frame = top10_increase_dataset3,
    hover_name = "Entity",
    hover_data = "Pct Difference",
    x = "Year",
    y = "Average",
    color = "Entity",
    title = "Top 10 Countries Greatest Increase From Previous Test",
    markers = True,
    labels = {
        "Year": "",
        "Average": "Average Score"
    }

)

fig3.show()

# Analisar os 10 países que tiveram pior variação em relação ao último teste
top10_decrease_dataset3 = dataset3.sort_values(["Entity", "Year"])
top10_decrease_dataset3["Pct Difference"] = top10_decrease_dataset3.groupby("Entity")["Average"].pct_change() * 100


top10_decrease_filter = top10_decrease_dataset3[top10_decrease_dataset3["Year"] == max_year].sort_values("Pct Difference", ascending = True).head(10)
top10_decrease_filter

top10_decrease_dataset3 = top10_decrease_dataset3[top10_decrease_dataset3["Entity"].isin(top10_decrease_filter["Entity"])]
top10_decrease_dataset3

fig4 = px.line(
    data_frame = top10_decrease_dataset3,
    hover_name = "Entity",
    hover_data = "Pct Difference",
    x = "Year",
    y = "Average",
    color = "Entity",
    title = "Top 10 Countries Greatest Decrease From Previous Test",
    markers = True,
    labels = {
        "Year": "",
        "Average": "Average Score"
    }
)

fig4.show()