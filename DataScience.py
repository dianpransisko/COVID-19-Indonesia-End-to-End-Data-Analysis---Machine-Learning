import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Load data
df = pd.read_csv('covid_19_indonesia_time_series_all.csv', sep=';')
df['Date'] = pd.to_datetime(df['Date'])

# 2. Data Preparation for Clustering (Latest state per Province)
df_prov = df[df['Location Level'] == 'Province']
latest_data = df_prov.sort_values('Date').groupby('Location').last().reset_index()

# Features for clustering: Total Cases per Million vs Case Fatality Rate
# We need to clean the CFR (remove % and convert to float)
latest_data['CFR_numeric'] = (latest_data['Total Deaths'] / latest_data['Total Cases']) * 100

# Select features
features = ['Total Cases per Million', 'CFR_numeric']
X = latest_data[features].fillna(0)

# 3. Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. K-Means Clustering (e.g., 3 clusters: High Risk, Medium, Low)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
latest_data['Cluster'] = kmeans.fit_predict(X_scaled)

# 5. Visualization
plt.figure(figsize=(12, 8))
sns.scatterplot(data=latest_data, x='Total Cases per Million', y='CFR_numeric', 
                hue='Cluster', palette='viridis', s=100, style='Cluster')

# Annotate some province names
for i in range(latest_data.shape[0]):
    plt.text(latest_data['Total Cases per Million'][i]+1000, 
             latest_data['CFR_numeric'][i], 
             latest_data['Location'][i], fontsize=9, alpha=0.7)

plt.title('Clustering Provinsi Berdasarkan Risiko COVID-19', fontsize=16)
plt.xlabel('Total Kasus per 1 Juta Penduduk')
plt.ylabel('Case Fatality Rate (%)')
plt.grid(True, alpha=0.3)
plt.savefig('clustering_provinsi.png')

# Summary of clusters
cluster_summary = latest_data.groupby('Cluster')[features].mean()
print(cluster_summary)
print("\nProses selesai! Periksa folder kamu untuk melihat hasil grafiknya.")