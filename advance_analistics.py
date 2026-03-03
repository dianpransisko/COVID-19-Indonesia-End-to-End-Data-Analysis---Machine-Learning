import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Load and prepare data
df = pd.read_csv('covid_19_indonesia_time_series_all.csv', sep=';')
df['Date'] = pd.to_datetime(df['Date'])
df_prov = df[df['Location Level'] == 'Province']

# Get latest data per province
latest_data = df_prov.sort_values('Date').groupby('Location').last().reset_index()

# Calculate Features for Clustering
# We use per million and rate to normalize for population size differences
latest_data['CFR'] = (latest_data['Total Deaths'] / latest_data['Total Cases']) * 100
X = latest_data[['Total Cases per Million', 'CFR']]

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-Means clustering (let's use 3 clusters)
kmeans = KMeans(n_clusters=3, random_state=42)
latest_data['Cluster'] = kmeans.fit_predict(X_scaled)

# Visualize Clustering
plt.figure(figsize=(10, 8))
sns.scatterplot(data=latest_data, x='Total Cases per Million', y='CFR', hue='Cluster', palette='viridis', s=100)

# Annotate some provinces
for i in range(latest_data.shape[0]):
    plt.text(latest_data['Total Cases per Million'][i], latest_data['CFR'][i], latest_data['Location'][i], fontsize=9)

plt.title('Clustering Provinsi Berdasarkan Kasus per Juta & Tingkat Kematian (CFR)', fontsize=14)
plt.xlabel('Total Kasus per 1 Juta Penduduk')
plt.ylabel('Case Fatality Rate (%)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('clustering_provinsi.png')

print(latest_data[['Location', 'Cluster', 'Total Cases per Million', 'CFR']].sort_values('Cluster'))
print("\nProses selesai! Periksa folder kamu untuk melihat hasil grafiknya.")