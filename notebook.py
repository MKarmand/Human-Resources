# -*- coding: utf-8 -*-
"""HumanRecourcesDataScience.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NAVdt3UD1KS-IoSAzfUXq_EhL56UubPW

# Proyek Akhir: Menyelesaikan Permasalahan Drancang Company

- Nama: Muhammad Kristover Armand
- Email: mkarmand43@gmail.com
- Id Dicoding: mk_armand_13

**Menyiapkan library yang dibutuhkan**

---
"""

# Import library yang diperlukan
import pandas as pd
import joblib
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

"""**Menyiapkan data yang akan diguankan**"""

# 1. Load data
df = pd.read_csv("data.csv")
df

"""# Data Understanding"""

df.info()

# Pilih kolom numerik
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
# Create the numerical_df
numerical_df = df[numerical_cols]

plt.figure(figsize=(16, 12))  # Perbesar area plot
sns.heatmap(numerical_df.corr(),
            annot=True,            # Tampilkan angka korelasi
            fmt=".2f",             # Dua angka desimal
            cmap='coolwarm',       # Skema warna
            cbar=True,             # Tampilkan colorbar
            square=True,           # Kotak per sel
            linewidths=0.5,        # Garis antar sel
            linecolor='gray')      # Warna garis antar sel

plt.title('Correlation Heatmap - Fitur Numerik', fontsize=16)
plt.xticks(rotation=45, ha='right')  # Putar label X
plt.yticks(rotation=0)               # Label Y tetap horizontal
plt.tight_layout()
plt.show()

# Tentukan ukuran figure dan grid
plt.figure(figsize=(18, 15))
df[numerical_cols].hist(bins=20, layout=(6, 5), figsize=(18, 15), edgecolor='black')
plt.tight_layout()
plt.suptitle("Distribusi Fitur Numerikal", fontsize=20, y=1.02)
plt.show()

# Pilih hanya kolom numerik
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns

# Tampilkan nilai minimum dan maksimum
df[numerical_cols].agg(['min', 'max'])

import math

# Ambil semua kolom kategorikal
categorical_cols = df.select_dtypes(include=['object']).columns

# Hitung jumlah baris dan kolom grid
n_cols = 3
n_rows = math.ceil(len(categorical_cols) / n_cols)

# Buat figure besar
fig, axes = plt.subplots(n_rows, n_cols, figsize=(18, n_rows * 4))
axes = axes.flatten()

# Plot semua fitur dalam grid
for i, col in enumerate(categorical_cols):
    sns.countplot(x=col, hue='Attrition', data=df, ax=axes[i])
    axes[i].set_title(f'Distribusi {col} berdasarkan Attrition')
    axes[i].tick_params(axis='x', rotation=45)

# Sembunyikan subplot kosong (jika ada)
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.suptitle("Distribusi Fitur Kategorikal berdasarkan Attrition", fontsize=20, y=1.02)
plt.show()

"""# Data Preparation / Preprocessing"""

# 2. Salin data untuk diproses
data = df.copy()

# 3. Pisahkan data berlabel dan tidak berlabel
train_data = data[data['Attrition'].notna()].copy()
predict_data = data[data['Attrition'].isna()].copy()

# 4. Ubah kolom Attrition ke integer
train_data['Attrition'] = train_data['Attrition'].astype(int)

# 5. Tentukan kolom yang tidak diperlukan
drop_cols = ['EmployeeCount', 'StandardHours', 'EmployeeId', 'Over18']
X = train_data.drop(columns=['Attrition'] + drop_cols)
y = train_data['Attrition']

# 6. Encode fitur kategorikal
encoder = {}
for col in X.select_dtypes(include='object').columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))
    encoder[col] = le

# Siapkan data prediksi
X_pred = predict_data.drop(columns=['Attrition'] + drop_cols)
for col in X_pred.select_dtypes(include='object').columns:
    if col in encoder:
        le = encoder[col]
        X_pred[col] = X_pred[col].map(lambda x: le.transform([x])[0] if x in le.classes_ else -1)

# Pastikan tidak ada kolom bertipe object
assert X_pred.select_dtypes(include='object').empty, "Masih ada kolom object di X_pred!"

smote = SMOTE(random_state=42)
X_balanced, y_balanced = smote.fit_resample(X, y)

# Split data balanced
X_train, X_test, y_train, y_test = train_test_split(X_balanced, y_balanced, test_size=0.2, random_state=42)

# # 8. Split data
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

"""# Modeling"""

# 9. Latih model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

"""# Evaluasi"""

# Prediksi pada data uji
y_pred_test = model.predict(X_test)
# Akurasi
accuracy = accuracy_score(y_test, y_pred_test)
print("Akurasi:", accuracy)

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred_test)
print("Confusion Matrix:\n", conf_matrix)

# Classification Report
report = classification_report(y_test, y_pred_test)
print("Classification Report:\n", report)

predicted_attrition = model.predict(X_pred)
predict_data['Predicted_Attrition'] = predicted_attrition
train_data['Predicted_Attrition'] = train_data['Attrition']

# Gabungkan semua data
final_df = pd.concat([train_data, predict_data], axis=0)

# Isi nilai kosong di kolom Attrition
final_df['Attrition'] = final_df['Attrition'].fillna(final_df['Predicted_Attrition'])

final_df.to_csv("data_filled.csv", index=False)
joblib.dump(model, 'model.pkl')
joblib.dump(encoder, 'encoder.pkl')

print("✅ Proses selesai! File disimpan: model.pkl, data_filled.csv")