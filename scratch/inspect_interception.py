import sys
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
url = "http://localhost:8000"

try:
    driver.get(url)
    import time
    time.sleep(1.5)
    
    next_arrow = driver.find_element(By.ID, "portal-next-btn")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_arrow)
    time.sleep(0.5)
    
    next_arrow.click()
except Exception as e:
    print("Full Exception Message:")
    print(str(e))
    driver.quit()
    sys.exit(1)

driver.quit()
print("Success!")
