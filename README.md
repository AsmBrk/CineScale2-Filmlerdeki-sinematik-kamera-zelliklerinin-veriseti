# CineScale2 Veri Seti ile Kamera Açısı ve Seviyesi Sınıflandırması

Bu proje, **BLM0463 Veri Madenciliğine Giriş** dersi dönem projesi kapsamında geliştirilmiştir. Projenin amacı, sinematik görüntü çerçevelerinin (CineScale2 veri seti) kamera açısı (Angle) ve kamera seviyesi (Level) parametrelerini makine öğrenmesi algoritmaları kullanarak otomatik olarak sınıflandırmaktır.

## 📌 Proje Özeti
Proje, görüntü işleme ve veri madenciliği tekniklerini birleştirmektedir. Orijinal veri setindeki ham görüntülerden **Ortalama RGB (Kırmızı, Yeşil, Mavi)** ve **Parlaklık** değerleri çıkarılarak iki farklı veri seti (tablo) oluşturulmuş ve bu veriler üzerinde **Karar Ağacı (Decision Tree)** modelleri eğitilmiştir.

* **Model 1 (Kamera Açısı):** 5 farklı sınıf (Overhead, High, Neutral, Low, Dutch). Başarı oranı: %55.91
* **Model 2 (Kamera Seviyesi):** 6 farklı sınıf (Aerial, Eye, Ground, Hip, Knee, Shoulder). Başarı oranı: %59.22

## 📁 Dosya Yapısı
* `veri_hazirla.py` / `level_veri_hazirla.py`: Ham görüntülerden renk özelliklerini çıkarıp `.csv` veri tablolarını oluşturan Python betikleri.
* `model_egit.py` / `level_model_egit.py`: Oluşturulan tabloları kullanarak Karar Ağacı modelini eğiten, test eden ve performans metriklerini hesaplayan betikler.
* `*.csv` dosyaları: Model eğitimi için oluşturulmuş sayısal veri setleri.
* `*.png` dosyaları: Modelin karar ağacı yapısını ve karmaşıklık matrisi (confusion matrix) sonuçlarını gösteren yüksek çözünürlüklü grafikler.

## 🛠️ Kullanılan Teknolojiler
* **Dil:** Python
* **Kütüphaneler:** `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `Pillow`

## 🚀 Nasıl Çalıştırılır?
1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn Pillow
