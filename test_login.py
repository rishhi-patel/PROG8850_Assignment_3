from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import mysql.connector
import os

driver = webdriver.Chrome()
driver.get("http://localhost:5000")

driver.find_element(By.NAME, "username").send_keys("testuser")
driver.find_element(By.NAME, "password").send_keys("testpass")
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(2)
driver.quit()

conn = mysql.connector.connect(
    host="localhost",
    user=os.getenv("MYSQL_USER", "root"),
    password=os.getenv("MYSQL_PASSWORD", "yourpassword"),
    database=os.getenv("MYSQL_DATABASE", "login_db")
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM users WHERE username='testuser'")
result = cursor.fetchone()
assert result is not None, "User was not inserted"
print("Test Passed: User inserted.")
conn.close()
