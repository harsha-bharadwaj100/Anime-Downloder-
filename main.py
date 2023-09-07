import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time

print("Supported site: https://www5.gogoanimes.fi", sep="\n")
animeLink = input("Enter Anime Link: ").strip().replace("category/", "")
episodeNumber = input("Enter Episode: ").strip()
episodeLink = animeLink + f"-episode-{episodeNumber}"
print(f"sanitized {animeLink = }", f"{episodeLink = }", sep="\n")

subprocess.Popen("Start-Chrome-Instance.bat")
# Initialize the WebDriver (make sure you have the appropriate driver for your browser installed)
option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(options=option)
driver.set_page_load_timeout(10)
# Open Episode Page
while 1:
    try:# Sometimes when you open link for the first time after turning on pc or restarting it kinda keeps loading forever...
        driver.get(episodeLink)# That's why I set page load timeout to say 10 seconds...
    except TimeoutException as err:# When the 10 seconds finish it will raise a timeout error and we will catch it...
        print(err)# and then try again...
        continue# if the same error occurs then just continue...
    break# if no timeout error, then move on.
# WebDriverWait(driver, 3).until
print("Before clicking downloadPageLink: ", driver.window_handles)
# Get and click Download page link
downloadPageLink = driver.find_element(By.PARTIAL_LINK_TEXT, 'Download')
print("Got download page link")
downloadPageLink.click()
print("Click download page link")
print("After clicking downloadPageLink: ", driver.window_handles)
print("Newly opened tab: ", driver.window_handles[-1])
# Switch to newly opened window
print("Before switching tab title: ", driver.title)
driver.switch_to.window(driver.window_handles[-1])
print("After switching tab title: ", driver.title)
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content-download > div:nth-child(1) > div:nth-child(3) > a')))
print("FOUND THE ELEMENT!!!!!!!!!!!!!!!!!!!!!!!!!")
# links = driver.find_elements(By.TAG_NAME, "a")
# # print(links)
# for link in links:
#     print(link.get_attribute("href"))
# Link opens in a new tab, click on download link
downloadLink = driver.find_element(By.CSS_SELECTOR, '#content-download > div:nth-child(1) > div:nth-child(3) > a')
print("Clicking the link: ", downloadLink.get_attribute("href"))
downloadLink.click()
# Close the browser
driver.quit()

# subprocess.Popen('close.ps1')