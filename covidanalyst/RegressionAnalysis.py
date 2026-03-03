import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Load data
df = pd.read_csv('covid_19_indonesia_time_series_all.csv', sep=';')

# 2. Filter for National Level (Indonesia)
df_nasional = df[df['Location'] == 'Indonesia'].copy()

# 3. Clean: Drop rows where New Cases or New Deaths might be NaN (though usually they aren't here)
df_nasional = df_nasional.dropna(subset=['New Cases', 'New Deaths'])

# 4. Define X (Independent) and y (Dependent)
# Reshape X because sklearn expects a 2D array
X = df_nasional[['New Cases']]
y = df_nasional['New Deaths']

# 5. Create and Train Model
model = LinearRegression()
model.fit(X, y)

# 6. Predict for the plot
y_pred = model.predict(X)

# 7. Visualization
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', alpha=0.3, label='Data Asli (Harian)')
plt.plot(X, y_pred, color='red', linewidth=2, label='Garis Regresi (Prediksi)')
plt.title('Hubungan antara Kasus Baru dan Kematian Baru (Indonesia)', fontsize=14)
plt.xlabel('Kasus Baru (New Cases)')
plt.ylabel('Kematian Baru (New Deaths)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('linear_regression_covid.png')

# 8. Output coefficients
slope = model.coef_[0]
intercept = model.intercept_
print(f"Slope (m): {slope}")
print(f"Intercept (c): {intercept}")

# Example prediction: if cases = 10000
test_cases = 10000
pred_death = model.predict([[test_cases]])[0]
print(f"Prediksi kematian jika kasus baru 10.000: {pred_death}")