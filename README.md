# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:26:58 2026

@author: NİSANUR
"""

# Sephora Ürün ve Müşteri İlgi Analizi

## Proje Amacı

Bu projede Sephora ürün ve müşteri değerlendirme verileri kullanılarak ürün kategorileri, müşteri ilgisi ve fiyat ilişkileri analiz edilmiştir.

Ayrıca geçmiş yorum verilerindeki aylık trend incelenerek gelecek 6 ay için müşteri ilgisine yönelik basit bir öngörü oluşturulmuştur.

## İş Problemi

Sephora'nın hangi ürün kategorilerine odaklanmasının daha avantajlı olabileceğini ve mevcut müşteri ilgi eğilimlerinin gelecekte nasıl değişebileceğini veri üzerinden değerlendirmek.

## Kullanılan Veriler

Projede Kaggle üzerinden alınan Sephora ürün ve müşteri değerlendirme verileri kullanılmıştır.

Ana ürün verisinde:

- Ürün bilgileri
- Marka bilgileri
- Fiyat
- Müşteri puanı
- Yorum sayısı
- Loves Count
- Ürün kategorileri
- Ürün özellikleri

bulunmaktadır.

Yorum verilerinde ise müşteri değerlendirmelerinin tarih bilgileri kullanılmıştır.

> loves_count ürünün favorilenme/beğenilme sayısını, 
reviews ise ürünün toplam yorum sayısını göstermektedir.
Bu değişkenler gerçek satış verisi değildir ve müşteri ilgisini değerlendirmek için
gösterge olarak kullanılmıştır.

## Proje Akışı

1. Veri CSV dosyalarından alındı.
2. Eksik değerler ve veri tipleri kontrol edildi.
3. Tekrarlanan kayıtlar incelendi.
4. Ürün kategorileri analiz edildi.
5. Kategori bazında müşteri ilgisi karşılaştırıldı.
6. Fiyat ile müşteri ilgisi arasındaki ilişki incelendi.
7. Aylık yorum trendi oluşturuldu.
8. Son 12 aylık trende dayanarak 6 aylık müşteri ilgisi öngörüsü oluşturuldu.
9. Analiz sonuçları grafiklerle görselleştirildi.
10. Temizlenmiş veri kaydedildi.

## Temel Bulgular

- Ürün sayısı açısından *Skincare* kategorisi öne çıkmaktadır.
- Ortalama müşteri ilgisi açısından *Makeup* kategorisi öne çıkmaktadır.
- Fiyat ile müşteri ilgisi arasında güçlü bir ilişki görülmemiştir.
- Son 12 aylık yorum trendine dayanan basit öngörü, gelecek 6 ayda yorum hacminde kademeli bir düşüş göstermektedir.

## Tahmin Yaklaşımı

6 aylık öngörü oluşturulurken son 12 aylık aylık yorum sayıları kullanılmış ve basit doğrusal trend yöntemi uygulanmıştır.

Bu tahmin gerçek satış veya gelir tahmini değildir. Yorum sayısı, müşteri ilgisini temsil eden bir gösterge olarak değerlendirilmiştir.

## Proje Yapısı

```text
sephora - project/
│
├── data/
│   ├── raw/
│   │   ├── product_info.csv
│   │   └── reviews_*.csv
│   │
│   └── processed/
│       └── temiz_veri.csv
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── analyze.py
│   ├── model.py
│   ├── visualize.py
│   └── save.py
│
├── output/
│   ├── kategori_urun_sayisi.png
│   ├── kategori_musteri_ilgisi.png
│   ├── fiyat_musteri_ilgisi.png
│   └── trend_ve_6_ay_tahmini.png
│
├── main.py
├── README.md
├── requirements.txt
└── sephora_analysis.ipynb



