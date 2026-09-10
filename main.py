## I really want a Zelda Switch 2, I am writing this code to build me a bot crawler
## that will check Nintendo's website and check to see if Pre-orders become available
import requests
import json
import time
from datetime import datetime
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
END_DATE = datetime(2026, 10, 30)
alert_sent = False

while datetime.now() < END_DATE:
    response = fetch_page (PRODUCT_URL)

#Use soup to find HTML element and find JSON block + Parse to return Availabitlity

    if response is not None:
        soup = BeautifulSoup(response.text, "html.parser")
        script_tag = soup.find("script", type="application/ld+json")
        if script_tag is not None:
            data = json.loads(script_tag.string)

             availability = data["@graph"][0]["offers"]["availability"]

        if availability.endswith("OutOfStock"):
            alert_sent = False  
            
        else:
            if alert_sent == False:
                print("Twilio will send text- Next Steps Implementation")
                alert_sent = True
        time.sleep(60)