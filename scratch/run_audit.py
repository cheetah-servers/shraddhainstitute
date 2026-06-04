import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

artifact_dir = r"C:\Users\metpa\.gemini\antigravity\brain\8c9ad20b-c217-42f1-8959-8ce7dd57a6d0"
viewports = [320, 375, 768, 1024, 1440, 1920]

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# Enable logging
options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})

driver = webdriver.Chrome(options=options)
url = "http://localhost:8000"

print(f"Starting audit for {url}...")

# Check script console log
def check_console_logs():
    try:
        logs = driver.get_log('browser')
        for log in logs:
            if log['level'] in ['SEVERE', 'WARNING']:
                print(f"Console {log['level']}: {log['message']}")
    except Exception as e:
        print(f"Could not read console logs: {e}")

# Check overflow script
overflow_script = """
const docWidth = document.documentElement.scrollWidth;
const viewWidth = window.innerWidth;
const elements = document.querySelectorAll('*');
const overflowing = [];
if (docWidth > viewWidth) {
    elements.forEach(el => {
        const rect = el.getBoundingClientRect();
        if (rect.right > viewWidth + 1 || rect.left < -1) {
            overflowing.push({
                tagName: el.tagName,
                id: el.id,
                className: el.className,
                left: rect.left,
                right: rect.right,
                width: rect.width
            });
        }
    });
}
return { docWidth, viewWidth, overflowing };
"""

try:
    driver.get(url)
    time.sleep(2)  # Wait for load & initial GSAP animation

    for width in viewports:
        print(f"\n--- Testing viewport width: {width}px ---")
        # Standard desktop height is 1080, scroll down if needed, but we can set height to 1200 or more
        height = 1200 if width < 1000 else 1080
        driver.set_window_size(width, height)
        time.sleep(1.5)  # Wait for transition/layouts

        # Measure page dimensions
        page_height = driver.execute_script("return document.documentElement.scrollHeight")
        print(f"Viewport Set: {width}x{height}, Scroll Height: {page_height}")

        # Check overflow
        result = driver.execute_script(overflow_script)
        if result['docWidth'] > result['viewWidth']:
            print(f"WARNING: Horizontal scroll detected! docWidth: {result['docWidth']}, viewWidth: {result['viewWidth']}")
            print(f"Overflowing elements count: {len(result['overflowing'])}")
            # Show first 5 overflowing elements
            for el in result['overflowing'][:5]:
                print(f" - {el['tagName']} #{el['id']}.{el['className'].replace(' ', '.')} (left: {el['left']}, right: {el['right']}, width: {el['width']})")
        else:
            print("OK: No horizontal scrolling detected.")

        # Check logs
        check_console_logs()

        # Capture screenshot
        screenshot_path = os.path.join(artifact_dir, f"screenshot_{width}.png")
        # Save screenshot
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

finally:
    driver.quit()
    print("\nAudit completed.")
