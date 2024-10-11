import pandas as pd 
df = pd.read_excel('teknolohik_urunler_zamanli.xlsx')
#tarih sütununu date time formatına çevirme ve indexleme işlemi 
df['Tarih'] = pd.to_datetime(df['Tarih'])
df.set_index('Tarih', inplace=True)
#veri setinin ilk 5 satırını görme
df=df.sort_index()
# print(df)
# en yüksek satışın yapıldığı aya göre sıralama
aylik_satis= df.resample("ME")["Satış"].sum()
max_ay = aylik_satis.idxmax()
max_satis_ay = aylik_satis.max()
max_satis_ay_urunler = df[df.index.to_series().between(max_ay-pd.offsets.MonthBegin(1),max_ay)]
# print(f"Enyüksek satış yapılan ay:  {max_ay} - Toplam  satış: {max_satis_ay}")
# print("O ayda satılan ürünler")
# print(max_satis_ay_urunler [["Ürün Adı","Satış"]])

# en Düşük satışın yapıldığı aya göre sıralama
min_ay = aylik_satis.idxmin()
min_satis_ay = aylik_satis.min()
min_satis_ay_urunler = df[df.index.to_series().between(max_ay-pd.offsets.MonthBegin(1),min_ay)]
# print(f"en düşük satış yapılan ay:  {min_ay} - Toplam  satış: {min_satis_ay}")
# print("O ayda satılan ürünler")
# print(min_satis_ay_urunler [["Ürün Adı","Satış"]])

# en fazla satış yapılan gün ve oyün satılan ürünler 
gunluk_satis= df.resample('D')['Satış'].sum()
max_gun = gunluk_satis.idxmax()
max_satis_gun = gunluk_satis.max()
max_satis_gun_urunler = df.loc[max_gun]
# print(f"\n Enfazla satış yapılan gün:{max_gun} - Toplam Satış : {max_satis_gun}")
# print("O günde satılan  ürünler")
# print(max_satis_gun_urunler[['Ürün Adı','Satış']])

haftalik_satis= df.resample('W')['Satış'].sum()
max_haftalik = haftalik_satis.idxmax()
max_satis_haftalik = haftalik_satis.max()
max_satis_haftalik_urunler = df[df.index.to_series().between(max_haftalik-pd.offsets.Week(1),max_haftalik)]
# print(f"\nE fazla satış yapılan hafta:  {max_haftalik} - Toplam satış: {max_satis_haftalik}")
# print("O haftada satılan ürünler")
# print(max_satis_haftalik_urunler [["Ürün Adı","Satış"]])

# aylık ortalam satış 
aylik_ortalama_satis = df.resample('ME')['Satış'].mean()
# print('Aylık ortalama satışlar:')
# print(aylik_ortalama_satis)

belirsi_aralik_urunler= df[df.index.to_series().between('2024-01-01','2024-03-31')]
# print("ocak 2024 ile mart 2024 arasında satılan ürünler:")
# print(belirsi_aralik_urunler[['Ürün Adı','Satış','Fiyat (TL)','Toplam Fiyat (TL)']])

# En yüksek toplam fiyatın olduğu ay ve o  ayda satılan ürünler
aylik_toplam_fiyat=df.resample('ME')['Toplam Fiyat (TL)'].sum()
max_ay_fiyat=aylik_toplam_fiyat.idxmax() #toplamı veriyor
max_fiyat_ay=aylik_toplam_fiyat.max()
max_fiyat_ay_urunler=df[df.index.to_series().between(max_ay_fiyat - pd.offsets.MonthBegin(1),max_ay_fiyat)]
print(f"Enyüksek toplam fiyata sahip ay : {max_ay_fiyat} - Toplam Fiyat : {max_fiyat_ay}")
print("O ayda satılan ürünler")
print(max_fiyat_ay_urunler[['Ürün Adı',  'Satış', 'Fiyat (TL)', 'Toplam Fiyat (TL)']])


