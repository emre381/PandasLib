import pandas as pd 
# read excel file 
df  = pd.read_excel('teknolojik_urunler.xlsx')

# eksik_veriler = df.isnull()
# print(eksik_veriler)
#temizleme
# temiz_df=df.dropna()
# print(temiz_df)
# doldurulmus_df=df.fillna("--")
# print(doldurulmus_df)
# df['Fiyat (TL)']= df['Fiyat (TL)'].astype(float)
#  #yada int64 yazabilirsin bu şekilde kullanılır 
# df.insert(2,"Yeni Sütun",range(1,21))
# print(df.head)
# df.to_excel('toexcel.xlsx',index=False)
# print("Veri kayıt edildi !")

# df_düsük = df.sort_values(by='Fiyat (TL)', ascending=False)
# print(df_düsük)
# df_fiyat_ust = df[df['Fiyat (TL)'] > 5000] 
# print(df_fiyat_ust)

# df_filtre = df[(df['Fiyat (TL)']> 5000) &  (df['Kategori'] == 'Bilgisayarlar')]
# print(df_filtre)

# df_secim=df.loc[:,['Ürün Adı','Fiyat (TL)']]
# index numarasına göre seçer
# df_secim=df.loc[:5,:]
# print(df_secim)


# sql tarzı sorgu 

# df_sorgu=df.query('Satış >10')
# print(df_sorgu)

df_kategoriler= df[df['Kategori'].isin(['Televizyonlar','Mobil Cihazlar'])]
print(df_kategoriler)


