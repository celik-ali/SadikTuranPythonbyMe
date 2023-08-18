import requests
from bs4 import BeautifulSoup

userInput = input("Enter to search: ").replace(" ", "+")
url = "https://google.com/search?q="
headerParams = {"User-Agent":" ########"} # Put your User-Agent here

searchUrl = url + userInput


response = requests.get(searchUrl, headers=headerParams)

soupObject = BeautifulSoup(response.text, "html.parser")

results = soupObject.find_all("div", class_ = "yuRUbf")

for div in results:
    anchor = div.find("a")
    link = anchor["href"]
    text = anchor.h3.string
    if div.next_sibling == None:
        description = div.parent.next_sibling.find("span").text
        # OR
        #description = div.parent.next_sibling.find("div", style="-webkit-line-clamp:2").text
    else:
        description = div.next_sibling.find("span").text
        # OR 
        #description = div.next_sibling.find("div", style="-webkit-line-clamp:2").text
    print(link + " ~~~~~~~~ " + text + " ~~~~~~~~ " + description)
    print("~".center(100,"~"))
