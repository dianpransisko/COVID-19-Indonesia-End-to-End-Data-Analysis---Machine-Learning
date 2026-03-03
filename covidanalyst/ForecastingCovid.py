import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import datetime as dt
import matplotlib.pyplot as plt

# 1. Load Data
df = pd.read_csv('covid_19_indonesia_time_series_all.csv', sep=';')
df['Date'] = pd.to_datetime(df['Date'])

# Kita ambil data Nasional 30 hari terakhir saja agar ramalannya lebih relevan dengan tren terbaru
df_indo = df[df['Location'] == 'Indonesia'].sort_values('Date').tail(30)

# 2. Ubah Tanggal menjadi angka (Ordinal) agar bisa dihitung Mesin
df_indo['Date_Ordinal'] = df_indo['Date'].map(dt.datetime.toordinal)

X = df_indo[['Date_Ordinal']] # Sebab (Waktu)
y = df_indo['New Cases']      # Akibat (Kasus)

# 3. Latih Model
model = LinearRegression()
model.fit(X, y)

# 4. Buat Tanggal untuk 7 Hari ke Depan
last_date = df_indo['Date'].max()
future_dates = [last_date + dt.timedelta(days=i) for i in range(1, 8)]
future_ordinal = np.array([d.toordinal() for d in future_dates]).reshape(-1, 1)

# 5. Prediksi!
predictions = model.predict(future_ordinal)

# 6. Tampilkan Hasil
print("--- RAMALAN KASUS 7 HARI KE DEPAN ---")
for date, pred in zip(future_dates, predictions):
    print(f"Tanggal {date.date()}: Prediksi {int(pred)} kasus baru")

# 7. Visualisasi
plt.figure(figsize=(10, 6))
plt.plot(df_indo['Date'], df_indo['New Cases'], label='Data 30 Hari Terakhir', marker='o')
plt.plot(future_dates, predictions, label='Ramalan (Trendline)', linestyle='--', marker='s', color='red')
plt.title('Forecasting: Tren Kasus COVID-19 Indonesia')
plt.xlabel('Tanggal')
plt.ylabel('Kasus Baru')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()