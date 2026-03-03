import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load & Clean Data
df = pd.read_csv('covid_19_indonesia_time_series_all.csv', sep=';')
df['Date'] = pd.to_datetime(df['Date'])

# 2. Persiapan Data Nasional (Moving Average)
df_nasional = df[df['Location'] == 'Indonesia'].sort_values('Date')
df_nasional['MA_7_Days'] = df_nasional['New Cases'].rolling(window=7).mean()

# 3. Persiapan Data Provinsi (Rankings)
df_prov = df[df['Location Level'] == 'Province']
latest_prov_data = df_prov.sort_values('Date').groupby('Location').last().reset_index()

top_cases = latest_prov_data.nlargest(10, 'Total Cases')
latest_prov_data['CFR_Calc'] = (latest_prov_data['Total Deaths'] / latest_prov_data['Total Cases']) * 100
top_cfr = latest_prov_data.nlargest(10, 'CFR_Calc')

# 4. Membuat Dashboard 2x2
fig, axes = plt.subplots(2, 2, figsize=(18, 12))
fig.suptitle('Dashboard Analisis COVID-19 Indonesia (Final)', fontsize=22, fontweight='bold')

# Panel 1: Trend Kasus
axes[0, 0].plot(df_nasional['Date'], df_nasional['New Cases'], color='lightgrey', alpha=0.5, label='Harian')
axes[0, 0].plot(df_nasional['Date'], df_nasional['MA_7_Days'], color='red', linewidth=2, label='Rata-rata 7 Hari')
axes[0, 0].set_title('Trend Penularan Nasional', fontsize=14)
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.2)

# Panel 2: Top Kasus (SUDAH DIPERBAIKI)
sns.barplot(
    ax=axes[0, 1], 
    data=top_cases, 
    x='Total Cases', 
    y='Location', 
    hue='Location',    # Menugaskan variabel 'Location' ke 'hue'
    palette='Reds_r', 
    legend=False       # Mematikan legenda agar tidak menumpuk
)
axes[0, 1].set_title('Top 10 Provinsi: Total Kasus', fontsize=14)

# Panel 3: Top CFR (SUDAH DIPERBAIKI)
sns.barplot(
    ax=axes[1, 0], 
    data=top_cfr, 
    x='CFR_Calc', 
    y='Location', 
    hue='Location',    # Menugaskan variabel 'Location' ke 'hue'
    palette='Oranges_r', 
    legend=False       # Mematikan legenda
)
axes[1, 0].set_title('Top 10 Provinsi: Tingkat Kematian (%)', fontsize=14)
axes[1, 0].set_xlabel('CFR (%)')

# Panel 4: Ringkasan Teks
axes[1, 1].axis('off')
summary = (f"RINGKASAN LAPORAN AKHIR\n"
           f"----------------------------\n"
           f"Total Kasus Nasional : {df_nasional['New Cases'].sum():,}\n"
           f"Total Kematian       : {df_nasional['New Deaths'].sum():,}\n"
           f"Puncak Pandemi       : 16 Feb 2022\n"
           f"Provinsi Terbanyak   : DKI Jakarta\n"
           f"Fatality Rate Tertinggi: Lampung\n\n"
           f"Status Code: Clean & Modern Plot")
axes[1, 1].text(0.1, 0.5, summary, fontsize=16, family='monospace', va='center')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('laporan_final_covid_clean.png')
plt.show()
print("Grafik berhasil disimpan: laporan_final_covid_clean.png")