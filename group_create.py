import pandas as pd 

df = pd.read_excel('teknolojik_urunler.xlsx')

gruplar = df.groupby('Kategori')

# toplam_satis=df.groupby('Kategori')['Satış'].sum()
# toplam_satis_fiyat=df.groupby('Kategori')['Fiyat (TL)'].sum()
# ortalama_toplam_satis=df.groupby('Kategori')['Fiyat (TL)'].mean()

# toplam_ve_ortalama=df.groupby('Kategori').agg(


#     {
#         'Satış': 'sum',
#         'Fiyat (TL)': 'mean'
#     }
# )
# print(toplam_ve_ortalama)

# en_pahali_urun=df.loc[df.groupby('Kategori')['Fiyat (TL)'].idxmax()]
satıs_ust_gruplar=df.groupby('Kategori').filter(lambda x:x['Satış'].sum()>50)
print(satıs_ust_gruplar[['Kategori','Ürün Adı','Satış']])