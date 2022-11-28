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
new_columns = columns.append('hey')
print(new_columns)                      
#%%
scripture_BOM.loc['1 Nephi', 'Place'] = ['Jerusalem', 'Lehi\'s House']
#%% 
# scripture_BOM
type(scripture_BOM.loc['1 Nephi', 'Place'])
# %%
