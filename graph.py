import pandas as pd
import plotly.express as px

f = pd.read_csv("CovidData.csv")

figure = px.scatter(f, x="date", y="cases", color="country")
figure.show()