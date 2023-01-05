#%% 
import altair as alt
from vega_datasets import data

source = data.seattle_weather()

#%%
alt.Chart(source).mark_bar(
    cornerRadiusTopLeft=3,
    cornerRadiusTopRight=3
).encode(
    x='month(date):O',
    y='count():Q',
    color='weather:N'
)
# %%
import pandas as pd

iris = pd.read_csv("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")

#%% 
iris_chart = (alt.Chart(iris)
    .mark_bar(cornerRadiusTopLeft=4, cornerRadiusTopRight=4)
    .encode(
        alt.X('petal_length', bin=True, title="Petal Length"), 
        alt.Y('count()')
        )
    .interactive()
)
iris_chart
# %%

iris1 = (alt.Chart(iris)
    .mark_boxplot()
    .encode(
        alt.X('species'), 
        alt.Y("petal_width"),
        alt.Color('species'),
        alt.OpacityValue(0.5), 
        )
    )

iris2 = (alt.Chart(iris)
    .mark_point()
    .encode(
        alt.X('species'), 
        alt.Y("petal_width"), 
        alt.Color('species'),
        alt.OpacityValue(0.5), 
        tooltip = [
            alt.Tooltip('sepal_length'),
            alt.Tooltip('sepal_width'),
            alt.Tooltip('petal_length'), 
            alt.Tooltip('petal_width'), 
            alt.Tooltip('species')
            ])
    .properties(width=400, height=400)
)


alt.layer(iris2, iris1)



# alt.layer(tempMinMax, precip)