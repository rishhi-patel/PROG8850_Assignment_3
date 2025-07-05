from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import mysql.connector

chrome_opts = webdriver.ChromeOptions()
chrome_opts.add_argument("--headless=new")          # run headless
chrome_opts.add_argument("--no-sandbox")            # good for Docker
chrome_opts.add_argument("--disable-dev-shm-usage")  # prevent /dev/shm errors

SELENIUM_HUB = "http://localhost:4444/wd/hub"
APP_URL = "http://app:5000"


driver = webdriver.Remote(
    command_executor=SELENIUM_HUB,
    options=chrome_opts
)


try:
    driver.get(APP_URL)
    driver.find_element(By.NAME, "username").send_keys("testuser")
    driver.find_element(By.NAME, "password").send_keys("testpass")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
finally:
    driver.quit()


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="login_db"
)
cur = conn.cursor()
cur.execute("SELECT 1 FROM users WHERE username=%s", ("testuser",))
assert cur.fetchone(), "User insertion failed!"
print("✅  Test passed.")
conn.close()
