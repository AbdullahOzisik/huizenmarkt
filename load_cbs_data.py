import pandas as pd
import requests
from sqlalchemy import create_engine

# 🔗 URL naar JSON (CBS OData v4 API)
url = "https://opendata.cbs.nl/ODataFeed/odata/83765NED/TypedDataSet?$format=json"

print("📥 Data downloaden van CBS...")

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    df = pd.json_normalize(data['value'])
    print(f"✅ Data geladen met {df.shape[0]} rijen en {df.shape[1]} kolommen")
except Exception as e:
    print("❌ Fout bij downloaden:", e)
    exit()

# 🔌 Verbind met PostgreSQL database 'huizenmarkt'
engine = create_engine("postgresql://postgres:Kayseri38@localhost:5432/huizenmarkt")

# 💾 Data opslaan in tabel 'woningprijzen_raw'
try:
    df.to_sql('woningprijzen_raw', engine, if_exists='replace', index=False)
    print("✅ Data succesvol opgeslagen in database.")
except Exception as e:
    print("❌ Fout bij opslaan in database:", e)

