# %% 
import pandas as pd
import numpy as np

# %%
First_Nephi = pd.DataFrame(data = {'Book': "1 Nephi", 'Chapter': range(1, 23)})
Second_Nephi = pd.DataFrame(data = {'Book': "2 Nephi", 'Chapter': range(1, 34)})
Jacob = pd.DataFrame(data = {'Book': "Jacob", 'Chapter': range(1, 8)})
Enos = pd.DataFrame(data = {'Book': "Enos", 'Chapter': range(1, 2)})
Jarom = pd.DataFrame(data = {'Book': "Jarom", 'Chapter': range(1, 2)})
Omni = pd.DataFrame(data = {'Book': "Omni", 'Chapter': range(1, 2)})
Words_of_Mormon = pd.DataFrame(data = {'Book': "Words of Mormon", 'Chapter': range(1, 2)})
Mosiah = pd.DataFrame(data = {'Book': "Mosiah", 'Chapter': range(1, 30)})
Alma = pd.DataFrame(data = {'Book': "Alma", 'Chapter': range(1, 64)})
Helaman = pd.DataFrame(data = {'Book': "Helaman", 'Chapter': range(1, 17)})
Third_Nephi = pd.DataFrame(data = {'Book': "Third Nephi", 'Chapter': range(1, 31)})
Fourth_Nephi = pd.DataFrame(data = {'Book': "Fourth Nephi", 'Chapter': range(1, 2)})
Mormon = pd.DataFrame(data = {'Book': "Mormon", 'Chapter': range(1, 10)})
Ether = pd.DataFrame(data = {'Book': "Ether", 'Chapter': range(1, 16)})
Moroni = pd.DataFrame(data = {'Book': "Moroni", 'Chapter': range(1, 11)})

BOM = (
    pd.concat([First_Nephi, Second_Nephi, Jacob, Enos, Jarom, Omni, Words_of_Mormon, Mosiah, Alma, Helaman, Third_Nephi, Fourth_Nephi, Mormon, Ether, Moroni], axis = 0)
    .assign(
        Place = np.nan,
        People = np.nan,
        Doctrine = np.nan, 
        References_to_Christ = np.nan, 
        )
)

BOM.head()
# BOM.to_csv("Book_of_Mormon.csv")

# %%
scriptures = pd.read_csv("Scriptures.csv")