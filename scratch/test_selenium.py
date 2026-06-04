import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print("Starting Selenium test...")
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

try:
    driver = webdriver.Chrome(options=options)
    print("Driver started successfully.")
    driver.get("http://localhost:8000")
    print(f"Page title is: {driver.title}")
    driver.quit()
    print("Test passed!")
except Exception as e:
    print(f"Failed to start Selenium: {e}")
    sys.exit(1)
