import pandas as pd 
# read excel file 
df  = pd.read_excel('teknolojik_urunler.xlsx')
# read  excel file for first rows
# print(df)

# ortalam_fiyat=df['Fiyat (TL)'].mean()
# print(f"Ortalama Fiyat :  {ortalam_fiyat} TL")  # print avarage price

# max gelir getiren ürün sıralama

# kategori_bazli_satis = df.groupby('Kategori')['Satış'].sum()
# print(kategori_bazli_satis)
# ençok gelir getiren ürünü bulma 
# fonksiyonlara parantez atmamak hatay neden olur idxmax()
# loc belirli satır yada stüna index ile ulaşır 
# idxmax ise  en büyük değeri bulur en yüksek değere sahip olan öğenin indeksini döner.

# max_gelir = df.loc[df['Toplam Fiyat (TL)'].idxmax()]
# print(f"En çok gelir getiren ürün:\n{max_gelir}")

#  belirli bir fiyat üstünü göster

fiyat_ust_urunler= df[df['Fiyat (TL)'] >4000]
print('Fiyatı 4000 TL üzerinde olan ürünler:')
print(fiyat_ust_urunler,)
fiyat_ust_urunler.to_excel('Fiyatı_4000_TL_sutu_olanlar.xlsx',index=False)