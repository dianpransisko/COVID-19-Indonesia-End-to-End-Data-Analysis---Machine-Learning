import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Data
df = pd.read_csv('covid_19_indonesia_time_series_all.csv', sep=';')

# Ambil data terbaru untuk setiap provinsi saja
df_prov = df[df['Location Level'] == 'Province']
latest_data = df_prov.sort_values('Date').groupby('Location').last().reset_index()

# 2. Menyiapkan Fitur (Features)
# Kita hitung ulang CFR agar akurat (karena di CSV formatnya string %)
latest_data['CFR'] = (latest_data['Total Deaths'] / latest_data['Total Cases']) * 100

# Pilih kolom untuk Clustering
features = ['Total Cases per Million', 'CFR']
X = latest_data[features]

# 3. Scaling (Sangat Penting untuk K-Means)
# Karena skala 'Total Cases per Million' (ribuan) beda jauh dengan 'CFR' (satuan)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Membuat Model K-Means (Kita buat 3 Kelompok/Cluster)
kmeans = KMeans(n_clusters=3, random_state=42)
latest_data['Cluster'] = kmeans.fit_predict(X_scaled)

# 5. Visualisasi Hasil
plt.figure(figsize=(12, 8))
sns.scatterplot(
    data=latest_data, 
    x='Total Cases per Million', 
    y='CFR', 
    hue='Cluster', 
    palette='viridis', 
    s=100
)

# Menambahkan nama provinsi pada titik-titik di grafik
for i in range(latest_data.shape[0]):
    plt.text(
        latest_data['Total Cases per Million'][i]+1000, 
        latest_data['CFR'][i], 
        latest_data['Location'][i], 
        fontsize=8, 
        alpha=0.7
    )

plt.title('Clustering Provinsi Berdasarkan Penularan vs Tingkat Kematian', fontsize=15)
plt.xlabel('Total Kasus per 1 Juta Penduduk')
plt.ylabel('Tingkat Kematian (CFR) %')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 6. Tampilkan Anggota Cluster
for i in range(3):
    print(f"\n--- ANGGOTA CLUSTER {i} ---")
    print(latest_data[latest_data['Cluster'] == i]['Location'].values)
print("\nProses selesai! Periksa folder kamu untuk melihat hasil grafiknya.")