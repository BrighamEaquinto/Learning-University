import pandas as pd

dat = pd.read_csv("https://raw.githubusercontent.com/BrighamEaquinto/brighameaquinto.github.io/master/datasets/insurance.csv")

dat

import plotly.express as px

fig = px.bar(dat, x = 'sex')
fig.show()