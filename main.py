## I really want a Zelda Switch 2, I am writing this code to build me a bot crawler
## that will check Nintendo's website and check to see if Pre-orders become available
import requests
import json
import time
from bs4 import BeautifulSoup

#Find URL, Check Access

def fetch_page (url):
    try:
        response = requests.get(url, timeout=15)
   
        if response.status_code == 200:
            return response
  
        print("Website returned status:", response.status_code)
        return None

    except requests.RequestException as error:
        print("Request failed:", error)
        return None

PRODUCT_URL = "https://www.nintendo.com/us/store/products/nintendo-switch-2-the-legend-of-zelda-40th-anniversary-edition-121642/"
for i in range (3):
    response = fetch_page (PRODUCT_URL)

#Use soup to find HTML element and find JSON block + Parse to return Availabitlity

    if response is not None:
        soup = BeautifulSoup(response.text, "html.parser")
        script_tag = soup.find("script", type="application/ld+json")
        data = json.loads(script_tag.string)

        availability = data["@graph"][0]["offers"]["availability"]

        if availability.endswith("OutOfStock"):
            alert_sent = False  
            

        else:
            if alert_sent == False:
                print("Twilio will send text")
                alert_sent = True
        time.sleep(60)