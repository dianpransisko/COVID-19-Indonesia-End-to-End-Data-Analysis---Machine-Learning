import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('covid_19_indonesia_time_series_all.csv', sep=';')
df_indo = df[df['Location'] == 'Indonesia'].copy()

# Prepare X and y
X = df_indo[['New Cases']].values
y = df_indo['New Deaths'].values

# Create and fit the model
model = LinearRegression()
model.fit(X, y)

# Get parameters
m = model.coef_[0]
c = model.intercept_

# Prediction for 1000 new cases
pred_1000 = model.predict([[1000]])[0]

# Visualize
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', alpha=0.3, label='Data Aktual')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Garis Regresi (Prediksi)')
plt.title('Linear Regression: Hubungan New Cases vs New Deaths (Nasional)', fontsize=14)
plt.xlabel('Jumlah Kasus Baru')
plt.ylabel('Jumlah Kematian Baru')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('regression_cases_vs_deaths.png')

print(f"Slope (m): {m}")
print(f"Intercept (c): {c}")
print(f"Prediksi kematian untuk 1000 kasus baru: {pred_1000}")
print("\nProses selesai! Periksa folder kamu untuk melihat hasil grafiknya.")