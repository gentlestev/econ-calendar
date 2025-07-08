import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Target URL
url = "https://www.nci-marketstructure.com/economic-news"

# Send request and parse HTML
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Adjust this selector based on actual page structure (example)
table = soup.find("table")  # assuming there's a table
rows = table.find_all("tr")

# Prepare extracted data
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

# Create DataFrame
df = pd.DataFrame(data, columns=["date", "time", "currency", "event", "impact"])

# Save to CSV
df.to_csv("calendar.csv", index=False)
print("✅ News calendar saved as calendar.csv")
