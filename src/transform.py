# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:23:45 2026

@author: NİSANUR
"""

import pandas as pd

# Veriyi temizleme ve dönüştürme işlemleri
def clean_data(veri):

    # Eksik değerleri kontrol ediyoruz
    print("Eksik değerler:")
    print(veri.isnull().sum())

    # Veri tiplerini kontrol ediyoruz
    print("\nVeri tipleri:")
    print(veri.dtypes)

    # Tekrarlanan satırları kontrol ediyoruz
    print("\nTekrarlanan satır sayısı:")
    print(veri.duplicated().sum())
    
    # Eksik değer oranlarını hesaplıyoruz
    eksik_oran = veri.isnull().mean() * 100

    print("\nEksik değer oranları (%):")
    print(eksik_oran[eksik_oran > 0].sort_values(ascending=False))
    
    # Fiyat sütunlarını kontrol ediyoruz
    print("\nFiyat bilgileri:")
    print(veri[["price_usd", "value_price_usd", "sale_price_usd"]].describe())
    
    # Ürün kategorilerini kontrol ediyoruz
    print("\nAna kategoriler:")
    print(veri["primary_category"].value_counts())
    
    # Kategorilerin müşteri ilgisini karşılaştırıyoruz
    kategori_ilgi = veri.groupby("primary_category")["loves_count"].mean()

    print("\nKategori bazında ortalama müşteri ilgisi:")
    print(kategori_ilgi.sort_values(ascending=False))
    
    # Kategorilerin ortalama puanlarını karşılaştırıyoruz
    kategori_puan = veri.groupby("primary_category")["rating"].mean()

    print("\nKategori bazında ortalama puan:")
    print(kategori_puan.sort_values(ascending=False))
    
    # Kategori büyüklüğü ve ortalama puanı birlikte inceliyoruz
    kategori_analiz = veri.groupby("primary_category").agg(
        urun_sayisi=("product_id", "count"),
        ortalama_puan=("rating", "mean")
    )

    print("\nKategori performans özeti:")
    print(kategori_analiz.sort_values("ortalama_puan", ascending=False))
        
    return veri


    