import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://www.theblueground.com/sp?checkIn=2025-06-01&checkOut=2026-05-31&placeId=ct-eyJ0eXBlIjoiY2l0eSIsImxhdCI6MzQuMDU0OTA3NiwibG5nIjotMTE4LjI0MjY0M30"

# Proxy configuration of choice; DataImpusle is used here
#proxy_host = 'gw.dataimpusle.com'
#proxy_port = 823
#proxy_login = ''
#proxy_password = ''
#proxy = f'https://{proxy_login}:{proxy_password}@{proxy_host}:{proxy_port}'

#proxies = {
#    'http': proxy,
#    'https': proxy
#}

#List to store aparmtents URLS
apartment_urls = []

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

apt_list = soup.find_all('a', class_="property")
print(f"Total apartments found: {len(apt_list)}")

for apt in apt_list:
    relative_url = apt.get('href')

    if relative_url:
        # Construct full URL
        full_url = urljoin("https://theblueground.com", relative_url)
        apartment_urls.append(full_url)

# Print all apartment URLS
print("\nAparmtnet URLs:")
for apt_url in apartment_urls:
    print(apt_url)

# Optional: Save URLs to a file
with open('apartment_urls.txt', 'w') as f:
    for apt_url in apartment_urls:
        f.write(apt_url + '\n')