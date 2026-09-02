# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 17:36:15 2026

@author: NİSANUR
"""

import pandas as pd
from pathlib import Path

# Proje ana klasörünü buluyoruz
BASE_DIR = Path(__file__).resolve().parent.parent

# Ham veri dosyasının yolu
DATA_PATH = BASE_DIR / "data" / "raw" / "product_info.csv"


# Veriyi okuyoruz
def load_data():
    veri = pd.read_csv(DATA_PATH)

    # Veri hakkında temel bilgi
    print("Veri boyutu:", veri.shape)
    print("\nSütunlar:")
    print(veri.columns.tolist())

    return veri


# Fonksiyonu çalıştırıyoruz
if __name__ == "__main__":
    veri = load_data()
    print("\nİlk 5 satır:")
    print(veri.head())
    

def load_review_trend():

    # Review dosyalarını buluyoruz
    review_files = list((BASE_DIR / "data" / "raw").glob("reviews_*.csv"))

    aylik_yorumlar = []

    # Dosyaları parça parça okuyoruz
    for dosya in review_files:

        for parca in pd.read_csv(
            dosya,
            usecols=["submission_time"],
            chunksize=50000
        ):
            parca["submission_time"] = pd.to_datetime(
                parca["submission_time"],
                errors="coerce"
            )

            parca = parca.dropna(subset=["submission_time"])

            aylik = parca["submission_time"].dt.to_period("M").value_counts()
            aylik_yorumlar.append(aylik)

    # Tüm dosyalardaki aylık sayıları birleştiriyoruz
    aylik_yorumlar = pd.concat(aylik_yorumlar)
    aylik_yorumlar = aylik_yorumlar.groupby(level=0).sum().sort_index()

    return aylik_yorumlar
    


