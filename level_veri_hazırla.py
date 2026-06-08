import os
from PIL import Image
import numpy as np
import pandas as pd

# SADECE LEVEL KLASÖRÜNÜN YOLUNU BURAYA YAPIŞTIR (Baştaki 'r' harfini silme)
veri_klasoru = r"C:\Users\03asm\OneDrive\Masaüstü\CineScale2\CineScale2\cinescale2\cinescale2\level" 

veriler = []
print("Kamera seviyesi (level) resimlerinden özellikler çıkartılıyor... Lütfen bekleyin.")

for sinif_adi in os.listdir(veri_klasoru):
    sinif_yolu = os.path.join(veri_klasoru, sinif_adi)
    
    if os.path.isdir(sinif_yolu):
        print(f"{sinif_adi} klasörü işleniyor...")
        for resim_adi in os.listdir(sinif_yolu):
            if resim_adi.lower().endswith(('.jpg', '.png', '.jpeg')):
                resim_yolu = os.path.join(sinif_yolu, resim_adi)
                
                try:
                    img = Image.open(resim_yolu).convert('RGB')
                    img = img.resize((64, 64)) 
                    img_array = np.array(img)
                    
                    veriler.append({
                        'R_Ortalama': np.mean(img_array[:, :, 0]),
                        'G_Ortalama': np.mean(img_array[:, :, 1]),
                        'B_Ortalama': np.mean(img_array[:, :, 2]),
                        'Parlaklik': np.mean(img_array),
                        'Seviye_Sinifi': sinif_adi # Hedef Değişkenimiz değişti
                    })
                except Exception:
                    continue

df = pd.DataFrame(veriler)
df.to_csv("cinescale_level_veriseti.csv", index=False)
print("\nİşlem tamam! 'cinescale_level_veriseti.csv' başarıyla oluşturuldu.")