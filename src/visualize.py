# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:39:31 2026

@author: NİSANUR
"""

import matplotlib.pyplot as plt
from pathlib import Path


# Proje klasörünü buluyoruz
BASE_DIR = Path(__file__).resolve().parent.parent

# Grafiklerin kaydedileceği klasör
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


def kategori_urun_sayisi(veri):

    # Kategorilerdeki ürün sayılarını hesaplıyoruz
    kategori_sayisi = veri["primary_category"].value_counts().sort_values()

    # Grafiği oluşturuyoruz
    plt.figure(figsize=(10, 6))
    kategori_sayisi.plot(kind="barh")

    plt.title("Kategori Bazında Ürün Sayısı")
    plt.xlabel("Ürün Sayısı")
    plt.ylabel("Ana Kategori")

    plt.tight_layout()

    # Grafiği kaydediyoruz
    plt.savefig(OUTPUT_DIR / "kategori_urun_sayisi.png", dpi=150)

    plt.show()
    
def kategori_musteri_ilgisi(veri):

    # Kategorilerin ortalama müşteri ilgisini hesaplıyoruz
    kategori_ilgi = veri.groupby("primary_category")["loves_count"].mean()
    kategori_ilgi = kategori_ilgi.sort_values()

    # Grafiği oluşturuyoruz
    plt.figure(figsize=(10, 6))
    kategori_ilgi.plot(kind="barh")

    plt.title("Kategori Bazında Ortalama Müşteri İlgisi")
    plt.xlabel("Ortalama Loves Count")
    plt.ylabel("Ana Kategori")

    plt.tight_layout()

    # Grafiği kaydediyoruz
    plt.savefig(OUTPUT_DIR / "kategori_musteri_ilgisi.png", dpi=150)

    plt.show()
    
    
def fiyat_musteri_ilgisi(veri):

    # Eksik fiyat ve ilgi değerlerini çıkarıyoruz
    grafik_verisi = veri[["price_usd", "loves_count"]].dropna()

    # Dağılım grafiğini oluşturuyoruz
    plt.figure(figsize=(10, 6))
    plt.scatter(
        grafik_verisi["price_usd"],
        grafik_verisi["loves_count"],
        alpha=0.5
    )

    plt.title("Fiyat ile Müşteri İlgisi Arasındaki İlişki")
    plt.xlabel("Fiyat (USD)")
    plt.ylabel("Loves Count")

    plt.tight_layout()

    # Grafiği kaydediyoruz
    plt.savefig(OUTPUT_DIR / "fiyat_musteri_ilgisi.png", dpi=150)

    plt.show()
    
    
def trend_ve_tahmin_grafigi(aylik_yorumlar, tahminler):

    # Son 12 aylık gerçek veriyi alıyoruz
    gercek_veri = aylik_yorumlar.tail(12)

    plt.figure(figsize=(10, 6))

    # Gerçek değerleri gösteriyoruz
    plt.plot(
        gercek_veri.index.astype(str),
        gercek_veri.values,
        marker="o",
        label="Gerçek Veri"
    )

    # Tahmin değerlerini gösteriyoruz
    plt.plot(
        tahminler.index.astype(str),
        tahminler.values,
        marker="o",
        linestyle="--",
        label="6 Aylık Öngörü"
    )

    plt.title("Müşteri İlgisi: Gerçek Trend ve 6 Aylık Öngörü")
    plt.xlabel("Ay")
    plt.ylabel("Yorum Sayısı")
    plt.xticks(rotation=45)
    plt.legend()

    plt.tight_layout()

    # Grafiği kaydediyoruz
    plt.savefig(
        OUTPUT_DIR / "trend_ve_6_ay_tahmini.png",
        dpi=150
    )

    plt.show()
    
    
    
    