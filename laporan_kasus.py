import matplotlib.pyplot as plt

# Data hasil query SQL kamu
provinsi = ['DKI Jakarta', 'Jawa Barat', 'Jawa Tengah', 'Jawa Timur', 'Banten']
total_kasus = [1412511, 1173731, 627654, 576374, 333875] # Contoh top 5

# Membuat grafik untuk laporan
plt.figure(figsize=(10,6))
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0']
plt.barh(provinsi[::-1], total_kasus[::-1], color='teal')

plt.title('Top 5 Provinsi Kasus COVID-19 Tertinggi di Indonesia', fontsize=14)
plt.xlabel('Jumlah Kasus (Juta)')
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Menambahkan label angka di ujung bar
for i, v in enumerate(total_kasus[::-1]):
    plt.text(v, i, f' {v:,}', va='center', fontweight='bold')

plt.tight_layout()
plt.show()