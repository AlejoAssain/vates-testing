import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


# Ruta al Chromedriver descargado
chrome_driver_path = 'C:\\dev\\chromedriver_win32\\chromedriver.exe' # En Windows | tu ruta aqui
# chrome_driver_path = '/ruta/al/chromedriver' # En macOS/Linux

# Configuración del Service de Chrome
service = ChromeService(executable_path=chrome_driver_path)

# Configuración del controlador Chrome con el Service
driver = webdriver.Chrome(service=service)

# Utilizamos una espera implícita para evitar el uso innecesario de time.sleep
driver.implicitly_wait(10)

# Go to webpage
driver.get("https://practicetestautomation.com/practice-test-login/")

# Type username "student" into Username field
username_locator = driver.find_element(By.ID, "username")
username_locator.send_keys("student")

# Type password "Password123" into Password field
password_locator = driver.find_element(By.NAME, "password")
password_locator.send_keys("Password123")

# Find and click the "Submit" button
submit_button_locator = driver.find_element(By.ID, "submit")
submit_button_locator.click()
time.sleep(10)
driver.quit()
