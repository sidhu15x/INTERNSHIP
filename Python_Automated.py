from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 20)

try:
    driver.get("https://dev-admin.cloudstay.app")

    # Login
    wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("admin@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("qwerty1")
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()

    # Wait for dashboard to load
    WebDriverWait(driver, 15).until(
        lambda d: d.current_url == "https://dev-admin.cloudstay.app/stats"
    )

    # Click "All Organisations"
    org_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='All Organisations']")))
    org_dropdown.click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='listbox']")))
    time.sleep(1)

    # Select "DesiUrban"
    org_options = driver.find_elements(By.XPATH, "//div[@role='option']")
    for option in org_options:
        if "DesiUrban" in option.text:
            driver.execute_script("arguments[0].scrollIntoView(true);", option)
            time.sleep(0.5)
            driver.execute_script("arguments[0].click();", option)
            print("✅ DesiUrban selected.")
            break
    else:
        print("❌ DesiUrban not found.")

    # Wait for hotels dropdown to load
    time.sleep(2)

    # Click "All Hotels"
    hotel_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='All Hotels']")))
    hotel_dropdown.click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='listbox']")))
    time.sleep(1)

    # Select "Desi Urban Hotel"
    hotel_options = driver.find_elements(By.XPATH, "//div[@role='option']")
    for hotel in hotel_options:
        if "Desi Urban Hotel" in hotel.text:
            driver.execute_script("arguments[0].scrollIntoView(true);", hotel)
            time.sleep(0.5)
            driver.execute_script("arguments[0].click();", hotel)
            print("✅ Desi Urban Hotel selected.")
            break
    else:
        print("❌ Desi Urban Hotel not found.")

    # Verify the heading "Total Hotels:1"
    heading = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[contains(text(), 'Total Hotels:')]")
    ))
    print("✅ Heading found:", heading.text)

    print("🎉 Script completed. Press Enter to exit.")
    input()

except Exception as e:
    print(f"Test failed: {e}")
finally:
    driver.quit()
