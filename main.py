import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
AMAZON_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
headers = {
    "Accept-Language" : "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

response = requests.get(url=AMAZON_URL, headers=headers)
print(response.text)
data = response.text

soup = BeautifulSoup(data, "lxml")
price = soup.find(name="span", class_="a-price-whole").getText()
decimal_part_of_price = soup.find(name="span", class_="a-price-fraction").getText()
price = float(f"{price}{decimal_part_of_price}")
print(price)

MY_EMAIL = "danyloivanov54@gmail.com"
PASSWORD = "##############"

if price < 90:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="stalkerdan10@gmail.com",
                            msg=f"Subject:AMAZON\n\nCurrent price of product {price}, here is URL to amazon web page: {AMAZON_URL}"
                            )
