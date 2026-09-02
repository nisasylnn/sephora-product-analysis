# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:24:25 2026

@author: NİSANUR
"""
import pandas as pd
import numpy as np

def model_olustur(veri):
    # Fiyat ve puanı kullanıyoruz
    X = veri[["price_usd", "rating"]].dropna()

    # Müşteri ilgisini alıyoruz
    y = veri.loc[X.index, "loves_count"]

    # Korelasyonları hesaplıyoruz
    fiyat_ilgi = X["price_usd"].corr(y)
    puan_ilgi = X["rating"].corr(y)

    print("\nModel için ilişkiler:")
    print("Fiyat - müşteri ilgisi:", fiyat_ilgi)
    print("Puan - müşteri ilgisi:", puan_ilgi)

    return fiyat_ilgi, puan_ilgi

def alti_ay_tahmini(aylik_yorumlar):

    # Son 12 aylık veriyi kullanıyoruz
    son_12_ay = aylik_yorumlar.tail(12)

    # Ayları sayısal değerlere çeviriyoruz
    x = np.arange(len(son_12_ay))
    y = son_12_ay.values

    # Basit doğrusal trend oluşturuyoruz
    katsayilar = np.polyfit(x, y, 1)

    # Gelecek 6 ayı tahmin ediyoruz
    gelecek_x = np.arange(len(son_12_ay), len(son_12_ay) + 6)
    tahmin = np.polyval(katsayilar, gelecek_x)

    # Negatif tahminleri sıfırlıyoruz
    tahmin = np.maximum(tahmin, 0)

    gelecek_aylar = pd.period_range(
        start=aylik_yorumlar.index[-1] + 1,
        periods=6,
        freq="M"
    )

    tahminler = pd.Series(
        tahmin.astype(int),
        index=gelecek_aylar
    )

    print("\n6 Aylık Müşteri İlgi Öngörüsü:")
    print(tahminler)

    return tahminler





