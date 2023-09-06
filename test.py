import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

subprocess.Popen("Start-Chrome-Instance.bat")

# Initialize the WebDriver (make sure you have the appropriate driver for your browser installed)
option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress", "localhost:9222")

driver = webdriver.Chrome(options=option)
# Open Episode Page
driver.get("https://goone.pro/download?id=MzcyOA==&typesub=Gogoanime-SUB&title=One+Piece+Episode+64")
links = driver.find_elements(By.TAG_NAME, "a")
# print(links)
for link in links:
    print(link.get_attribute("href"))
# Link opens in a new tab, click on download link
time.sleep(5)
links = driver.find_elements(By.TAG_NAME, "a")
# print(links)
for link in links:
    print(link.get_attribute("href"))
try:
    downloadLink = driver.find_element(By.CSS_SELECTOR, '#content-download > div:nth-child(1) > div:nth-child(3) > a')
    downloadLink.click()
except NoSuchElementException as error:
    print(error)
# Close the browser
driver.quit()

# subprocess.Popen('close.ps1')