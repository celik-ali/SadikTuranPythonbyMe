import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"
headers = {"User-Agent":"###################"} # Insert your User-Agent here

html = requests.get(url, headers=headers).text

soupObject = BeautifulSoup(html, "html.parser")

laptops = soupObject.find_all("li", class_= "column")
for laptop in laptops:
    name = laptop.find("h3").string
    link = laptop.div.a["href"]
    print("Product Link: "+link)
    priceCont = laptop.find("div", class_= "priceContainer").div.span
    if priceCont.next_sibling.next_sibling.next_sibling.next_sibling != None: # If there is a discount on the cart n11 has 3 spans for it in the html. Therefore, I preferred to check discount number of spans
        price = priceCont.find("del").text.strip("TL").strip() # We are deleting unnecessary things like currency and spaces. In case of converting string to float or int.
        cartPrice = priceCont.next_sibling.next_sibling.next_sibling.next_sibling.find('ins').text.strip('TL').strip() # We are deleting unnecessary things like currency and spaces. In case of converting string to float or int.
        floatPrice = float(price[:-3])
        floatCartPrice = float(cartPrice[:-3])
        print(f"Product: {(name+',').ljust(110)} Price: {(price+ 'TL').ljust(12)} Price in cart: {cartPrice} You are getting:%{(100*(floatPrice-floatCartPrice)/floatPrice)} discount")

    else:
        price = priceCont.next_sibling.next_sibling.find("ins").text.strip("TL").strip() # We are deleting unnecessary things like currency and spaces. In case of converting string to float or int.
        floatPrice = price[:-3]
        print(f"Product: {(name+',').ljust(110)} Price: {(price+ 'TL').ljust(12)} (***This product does not have any discount***) Price in cart: {priceCont.next_sibling.next_sibling.find('ins').text}")
    print("".center(50, "#"))
