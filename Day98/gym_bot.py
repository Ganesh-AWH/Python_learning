from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Keep browser open after script finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

def book_class():
    driver.get("https://yourgym.com/login")
    
    # Log In
    driver.find_element(By.NAME, "username").send_keys("YOUR_EMAIL")
    driver.find_element(By.NAME, "password").send_keys("YOUR_PASSWORD", Keys.ENTER)
    
    time.sleep(3) # Wait for dashboard to load
    
    # Navigate to Bookings
    driver.get("https://yourgym.com/bookings/friday-yoga")
    
    try:
        book_button = driver.find_element(By.ID, "reserve-button")
        book_button.click()
        print("Spot secured!")
    except:
        print("Class not available yet. Retrying...")
        driver.refresh()

# In a real scenario, you'd use a while loop or a cron job to trigger this
book_class()