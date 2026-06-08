import os
from PIL import Image
import numpy as np
import pandas as pd

# SADECE ANGLE KLASÖRÜNÜN YOLUNU BURAYA YAPIŞTIR
veri_klasoru = r"C:\Users\03asm\OneDrive\Masaüstü\CineScale2\CineScale2\cinescale2\cinescale2\angle" 

veriler = []
print("Kamera açısı resimlerinden özellikler çıkartılıyor... Lütfen bekleyin.")

# Angle klasörünün içindeki alt klasörleri (High, Low vb.) geziyoruz
for sinif_adi in os.listdir(veri_klasoru):
    sinif_yolu = os.path.join(veri_klasoru, sinif_adi)
    
    if os.path.isdir(sinif_yolu):
        print(f"{sinif_adi} klasörü işleniyor...")
        for resim_adi in os.listdir(sinif_yolu):
            if resim_adi.lower().endswith(('.jpg', '.png', '.jpeg')):
                resim_yolu = os.path.join(sinif_yolu, resim_adi)
                
                try:
                    # Resmi açıp 64x64 piksele küçültüyoruz (İşlemi hızlandırmak için)
                    img = Image.open(resim_yolu).convert('RGB')
                    img = img.resize((64, 64)) 
                    img_array = np.array(img)
                    
                    # Veri Madenciliği: Resimden anlamlı matematiksel özellikler (feature) çıkartma
                    r_ortalama = np.mean(img_array[:, :, 0])
                    g_ortalama = np.mean(img_array[:, :, 1])
                    b_ortalama = np.mean(img_array[:, :, 2])
                    parlaklik = np.mean(img_array)
                    
                    # Satır verisini listeye ekle
                    veriler.append({
                        'R_Ortalama': r_ortalama,
                        'G_Ortalama': g_ortalama,
                        'B_Ortalama': b_ortalama,
                        'Parlaklik': parlaklik,
                        'Aci_Sinifi': sinif_adi # Hedef Değişkenimiz (Target)
                    })
                except Exception:
                    continue # Bozuk resim varsa atla

# Özellikleri tabloya dönüştür ve kaydet
df = pd.DataFrame(veriler)
df.to_csv("cinescale_angle_veriseti.csv", index=False)
print("\nİşlem tamam! 'cinescale_angle_veriseti.csv' başarıyla oluşturuldu.")