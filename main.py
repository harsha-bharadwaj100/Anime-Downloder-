import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

subprocess.Popen("Start-Chrome-Instance.bat")

# Initialize the WebDriver (make sure you have the appropriate driver for your browser installed)
option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress", "localhost:9222")

driver = webdriver.Chrome(options=option)
# Open Episode Page
driver.get("https://www5.gogoanimes.fi/one-piece-episode-64")
print("Before clicking downloadPageLink: ", driver.window_handles)
# Get and click Download page link
downloadPageLink = driver.find_element(By.PARTIAL_LINK_TEXT, 'Download')
downloadPageLink.click()
print("After clicking downloadPageLink: ", driver.window_handles)
print("Newly opened tab: ", driver.window_handles[-1])
# Switch to newly opened window
print("Before switching tab title: ", driver.title)
driver.switch_to.window(driver.window_handles[-1])
print("After switching tab title: ", driver.title)
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content-download > div:nth-child(1) > div:nth-child(5) > a')))
print("FOUND THE ELEMENT!!!!!!!!!!!!!!!!!!!!!!!!!")
# links = driver.find_elements(By.TAG_NAME, "a")
# # print(links)
# for link in links:
#     print(link.get_attribute("href"))
# Link opens in a new tab, click on download link
downloadLink = driver.find_element(By.CSS_SELECTOR, '#content-download > div:nth-child(1) > div:nth-child(5) > a')
print("Clicking the link: ", downloadLink.get_attribute("href"))
downloadLink.click()
# Close the browser
driver.quit()

# subprocess.Popen('close.ps1')