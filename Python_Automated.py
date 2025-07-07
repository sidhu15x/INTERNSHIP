from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 20)

try:
    driver.get("https://dev-admin.cloudstay.app")
    wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("admin@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("qwerty1")
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Dashboard')]")))

    # Click on "Hotel" from the sidebar
    hotel_tab = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//nav//*[text()='Hotel' or contains(., 'Hotel')]")
    ))
    hotel_tab.click()

    print("Hotel tab clicked. Press Enter to close the browser.")
    input()
except Exception as e:
    print(f"Test failed: {e}")
finally:
    driver.quit()
