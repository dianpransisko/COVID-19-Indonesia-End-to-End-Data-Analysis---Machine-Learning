import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LOAD DATA
# Karena file kamu menggunakan titik koma (;) sebagai pemisah
df = pd.read_csv('covid_19_indonesia_time_series_all.csv', sep=';')

# 2. PEMBERSIHAN DATA (DATA CLEANSING)
# Mengubah kolom Date menjadi tipe data tanggal (datetime)
df['Date'] = pd.to_datetime(df['Date'])

# Dataset ini mencampur data Nasional dan Provinsi. Kita pisahkan.
df_nasional = df[df['Location'] == 'Indonesia'].sort_values('Date')
df_provinsi = df[df['Location Level'] == 'Province']

# 3. ANALISIS SEDERHANA (SUMMARY)
total_kasus = df_nasional['New Cases'].sum()
total_mati = df_nasional['New Deaths'].sum()
latest_date = df_nasional['Date'].max().date()

print(f"--- LAPORAN RINGKAS (Per {latest_date}) ---")
print(f"Total Kasus Terkonfirmasi: {total_kasus:,}")
print(f"Total Kematian: {total_mati:,}")
print(f"Tingkat Kematian Nasional (CFR): {(total_mati/total_kasus)*100:.2f}%")
print("-" * 40)

# 4. VISUALISASI 1: TREND KASUS HARIAN NASIONAL
plt.figure(figsize=(12, 6))
plt.plot(df_nasional['Date'], df_nasional['New Cases'], color='red', linewidth=1)
plt.title('Trend Kasus Baru COVID-19 di Indonesia', fontsize=14)
plt.xlabel('Tahun')
plt.ylabel('Jumlah Kasus Baru')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('trend_covid_indonesia.png')
print("Grafik trend berhasil disimpan: trend_covid_indonesia.png")

# 5. VISUALISASI 2: TOP 10 PROVINSI TERBANYAK
# Kita ambil data pada tanggal terbaru saja untuk ranking
last_update_prov = df_provinsi['Date'].max()
top_10 = df_provinsi[df_provinsi['Date'] == last_update_prov].nlargest(10, 'Total Cases')

plt.figure(figsize=(10, 6))
sns.barplot(
    data=top_10, 
    x='Total Cases', 
    y='Location', 
    hue='Location',    # Menugaskan variabel 'Location' ke 'hue' untuk pewarnaan
    palette='Reds_r', 
    legend=False       # Menghilangkan legenda karena sudah diwakili sumbu Y
)
plt.title(f'Top 10 Provinsi dengan Total Kasus Terbanyak (Update: {last_update_prov.date()})')
plt.xlabel('Total Kasus (Juta)')
plt.ylabel('Provinsi')
plt.tight_layout()
plt.savefig('top_10_provinsi.png')
print("Grafik ranking provinsi berhasil disimpan: top_10_provinsi.png")

print("\nProses selesai! Periksa folder kamu untuk melihat hasil grafiknya.")