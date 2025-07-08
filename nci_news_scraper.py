import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.nci-marketstructure.com/economic-news"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Adjust based on actual structure — this is a placeholder
table = soup.find("table")
rows = table.find_all("tr") if table else []

data = []
for row in rows[1:]:
    cols = row.find_all("td")
    if len(cols) >= 5:
        date = cols[0].text.strip()
        time = cols[1].text.strip()
        currency = cols[2].text.strip()
        event = cols[3].text.strip()
        impact = cols[4].text.strip()
        data.append([date, time, currency, event, impact])

df = pd.DataFrame(data, columns=["date", "time", "currency", "event", "impact"])
df.to_csv("calendar.csv", index=False)
print("✅ calendar.csv updated.")
