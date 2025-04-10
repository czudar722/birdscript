from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
# optional: options.add_argument("--headless")

service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)


driver.get("<URL>")
print(driver.title)
sleep(5)
driver.quit()

