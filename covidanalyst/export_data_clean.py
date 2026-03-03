import pandas as pd
from sqlalchemy import create_engine

# 1. Koneksi ke Database
# Ganti user, password, dan nama_db sesuai milik Anda
engine = create_engine('postgresql://postgres:paswrdmu@localhost:5432/database_mu') 

# 2. Tarik data menggunakan query SQL
query = "SELECT * FROM covid_indonesia"
df_clean = pd.read_sql(query, engine)

# 3. Export ke CSV
df_clean.to_csv('covid_clean_dari_python.csv', index=False, sep=';')

print("Data berhasil diekspor ke CSV!")