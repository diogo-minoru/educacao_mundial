import pandas as pd
import plotly.express as px

file1 = r"..\educacao_mundial\dataset\learning-adjusted-years-of-school-lays.csv"

dataset1 = pd.read_csv(file1)
dataset1

dataset1.info()
dataset1.memory_usage()

dataset1["Entity"] = dataset1["Entity"].astype("category")
dataset1["Code"] = dataset1["Code"].astype("category")
dataset1["Year"] = dataset1["Year"].astype("int64")

# Verificando se há algum valor nulo em todo o dataset
if dataset1.isnull().values.any():
    print("valores nulos")
else:
    print("sem valores nulos")

# Código para contar quantas linhas possui para cada "Entity", e filtrar apenas aqueles em que aparecem menos que 4 vezes
count = dataset1["Entity"].value_counts()
count

one_ocurrence = count[count < 4].index
one_ocurrence


filtered_dataset = dataset1[dataset1["Entity"].isin(one_ocurrence)]
filtered_dataset

fig1 = px.line(
            data_frame = dataset1,#[dataset["Entity"] == "Brazil"], 
            x = "Year", 
            y = "Learning-Adjusted Years of School", 
            color = "Entity", 
            markers = True,
            title = "Learning-Adjusted Years of School",
            labels = {
                "Year": "Year",
                "Learning-Adjusted Years of School": "Years"
            })
fig1.show()