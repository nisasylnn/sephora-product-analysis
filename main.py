# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:25:42 2026

@author: NİSANUR
"""

from src.extract import load_data , load_review_trend
from src.transform import clean_data
from src.analyze import analiz_yap
from src.model import model_olustur, alti_ay_tahmini
from src.save import save_data
from src.visualize import (
    kategori_urun_sayisi,
    kategori_musteri_ilgisi,
    fiyat_musteri_ilgisi,
    trend_ve_tahmin_grafigi
)


# Veriyi alıyoruz
veri = load_data()

# Veriyi kontrol ediyoruz
veri = clean_data(veri)

# Analizi çalıştırıyoruz
korelasyon = analiz_yap(veri)

# Model analizini çalıştırıyoruz
model_olustur(veri)

# Yorumların aylık trendini çıkarıyoruz
aylik_yorumlar = load_review_trend()

print("\nAylık yorum sayıları:")
print(aylik_yorumlar)

# Gelecek 6 ay için müşteri ilgisi öngörüsü
tahminler = alti_ay_tahmini(aylik_yorumlar)

# Temizlenmiş veriyi kaydediyoruz
save_data(veri)

#grafikler
kategori_urun_sayisi(veri)

kategori_musteri_ilgisi(veri)

fiyat_musteri_ilgisi(veri)

trend_ve_tahmin_grafigi(aylik_yorumlar, tahminler)
    
print("\nAnaliz tamamlandı.")




