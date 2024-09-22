import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Instagram profile URL
profile_url = "https://www.instagram.com/[username]/"  # Replace [username] with the actual username

# Set up Selenium webdriver
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('--headless=new') # Run in headless mode (no visible browser window)
driver = webdriver.Chrome(service=service, options=options)

# Load the Instagram profile page
driver.get(profile_url)

# Scroll down to load more images (adjust the number of scrolls as needed)
for _ in range(5):  # Scroll 5 times
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for images to load

# Get all image elements using the updated method
img_elements = driver.find_elements(By.TAG_NAME, 'img')

# Extract image URLs
img_urls = []
for img in img_elements:
    src = img.get_attribute('src')
    if src and src.startswith("https://scontent"): # Filter for image URLs from Instagram's CDN
        img_urls.append(src)

# Print or save the image URLs
for img_url in img_urls:
    print(img_url)

# Close the webdriver
driver.quit()