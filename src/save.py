# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:24:43 2026

@author: NİSANUR
"""

from pathlib import Path


# Proje klasörünü buluyoruz
BASE_DIR = Path(__file__).resolve().parent.parent

# İşlenmiş veri klasörü
OUTPUT_PATH = BASE_DIR / "data" / "processed" / "temiz_veri.csv"


def save_data(veri):

    # Temizlenmiş veriyi kaydediyoruz
    veri.to_csv(OUTPUT_PATH, index=False)

    print("Veri başarıyla kaydedildi.")