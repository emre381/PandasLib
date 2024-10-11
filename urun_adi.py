import pandas as pd 

df = pd.read_excel('teknolojik_urunler.xlsx')


print(df[['Kategori','Toplam Fiyat (TL)']])