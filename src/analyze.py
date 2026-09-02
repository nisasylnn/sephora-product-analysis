# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:24:04 2026

@author: NİSANUR
"""

import pandas as pd

def analiz_yap(veri):

    # Fiyat ile müşteri puanı arasındaki ilişki
    korelasyon = veri["price_usd"].corr(veri["rating"])

    print("\nFiyat ile puan arasındaki korelasyon:")
    print(korelasyon)

    # Kategorilerin ortalama müşteri ilgisini karşılaştırıyoruz
    kategori_ilgi = veri.groupby("primary_category")["loves_count"].mean()

    print("\nKategori bazında ortalama müşteri ilgisi:")
    print(kategori_ilgi.sort_values(ascending=False))
    
    # Fiyat ile müşteri ilgisi arasındaki ilişki
    fiyat_ilgi = veri["price_usd"].corr(veri["loves_count"])

    print("\nFiyat ile müşteri ilgisi arasındaki korelasyon:")
    print(fiyat_ilgi)
    
    return korelasyon




    

