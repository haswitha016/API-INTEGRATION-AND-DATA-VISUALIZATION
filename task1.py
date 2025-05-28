#TASK-1 internship--API-INTEGRATION AND DATA VISUALIZATION
import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
API_KEY = "2f0dbd93d0961c164232ec60957a94de"
CITY = "Mumbai"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(URL)
data = response.json()
dates, temperatures, humidities = [], [], []
for entry in data['list']:
    dt = datetime.fromtimestamp(entry['dt'])
    temp = entry['main']['temp']
    humidity = entry['main']['humidity']   
    dates.append(dt)
    temperatures.append(temp)
    humidities.append(humidity)
sns.set(style="darkgrid")
#temp plot
plt.figure(figsize=(10, 5))
sns.lineplot(x=dates, y=temperatures, marker="o", color="orange")
plt.title(f"Temperature Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("temperature_plot.png")
plt.show()
#humidity plot
plt.figure(figsize=(10, 5))
sns.lineplot(x=dates, y=humidities, marker="s", color="blue")
plt.title(f"Humidity Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("humidity_plot.png")
plt.show()
