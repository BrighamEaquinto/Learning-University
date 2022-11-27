#%% 
import pandas as pd
import numpy as np
from plotnine import *
dat = pd.read_csv("C:/Users/Bethany/Downloads/grades.csv")

#%%
is_math = ("FDMAT108", "MATH101")
is_stats = ("MATH221A", "MATH325")
is_major = ("CIT111", "CIT225")
is_general_ed = ("FDAMF101", "FDENG101")

#%% 

dat1 = (dat
    # .filter([])
    .drop(['Course Program', 'Catalog', 'Grade Type'], axis = 1)
    .query("~Grade.str.startswith('N/A')")
    .assign(
        Grade = lambda X: pd.Categorical(X.Grade, categories = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F", "P", "W"]), 
        Semester = lambda X: pd.Categorical(X.Semester, ["WI19", "SP19", "FA19", "WI20", "SP20", "FA20", "WI21", "SP21", "FA21", "WI22", "SP22", "FA22"]),
        Grade_Points = lambda X: X['Grade'].replace({
            "A": 4, "A-": 3.7,
            "B+": 3.4, "B": 3,
            "B-": 2.7, "C+": 2.4,
            "C": 2, "C-": 1.7,
            "D+": 0.4, "D": 1,
            "D-": 0.7, "F": 0,
            "UW": 0, "P": np.nan,
            "W": np.nan, "I": np.nan,
            "T": np.nan, "NR": np.nan}),
        Course = lambda X: X['Course'].replace({r"-\d\d": "", r"\W":""}, regex=True),
        is_math = lambda X: np.where(X['Course'].isin(is_math), True, False), 
        is_stats = lambda X: np.where(X['Course'].isin(is_stats), True, False), 
        is_major = lambda X: np.where(X['Course'].isin(is_major), 1, 0), 
        is_general_ed = lambda X: np.where(X['Course'].isin(is_general_ed), 1, 0)
        )
)
dat1.head()
#%%
plot1 = (
ggplot(dat1, aes('Grade'))+
    geom_bar()+
    labs(
        title = "Title", 
        x = "Grade Distribution", 
        y = "Count", 
        caption = "Subtitle")
)
plot1

#%% 
pd.DataFrame({"key1": ['value1', 'value2'], 
              'key2': 'valuea',})
# %%
scripture_BOM = pd.DataFrame(
        index = ['1 Nephi', '2 Nephi', 'Jacob', 'Enos', 'Jarom', 'Omni', 'Words of Mormon', 'Mosiah', 'Alma', 'Helaman', '3 Nephi', '4 Nephi', 'Mormon', 'Ether', 'Moroni'], 
        columns = ['Place', 'People', 'Doctrines', 'References to Christ']
        )
#%%
columns = ['Place', 'People', 'Doctrines', 'References to Christ']

First_Nephi = (pd.DataFrame(
    index = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,31], 
    columns = columns)
.assign(
    Book = '1 Nephi', 
    Chapters = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,31])
.filter(['Book', 'Chapters', 'Place', 'People', 'Doctrines', 'References to Christ'])
)
#%%
new_columns = columns.append('hey')zip
print(new_columns)                      
#%%
scripture_BOM.loc['1 Nephi', 'Place'] = ['Jerusalem', 'Lehi\'s House']
#%% 
scripture_BOM
