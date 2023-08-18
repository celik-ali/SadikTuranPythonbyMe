from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
chrom_driver_path = "*******************" # You need to write your drivers path here. You can get the path easily by looking at the properties of driver.

options = webdriver.ChromeOptions() # Because of the certificates it was giving some errors. By writing this and following two lines we aimed to get rid of them but still there are some trash values in the terminal. However, it is not a big issue we can ignore them.
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=options)

driver.get("https://www.n11.com/urun/madame-coco-charmes-yemek-tabagi-22-cm-taba0000000082yemek-tabagi-std-42015439?magaza=madamecoco")
title = driver.find_element(By.CLASS_NAME, "proName").text # Because of the selenium's new version find_element_by_xxxxx kinds of searches are no reachable. This is for the version for(August 2023)
price = driver.find_element(By.CLASS_NAME, "newPrice").find_element(By.TAG_NAME, "ins").text
searchInput = driver.find_element(By.ID, "productSearchForm").find_element(By.TAG_NAME, "input").get_attribute("value")
link = driver.find_element(By.ID,"productSearchForm").find_element(By.TAG_NAME, "input").get_attribute("data-url")
logo = driver.find_element(By.CSS_SELECTOR, ".logo img").get_attribute("src")
print(f"Product Title:{title}")
print(f"Product Price:{price}")
print(f"SearchBox Text:{searchInput}")
print(f"SearchBox Link:{link}")
print(f"Website Logo:{logo}")
