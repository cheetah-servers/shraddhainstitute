import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

print("Starting Interactivity test suite (JS-based clicks)...")
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
url = "http://localhost:8000"

def js_click(element):
    driver.execute_script("arguments[0].click();", element)
    time.sleep(0.5)

try:
    driver.get(url)
    time.sleep(1.5)
    
    body = driver.find_element(By.TAG_NAME, "body")

    # 1. Test Methodology Slider Navigation
    print("\n[Test 1] Methodology Slider Navigation:")
    slide_number = driver.find_element(By.ID, "portal-slide-number")
    slide_title = driver.find_element(By.ID, "portal-slide-title-header")
    next_arrow = driver.find_element(By.ID, "portal-next-btn")
    prev_arrow = driver.find_element(By.ID, "portal-prev-btn")
    
    print(f"On load: slide text='{slide_number.text}', title='{slide_title.text}'")
    
    # Click next to go to Slide 2 (Misconceptions)
    js_click(next_arrow)
    print(f"After next click (Slide 2): slide text='{slide_number.text}', title='{slide_title.text}'")
    
    # 2. Test Accordion Interactivity on Slide 2
    print("\n[Test 2] Accordion Interactivity (Slide 2):")
    accordion_headers = driver.find_elements(By.CLASS_NAME, "accordion-header")
    print(f"Found {len(accordion_headers)} accordion headers.")
    
    first_item = accordion_headers[0].find_element(By.XPATH, "..")
    print(f"First accordion active state: {first_item.get_attribute('class')}")
    
    # Click the second accordion header
    js_click(accordion_headers[1])
    print(f"First accordion active state after clicking second: {first_item.get_attribute('class')}")
    second_item = accordion_headers[1].find_element(By.XPATH, "..")
    print(f"Second accordion active state after click: {second_item.get_attribute('class')}")
    
    # Go to Slide 3 (Grammar Methodology)
    js_click(next_arrow)
    print(f"After next click (Slide 3): slide text='{slide_number.text}', title='{slide_title.text}'")

    # 3. Test Booking Form Modal opening
    print("\n[Test 3] Apply Modal Opening & Scroll Lock:")
    apply_btn = driver.find_element(By.CLASS_NAME, "open-apply-modal")
    js_click(apply_btn)
    
    apply_modal = driver.find_element(By.ID, "apply-modal")
    print(f"Apply modal class list: {apply_modal.get_attribute('class')}")
    print(f"Body style overflow attribute: {body.get_attribute('style')}")
    
    # 4. Test Booking Form Modal closing
    print("\n[Test 4] Apply Modal Closing & Scroll Release:")
    close_btn = driver.find_element(By.ID, "close-apply-modal")
    js_click(close_btn)
    print(f"Apply modal class list after closing: {apply_modal.get_attribute('class')}")
    print(f"Body style overflow attribute after closing: {body.get_attribute('style')}")

    # 5. Test Form Submission and Success Modal
    print("\n[Test 5] Form Submission Flow:")
    # Reopen modal
    js_click(apply_btn)
    
    # Fill in form
    driver.find_element(By.ID, "apply-name").send_keys("Test Auditor")
    driver.find_element(By.ID, "apply-phone").send_keys("9876543210")
    driver.find_element(By.ID, "apply-email").send_keys("audit@example.com")
    
    # Select occupation
    occupation_select = driver.find_element(By.ID, "apply-occupation")
    js_click(occupation_select)
    occupation_select.find_element(By.XPATH, "//option[@value='student']").click()
    
    # Select course
    course_select = driver.find_element(By.ID, "apply-course")
    js_click(course_select)
    course_select.find_element(By.XPATH, "//option[@value='school']").click()
    
    # Submit form
    submit_btn = driver.find_element(By.XPATH, "//form[@id='apply-form']/button[@type='submit']")
    js_click(submit_btn)
    
    success_modal = driver.find_element(By.ID, "success-modal")
    print(f"Success modal class list after form submission: {success_modal.get_attribute('class')}")
    print(f"Apply modal class list after form submission: {apply_modal.get_attribute('class')}")
    print(f"Body style overflow: {body.get_attribute('style')}")

    # Close success modal
    success_close_btn = driver.find_element(By.ID, "close-success-modal")
    js_click(success_close_btn)
    print(f"Success modal class list after closing: {success_modal.get_attribute('class')}")
    print(f"Body style overflow after closing: {body.get_attribute('style')}")

    # 6. Test Hamburger Menu on Mobile Viewport
    print("\n[Test 6] Hamburger Menu (Mobile Viewport):")
    driver.set_window_size(375, 812) # iPhone size
    time.sleep(1.0)
    
    hamburger = driver.find_element(By.ID, "hamburger-toggle")
    nav_menu = driver.find_element(By.ID, "nav-menu")
    
    # Open Menu
    js_click(hamburger)
    print("Clicked hamburger to open menu.")
    print(f"Hamburger class: {hamburger.get_attribute('class')}")
    print(f"Hamburger aria-expanded: {hamburger.get_attribute('aria-expanded')}")
    print(f"Nav Menu classes: {nav_menu.get_attribute('class')}")
    
    # Close Menu by clicking a link
    journey_link = driver.find_element(By.XPATH, "//nav[@id='nav-menu']/a[@href='#journey']")
    js_click(journey_link)
    print("Clicked Journey link inside mobile menu.")
    print(f"Hamburger aria-expanded: {hamburger.get_attribute('aria-expanded')}")
    print(f"Nav Menu classes: {nav_menu.get_attribute('class')}")

    print("\nAll interactivity tests completed successfully!")
except Exception as e:
    print(f"\nERROR: Interactivity test failed: {e}")
    sys.exit(1)
finally:
    driver.quit()
