# Sephora Ürün ve Müşteri İlgisi Analizi

## Proje Amacı

Bu projede Sephora ürün ve müşteri değerlendirme verileri kullanılarak ürün kategorileri, müşteri ilgisi ve fiyat ilişkileri analiz edilmiştir.

Ayrıca geçmiş müşteri yorumlarındaki aylık trend incelenerek gelecek 6 ay için müşteri ilgisine yönelik basit bir trend öngörüsü oluşturulmuştur.

## İş Problemi

Sephora'nın hangi ürün kategorilerinde daha fazla çeşitliliğe sahip olduğu, hangi kategorilerin daha yüksek müşteri ilgisi gördüğü ve mevcut müşteri ilgisi eğiliminin gelecekte nasıl değişebileceği veri üzerinden değerlendirilmiştir.

## Kullanılan Veriler

Projede Kaggle üzerinden alınan Sephora ürün ve müşteri değerlendirme verileri kullanılmıştır.

Ana ürün verisinde;

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

loves_count ürünün favorilenme/beğenilme sayısını, reviews ise ürünün toplam yorum sayısını göstermektedir.

Bu değişkenler gerçek satış verisi değildir ve projede müşteri ilgisini değerlendirmek için gösterge olarak kullanılmıştır.

## Proje Akışı

1. Veri CSV dosyalarından alındı.
2. Eksik değerler ve veri tipleri kontrol edildi.
3. Tekrarlanan kayıtlar incelendi.
4. Ürün kategorileri analiz edildi.
5. Kategori bazında müşteri ilgisi karşılaştırıldı.
6. Fiyat ile müşteri puanı arasındaki ilişki incelendi.
7. Fiyat ile müşteri ilgisi arasındaki ilişki incelendi.
8. Aylık müşteri yorum trendi oluşturuldu.
9. Son 12 aylık trende dayanarak 6 aylık müşteri ilgisi öngörüsü oluşturuldu.
10. Analiz sonuçları grafiklerle görselleştirildi.
11. İşlenmiş veri kaydedildi.

## Temel Bulgular

- Ürün sayısı açısından *Skincare* kategorisi öne çıkmaktadır.
- Ortalama müşteri ilgisi açısından *Makeup* kategorisi öne çıkmaktadır.
- Fiyat ile müşteri puanı arasında güçlü bir ilişki görülmemiştir.
- Fiyat ile müşteri ilgisi arasında güçlü bir ilişki görülmemiştir.
- Son 12 aylık müşteri yorum trendine göre gelecek 6 ay için kademeli bir düşüş öngörülmüştür.

## Tahmin Yaklaşımı

6 aylık öngörü oluşturulurken son 12 aylık aylık müşteri yorum sayıları kullanılmış ve basit doğrusal trend yöntemi uygulanmıştır.

Bu tahmin gerçek satış veya gelir tahmini değildir.

Yorum sayısı, müşteri ilgisini değerlendirmek için kullanılan bir gösterge olarak ele alınmıştır.

## Proje Yapısı

```text
sephora-product-analysis/
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
├── sephora_analysis.ipynb
├── requirements.txt
└── README.md

## Kullanılan Teknolojiler

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

## Analiz Bulguları ve Yorumlar

### Kategori Bazında Ürün Sayısı

Skincare ve Makeup kategorileri ürün sayısı açısından öne çıkmaktadır.

*Yorum:* Bu kategoriler Sephora'nın ürün portföyünde önemli bir ağırlığa sahiptir.

### Kategori Bazında Ortalama Müşteri İlgisi

Makeup kategorisi ortalama loves_count açısından diğer kategorilere göre daha yüksek müşteri ilgisi göstermektedir.

*Yorum:* Makeup kategorisi müşteri ilgisi açısından güçlü bir kategori olarak değerlendirilebilir.

### Fiyat ve Müşteri Puanı

Fiyat ile müşteri puanı arasındaki korelasyon yaklaşık *0.057* bulunmuştur.

*Yorum:* Fiyat ile müşteri puanı arasında güçlü bir doğrusal ilişki görülmemektedir.

### Fiyat ve Müşteri İlgisi

Fiyat ile loves_count arasındaki korelasyon yaklaşık *-0.09* bulunmuştur.

*Yorum:* Fiyat ile müşteri ilgisi arasında güçlü bir ilişki görülmemektedir. Müşteri ilgisini değerlendirirken yalnızca fiyata odaklanılmamalıdır.

### 6 Aylık Müşteri İlgisi Öngörüsü

Son 12 aylık müşteri yorum trendine göre gelecek 6 ay için kademeli bir düşüş öngörülmüştür.

*Yorum:* Mevcut trendin devam etmesi durumunda müşteri etkileşiminde bir zayıflama görülebilir. Ancak bu sonuç satış veya gelir tahmini değildir.

## Yönetici İçin Öneriler

- Makeup kategorisi müşteri ilgisi açısından öncelikli takip alanı olarak değerlendirilebilir.
- Skincare kategorisindeki güçlü ürün çeşitliliği korunabilir.
- Fiyat tek başına müşteri ilgisini açıklamadığı için ürün özellikleri, marka ve müşteri deneyimi birlikte değerlendirilmelidir.
- Müşteri yorum trendleri düzenli olarak takip edilmelidir.
- Yüksek müşteri ilgisi gösteren ürünlerin ortak özellikleri ayrıca incelenebilir.

## Sınırlılıklar

- Veri seti gerçek satış miktarlarını içermemektedir.
- loves_count satış miktarı değildir; müşteri ilgisini gösteren bir metriktir.
- reviews ürünün toplam yorum sayısını ifade etmektedir.
- 6 aylık öngörü gerçek satış veya gelir tahmini değildir.
- Öngörü basit doğrusal trend yaklaşımına dayanmaktadır.
- Sonuçlar kullanılan veri setinin kapsamı ve dönemine bağlıdır.

## Sonuç

Bu proje kapsamında Sephora ürün ve müşteri değerlendirme verileri kullanılarak veri alma, veri kontrolü, analiz, görselleştirme ve trend öngörüsü gerçekleştirilmiştir.

Analiz sonucunda Skincare kategorisinin ürün sayısı açısından, Makeup kategorisinin ise ortalama müşteri ilgisi açısından öne çıktığı görülmüştür.

Fiyat ile müşteri ilgisi arasında güçlü bir ilişki bulunmamıştır.

Geçmiş müşteri yorum trendine dayalı 6 aylık öngörü ise mevcut eğilimin devam etmesi durumunda yorum hacminde kademeli bir düşüş sinyali vermektedir.

Bu çalışma, ürün ve müşteri verilerinin veri odaklı karar destek süreçlerinde kullanılabileceğini göstermektedir.



