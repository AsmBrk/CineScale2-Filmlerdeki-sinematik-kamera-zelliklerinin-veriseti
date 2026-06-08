import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, recall_score, f1_score, confusion_matrix

df = pd.read_csv("cinescale_level_veriseti.csv")


X = df[['R_Ortalama', 'G_Ortalama', 'B_Ortalama', 'Parlaklik']]
y = df['Seviye_Sinifi']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


dt_model = DecisionTreeClassifier(random_state=42, max_depth=5)
dt_model.fit(X_train, y_train)


y_pred = dt_model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
sensitivity = recall_score(y_test, y_pred, average='macro', zero_division=0)
f_measure = f1_score(y_test, y_pred, average='macro', zero_division=0)

cm = confusion_matrix(y_test, y_pred)
specificity_list = []
for i in range(len(cm)):
    gercek_negatifler = np.sum(cm) - (np.sum(cm[i, :]) + np.sum(cm[:, i]) - cm[i, i])
    yanlis_pozitifler = np.sum(cm[:, i]) - cm[i, i]
    spec = gercek_negatifler / (gercek_negatifler + yanlis_pozitifler) if (gercek_negatifler + yanlis_pozitifler) != 0 else 0
    specificity_list.append(spec)
specificity = np.mean(specificity_list)

print("\n--- LEVEL MODELİ PERFORMANS SONUÇLARI ---")
print(f"Accuracy (Doğruluk)  : {accuracy:.4f}")
print(f"Sensitivity (Duyarlılık): {sensitivity:.4f}")
print(f"Specificity (Özgüllük)  : {specificity:.4f}")
print(f"F-measure (F1-Skoru)    : {f_measure:.4f}")
print("-" * 40)


plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Oranges', xticklabels=dt_model.classes_, yticklabels=dt_model.classes_)
plt.title('Karmaşıklık Matrisi - Level (Kamera Seviyesi)')
plt.xlabel('Tahmin Edilen Seviye')
plt.ylabel('Gerçek Seviye')

plt.savefig("level_confusion_matrix.png", dpi=300, bbox_inches='tight')
plt.show() 


plt.figure(figsize=(40, 20)) 
plot_tree(dt_model, filled=True, feature_names=X.columns, class_names=dt_model.classes_, rounded=True, fontsize=10)
plt.title('Karar Ağacı Yapısı - Kamera Seviyesi (Level)')
plt.savefig("level_karar_agaci_net.png", dpi=300, bbox_inches='tight') 
plt.show()
